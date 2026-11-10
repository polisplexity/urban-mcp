# Working on Urban MCP

The research registry is a proposal, and the Helsinki municipal reference package has an executable Docker/MCP implementation. Admit only the operations and cases supported by committed evidence; do not generalize their results to the whole registry or every function of GDAL/GeoPandas.

- Preserve the original tool and reuse its supported API/MCP before writing another adapter. The product implementation language is not selected by the Python maintenance utilities.
- A source page is not an admitted dataset. Record exact assets, rights, versions/hashes, area/time, units/CRS, preparation and unresolved inputs.
- Do not infer physical parameters, identities or calibration silently. Synthetic examples must remain distinguishable from real-city evidence.
- Do not promote readiness from a successful metadata check, Docker startup or tools/list alone. Native, MCP and agent evidence are separate milestones.
- Keep credentials, operator datasets, caches, bulk generated outputs and private product code outside Git. Compact reviewed public evidence and manifests belong in the case; larger permitted data snapshots/artifacts go in versioned releases with attribution.
- New skills support the user's existing agent; they do not grant additional permissions, require a provider or override host/user instructions.
- Validate changes with `python tools/validate.py`, `python -m unittest discover -s tests` and the affected case's data preflight. Rebuild generated registries/docs after changing planning TSVs.
- For Helsinki changes, run the Docker native/MCP suite. Test all exposed tools and resource/prompt families. Agent testing uses independent workspaces and existing host authentication, with no messaging connectors. A tool script passing is not equivalent to a successful LLM workflow; review both traces and conclusions.
