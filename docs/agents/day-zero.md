# Operación del agente desde el primer caso

Objetivo de aceptación: un agente nuevo puede completar un caso admitido sin conocer esta conversación. Debe conocer entradas/fuentes disponibles y reconocer qué no puede ejecutar todavía.

| Pieza | Función | Límite |
|---|---|---|
| MCP | Operaciones, recursos y resultados tipados. | No entrega por sí solo datos completos ni conocimiento de preparación. |
| Registro/preflight | Requisitos, disponibilidad por caso/entorno y faltantes. | Una fuente candidata no autoriza ejecución. |
| Agent Skill | Procedimiento breve, selección de caso, límites y verificación. | Su carga/uso depende del cliente; no es un sandbox ni permiso adicional. |
| Runbook/prompts/resources | Ruta equivalente para hosts sin Agent Skills. | Soporte y descubrimiento deben comprobarse. |
| AGENTS.md | Reglas para contribuir al código/repositorio. | No es un contrato de ejecución científica. |
| SOUL.md opcional | Identidad o estilo en un runtime que lo admita. | No es estándar MCP, fuente de datos ni sustituto de permisos/validación. |
| Framework/runtime de agentes | Orquestación/modelo del usuario. | No será dependencia obligatoria del paquete de herramienta. |

Se propone el formato abierto [Agent Skills](https://agentskills.io/specification), con descubrimiento progresivo. No cargar las 229 fichas ni miles de herramientas en cada sesión: seleccionar capacidad/caso y consultar sus requisitos. La skill incluida orienta la preparación y **no afirma que el sandbox científico o los MCP ya estén implementados**.

## Prueba de comportamiento pendiente

Entregar a un agente independiente el paquete, su skill y una solicitud concreta. Probar caso completo, dato obligatorio ausente, unidad incompatible y fallo del original. Comprobar que produce un artefacto/recibo verificable o informa el bloqueo preciso. No darle la respuesta esperada ni considerar exitoso que solo enumere herramientas.

La aceptación registra host/modelo/versión y soporte de skills/transporte. No promete que todos los clientes cargarán automáticamente un archivo o razonarán igual.
