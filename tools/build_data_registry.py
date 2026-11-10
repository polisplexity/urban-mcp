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
    sources = []
    for row in rows("data-sources.tsv"):
        sources.append({**row, "url": row["url"] or None,
            "checked_on": "2026-11-10" if row["evidence"].startswith("publisher-") else None,
            "asset_admission": "per_asset_review_required", "download_implemented": False,
            "license_policy": "Record exact asset terms and attribution; code license does not cover all datasets or weights"})
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
    tools = json.loads((ROOT / "registry/tools.json").read_text(encoding="utf-8"))["tools"]
    by_profile = {profile["id"]: profile for profile in profiles}
    by_source = {source["id"]: source for source in sources}
    doc = ["# Matriz inicial de datos por herramienta\n\n",
        "**Estado: propuesta de requisitos, no disponibilidad operativa.** Cada fila tiene una ficha individual. Los perfiles agrupan datos de un primer caso representativo; cada operación necesita un binding nativo y puede requerir un subconjunto diferente. Las dependencias heredan datos del paquete padre. No se exige GTFS para una validación geométrica ni HVAC para un cálculo de iluminación.\n\n",
        "Fuentes candidatas no equivalen a assets descargados, licenciados o adecuados. Las fuentes de operador necesitan proyecto y autorización concretos. `ready_to_run=false` en los 229 candidatos.\n\n",
        "| Herramienta | Perfil propuesto | Estado |\n|---|---|---|\n"]
    for tool in tools:
        doc.append(f"| [{tool['repository']}](#data-{tool['id']}) | `{tool['data_profile']}` | {tool['execution_role']}; binding pendiente |\n")
    for tool in tools:
        profile = by_profile[tool["data_profile"]]
        doc.append(f"\n<a id=\"data-{tool['id']}\"></a>\n\n## {tool['repository']}\n\n")
        doc.append(f"- **Interfaz original:** {tool['original_interface']}\n")
        doc.append(f"- **Alcance de esta ficha:** {tool['execution_role']}. {tool['data_note']}\n")
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
        doc.append("- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.\n")
        doc.append(f"- **Crítica propia del proyecto:** {tool['critical_limit']}\n")
        doc.append("- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.\n")
    path = ROOT / "docs/data/tool-data-matrix.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(doc), encoding="utf-8")
    print(f"Rendered {len(tools)} tools, {len(profiles)} proposed profiles, {len(sources)} source channels.")


if __name__ == "__main__":
    main()
