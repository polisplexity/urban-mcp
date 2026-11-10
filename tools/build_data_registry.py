"""Render the proposed data contracts; does not resolve or execute a model."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows(name):
    with (ROOT / "planning" / name).open(encoding="utf-8") as stream:
        return list(csv.DictReader(stream, delimiter="|"))


def write(name, data):
    path = ROOT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    cases = [json.loads(path.read_text(encoding="utf-8")) for path in sorted((ROOT/"cases").glob("*/case.json"))]
    admitted = [case for case in cases if case.get("ready_to_run") and case.get("status") == "admitted"]
    sources = []
    for row in rows("data-sources.tsv"):
        sources.append({**row, "url": row["url"] or None,
            "checked_on": "2026-11-10" if row["evidence"].startswith("publisher-") else None,
            "asset_admission": "per_asset_review_required", "download_implemented": False,
            "license_policy": "Record exact asset terms and attribution; code license does not cover all datasets or weights"})
        implemented = [case["id"] for case in admitted if row["id"] in case.get("source_ids", [])]
        sources[-1].update(download_implemented=bool(implemented), implemented_cases=implemented)
    profiles = []
    for row in rows("data-profiles.tsv"):
        requirements = []
        for raw in row["required_inputs"].split(";"):
            name, formats, source_ids, condition = raw.split("~")
            requirements.append({"id": name, "format_contract": formats,
                "candidate_sources": source_ids.split(","), "required": True,
                "admission_condition": condition})
        profiles.append({"id": row["id"], "scope": "proposed_representative_case_not_every_operation",
            "requirements": requirements, "preparation": row["preparation"],
            "validation": row["validation"], "real_city_blocker": row["city_blocker"],
            "status": "needs_operation_binding"})
    write("registry/sources.json", {"schema_version": "0.1.0", "sources": sources})
    write("registry/data-profiles.json", {"schema_version": "0.1.0", "profiles": profiles})
    tool_document = json.loads((ROOT / "registry/tools.json").read_text(encoding="utf-8"))
    tools = tool_document["tools"]
    for tool in tools:
        supported = [case for case in admitted if case["tool_id"] == tool["id"]]
        if supported:
            tool.update(input_binding_status="verified",engine_runtime_status="verified",reference_case_status="verified",real_city_status="verified_for_declared_scope",ready_to_run=True)
            tool["admitted_scope"] = [{"case_id": case["id"], "operations": case["mcp_tools"], "evidence": case["municipal_case"], "limit": "Only the declared operations/parameters/municipal reference case, not every upstream function or city"} for case in supported]
        elif tool.pop("admitted_scope", None) is not None:
            tool.update(input_binding_status="not_implemented",engine_runtime_status="not_verified",reference_case_status="not_verified",real_city_status="needs_input_review",ready_to_run=False)
    write("registry/tools.json", tool_document)
    by_profile = {profile["id"]: profile for profile in profiles}
    by_source = {source["id"]: source for source in sources}
    doc = ["# Tool data requirements and admitted scopes\n\n",
        "**Status: proposed requirements, not general operational availability.** Each tool has a profile. These describe a first representative case; every operation needs its own native binding and may use a different subset. Dependencies inherit the parent capability's inputs. GTFS is not mandatory for geometric validation, nor HVAC inputs for a daylight calculation. Historical research descriptions retain their original language.\n\n",
        f"Candidate sources are not automatically downloaded, licensed or suitable assets. Operator sources require a specific project and authorization. {sum(t['ready_to_run'] for t in tools)} entry/entries have case-scoped admission; the rest retain `ready_to_run=false`. Admission does not cover every upstream function. See [the master test record](../../MASTER_TEST_RECORD.md) for executed evidence.\n\n",
        "| Tool | Proposed profile | Status |\n|---|---|---|\n"]
    for tool in tools:
        binding = "case-scoped admission" if tool["ready_to_run"] else "binding pending"
        doc.append(f"| [{tool['repository']}](#data-{tool['id']}) | `{tool['data_profile']}` | {tool['execution_role']}; {binding} |\n")
    for tool in tools:
        profile = by_profile[tool["data_profile"]]
        doc.append(f"\n<a id=\"data-{tool['id']}\"></a>\n\n## {tool['repository']}\n\n")
        doc.append(f"- **Original interface:** {tool['original_interface']}\n")
        doc.append(f"- **Profile scope:** {tool['execution_role']}. {tool['data_note']}\n")
        for scope in tool.get("admitted_scope", []):
            doc.append(f"- **Scoped executable case:** [{scope['case_id']}](../../cases/{scope['case_id']}/README.md); operations: {', '.join(scope['operations'])}. The generic profile below remains a proposal for other operations.\n")
        doc.append("\n| Candidate input | Format/contract | Candidate sources | Admission condition |\n|---|---|---|---|\n")
        for req in profile["requirements"]:
            links = []
            for sid in req["candidate_sources"]:
                source = by_source[sid]
                links.append(f"[{source['name']}]({source['url']})" if source["url"] else source["name"] + " (configuration required)")
            doc.append(f"| {req['id']} | {req['format_contract']} | {'; '.join(links)} | {req['admission_condition']} |\n")
        doc.append(f"\n- **Preparation required:** {profile['preparation']}\n")
        doc.append(f"- **Validation required:** {profile['validation']}\n")
        doc.append(f"- **Real-city blocker:** {profile['real_city_blocker']}\n")
        if tool["ready_to_run"]:
            doc.append("- **Native binding:** verified only for the linked case and operations; the generic profile does not admit additional operations.\n")
        else:
            doc.append("- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.\n")
        doc.append(f"- **Project critique:** {tool['critical_limit']}\n")
        doc.append("- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.\n")
    path = ROOT / "docs/data/tool-data-matrix.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(doc), encoding="utf-8")
    print(f"Rendered {len(tools)} tools, {len(profiles)} proposed profiles, {len(sources)} source channels.")


if __name__ == "__main__":
    main()
