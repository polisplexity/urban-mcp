# Public contribution tasks

## Current qualification priority

[Issue #41: independent third-city walking reproduction](https://github.com/polisplexity/urban-mcp/issues/41) is required before final-product promotion. A person outside the original implementation/initial test team must harvest another city's inputs, run the complete native/MCP case and both hosts, and submit public evidence for review. The [policy](product-qualification.md), [qualification register](../registry/product-qualification.json) and [master](../MASTER_TEST_RECORD.md) keep that stage pending. Initial developer-operated cases and another model run by the same team do not satisfy it.

SWMM [issue #46](https://github.com/polisplexity/urban-mcp/issues/46) and its
[checklist](tasks/swmm-third-city.md) request an independent person's third-city
reproduction of the [Odense/Utrecht case](../cases/two-city-swmm/README.md),
integrated into `main` in PR #45. Native/MCP reproduction, source rights,
two-host artifacts, task coverage and prose require separate evidence. The
original Hermes omissions and failed prose remain visible; numerical matches
do not admit them. This task does not replace walking #41 or SUMO #44.

## Historical planning backlog

Current implementation is on `main`: [Helsinki inventory](../cases/helsinki-service-inventory/README.md), [two-city walking diagnostics](../cases/two-city-walking/issue-39.md), [Helsinki/Amsterdam historical vegetation](../cases/two-city-vegetation/README.md), [Bologna/Ingolstadt historical SUMO](../cases/two-city-sumo/README.md) and [Odense/Utrecht historical SWMM](../cases/two-city-swmm/README.md). Vegetation [issue #35](https://github.com/polisplexity/urban-mcp/issues/35) was closed by merged [PR #42](https://github.com/polisplexity/urban-mcp/pull/42). The original planning text below is historical; use the [master](../MASTER_TEST_RECORD.md) and exact case evidence for current readiness. Independent-person qualification remains pending.

El primer caso ejecutable es [Helsinki: bibliotecas y salud](../cases/helsinki-service-inventory/README.md), con cosecha, original/MCP y dos agentes. Las prioridades siguientes son accesibilidad y cobertura vegetal. Cada capacidad se admite con cosecha, resultado municipal y reproducción independiente; SUMO Hello es una referencia técnica auxiliar. Ver [criterios](cases/municipal-first.md) y [plantilla](cases/municipal-case-template.md). Las tareas de familia seleccionan operaciones/casos y datos, no ordenan implementar todo el inventario.

| Tarea | Hito |
|---|---|
| [Revisar RFC 0001 y definir campos por operacion](https://github.com/polisplexity/urban-mcp/issues/2) | M0 - RFC y contratos |
| [Definir primer municipio, pregunta y fuentes reproducibles](https://github.com/polisplexity/urban-mcp/issues/8) | M1 - Datos y binding del caso |
| [Caso municipal 1: inventario de equipamientos y poblacion](https://github.com/polisplexity/urban-mcp/issues/33) | M1 - Datos y binding del caso |
| [Caso municipal 2: accesibilidad peatonal a servicios](https://github.com/polisplexity/urban-mcp/issues/34) | M6 - Investigacion por familias |
| [Caso municipal 3: cobertura vegetal y poblacion](https://github.com/polisplexity/urban-mcp/issues/35) | M6 - Investigacion por familias |
| [Reproducir y admitir el primer caso municipal publico](https://github.com/polisplexity/urban-mcp/issues/36) | M5 - Aceptacion municipal reproducible |
| [Admitir los assets de referencia SUMO Hello](https://github.com/polisplexity/urban-mcp/issues/3) | M1 - Datos y binding del caso |
| [Mapear entradas SUMO al contrato nativo y a una operacion MCP](https://github.com/polisplexity/urban-mcp/issues/4) | M1 - Datos y binding del caso |
| [Construir sandbox Docker de SUMO y baseline nativo](https://github.com/polisplexity/urban-mcp/issues/5) | M2 - Sandbox nativo |
| [Comparar MCP SUMO existente contra el baseline](https://github.com/polisplexity/urban-mcp/issues/6) | M3 - MCP verificado |
| [Ensayar skill y operacion por un agente independiente](https://github.com/polisplexity/urban-mcp/issues/7) | M4 - Agente dia cero |
| [Revisar fuentes, credenciales y adquisicion reproducible](https://github.com/polisplexity/urban-mcp/issues/9) | M1 - Datos y binding del caso |
| [Investigar capacidad y datos: Agua drenaje e inundaciones](https://github.com/polisplexity/urban-mcp/issues/10) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: BIM CAD y diseño computacional](https://github.com/polisplexity/urban-mcp/issues/11) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Catálogos de descubrimiento](https://github.com/polisplexity/urban-mcp/issues/12) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Clima urbano y atmósfera](https://github.com/polisplexity/urban-mcp/issues/13) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Contexto urbano IoT e interoperabilidad](https://github.com/polisplexity/urban-mcp/issues/14) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Desarrollo urbano y uso del suelo](https://github.com/polisplexity/urban-mcp/issues/15) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Diseño urbano participativo](https://github.com/polisplexity/urban-mcp/issues/16) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Ecología paisaje y naturaleza urbana](https://github.com/polisplexity/urban-mcp/issues/17) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Energía urbana y edificios](https://github.com/polisplexity/urban-mcp/issues/18) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: LiDAR y nubes de puntos](https://github.com/polisplexity/urban-mcp/issues/19) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: MCP geoespacial y urbano existente](https://github.com/polisplexity/urban-mcp/issues/20) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Modelos urbanos 3D y reconstrucción](https://github.com/polisplexity/urban-mcp/issues/21) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Morfología y estadística espacial](https://github.com/polisplexity/urban-mcp/issues/22) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Movilidad y transporte](https://github.com/polisplexity/urban-mcp/issues/23) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Observación terrestre y GeoAI](https://github.com/polisplexity/urban-mcp/issues/24) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Peatones y multitudes](https://github.com/polisplexity/urban-mcp/issues/25) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Redes eléctricas y optimización energética](https://github.com/polisplexity/urban-mcp/issues/26) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Riesgo y resiliencia](https://github.com/polisplexity/urban-mcp/issues/27) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Ruido ambiental](https://github.com/polisplexity/urban-mcp/issues/28) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: SIG y geoprocesamiento](https://github.com/polisplexity/urban-mcp/issues/29) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Servicios geoespaciales y catálogos](https://github.com/polisplexity/urban-mcp/issues/30) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Simulación social y agentes](https://github.com/polisplexity/urban-mcp/issues/31) | M6 - Investigacion por familias |
| [Investigar capacidad y datos: Visualización cartográfica y 3D](https://github.com/polisplexity/urban-mcp/issues/32) | M6 - Investigacion por familias |
## SUMO development and next reproduction

[PR #43](https://github.com/polisplexity/urban-mcp/pull/43) merged the
[Bologna/Ingolstadt historical works case](../cases/two-city-sumo/README.md)
into `main`. The native/model-quality and host prose limits remain explicit.
[Issue #44](https://github.com/polisplexity/urban-mcp/issues/44) and its
[reproduction checklist](tasks/sumo-third-city.md) invite an independent person.
Contributors can review native model warnings, preserve/repair source signal
compatibility with independent field validation, or propose a distinct third
city with exact rights-reviewed demand and signal inputs. An independent
person's native/MCP/two-host evidence and accepted review are required for
final-product qualification. [Issue #41](https://github.com/polisplexity/urban-mcp/issues/41)
remains the separate walking reproduction task. Historical task titles below
retain their original wording.
