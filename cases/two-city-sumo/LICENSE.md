# License and attribution boundaries

Urban MCP's original binding, checks and documentation use the repository MIT
license. That license does not replace any original software or data terms.

| Material | Exact original source | Terms and attribution |
| --- | --- | --- |
| SUMO simulator, TraCI and sumolib 1.28.0 | [Eclipse SUMO](https://github.com/eclipse-sumo/sumo/tree/daf91b5578901d599ac9af53f49d26eeb9aefc3b) | EPL-2.0; original notices remain in the wheel/runtime. See the original distribution for its additional notices |
| Reused original MCP source | [XRDS76354/SUMO-MCP-Server](https://github.com/XRDS76354/SUMO-MCP-Server/tree/6b62a25c1b13751d636309a03e4388594fcd7620) | MIT; the complete checksum-pinned checkout and original LICENSE remain in the image |
| Bologna Acosta model and original files | [DLR-TS/sumo-scenarios](https://github.com/DLR-TS/sumo-scenarios/tree/79d2e1837a9683617393c69aaf754c6bc812e3f8) | EPL-2.0; DLR Institute of Transportation Systems, Comune di Bologna and iTETRIS scenario authors. Original LICENSE is in the snapshot and readable through MCP |
| Ingolstadt simulation model and original files | [TUM-VT/sumo_ingolstadt](https://github.com/TUM-VT/sumo_ingolstadt/tree/e0a95deebe200ff81b6705044d66310d6266d42b) | The publisher explicitly licenses `simulation` under Apache-2.0 in [LICENSE.md](https://github.com/TUM-VT/sumo_ingolstadt/blob/e0a95deebe200ff81b6705044d66310d6266d42b/LICENSE.md). Preserve TUM-VT/IngTAS authors' notices. This is separate from any repository code license |
| AgentSUMO and legacy source probes | Links and exact revisions in [the audit](upstream-audit.md) | MIT originals; probes download pinned source and preserve hashes. They execute isolated methods with declared stubs, not full installations |
| Simulation outputs, source receipts and maps | Exact input licenses and provenance above | Retain original data attribution and each city's source-model terms when redistributing derived material. Simulated vehicle IDs are modeled identifiers, not observations of people or registration plates |

The [data prerelease](https://github.com/polisplexity/urban-mcp/releases/tag/data-sumo-20261110)
contains original permitted inputs, their licenses and manifests. It is not a
final product release. GUI-only optional inputs are explicitly excluded in
the recipe; required signals, vehicle types, routes, stops and detectors are
included. No raw municipal detector counts, private VISSIM project or newly
validated calibration is implied by access to a published model.
