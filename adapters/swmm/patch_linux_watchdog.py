"""Apply reviewed worker-lifetime/metadata fixes; never patch solver mathematics."""
from pathlib import Path
import hashlib
import json
import sys

path=Path(sys.argv[1])/'src/pyswmm_mcp/worker.py'
before=path.read_bytes()
text=before.decode()
needle='    """Exit a Windows worker when its owning MCP process disappears."""\n    if os.name != "nt":\n        return\n'
replacement='''    """Exit a worker when its owner disappears (Windows original; Linux patch)."""
    import sys
    if sys.platform == "linux":
        import subprocess
        # Linux PDEATHSIG observes the creating THREAD, which an AnyIO pool
        # may retire while the server process remains alive. A separate tiny
        # watcher monitors process pidfds and can kill a GIL-busy native worker.
        owner_fd = os.pidfd_open(parent_pid)
        worker_fd = os.pidfd_open(os.getpid())
        try:
            if os.getppid() != parent_pid:
                os._exit(1)
            subprocess.Popen(
                [sys.executable, "/opt/swmm-linux-watchdog.py", str(owner_fd), str(worker_fd)],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                pass_fds=(owner_fd, worker_fd),
            )
        finally:
            os.close(owner_fd)
            os.close(worker_fd)
        return
    if os.name != "nt":
        return
'''
if text.count(needle)!=1:raise ValueError('Pinned original watchdog context changed')
text=text.replace(needle,replacement)
start=text.index('def _run_simulation(')
end=text.index('\ndef _inspect_output(',start)
original_batch=text[start:end]
if 'simulation.execute()' not in original_batch or 'simulation.flow_routing_error' not in original_batch:raise ValueError('Pinned original batch context changed')
batch='''def _run_simulation(
    input_path: Path,
    report_path: Path,
    output_path: Path,
) -> dict[str, Any]:
    from pyswmm import Links, Nodes, Simulation, Subcatchments

    previous_directory = Path.cwd()
    os.chdir(input_path.parent)
    try:
        balances = {}
        with Simulation(str(input_path), str(report_path), str(output_path)) as simulation:
            metadata = {
                "engine_version": str(simulation.engine_version),
                "system_units": simulation.system_units,
                "flow_units": simulation.flow_units,
                "start_time": _iso(simulation.start_time),
                "end_time": _iso(simulation.end_time),
                "counts": {
                    "nodes": len(Nodes(simulation)),
                    "links": len(Links(simulation)),
                    "subcatchments": len(Subcatchments(simulation)),
                },
            }
            # The native mass-balance API is valid after swmm_end and before
            # swmm_close. execute() closes first and misleadingly returns zero.
            def capture_balances():
                balances.update(
                    runoff_error=simulation.runoff_error,
                    flow_routing_error=simulation.flow_routing_error,
                    quality_error=simulation.quality_error,
                )
            simulation.add_after_end(capture_balances)
            for _ in simulation:
                pass
        if not balances:
            raise RuntimeError("Native mass balances were not captured before close")
        return {**metadata, **balances}
    finally:
        os.chdir(previous_directory)

'''
text=text[:start]+batch+text[end:]
path.write_text(text,encoding='utf-8')
print(json.dumps({'original_worker_sha256':hashlib.sha256(before).hexdigest(),
    'patched_worker_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
    'changes':['Linux process pidfd watcher with race check, outside the native worker GIL; creator-thread exit is harmless. Container init reaps orphan watchers/workers. Original Windows implementation retained.',
        'Original PySWMM context/iterator/after_end callback captures native balances after end and before close. No solver mathematics, model parameters, time steps or routing are changed.'],
    'original_batch_sha256':hashlib.sha256(original_batch.encode()).hexdigest()}))
