"""Keep native TraCI retry messages out of the MCP JSON-RPC channel."""
import builtins
import sys
import traci.main


def install_traci_stderr():
    # SUMO's subprocess stdout and Python TraCI's own prints are different
    # streams. The original MCP suppresses only the subprocess stream.
    if getattr(traci.main, "_urban_mcp_stderr_installed", False):
        return
    def stderr_print(*args, **kwargs):
        kwargs["file"] = sys.stderr
        return builtins.print(*args, **kwargs)
    traci.main.print = stderr_print
    traci.main._urban_mcp_stderr_installed = True
