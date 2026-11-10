"""Emit a client-neutral stdio configuration; no agent or credential dependency."""
import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = "urban_mcp_helsinki"


def wsl_path(path):
    value = str(path.resolve())
    if len(value) < 3 or value[1:3] != ":\\":
        raise ValueError("WSL mode requires a Windows drive path")
    return "/mnt/" + value[0].lower() + "/" + value[3:].replace("\\", "/")


def server_config(data_dir=None, wsl_distro=None):
    data = Path(data_dir).resolve() if data_dir else ROOT / ".urban-mcp/helsinki"
    data.mkdir(parents=True, exist_ok=True)
    if wsl_distro:
        command = "wsl.exe"
        args = ["-d", wsl_distro, "--cd", wsl_path(ROOT), "--exec", "env", "URBAN_MCP_WORKDIR="+wsl_path(data), "docker", "compose", "--profile", "municipal", "run", "--rm", "-T", "--no-deps", "municipal-mcp"]
        env = {}
    else:
        command = "docker"
        args = ["compose", "--project-directory", str(ROOT), "--profile", "municipal", "run", "--rm", "-T", "--no-deps", "municipal-mcp"]
        env = {"URBAN_MCP_WORKDIR": str(data)}
        if hasattr(os, "getuid"):
            env.update(URBAN_MCP_UID=str(os.getuid()), URBAN_MCP_GID=str(os.getgid()))
    return {"command": command, "args": args, "env": env}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=["mcp-json", "codex", "hermes"], default="mcp-json")
    parser.add_argument("--data-dir")
    parser.add_argument("--wsl-distro")
    args=parser.parse_args()
    cfg=server_config(args.data_dir,args.wsl_distro)
    if args.format == "mcp-json":
        print(json.dumps({"mcpServers":{NAME:cfg}},indent=2))
    elif args.format == "hermes":
        import yaml
        print(yaml.safe_dump({"mcp_servers":{NAME:{**cfg,"connect_timeout":60,"timeout":300}}},sort_keys=False))
    else:
        print(f"[mcp_servers.{NAME}]")
        for key in ("command","args"):
            print(key+" = "+json.dumps(cfg[key]))
        print("startup_timeout_sec = 60\ntool_timeout_sec = 300\n# Review and approve this case server in your host before operating it.")
        if cfg["env"]:
            print(f"[mcp_servers.{NAME}.env]")
            for key,value in cfg["env"].items(): print(key+" = "+json.dumps(value))


if __name__ == "__main__":
    main()
