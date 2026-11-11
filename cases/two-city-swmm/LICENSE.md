# Code, model and observation rights

The repository's MIT license covers its original integration code. It does
not relicense third-party engines, adapters, datasets or model outputs.

| Component / exact source | Reviewed rights and retained notices |
| --- | --- |
| EPA SWMM C 5.2.4, `07c371f8a0d477da1d9d4e7c0d75719664f62fec` | Public domain as stated in the original EPA README; original disclaimer retained in `/opt/epa`. No EPA endorsement implied. |
| PySWMM 2.2.0 | BSD-2-Clause; [notice](../../adapters/swmm/licenses/pyswmm-BSD-2-Clause.txt), upstream author/copyright retained. |
| swmm-toolkit 0.17.0 | Installed metadata declares `CC0-1.0 AND (MIT OR Apache-2.0)`; original distribution license, authors and OpenMP notices remain installed. |
| PySWMM MCP `a4db37b45d3b30dcfbd80fc0162a8238e727a80f` | Apache-2.0; [notice](../../adapters/swmm/licenses/pyswmm-mcp-Apache-2.0.txt). Pristine source remains `/opt/pyswmm-mcp`; marked runtime changes are made in a separate copy. |
| swmm-api 0.4.74 / official Python MCP SDK 2.3.0 | MIT; original installed notices remain present. They are dependencies, not a new municipal data license. |
| kLabUM SWMM-MCP-PUB / agentic-swmm-workflow | MIT source reviewed and downloaded with pinned archive hashes for isolated audits. Neither entire alternative server is claimed as executed or incorporated as this runtime. |
| Bellinge model, DOI `10.11583/DTU.12513428.v2` | CC BY 4.0. Credit Pedersen et al. and the original dataset record. Only the original INP is redistributed; the converted local rain file is excluded. |
| Original Bellinge rain-gauge collection, DOI `10.11583/DTU.12509774.v2` | **CC BY-NC 4.0; excluded.** A differently licensed model archive is not used to silently relabel that collection. |
| DMI climateData hourly `acc_precip`, station 06120 | CC BY 4.0 under [DMI Open Data terms](https://www.dmi.dk/friedata/dokumentation/terms-of-use). Credit DMI; original responses and QA metadata retained. |
| Tuindorp development INP, DOI `10.4121/fec1e3de-9586-4a61-b3a1-02382592e52c.v1` | CC BY 4.0, copyright Jorge Alexander Garzón Díaz (2024). Credit Garzón, Kapelan, Langeveld and Taormina. The publisher README/rights remain bundled. |
| KNMI hourly station 260 archive | CC0 under [KNMI copyright terms](https://www.knmi.nl/copyright), with publisher-requested attribution: source KNMI; KNMI was not involved in and does not necessarily endorse this derived work. Archive warning against climate-trend use retained. |

GNU libgomp's distribution copyright and GPL/runtime notices are retained
under `/opt/licenses` in the built image. Runtime/license file hashes are in
[the source audit](evidence/upstream-audit.json). Apt/base dependencies retain
their distribution terms; whole-OS bit-for-bit reproducibility is not claimed.

Snapshots and derived model geometry/results retain dataset attribution.
They contain no utilities-private data, original noncommercial Bellinge rain,
learned GNN weights, provider credentials or host reasoning. A new contributor
must review rights for each new municipality's actual model and observations.
