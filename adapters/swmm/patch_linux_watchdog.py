"""Apply one reviewed Linux portability change; never patch solver mathematics."""
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
        import ctypes
        import signal
        # Set in the spawned worker, before opening native files. The post-set
        # parent check closes the race in which the owner died before prctl.
        libc = ctypes.CDLL(None, use_errno=True)
        if libc.prctl(1, signal.SIGKILL, 0, 0, 0) != 0:  # PR_SET_PDEATHSIG
            raise OSError(ctypes.get_errno(), "Cannot set Linux parent-death signal")
        if os.getppid() != parent_pid:
            os._exit(1)
        return
    if os.name != "nt":
        return
'''
if text.count(needle)!=1:raise ValueError('Pinned original watchdog context changed')
path.write_text(text.replace(needle,replacement),encoding='utf-8')
print(json.dumps({'original_worker_sha256':hashlib.sha256(before).hexdigest(),
    'patched_worker_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
    'change':'Linux parent-death SIGKILL with race check; use container init to reap orphans. Original Windows implementation retained.'}))
