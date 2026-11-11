Use only the urban_mcp_swmm MCP in a fresh workspace for **{{city}}**.
This is a narrow supplementary interface test, not a full municipal result
or a replacement for earlier observed answers. Do not use shell, web, scripts,
other MCPs or previous answers. Write in English.

1. Call swmm_status, restore the city snapshot, prepare and inspect the case.
2. Create the returned **inspection.inp**, start its session and retain the
   exact returned subcatchment ID. Do not open a second session.
3. Call simulation_observe with exactly this request shape, replacing the ID:
   `observe={"subcatchments":[{"id":"RETURNED_ID","fields":["rainfall","runoff"]}]}`.
   These are **live fields**. `runoff_rate` is a binary-output vocabulary name
   and must not be substituted for live `runoff`.
4. Call simulation_step with advance_seconds=30 and the **same observe**
   request. Require both fields in the actual returned observation.
5. Read its exact returned session resource_uri while open; stop and close
   the session. Finish with swmm_status. Preserve any failure/recovery.

Finish with at most 80 prose words and one JSON block containing exactly:
`city`, `subcatchment_id`, `initial_rainfall`, `initial_runoff`,
`after_step_rainfall`, `after_step_runoff`, `session_closed` (true),
`forecast_admitted` (false). Values must come from actual observations;
do not invent expected numbers or describe them as field measurements.
