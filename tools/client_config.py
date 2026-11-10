"""Emit a client-neutral stdio configuration; no agent or credential dependency."""
import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = "urban_mcp_helsinki"


def server_name(capability="inventory"):
    return {"inventory": NAME, "walking": "urban_mcp_walking", "vegetation": "urban_mcp_vegetation", "sumo":"urban_mcp_sumo", "swmm":"urban_mcp_swmm"}[capability]


def wsl_path(path):
    value = str(path.resolve())
    if len(value) < 3 or value[1:3] != ":\\":
        raise ValueError("WSL mode requires a Windows drive path")
    return "/mnt/" + value[0].lower() + "/" + value[3:].replace("\\", "/")


def server_config(data_dir=None, wsl_distro=None, capability="inventory"):
    profile, service, variable, default_folder = {"walking": ("walking", "walking-mcp", "URBAN_MCP_WALKING_WORKDIR", "walking"), "inventory": ("municipal", "municipal-mcp", "URBAN_MCP_WORKDIR", "helsinki"), "vegetation": ("vegetation", "vegetation-mcp", "URBAN_MCP_VEGETATION_WORKDIR", "vegetation"), "sumo":("sumo","sumo-mcp","URBAN_MCP_SUMO_WORKDIR","sumo"), "swmm":("swmm","swmm-mcp","URBAN_MCP_SWMM_WORKDIR","swmm")}[capability]
    data = Path(data_dir).resolve() if data_dir else ROOT / ".urban-mcp" / default_folder
    data.mkdir(parents=True, exist_ok=True)
    if wsl_distro:
        command = "wsl.exe"
        args = ["-d", wsl_distro, "--cd", wsl_path(ROOT), "--exec", "env", variable+"="+wsl_path(data), "docker", "compose", "--profile", profile, "run", "--rm", "-T", "--no-deps", service]
        env = {}
    else:
        command = "docker"
        args = ["compose", "--project-directory", str(ROOT), "--profile", profile, "run", "--rm", "-T", "--no-deps", service]
        env = {variable: str(data)}
        if hasattr(os, "getuid"):
            env.update(URBAN_MCP_UID=str(os.getuid()), URBAN_MCP_GID=str(os.getgid()))
    return {"command": command, "args": args, "env": env, "cwd": str(ROOT)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=["mcp-json", "codex", "hermes"], default="mcp-json")
    parser.add_argument("--data-dir")
    parser.add_argument("--wsl-distro")
    parser.add_argument("--capability", choices=["inventory", "walking", "vegetation", "sumo", "swmm"], default="inventory")
    args=parser.parse_args()
    cfg=server_config(args.data_dir,args.wsl_distro,args.capability)
    name=server_name(args.capability)
    if args.format == "mcp-json":
        print(json.dumps({"mcpServers":{name:cfg}},indent=2))
    elif args.format == "hermes":
        import yaml
        if sys.platform == "linux" and not args.wsl_distro:
            # Hermes 0.18.2 does not forward a configured cwd to its stdio
            # watchdog. GNU env changes directory before Docker starts.
            cfg={**cfg,"command":"/usr/bin/env","args":["-C",str(ROOT),cfg["command"],*cfg["args"]]}
        print(yaml.safe_dump({"mcp_servers":{name:{**cfg,"connect_timeout":60,"timeout":420 if args.capability in {"sumo","swmm"} else 300}}},sort_keys=False))
    else:
        print(f"[mcp_servers.{name}]")
        for key in ("command","args","cwd"):
            print(key+" = "+json.dumps(cfg[key]))
        print("startup_timeout_sec = 60\ntool_timeout_sec = "+str(420 if args.capability in {"sumo","swmm"} else 300)+"\n# Review and approve this case server in your host before operating it.")
        if cfg["env"]:
            print(f"[mcp_servers.{name}.env]")
            for key,value in cfg["env"].items(): print(key+" = "+json.dumps(value))


if __name__ == "__main__":
    main()
