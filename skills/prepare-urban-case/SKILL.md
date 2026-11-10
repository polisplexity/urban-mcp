---
name: prepare-urban-case
description: Preparar o revisar un caso de una herramienta urbana del registro Urban MCP, identificando datos, fuentes, transformaciones, bindings y bloqueos antes de ejecutarlo. Usar con un paquete o caso Urban MCP; no para declarar operativo un candidato de investigación.
---

Lee primero el manifiesto de la capacidad/caso solicitado y el registro de la herramienta. Selecciona solo su perfil de datos y sus fuentes. Los perfiles de esta RFC proponen un primer caso; no son el esquema de todas las operaciones del motor.

Determina qué está disponible en el entorno: assets admitidos, runtime, herramientas MCP reales y estado de las pruebas. No supongas que los nombres propuestos en la RFC son herramientas instaladas.

Separa caso de referencia y ciudad real. Para cada entrada obligatoria, identifica asset o fuente y comprueba versión/hash, derechos, cobertura, unidades/CRS y preparación. Datos de operador y parámetros físicos desconocidos son faltantes; no se rellenan silenciosamente con mapas globales o defaults.

Mapea entradas preparadas a la API/archivo/argumento original y después al esquema MCP efectivamente expuesto. Conserva originales y escenario base. Prefiere funciones/jobs existentes del upstream a otra infraestructura propia.

En este PR, `python tools/validate.py` comprueba la planificación; no ejecuta motores ni acredita disponibilidad. El primer caso propuesto está en `cases/sumo-reference-hello/`. Consulta `docs/data/contracts.md` para las reglas de asset y `docs/agents/day-zero.md` para el criterio de operación del agente.

Ejecuta solo cuando el caso y su entorno tengan la evidencia/alcance necesarios. Recupera artefactos y diagnósticos, contrasta con el baseline nativo y reporta límites. Si falta algo, informa el dato/contrato/componente preciso y la siguiente acción posible. Nunca declares una ciudad calibrada por completar un ejemplo sintético.
