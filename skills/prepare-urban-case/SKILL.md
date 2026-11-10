---
name: prepare-urban-case
description: Preparar o revisar un caso de una herramienta urbana del registro Urban MCP, identificando datos, fuentes, transformaciones, bindings y bloqueos antes de ejecutarlo. Usar con un paquete o caso Urban MCP; no para declarar operativo un candidato de investigación.
---

Lee primero el manifiesto de la capacidad/caso solicitado y el registro de la herramienta. Selecciona solo su perfil de datos y sus fuentes. Los perfiles de esta RFC proponen un primer caso; no son el esquema de todas las operaciones del motor.

Determina qué está disponible en el entorno: assets admitidos, runtime, herramientas MCP reales y estado de las pruebas. No supongas que los nombres propuestos en la RFC son herramientas instaladas.

Separa caso de referencia y ciudad real. Para cada entrada obligatoria, identifica asset o fuente y comprueba versión/hash, derechos, cobertura, unidades/CRS y preparación. Datos de operador y parámetros físicos desconocidos son faltantes; no se rellenan silenciosamente con mapas globales o defaults.

Mapea entradas preparadas a la API/archivo/argumento original y después al esquema MCP efectivamente expuesto. Conserva originales y escenario base. Prefiere funciones/jobs existentes del upstream a otra infraestructura propia.

`python tools/validate.py` comprueba contratos/metadatos y no ejecuta motores. `cases/helsinki-service-inventory/README.md` describe el primer caso ejecutable por Docker/MCP; su admisión está delimitada por operaciones, parámetros y evidencia. `cases/sumo-reference-hello/` permanece como referencia técnica sintética sin motor admitido. Consulta `docs/cases/municipal-first.md`, `docs/data/contracts.md` y `docs/agents/day-zero.md` para prioridades, datos y prueba del agente.

En Helsinki comienza por `municipal_status`; adquiere el snapshot fijado si faltan datos, prepara, busca las categorías reales y ejecuta el inventario. Los nombres y rutas devueltos son los del servidor/contenedor. Usa CRS proyectado en metros para buffers/simplificación. La diferencia entre población municipal y filas distritales es una conciliación estadística, no ubicación de residentes. El ráster de IDs distritales es categórico, no población. No deduzcas falta de acceso por un cero de registros.

En un caso municipal, identifica municipio, pregunta y periodo antes de adquirir. Usa la receta real del paquete, conserva recibo de cosecha (filtros/paginación, obtenidos/faltantes/fallidos, versiones y hashes) y separa actualización de reproducción de un snapshot. Nunca incluyas credenciales en el recibo. Comprueba que el resultado responde la pregunta dentro de sus límites y deja instrucciones que otra persona pueda repetir.

Ejecuta solo cuando el caso y su entorno tengan la evidencia/alcance necesarios. Recupera artefactos y diagnósticos, contrasta con el baseline nativo y reporta límites. Si falta algo, informa el dato/contrato/componente preciso y la siguiente acción posible. Nunca declares una ciudad calibrada por completar un ejemplo sintético.
