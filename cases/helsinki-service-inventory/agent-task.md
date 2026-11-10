Act as a municipal analyst operating the Urban MCP Helsinki server. Use only that MCP's tools: do not use a shell, browser, filesystem tool, other connectors, or inspect repository code/expected results. Start from the inputs actually available in your isolated workspace. Discover capabilities from tool schemas and returned metadata.

The municipality needs a reproducible inventory of public-library and health-station locations relative to population by district.

1. Inspect the case and input availability. Acquire the pinned snapshot if necessary and prepare the data.
2. Discover the exact service categories in the source taxonomy. Search is a substring: `librar` matches library/libraries. Do not guess IDs or expand a service hierarchy silently.
3. Produce one district inventory for public libraries and another for health stations. Use run IDs prefixed with your host name (`codex` or `hermes`) and retain CSV/GeoJSON/report artifacts.
4. Read the result tables. Report counts, districts without a selected registered location, the lowest three counts per 10000 residents, and data-quality/temporal limitations. A zero count does not prove lack of access or a planning need. Population reconciliation is a difference between statistical rows, not a spatial classification of residents: no resident coordinates were acquired.
5. Inspect vector metadata. Reproject only the selected library points to EPSG:3067, then create 500 metre Euclidean buffers as an exploratory map. Follow the server's methodological preflight and record a justified choice. This is not walking accessibility. Save files inside that inventory's existing output directory.
6. Inspect metadata/statistics for the supplied categorical district-ID raster. Explain what it represents and what cannot be inferred from it.
7. Deliberately test one unknown service ID, one missing input file and a negative buffer distance. Confirm precise rejections; do not fabricate a successful result.
8. Give a concise Spanish answer with results, artifact paths and encountered limits/failures. Do not modify the software or infer institutional endorsement. Distinguish what you executed from untested operations.

This task intentionally does not supply the expected counts or district results. The deterministic protocol suite separately exercises every exposed tool and resource/prompt family.
