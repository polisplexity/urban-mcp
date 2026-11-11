# Original-code review and justified integration

We reviewed code before selecting an adapter. Numerical SWMM remains the
original engine. The selected framework follows the reusable MCP's own
official Python SDK; it is not a project-wide language mandate.

| Original project / pinned source | Existing behavior found in code | Integration decision |
| --- | --- | --- |
| EPA Stormwater-Management-Model `07c371f8a0d477da1d9d4e7c0d75719664f62fec` | C 5.2.4 hydrology/hydraulics, original `runswmm`, reports and binary outputs. `gage.c` interprets VOLUME at interval start; `swmm_getMassBalErr` is valid after end and before close. | Compile the original CLI as an independent oracle. No routing, runoff, controls, node/pipe physics or report formulas are rewritten. Keep native and toolkit libraries isolated. |
| `foundanotusedname/pyswmm-mcp` `a4db37b45d3b30dcfbd80fc0162a8238e727a80f` | 18 tools, seven resource families; process isolation, staged dependencies/hashes, bounded output queries, interactive controls/hotstarts, cancellable tasks, worker limits and persistent run metadata. README scopes it as a trusted Windows alpha. | Reuse those functions/resources rather than recreate them. Demonstrate Linux operation with actual original tests and city cases; mark the small portability/metadata fixes separately. |
| `kLabUM/SWMM-MCP-PUB` `0c299b24196d1c8c32e92e8d4437958f237e4a88` | Third-party FastMCP 3.1 lock, upload/edit/run/report/plot tools and MCP Apps. `duplicate_model` uses unquoted shell `cp`; any existing `.out` suppresses a rerun. Storage argument is named cubic feet but used as native volume; `change_storm` clears the entire TIMESERIES section and generates a synthetic SCS storm. | Preserve credit for existing functionality. Do not treat synthetic-storm generation or CLI plot receipts as observed rain/verified visual display. This stack is not selected for the municipal experiment. |
| `Zhonghao1995/agentic-swmm-workflow` `a3bf4f23469cf4252955901176c86b9c94578963` | JS MCP components and a generic Python runner. The runner already has a native timeout and explicit report-error detection. Its compare command reports continuity errors, not full per-node overflow/hydrograph equivalence. | Acknowledge existing safeguards. Do not import its LLM orchestration or infer pipe parameters from GIS. Per-node comparison/source bindings remain a demonstrated missing layer. |
| PySWMM 2.2.0 / swmm-toolkit 0.17.0 / swmm-api 0.4.74 | Original native simulation and binary APIs; original report parser. `Simulation.execute()` closes the engine, so querying native mass balances afterward can return misleading zeros. | Use public PySWMM context, iterator and after-end callback for correct balance lifetime; reuse the original report parser and compare it with an independent native text/binary oracle. |

## What was executed, and what was only reviewed

The selected PySWMM MCP's **22 original tests** execute against the installed
marked runtime and a hash-pinned original fixture. The complete original test
source is retained unchanged. The fixture is synthetic/reference evidence,
not either municipal case. Both city suites separately execute all advertised
functions and protocol families using real published models/observed rain.

The [isolated audit](evidence/upstream-audit.json) executes seven probes from
exact original alternative methods with explicit stubs or the real report
parser: unsafe duplicate operands, ignored copy failure, existing-output run
suppression, storage creation against tested swmm-api 0.4.74, metric/cubic-foot
misinterpretation, continuity-only comparison and native report-error detection.
These are **not full alternative-server or original-lock executions**. The
storage property failure is scoped to the tested parser version, not generalized
to every historical stack. Downloaded archives/source files and probes have
public hashes; no untrusted shell command is executed in that duplicate probe.

## Failures that the actual host tests exposed

The original Windows-only watchdog leaves an orphan Linux worker after owner
death. A first Linux PDEATHSIG approach passed short tests but failed long
agent sessions because Linux watches the creating **thread**: an AnyIO pool
could retire that thread while the server process remained alive. The final
small external watcher uses process pidfds, is independent of the worker's
Python GIL and exits when either owner/worker ends. Docker init reaps orphans.
The regression explicitly retires the creator thread and kills the owner while
a native call retains the worker GIL. Linux pidfd support is required.

Agents also exposed misleading zero native balance metadata after
`Simulation.execute()` had closed SWMM. The marked worker now captures
native errors in `add_after_end`, before close. Short/full cases require those
values to round to the independent report within 0.00051 percentage points.
The five-minute Bellinge inspection can show about **−25.009% routing error**;
it is an API/lifecycle check, never an admitted municipal simulation result.

CI found an idle-reaping race: the internal unlocked state getter could expose
CLOSED while worker/accounting teardown still held the record lock. The getter
now uses that existing lock, as public status/close already did. A deterministic
regression and the unchanged original suite cover it; the failed CI attempt is
retained rather than dismissed as success.

Finally, an agent confused live `flooding` with binary `flooding_loss`. Generic
unexpected-exception messages hid that mistake and a worker-capacity condition.
The integration now publishes the original binary vocabulary in JSON-schema
enums/status, exposes anticipated domain failures as SDK ToolError messages,
and returns exact run/session/task resource URIs. The task checks run/output
resources before opening live sessions and reads session status before close.
Both prior host batches remain in versioned initial-observation directories.

## Original versus added functionality

The existing MCP supplies native execution/isolation, metadata, object listing,
live observations/controls, output series/snapshots, hotstarts, tasks/cancellation
and retention. We add **nine municipal tools**: source discovery, acquisition,
source paging, preparation, scoped inspection, bound scenario execution,
complete node comparison, artifact paging and a resource bridge for hosts.
Two metadata responses compact unbounded ID arrays; full IDs remain available.
Query wrappers retain original numerical functions while advertising their
valid vocabulary and expected errors. Retention is disabled in this profile.

Rainfall records, hydraulic assets, native algorithms and agent conclusions
have distinct provenance. No water-quality, groundwater, LID-design, 2D
inundation, damage, field-calibration or general municipal forecasting
capability is admitted by these cases merely because a software field exists.
