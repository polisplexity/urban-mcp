# Independent third-city qualification before product promotion

## Required rule

A transferable municipal capability may be promoted to a final product release, or copied into a final product repository as qualified, only after **a person outside the original implementation and initial test team reproduces it in a third, distinct city**. The implementer's first two cities are development evidence. The third city must supply its own admitted inputs and an independently operated municipal case.

For walking access, Helsinki and Amsterdam are the two initial cities. Neither rerunning them nor having their original operator launch another Codex/Hermes instance satisfies this rule. A different model, agent, account alias, workstation or CI runner does not establish an independent person. Record the operator's public identity, role and independence declaration; a maintainer must review that declaration and the evidence.

Merging experimental code into `main` is allowed before qualification. `ready_to_run`, case admission and successful native/MCP/host checks retain their existing case-scoped meanings. They do not mean `product_qualified`. Until the independent review is accepted, final-product promotion remains blocked. The [qualification register](../registry/product-qualification.json) and [master record](../MASTER_TEST_RECORD.md) must say so explicitly.

## What the independent contributor delivers

1. **A third municipality and useful question.** Identify country/municipal ID, study boundary, CRS, units, denominator and expected decision. Use a geographically different city, with its own observations. A renamed or repartitioned Helsinki/Amsterdam snapshot does not count.
2. **Data harvested for that city.** Record exact publisher requests/assets, acquisition time, rights/attribution, versions, byte sizes, hashes, coverage, rejected inputs and failures. Provide a permitted immutable snapshot and a documented refresh route. Never substitute invented municipal data or parameters silently.
3. **A fresh public checkout and empty sandbox.** Pin the candidate source commit, image/runtime and task. Work from public instructions and the contributor's own authentication. Record OS, Docker/Compose, host/model versions, commands and any help or undocumented steps required. No private author workspace is a prerequisite.
4. **The complete native and MCP case.** Compare the same inputs and parameters independently; test every exposed tool, resource/prompt family, exports, invalid/missing inputs and recovery. For walking, check threshold identities and closed-link use on actual keyed paths, unchanged/unreachable objects, snap rules and overlap. A third city is not required to have the same counts, five crossings or a positive threshold change.
5. **Two host observations.** Use the same versioned blind task through Codex and an independently configured Hermes profile, with separate initially empty mounts. Submit only reviewed public calls, permitted artifacts and observed answers. Compare native artifacts, structured claims and final prose separately. Record unsupported host features and failed claims honestly; no corrected or fabricated answer may replace an observed one.
6. **A public reproduction PR.** Include operator identity and independence declaration, exact tested commit, harvest/native/MCP/host evidence, hashes, findings, failed attempts, author assistance, portability changes and complete reproduction commands. Bind reports/reviews to observed artifacts and answers. Update the master, function coverage and qualification register.

The current walking package explicitly admits only Helsinki/Amsterdam and contains city allowlists and recipe/snapshot identity checks. A third-city contributor may need a narrow city/data binding contribution. Preserve the two existing snapshots and results; do not edit their locked inputs or expect an unconfigured city to run unchanged. Test the candidate contribution and rerun initial-city regressions. The independent operator must still run and report the final public candidate personally; author-run support checks are separate evidence.

## Acceptance and promotion

A maintainer other than the reproducer reviews the PR and evidence. The original implementer may review it, but cannot substitute their own run for the independent reproduction. Review must establish:

- Independence of the person, not just a different host or GitHub handle.
- Two initial cities plus the independently tested third city for the same capability.
- Reproducible third-city acquisition/preparation, correct native/MCP behavior, complete operation coverage and meaningful failures.
- Successful reviewed use through both hosts for the promoted scope. Qualified or failed prose stays explicit; exclude any unproven autonomous recommendation from the product claim.
- A repeatable public runbook, permitted data, retained failures and a precise supported scope.

Acceptance is a reviewed decision, never an automatic consequence of a green build, a JSON flag or three folder names. Metadata CI checks repository consistency; it cannot establish a person's independence or municipal validity. There is currently no automated final-product publishing workflow enforcing this human gate. Any future publishing workflow must require the accepted qualification record before publishing.

After acceptance, record contributor, third-city case, exact tested source/runtime, public reproduction PR, reviewer/decision and evidence hashes in the register/master. Then open a separate promotion change naming the actual destination repository or stable release, immutable source commit, included operations/data rights, reproduction instructions and limitations. Qualification applies to that reviewed scope/version; material solver, adapter, data-contract or interface changes require renewed independent evidence for the changed scope.

The final destination has not been selected. Passing this gate does not authorize creating or publishing into an unspecified repository. Existing `data-*` prereleases are input snapshots, not qualified final-product releases.

## Current status

Walking access has two author-operated cities and two agent hosts; independent third-city qualification is **pending**. The service inventory currently has one initial city, so its second initial city and independent third city are **pending**. Both remain reproducible development capabilities for their admitted scopes. No capability is currently qualified for final-product promotion under this rule.

The public contribution task is [issue #41: independent third-city walking reproduction](https://github.com/polisplexity/urban-mcp/issues/41). It remains unassigned until an independent contributor volunteers.
