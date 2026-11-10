# Roadmap por entregables

Primer recorrido ejecutado: [Helsinki, inventario municipal](../cases/helsinki-service-inventory/README.md), con fuentes cosechadas, Docker, original/MCP, matriz de funciones y ensayos de Codex/Hermes. La evidencia delimita esta capacidad; el roadmap continúa vigente para capacidades nuevas.

| Hito | Entrega revisable | Aceptación |
|---|---|---|
| M0 — RFC y contratos | Propuesta, matriz por herramienta/fuentes, contratos y tareas públicas. | Revisión de duplicidades, datos y límites; CI de metadatos. |
| M1 — Datos del primer caso | Pregunta y municipio definidos desde el inicio; assets/versiones/licencias/hashes, cosecha, preparación y binding. | Cosecha/snapshot reproducible, faltantes y caso inválido detectados. |
| M2 — Sandbox nativo | Imagen fijada y comandos del original con recursos/salidas separados. | Baseline conocido, repetición, fallo y cierre comprobados. |
| M3 — MCP | Reutilizar servidor elegido o implementar solo brecha comprobada. | Mismo caso nativo por MCP, resultados/errores y ciclo de vida. |
| M4 — Agente día cero | Skill/runbook y compatibilidad de cliente. | Un agente diferente completa el caso municipal y reconoce entrada ausente; fixtures auxiliares para diagnóstico. |
| M5 — Aceptación municipal | Pregunta, datos cosechados, resultado útil y expediente público reproducible. | Recorrido completo y reproducción independiente; fixture técnica no sustituye este hito. |
| M6 — Nuevas familias | Repetir paquete de capacidad y comparar alternativas. | Cada capacidad tiene su evidencia; ninguna hereda aprobación de otra herramienta. |

No se asignan fechas universales a modelos de complejidad tan distinta. La siguiente familia se elige por necesidad y disponibilidad de datos, interfaz y fixture, no por cantidad de repositorios.

## Primera secuencia propuesta

1. Revisar RFC/contratos con [aceptación municipal como prueba final](cases/municipal-first.md).
2. Elegir pregunta y municipio, inventariar fuentes y construir cosecha/preparación para inventario de equipamientos y población (GDAL/GeoPandas y dependencias).
3. Probar original y MCP con los mismos datos municipales; publicar método, calidad, salidas y reproducción.
4. Reutilizar la base para accesibilidad por red (OSMnx; otros componentes solo si aportan una operación necesaria).
5. Incorporar cobertura vegetal mediante ráster/catálogo con fuente y periodo verificables.
6. Avanzar a SUMO y luego modelos hidráulicos/energéticos cuando existan entradas reales suficientes. SUMO Hello permanece como fixture técnica auxiliar.
7. Para cada capacidad, probar agente y errores/faltantes y admitir el paquete municipal documentado; facilitar después transferencia a otro municipio.

## Cómo tomar una tarea

Una tarea de familia identifica interfaces/datos y propone una capacidad; no pide construir todo el ecosistema. Los PR de implementación deben partir de una operación y un caso, con enlaces a sus tareas de fuente, binding y prueba. Se pueden revisar fuentes o fixtures sin ser especialista en el framework MCP.
