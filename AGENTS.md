# Working on Urban MCP

This branch proposes a contribution plan, input/source contracts and reference cases. It does not ship admitted scientific adapters. Keep that distinction visible.

- Preserve the original tool and reuse its supported API/MCP before writing another adapter. The product implementation language is not selected by the Python maintenance utilities.
- A source page is not an admitted dataset. Record exact assets, rights, versions/hashes, area/time, units/CRS, preparation and unresolved inputs.
- Do not infer physical parameters, identities or calibration silently. Synthetic examples must remain distinguishable from real-city evidence.
- Do not promote readiness from a successful metadata check, Docker startup or tools/list alone. Native, MCP and agent evidence are separate milestones.
- Keep credentials, operator datasets, caches, generated outputs and private product code outside Git. Use only public research records in this repository.
- New skills support the user's existing agent; they do not grant additional permissions, require a provider or override host/user instructions.
- Validate changes with `python tools/validate.py`, `python -m unittest discover -s tests` and the affected case's data preflight. Rebuild generated registries/docs after changing planning TSVs.
