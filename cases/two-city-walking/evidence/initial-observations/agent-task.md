# Independent municipal walking test: {{city}}

You are reviewing an exploratory school-to-library walking-access case for {{city}}. Use only the `urban_mcp_walking` MCP server. Do not use a shell, browser, local-file tools, other connectors or an expected-answer file. Work entirely in English.

1. Discover the case, data status and interpretation limits. Restore the pinned snapshot for this city through MCP into this fresh workspace. Inspect graph identity and source/attribution, the school and library catalog, and snap quality.
2. Run an unmodified baseline with run_id `agent-baseline`, distance threshold 1200 m and assumed walking speed 4.8 km/h. Read its accessibility CSV and a page of its keyed route export. Report the exact denominator, routed/within/outside/unreachable/snap-rejected counts and units. Do not equate facility objects with pupils or residents.
3. Inspect a routed origin and its selected destination using the route, snap, node and edge operations. Request two alternative routes, network statistics and a 1200 m reachable-node count. Explain what these outputs measure and what they do not.
4. Choose the baseline's suggested closure pair (u,v); it is a reproducible stress-test link, not a real-world closure. Run `agent-closure` with the same threshold/speed, remove both directions of that pair and compare with baseline. Read the scenario CSV. Report affected objects and threshold changes, including a zero change if that is what the model returns.
5. Render the baseline map, export its GraphML and inspect their receipts. Retrieve the municipal review prompt if the host exposes prompts; if it does not, state that limitation without claiming to have retrieved it. Try an invalid remote coordinate with the snap operation and explain the rejection.
6. Finish with a concise municipal brief: findings supported by the artifacts, a practical next investigation, the exact study scope/date/input identity, source license/attribution, assumptions and missing evidence before a real intervention. Include the run IDs and artifact hashes needed to check your work. Do not claim wheelchair access, actual travel time, citywide coverage or an observed disruption.

No expected numerical answers are provided. A successful process exit is insufficient: your calls, artifacts and interpretation will be checked independently.
