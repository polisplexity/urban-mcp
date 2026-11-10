# Helsinki: inventario municipal por distrito

Primer caso ejecutable de Urban MCP: cosecha pública → preparación → herramientas originales → MCP → agentes. La pregunta es cómo se distribuyen las localizaciones registradas de bibliotecas públicas y centros de salud respecto de la población distrital de 2025. Un cero en el registro sirve para revisar el inventario; por sí mismo no justifica construir un equipamiento.

## Repetir en Docker

Requisitos: Git, Docker Engine/Compose y acceso HTTPS durante construcción/adquisición. El análisis y la suite de protocolo funcionan sin red una vez descargado el snapshot. No necesitan claves de datos ni proveedor de IA. Ejecución comprobada en Linux amd64 sobre WSL2; otras arquitecturas/plataformas requieren su ensayo.

```sh
git clone https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
git switch feat/helsinki-municipal-inventory

# Linux/WSL: escribir con el UID/GID propio, conservando un contenedor sin root.
export URBAN_MCP_UID="$(id -u)"
export URBAN_MCP_GID="$(id -g)"
mkdir -p .urban-mcp/helsinki

docker compose --profile municipal build inventory
docker compose --profile municipal run --rm harvest harvest --mode snapshot
docker compose --profile municipal run --rm inventory prepare
docker compose --profile municipal run --rm inventory inventory --service-id 813 --run-id native-library
docker compose --profile municipal run --rm inventory inventory --service-id 703 --run-id native-health
docker compose --profile municipal run --rm inventory test
```

En Windows se puede ejecutar este bloque dentro de WSL con integración Docker. Los resultados quedan en `.urban-mcp/helsinki/results/`: cada inventario entrega `summary.json`, CSV, GeoJSON de distritos/puntos y `report.html`, un mapa/tabla autónomo que se abre sin servicios externos. Las rutas `/data/...` devueltas por MCP son rutas del contenedor y corresponden a este directorio montado.

El servicio `inventory` tiene red deshabilitada, raíz de solo lectura, capacidades eliminadas y límites de CPU/memoria/procesos. `harvest` y `municipal-mcp` necesitan red para adquirir; el original procesa archivos locales. Cada cliente concurrente debe usar su propio `URBAN_MCP_WORKDIR`. No se admite todavía escritura concurrente de varios procesos sobre el mismo workspace.

## Cosechar nuevamente desde los publicadores

```sh
docker compose --profile municipal run --rm harvest
```

Eso crea otra versión de `sources/`, conserva las anteriores y cambia el puntero activo solo tras una adquisición completa. Después hay que preparar nuevamente. El modo `snapshot` recupera la versión fijada en [snapshot.lock.json](snapshot.lock.json); **actualizar** y **reproducir** son acciones distintas. Un resultado de una cosecha nueva necesita su revisión y no hereda el esperado del snapshot.

La [receta](recipe.json) identifica URLs, filtros, CRS, periodo, derechos y límites. El recibo registra páginas, URLs sin secretos, tamaños, SHA-256, recuentos, reintentos y final de paginación. Rechaza IDs duplicados, cambios del total durante paginación y respuestas incompletas. Conserva respuestas originales y la consulta PxWeb. La preparación verifica hashes, esquema, geometrías, claves y año; los datos preparados también llevan huellas.

## Usar el MCP desde cualquier agente

```sh
docker compose --profile municipal run --rm -T municipal-mcp
```

Este comando habla MCP por stdio. No es una API de un agente concreto. [tools/client_config.py](../../tools/client_config.py) genera configuración para clientes genéricos, Codex o Hermes:

```sh
python tools/client_config.py --format mcp-json
python tools/client_config.py --format codex
python tools/client_config.py --format hermes
# Desde Python en Windows con Docker dentro de WSL:
python tools/client_config.py --format codex --wsl-distro Ubuntu-22.04
```

La configuración impresa no instala cuentas ni lee credenciales. En Codex se añade al host y se autoriza este servidor de caso. En Hermes se puede crear un perfil vacío con `hermes profile create urbanmcp-test --no-skills --no-alias`, configurar ahí el proveedor propio y añadir únicamente el bloque MCP generado. No usar un perfil de mensajería/producción para el ensayo.

Los helpers requieren Python 3.11 o posterior; para emitir YAML instalar también `requirements-dev.txt` (PyYAML). Usar `--data-dir .urban-mcp/hermes-mi-ensayo` al generar la configuración de un nuevo ensayo Hermes para empezar con un workspace vacío. `--hermes-executable` permite indicar su ruta al runner si no está en PATH. La suite Docker no depende de instalar esas bibliotecas en el host.

Flujo disponible: `municipal_status` → `harvest_municipal_sources` → `prepare_municipal_data` → `service_catalog` → `inventory_by_district` → `read_case_artifact`. Los datos preparados y resultados devuelven rutas para las herramientas GDAL. La búsqueda de servicios usa subcadenas en los idiomas del publicador: `librar` encuentra library/libraries; las categorías comprobadas son `813` (public libraries) y `703` (health stations). La pertenencia es por ID exacto, sin expansión implícita de jerarquía.

## Qué se reutiliza y qué construimos

Se reutiliza [JordanGunn/gdal-mcp](https://github.com/JordanGunn/gdal-mcp) en `418f401c7987e388eaaee6ad13289798a1ff69b6`, con archivo fuente verificado por SHA-256. Conserva FastMCP 2.12.3, MCP SDK 1.14.0 y sus bibliotecas geoespaciales; los constraints provienen de su `uv.lock`. Python corresponde a esa API original y a GeoPandas, sin decidir el lenguaje de otras familias.

Nuestro delta: conectores de la receta, admisión/versionado de datos, preparación y enlace espacial con GeoPandas, consulta de categorías, agregación por distrito/población, reportes, sandbox, suite MCP y ensayo de agentes. No reimplementamos proyecciones, geometrías ni drivers. [La matriz de funciones](functionality.md) distingue originales y nuevas.

La receta aplica cuatro correcciones comprobadas al código fijado: plantillas URI incompatibles; argumentos/serialización/subdirectorio del catálogo; overviews creados antes de cerrar el escritor COG; y esquema tipado de justificación. [apply_compat.py](../../adapters/municipal_inventory/apply_compat.py) comprueba bloques exactos y falla ante cambios upstream. No es una actualización silenciosa del servidor ni reemplaza algoritmos geométricos. Véase [el registro de hallazgos](findings.md).

## Datos y límites del resultado

- Snapshot adquirido el 2026-11-10: 12,455 entradas Service Map, 34 distritos y 1,113 categorías. Preparación: 12,423 puntos válidos; 32 entradas sin punto utilizable y 26 puntos sin distrito único.
- Población al 31/12/2025: 694,392 en el total municipal y 680,710 en las 34 filas distritales seleccionadas. Los 13,682 restantes son una diferencia de agregados estadísticos; no se adquirieron coordenadas de residentes ni se demuestra que vivan fuera de los polígonos.
- `813`: 46 registros geolocalizados; `703`: 23. Son registros, no edificios únicos, plazas, capacidad, horarios o calidad. Bibliotecas sin registro seleccionado en distritos `302`, `402`, `405`, `601`; no equivale a ausencia de acceso.
- Las coordenadas se leen como GeoJSON WGS84; EPSG:3067 se usa para metros. Buffers de 500 m son euclídeos, sin red peatonal, barreras ni calibración de demanda.
- `district_ids.tif` es una rasterización categórica a 100 m para comprobar la cadena cartográfica. Sus píxeles codifican IDs de distrito; sus medias no son indicadores físicos y nunca se suman como población. No es el siguiente caso de vegetación ni un modelo de población.

Fuentes y derechos: [Service Map y CC BY 4.0](https://www.hel.fi/palvelukarttaws/restpages/index_en.html), [PxWeb de Helsinki](https://stat.hel.fi/Resources/Images/PxWebAPI_Help_Helsinki_en.pdf), [Statistics Finland y CC BY 4.0](https://stat.fi/en/about-us/get-to-know-statistics-finland/legislation/terms-of-use). Atribución: City of Helsinki Service Map; City of Helsinki Urban Research and Statistics / Statistics Finland. Se conserva procedencia y se identifican nuestras transformaciones. No se cosechan fotos ni campos de contacto. El código MIT no relicencia estos datos. No se implica aval institucional.

## Pruebas y contribuciones

La suite de protocolo inicia un proceso MCP real, descubre el catálogo y comprueba todas las funciones expuestas, recursos/prompts y casos inválidos. Compara IDs, geometrías, píxeles, estadísticas y resultado municipal con llamadas nativas. CI usa el snapshot pequeño; no descarga de nuevo la ciudad en cada PR. Las pruebas LLM son separadas y necesitan la autenticación de cada host; un exit code exitoso no basta para admitir sus conclusiones.

[agent-task.md](agent-task.md) es la misma tarea sin respuestas esperadas para ambos agentes. [tools/run_agent_check.py](../../tools/run_agent_check.py) permite repetirla con un host instalado. Registrar modelo, versión, transporte, llamadas, artefactos, errores/reintentos y revisión de afirmaciones. Los resultados de estos ensayos no prometen idéntico comportamiento de todos los modelos/clientes.

Para aportar: reproducir desde vacío; verificar una fuente o una transformación; probar un parámetro/driver adicional; mejorar un error; revisar un indicador con un especialista; traducir; o diseñar otro caso municipal. Una nueva ciudad necesita receta, fuentes/IDs, preparación y aceptación propios; no sustituir constantes y darla por validada. [Selección de ciudad y expansión](selection.md).
