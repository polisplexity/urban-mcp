# Independent third-city historical SUMO reproduction

The initial Bologna/Ingolstadt case is available on `main` after merged PR #43. Final-product
qualification requires a person outside its original implementation and
initial testing team. A different model/agent launched by that team does not
meet the [policy](../product-qualification.md). Issue #41 is the separate
walking reproduction task.

Choose a distinct municipality with a permitted published model or authorized
local network, time-specific demand, vehicle types and required signal/stops.
Document missing independent field observations and retain `forecast_admitted=false`
unless a separately reviewed calibration/validation case establishes more.
The current case admits historical computational reproduction, not operational
traffic advice. A useful contribution can expose an unsupported assumption or
source model-quality failure instead of manufacturing a successful forecast.

The public reproduction PR must include:

- Independent operator identity/relationship to the initial team and municipality/study area.
- Exact assets, rights, attribution, publisher revision/hash, source dates,
  coordinates/units, raw-versus-modeled demand and missing inputs.
- Reproducible live acquisition or permitted snapshot, native configuration,
  signal/additional-file order, departure/initialization/seed/processing choices.
- A municipal question and explicit corridor/cohort/counterfactual contract.
- Native XML/state/log oracles, all exposed MCP tools/resources/prompts,
  censored/teleport accounting and complete comparison CSVs.
- Separate fresh Codex and Hermes workspaces using the public task without
  expected answers; complete public payload/page/hash/JSON reviews and manual
  answer-hash-bound prose verdicts, including failures and recovery.
- Docker/client/start instructions and a master entry saying what passed,
  what failed, why the test matters, and exactly what remains unsupported.
- A request for public maintainer review of evidence and independent status.

Keep credentials, private configuration/databases, reasoning and bulk caches
out of Git. Use the [SUMO guide](../../cases/two-city-sumo/README.md),
[findings](../../cases/two-city-sumo/findings.md) and
[operation coverage](../../cases/two-city-sumo/functionality.md).
Keep `product_qualified=false`, the master and qualification register pending
until accepted review. A later promotion change must name the final repository
or release destination and exact admitted scope.
