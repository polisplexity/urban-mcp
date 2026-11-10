# Roadmap por entregables

| Hito | Entrega revisable | Aceptación |
|---|---|---|
| M0 — RFC y contratos | Propuesta, matriz por herramienta/fuentes, contratos y tareas públicas. | Revisión de duplicidades, datos y límites; CI de metadatos. |
| M1 — Datos del primer caso | Asset/versión/licencia/hash, preparación y binding nativo exactos. | Descarga/snapshot reproducible y caso inválido detectado. |
| M2 — Sandbox nativo | Imagen fijada y comandos del original con recursos/salidas separados. | Baseline conocido, repetición, fallo y cierre comprobados. |
| M3 — MCP | Reutilizar servidor elegido o implementar solo brecha comprobada. | Mismo caso nativo por MCP, resultados/errores y ciclo de vida. |
| M4 — Agente día cero | Skill/runbook y compatibilidad de cliente. | Un agente diferente completa referencia y reconoce entrada ausente; no inventa ciudad real. |
| M5 — Ciudad real | Fuente del proyecto, parámetros y propósito con calidad suficiente. | Caso validado para esa finalidad; datos restringidos permanecen separados. |
| M6 — Nuevas familias | Repetir paquete de capacidad y comparar alternativas. | Cada capacidad tiene su evidencia; ninguna hereda aprobación de otra herramienta. |

No se asignan fechas universales a modelos de complejidad tan distinta. La siguiente familia se elige por necesidad y disponibilidad de datos, interfaz y fixture, no por cantidad de repositorios.

## Primera secuencia propuesta

1. Revisar y aceptar RFC/contratos.
2. Cerrar fuente/fixture y binding del caso SUMO Hello.
3. Sandbox Docker nativo con baseline y recursos.
4. Comparar MCP SUMO existentes contra ese caso.
5. Ensayo independiente del agente con datos completos, ausentes e inválidos.
6. Elegir primer caso real y una segunda familia con frontera diferente (p. ej. servicio OGC o biblioteca de análisis).

## Cómo tomar una tarea

Una tarea de familia identifica interfaces/datos y propone una capacidad; no pide construir todo el ecosistema. Los PR de implementación deben partir de una operación y un caso, con enlaces a sus tareas de fuente, binding y prueba. Se pueden revisar fuentes o fixtures sin ser especialista en el framework MCP.
