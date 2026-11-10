# Contributing

Contribute a source, reproducible municipal case, interface fix, independent reproduction or new operation. You do not need to install every engine. Use English for new documentation, code comments, tasks and reports; keep source place names and historical evidence verbatim.

1. Select a public issue or propose a specific original tool, operation and municipal question. Define the study boundary, denominator, decision and required inputs first.
2. Inspect the original source/API/MCP before implementing anything. Document existing functions, licensing, concrete gaps and why the chosen runtime fits the native tool.
3. Admit actual assets: publisher URL/query, rights/attribution, version/hash, coverage/date, units/CRS, quality and unresolved inputs. A discovery portal is not an input dataset.
4. Document every preparation/binding step. Preserve failed acquisition receipts, reject incomplete/invalid inputs and separate observations from scenario assumptions.
5. Build a pinned, bounded Docker recipe. Keep bulk caches/private inputs outside Git. Publish only permitted snapshots with their original data license and immutable hashes.
6. Run the municipal case directly through the native engine. Then compare real MCP calls, artifacts, parameters, errors and lifecycle with that baseline. Exercise every exposed tool and resource/prompt family. Synthetic regressions support specific contracts; they do not replace real-city evidence.
7. Run the same blind task in independent, initially empty host workspaces. Review tool traces, numerical artifacts and final claims separately from process exit codes. Do not expose credentials, private host configuration, memories or reasoning.
8. Update the [master test record](MASTER_TEST_RECORD.md), case guide, function matrix and machine-readable evidence. A result is admitted only for its declared operation, inputs, parameters and city scope.

## Required checks

```sh
python -m pip install -r requirements-dev.txt
python tools/validate.py
python -m unittest discover -s tests
```

For walking changes, follow [the two-city case](cases/two-city-walking/README.md) and run native/MCP Docker checks in both cities. For service-inventory changes, follow [the Helsinki case](cases/helsinki-service-inventory/README.md), including its original-server regression suite. Live source calls belong in acquisition reviews, not routine CI; CI restores locked permitted snapshots without model credentials.

`planning/*.tsv` contains editable catalog decisions. Rebuild data registries/matrix with `python tools/build_data_registry.py` after changes. `tools/build_planning_catalog.py` imports reviewed research updates; do not mark readiness to make CI pass. Case admission derives from `case.json` and reviewed evidence, not a generic tool's reputation.

## Review questions

- Do these data actually feed this operation, with explicit transformations and omissions?
- Is the new code limited to a justified gap, while reusing the native solver/API?
- Can an independent person reproduce the municipal result without the author's credentials?
- Do the native/protocol/host checks establish the stated claim, including errors and recovery?
- Are scope, licenses, source completeness and practical decision limits clear?

Recognize upstream authors and contributors. Do not copy unlicensed source or private product code into an open demo. OSM-derived data remains ODbL even though repository code is MIT. Preserve meaningful failures and explain corrections. Independent reproductions and careful data-quality findings are valuable contributions even when they reveal that a proposed use is not yet supported.
