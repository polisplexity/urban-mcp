# Host artifact acceptance and narrative review

The primary implementing agent reviewed the observed answers against the actual CSV rows, keyed paths and tool receipts. This is not an independent municipal field review. All four final workspaces restored the pinned inputs, operated all 15 tools and reproduced baseline/closure CSVs, maps and GraphML exactly. **That establishes workflow/artifact compatibility, not automatic acceptance of each agent's prose.**

| City / host | Recorded case calls | Native artifacts | Written interpretation |
| --- | ---: | --- | --- |
| Helsinki / Codex CLI, configured `gpt-6.1-sol` | 36, including host resource helpers | Exact match | Passed for this observed brief |
| Amsterdam / Codex CLI, configured `gpt-6.1-sol` | 35, including host resource helpers | Exact match | Passed for this observed brief |
| Helsinki / Hermes, `claude-sonnet-4-6` | 26, including host resource/prompt helpers | Exact match | Failed factual narrative review; retain with corrections below |
| Amsterdam / Hermes, `claude-sonnet-4-6` | 24, including host resource/prompt helpers | Exact match | Failed factual narrative review; retain with corrections below |

The [machine-readable review](narrative-review.json) binds each verdict to the observed answer's SHA-256. `agents.json` links the mechanical checks to that review. Host versions: Codex CLI 0.167.0-alpha.3.2; Hermes 0.18.2 / runtime revision `b61c033c0bbed79e7f5ae2f44cdbff30ade6ee87`, Python 3.11.15. The MCP runs the separately pinned Python 3.12.14 container. Models use existing host authentication; no key or provider configuration is part of this repository.

## Helsinki: correct threshold identities

Hermes reports correct aggregate counts (45 → 40 within threshold) but labels several individual objects incorrectly. The actual five threshold crossings are:

| OSM origin object | Baseline total m | Closure total m |
| --- | ---: | ---: |
| `node/8862204483` | 961.726 | 1,241.224 |
| `node/8862204485` | 958.818 | 1,238.316 |
| `way/1038696462` | 977.964 | 1,471.872 |
| `way/38192458` | 1,055.248 | 1,340.131 |
| `way/592362656` | 1,058.541 | 1,292.431 |

`node/1017984829` remains within threshold at 782.194 m, and `way/128161235` remains within at 669.525 m. The five newly outside objects have detours of **233.890–493.909 m**. The larger 556.338/649.035 m detours belong to objects that remain within threshold. Check [baseline.csv](helsinki/baseline.csv) and [closure.csv](helsinki/closure.csv), not the raw prose's per-object annotations.

The raw answer also calls a routed object both within threshold and over 1,200 m, and says it verified exported topology by reload. The agent trace only exports and reads a receipt; the native/protocol suite performs the actual round-trip check. Keep those layers separate.

## Amsterdam: alternatives can overlap

Hermes describes its second k-shortest route as an alternative if the primary edge is removed. Both returned paths actually include node pair `(46386552,12534903767)`. The second route's total is **284.329 m**; it is not usable under that link-removal scenario. The separately solved closure route for `node/2741066971` is **513.679 m**, and the closure CSV is the authority for that question. The answer otherwise reports the correct 22 → 22 threshold count and five detours, but that incorrect alternative-route claim prevents admitting the prose as a reliable municipal brief. It also exceeds the requested short format.

## What this changes in the contribution contract

Preserve both successes and failures. Require per-object factual checks rather than matching only aggregate numbers. Treat k-shortest paths as potentially overlapping, and solve the actual closure scenario before claiming an available diversion. Distinguish unknown access, representative points and unverified connectors from field conditions. A useful next interface improvement is a comparison table with explicit before/after threshold booleans and per-route closed-link membership; it needs its own native/MCP/host tests rather than being declared fixed here.

The [project-authored municipal findings](../findings.md) use the checked artifacts and corrections above. The workflow is admitted for reproducible computation in the declared study areas. **Unsupervised municipal recommendations from Hermes prose are not admitted.** Codex's successful observed briefs are also not a guarantee for future runs. Neither host establishes actual public admission, safety, wheelchair suitability or complete municipal coverage.
