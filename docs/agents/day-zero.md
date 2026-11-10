# Operación del agente desde el primer caso

Objetivo de aceptación: un agente nuevo puede completar un caso admitido sin conocer esta conversación. Debe conocer entradas/fuentes disponibles y reconocer qué no puede ejecutar todavía.

La [prueba final es municipal](../cases/municipal-first.md): cosechar datos permitidos, preparar, ejecutar, comprobar y entregar un resultado que responda la pregunta. Una referencia sintética sirve para diagnóstico técnico. La skill guía el trabajo; el paquete debe aportar las recetas de adquisición y ejecución reales.

| Pieza | Función | Límite |
|---|---|---|
| MCP | Operaciones, recursos y resultados tipados. | No entrega por sí solo datos completos ni conocimiento de preparación. |
| Registro/preflight | Requisitos, disponibilidad por caso/entorno y faltantes. | Una fuente candidata no autoriza ejecución. |
| Agent Skill | Procedimiento breve, selección de caso, límites y verificación. | Su carga/uso depende del cliente; no es un sandbox ni permiso adicional. |
| Runbook/prompts/resources | Ruta equivalente para hosts sin Agent Skills. | Soporte y descubrimiento deben comprobarse. |
| AGENTS.md | Reglas para contribuir al código/repositorio. | No es un contrato de ejecución científica. |
| SOUL.md opcional | Identidad o estilo en un runtime que lo admita. | No es estándar MCP, fuente de datos ni sustituto de permisos/validación. |
| Framework/runtime de agentes | Orquestación/modelo del usuario. | No será dependencia obligatoria del paquete de herramienta. |

Se propone el formato abierto [Agent Skills](https://agentskills.io/specification), con descubrimiento progresivo. No cargar las 229 fichas ni miles de herramientas en cada sesión: seleccionar capacidad/caso y consultar sus requisitos. La skill distingue la capacidad implementada de Helsinki de las fichas todavía propuestas.

## Primer ensayo ejecutado y cómo repetirlo

[Helsinki](../../cases/helsinki-service-inventory/README.md) incorpora la [misma tarea](../../cases/helsinki-service-inventory/agent-task.md) para Codex CLI y un perfil aislado de Hermes. Usaron el mismo MCP por stdio con workspaces separados y obtuvieron inventarios de bibliotecas/salud comparados con el original. El servidor no importa ninguno de sus SDKs de agente ni sus credenciales. La suite libre sin LLM sigue siendo ejecutable sin cuentas de IA.

La [evidencia](../../cases/helsinki-service-inventory/evidence) registra versiones, llamadas y resultados; los [hallazgos](../../cases/helsinki-service-inventory/findings.md) incluyen acceso distinto a prompts, fricción de schema y una inferencia incorrecta detectada/reprobada antes de precisar el contrato. No basta un exit code o una respuesta convincente.

```sh
python tools/run_agent_check.py codex --label mi-ensayo
# Windows con Docker en WSL: añadir --wsl-distro Ubuntu-22.04
# Hermes: configurar antes un perfil aislado y el MCP con tools/client_config.py.
python tools/run_agent_check.py hermes --hermes-home /ruta/al/perfil-de-prueba --label mi-ensayo
python tools/export_hermes_trace.py --state-db /ruta/al/perfil-de-prueba/state.db --output .urban-mcp/agent-evidence/mi-traza.json
```

Cada ejecución usa la autenticación existente del host elegido. Los scripts no provisionan claves, no crean conectores de mensajería y no exportan prompts de sistema, razonamiento ni configuración privada. El perfil Hermes de prueba no es el agente de producción del operador. Los permisos del cliente se configuran explícitamente para este servidor de caso; el benchmark Codex autoriza sus herramientas y prohíbe otros conectores/shell en la tarea, verificando luego la traza.

## Criterio para nuevos ensayos

Entregar a un agente independiente el paquete, su skill y una solicitud concreta. Probar caso completo, dato obligatorio ausente, unidad incompatible y fallo del original. Comprobar que produce un artefacto/recibo verificable o informa el bloqueo preciso. No darle la respuesta esperada ni considerar exitoso que solo enumere herramientas.

La aceptación registra host/modelo/versión y soporte de skills/transporte. No promete que todos los clientes cargarán automáticamente un archivo o razonarán igual.
