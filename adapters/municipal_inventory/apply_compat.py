"""Compatibility delta for the pinned GDAL-MCP/FastMCP 2.12.3 combination.

RFC6570 query expansions are accepted at registration but crash the runtime's
regex matcher. Keep path parameters and documented function defaults instead.
No geometry operation is replaced. Exact replacement counts prevent silent drift.
"""
import json
from pathlib import Path
import sys

ROOT = Path(sys.argv[1])
changes = {
    "resources/catalog/all.py": "{?limit,include_hidden,extensions}",
    "resources/catalog/vector.py": "{?limit,include_hidden,extensions}",
    "resources/catalog/raster.py": "{?limit,include_hidden,extensions}",
    "resources/catalog/by_crs.py": "{?kind,include_hidden}",
    "resources/metadata/band.py": "{?include_statistics}",
}
for filename, expression in changes.items():
    path = ROOT / filename
    content = path.read_text(encoding="utf-8")
    if content.count(expression) != 1:
        raise RuntimeError(f"Upstream drift: expected exactly one expansion in {filename}")
    path.write_text(content.replace(expression, ""), encoding="utf-8")

def replace(filename, old, new):
    path = ROOT / filename
    content = path.read_text(encoding="utf-8")
    if content.count(old) != 1:
        raise RuntimeError(f"Upstream drift: expected one exact block in {filename}")
    path.write_text(content.replace(old, new), encoding="utf-8")

for kind in ("all", "vector", "raster"):
    filename = f"resources/catalog/{kind}.py"
    replace(filename, f'        kind="{kind}",', f'        kind="{kind}",\n        subpath=subpath,')
    replace(filename, "return response.to_dict()", "return response.model_dump()")
replace("resources/catalog/base.py", "from fastmcp import Context", "from fastmcp import Context\nfrom pathlib import Path\nfrom src.config import get_workspace_root")
replace("resources/catalog/base.py", '    kind: Literal["all", "raster", "vector"],', '    kind: Literal["all", "raster", "vector"],\n    subpath: str = "",\n    limit: int | None = None,')
replace("resources/catalog/base.py", "    return CatalogResponse(", '''    if subpath:
        workspace = get_workspace_root().resolve()
        selected = (workspace / subpath).resolve()
        if not selected.is_relative_to(workspace):
            raise ValueError("Catalog subpath is outside the workspace")
        entries = [entry for entry in entries if Path(entry.ref.path).resolve().is_relative_to(selected)]
    if limit is not None:
        if limit < 1:
            raise ValueError("Catalog limit must be positive")
        entries = entries[:limit]
    return CatalogResponse(''')

path = ROOT / "tools/raster/convert.py"
content = path.read_text(encoding="utf-8")
start = content.index("            # Build overviews if requested (must reopen in update mode)")
end = content.index("            # Get output file size", start)
content = content[:start] + content[end:]
anchor = "                        dst.update_tags(band_idx, **src.tags(band_idx))"
assert content.count(anchor) == 1
inside = '''

                    # Build before closing the writer, so the COG driver optimizes
                    # the final file without reopening and breaking its layout.
                    overviews_built = []
                    if options.overviews:
                        method = getattr(Resampling, options.overview_resampling.lower(), None)
                        if method is None:
                            raise ToolError("Unsupported overview resampling method")
                        dst.build_overviews(options.overviews, method)
                        overviews_built = options.overviews'''
path.write_text(content.replace(anchor, anchor + inside), encoding="utf-8")
replace("tools/reflection/store_justification.py", "    justification: dict,", "    justification: Justification,")
replace("tools/reflection/store_justification.py", "import logging", "import logging\nfrom typing import Literal")
replace("tools/reflection/store_justification.py", "    domain: str,", '    domain: Literal["crs_datum", "resampling", "hydrology", "aggregation", "spatial_query"],')
print(json.dumps({"deltas": ["resource-template-query-expansion", "catalog-argument-serialization-and-subpath", "COG-overview-writer-lifecycle", "typed-justification-schema"], "geometry_algorithms_replaced": False}))
