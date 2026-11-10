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
    doc = ["# Matriz inicial de datos por herramienta\n\n",
        "**Estado: propuesta de requisitos, no disponibilidad operativa.** Cada fila tiene una ficha individual. Los perfiles agrupan datos de un primer caso representativo; cada operación necesita un binding nativo y puede requerir un subconjunto diferente. Las dependencias heredan datos del paquete padre. No se exige GTFS para una validación geométrica ni HVAC para un cálculo de iluminación.\n\n",
        f"Fuentes candidatas no equivalen a assets descargados, licenciados o adecuados. Las fuentes de operador necesitan proyecto y autorización concretos. {sum(t['ready_to_run'] for t in tools)} entrada(s) con alcance admitido por caso; el resto conserva `ready_to_run=false`. La admisión no abarca todas las funciones del upstream.\n\n",
        "| Herramienta | Perfil propuesto | Estado |\n|---|---|---|\n"]
    for tool in tools:
        binding = "alcance admitido por caso" if tool["ready_to_run"] else "binding pendiente"
        doc.append(f"| [{tool['repository']}](#data-{tool['id']}) | `{tool['data_profile']}` | {tool['execution_role']}; {binding} |\n")
    for tool in tools:
        profile = by_profile[tool["data_profile"]]
        doc.append(f"\n<a id=\"data-{tool['id']}\"></a>\n\n## {tool['repository']}\n\n")
        doc.append(f"- **Interfaz original:** {tool['original_interface']}\n")
        doc.append(f"- **Alcance de esta ficha:** {tool['execution_role']}. {tool['data_note']}\n")
        for scope in tool.get("admitted_scope", []):
            doc.append(f"- **Caso ejecutable delimitado:** [{scope['case_id']}](../../cases/{scope['case_id']}/README.md); operaciones: {', '.join(scope['operations'])}. La ficha genérica siguiente sigue siendo propuesta para otras operaciones.\n")
        doc.append("\n| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |\n|---|---|---|---|\n")
        for req in profile["requirements"]:
            links = []
            for sid in req["candidate_sources"]:
                source = by_source[sid]
                links.append(f"[{source['name']}]({source['url']})" if source["url"] else source["name"] + " (por configurar)")
            doc.append(f"| {req['id']} | {req['format_contract']} | {'; '.join(links)} | {req['admission_condition']} |\n")
        doc.append(f"\n- **Preparación que hay que resolver:** {profile['preparation']}\n")
        doc.append(f"- **Validación requerida:** {profile['validation']}\n")
        doc.append(f"- **Faltante para un caso real:** {profile['real_city_blocker']}\n")
        if tool["ready_to_run"]:
            doc.append("- **Binding nativo:** comprobado únicamente para el caso y operaciones enlazados; la ficha genérica no admite otras operaciones.\n")
        else:
            doc.append("- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.\n")
        doc.append(f"- **Crítica propia del proyecto:** {tool['critical_limit']}\n")
        doc.append("- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.\n")
    path = ROOT / "docs/data/tool-data-matrix.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(doc), encoding="utf-8")
    print(f"Rendered {len(tools)} tools, {len(profiles)} proposed profiles, {len(sources)} source channels.")


if __name__ == "__main__":
    main()
