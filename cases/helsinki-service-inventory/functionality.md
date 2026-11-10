# Cobertura por función expuesta

La admisión corresponde a las operaciones de este caso y sus parámetros comprobados. GDAL/GeoPandas tienen muchas más funciones y drivers: esta tabla no acredita todo su universo. Cada fila es llamada en `python -m urban_mcp_case test`, mediante un proceso MCP por stdio.

El perfil municipal añade validación de CRS proyectado en metros para buffers/simplificación. Se rechaza explícitamente intentar un buffer de 500 sobre coordenadas en grados; no se convierte una unidad silenciosamente. Las comprobaciones de errores revisan el mensaje esperado además de `isError`.

| Función MCP | Origen | Uso municipal y comprobación |
|---|---|---|
| `vector_info` | GDAL-MCP | Inspeccionar esquema/CRS/extensión/recuento del inventario; contraste nativo y archivo ausente. |
| `vector_convert` | GDAL-MCP | GeoJSON a GeoPackage para compartir el inventario; conservar IDs y geometrías. |
| `vector_reproject` | GDAL-MCP | Preparar puntos para operaciones métricas en EPSG:3067; comparar coordenadas. |
| `vector_buffer` | GDAL-MCP | Capa exploratoria de 500 m alrededor de bibliotecas; área frente al círculo y distancia negativa rechazada. |
| `vector_clip` | GDAL-MCP | Extraer puntos de un sector central; comparar los IDs seleccionados nativamente. |
| `vector_query` | GDAL-MCP | Consultar una extensión para revisión del inventario; comparar subconjunto y leer recurso del resultado. La geometría se usa como bounding box, no máscara poligonal exacta. |
| `vector_simplify` | GDAL-MCP | Exportación cartográfica distrital con tolerancia de 20 m; preservar IDs y contrastar con simplificación nativa. No es límite catastral ni preservación de adyacencia entre distritos. |
| `raster_info` | GDAL-MCP | Revisar georreferenciación, resolución y clases del ráster derivado de IDs distritales. |
| `raster_stats` | GDAL-MCP | Comprobar celdas válidas/NoData y estadísticas frente a Rasterio/NumPy. La media de IDs no representa una variable física. |
| `raster_convert` | GDAL-MCP | Publicación COG con overviews nearest; conservar píxeles, estructura COG y niveles. |
| `raster_query` | GDAL-MCP | Extraer tesela de 30×30 píxeles y comparar con ventana nativa; extensión inválida rechazada. |
| `raster_reproject` | GDAL-MCP | Derivado web en EPSG:3857 con nearest; comprobar CRS y dominio categórico. No usar Mercator para medir buffers. |
| `store_justification` | GDAL-MCP, schema corregido | Registrar selección de CRS, muestreo y extensión. Una justificación almacenada no certifica científicamente la decisión. |
| `municipal_status` | Urban MCP | Inspeccionar entradas, integridad, preparación y bloqueos del caso. |
| `harvest_municipal_sources` | Urban MCP | Cosecha live con recibo y reproducción del snapshot fijado; hashes, paginación, duplicados y fallos controlados. |
| `prepare_municipal_data` | Urban MCP + GeoPandas | Preparar GeoJSON/GeoPackage, unir por clave población/distrito y asignar puntos por polígono exacto; informar rechazos/no correspondencia. |
| `service_catalog` | Urban MCP | Descubrir IDs reales antes del análisis; búsqueda, límites y selección exacta. |
| `inventory_by_district` | Urban MCP + GeoPandas | Agregar registros distintos por distrito, adjuntar población/tasas, emitir CSV/GeoJSON/HTML; comparación nativa/MCP y servicio desconocido rechazado. |
| `read_case_artifact` | Urban MCP | Recuperar tabla/resumen con huella; rechazar rutas fuera del caso. |

Además: 2 recursos concretos del caso, 16 familias de recursos upstream y 4 prompts. La suite lee metadatos vectoriales/ráster, bandas/estadísticas, catálogo/CRS/referencias y un resultado de consulta; renderiza las cuatro familias de prompts. Los hosts pueden exponer estos elementos de forma diferente: el ensayo registró que Codex no ofrecía el selector de prompts de GDAL y sí pudo registrar la justificación mediante la herramienta tipada. Hermes ofreció acceso a prompts/recursos.

Las pruebas con agentes usan la tarea municipal de bibliotecas y salud. No se les atribuye cada llamada de la suite determinista: la evidencia distingue funciones llamadas por cada agente de las probadas por el cliente de protocolo.
