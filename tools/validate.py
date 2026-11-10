"""Validate proposal integrity; never infer scientific/runtime readiness."""
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_url(url):
    if url is None:
        return True
    parsed = urlsplit(url)
    return parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username and not parsed.password


def validate_data(tools, sources, profiles, cases, root=ROOT):
    errors = []
    definitions = read(root / "schemas/registry.schema.json")
    def validate(document, schema, label):
        for error in Draft202012Validator(schema).iter_errors(document):
            errors.append(f"{label} {error.json_path}: {error.message}")
    for kind, documents in [("tool", tools), ("source", sources), ("profile", profiles)]:
        ids = [item.get("id") for item in documents]
        if len(ids) != len(set(ids)):
            errors.append(f"Duplicate {kind} id")
        for item in documents:
            validate(item, {"$ref": f"#/$defs/{kind}", "$defs": definitions["$defs"]}, f"{kind}:{item.get('id')}")
    source_ids = {item["id"] for item in sources}
    profile_ids = {item["id"] for item in profiles}
    tool_ids = {item["id"] for item in tools}
    for source in sources:
        if not check_url(source["url"]):
            errors.append(f"Source URL must be HTTPS without credentials: {source['id']}")
    for profile in profiles:
        ids = [r["id"] for r in profile["requirements"]]
        if len(ids) != len(set(ids)):
            errors.append(f"Duplicate input id in {profile['id']}")
        for req in profile["requirements"]:
            for sid in req["candidate_sources"]:
                if sid not in source_ids:
                    errors.append(f"Unknown source {sid} in {profile['id']}")
    for tool in tools:
        if tool["data_profile"] not in profile_ids:
            errors.append(f"Unknown data profile for {tool['id']}")
        if not check_url(tool["url"]):
            errors.append(f"Invalid public tool URL: {tool['id']}")
        if tool["ready_to_run"]:
            if tool["execution_role"] != "candidate" or any(tool[key] != "verified" for key in ("input_binding_status", "engine_runtime_status", "reference_case_status")):
                errors.append(f"Unverified runtime cannot be ready: {tool['id']}")
            if not any(c.get("tool_id") == tool["id"] and c.get("ready_to_run") for c in cases):
                errors.append(f"Ready tool requires an admitted executable case: {tool['id']}")
    for case in cases:
        validate(case, read(root / "schemas/case.schema.json"), f"case:{case.get('id')}")
        if case["tool_id"] not in tool_ids:
            errors.append(f"Unknown tool for case {case['id']}")
        names = [asset["file"] for asset in case["assets"]]
        if len(names) != len(set(names)):
            errors.append(f"Duplicate asset filename in {case['id']}")
        for asset in case["assets"]:
            if asset["source_id"] not in source_ids or not check_url(asset["url"]):
                errors.append(f"Invalid source/URL in {case['id']}")
        if case["ready_to_run"] and (case["status"] != "admitted" or case["blockers"] or any(case[key] != "verified" for key in ("engine_status", "mcp_binding_status", "expected_result_status")) or any(a["license_status"] != "reviewed_for_declared_use" for a in case["assets"])):
            errors.append(f"Case still has admission blockers: {case['id']}")
    return errors


def load_all(root=ROOT):
    tools = read(root / "registry/tools.json")["tools"]
    sources = read(root / "registry/sources.json")["sources"]
    profiles = read(root / "registry/data-profiles.json")["profiles"]
    cases = [read(path) for path in sorted((root / "cases").glob("*/case.json"))]
    return tools, sources, profiles, cases


def main():
    data = load_all()
    errors = validate_data(*data)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(json.dumps({"status": "passed", "tools": len(data[0]), "sources": len(data[1]), "profiles": len(data[2]), "cases": len(data[3]), "scientific_runtime_verified_by_this_check": False}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
