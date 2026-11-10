# Casos municipales, cosecha de datos y crecimiento libre

Propuesta de la RFC 0001, actualizada el 2026-11-10. El caso municipal se define desde el comienzo; una fixture sintética comprueba partes técnicas y no sustituye la aceptación final.

## Orden de construcción

| Orden | Capacidad y herramientas candidatas | Pregunta municipal / salida | Datos a cosechar | Límite que debe quedar visible |
|---|---|---|---|---|
| 1 | Inventario y preparación geográfica: GDAL/OGR + GeoPandas; PROJ/Shapely como dependencias. QGIS opcional para inspección. | ¿Qué equipamientos identificados existen y cómo se distribuyen respecto de población/localidades/áreas censales? Inventario, tabla por zona y mapa con faltantes/discrepancias. | Marco Geoestadístico e IDs, población agregada del censo, establecimientos DENUE y contraste OSM pertinente. Fijar edición, categorías y geografía. | DENUE no garantiza todo equipamiento público ni describe capacidad, horarios o calidad. No confundir establecimientos con oferta de servicio suficiente. |
| 2 | Accesibilidad por red: OSMnx y análisis nativo; cityseer u otro motor solo si aporta una operación requerida. | ¿Qué zonas tienen menor acceso estimado por red peatonal a servicios definidos? Distancias/indicadores, zonas desconectadas y supuestos. | Reutilizar población/equipamientos; cosechar vías, restricciones y sentidos pertinentes de OSM. Contrastar otras fuentes cuando ayuden. | RNC no acredita una red peatonal completa. Tiempos con velocidad asumida son estimaciones; revisar barreras, accesos, snapping y agregación poblacional. |
| 3 | Cobertura vegetal: cliente de catálogo donde haga falta + Rasterio/GDAL. | ¿Qué zonas tienen menor cobertura vegetal estimada para el periodo del dataset y qué población agregada contienen? Raster, tabla, mapa y cobertura/nodata. | Cobertura terrestre o imágenes con fecha/calidad/resolución/bandas; límite y población ya admitidos. | Cobertura vegetal no equivale a parque accesible, arbolado actualizado o temperatura del aire. Asociación espacial no demuestra causalidad. |
| 4 | Tráfico: SUMO y un MCP existente seleccionado. | Comparar una intervención explícita en un cruce/corredor: base, variante e indicadores con alcance de calibración. | Geometría real más aforos/OD/demanda, señales, vehículos y parámetros documentados; cosechar lo público y obtener lo faltante del operador. | OSM no aporta demanda calibrada. Demanda supuesta produce un experimento de escenario, no una validación del tráfico actual. |
| 5 | Agua/drenaje o energía: elegir SWMM/PySWMM, WNTR/EPANET o EnergyPlus/MCP por modelo disponible. | Una pregunta acotada sobre una red o edificio municipal con entradas suficientes. | Modelo, operación, forzamientos y parámetros/observaciones con procedencia. | Calles/DEM no sustituyen tuberías/cotas/controles; huellas y EPW no completan materiales/HVAC/ocupación. |

Los tres primeros casos comparten artefactos y hacen crecer una base del proyecto. Los casos 4/5 pueden adelantarse si existe un modelo municipal adecuado y un caso reproducible. No se fija todavía municipio: seleccionarlo y auditar fuentes es trabajo inicial, antes del adaptador.

## Qué construir en el primer caso

Traer las funciones de lectura, transformación y análisis de las herramientas originales. Nuestro trabajo inicial es la receta de fuentes por municipio, la cosecha y su recibo, la preparación/binding, el sandbox, la operación MCP que falte y el expediente comprobable. Inspeccionar un MCP existente antes de escribir otro. Python es natural en una frontera GeoPandas/OSMnx; eso no selecciona el lenguaje de todos los adaptadores ni obliga a envolver cada dependencia en MCP.

Cerrar primero una operación de inventario con su caso completo. Después añadir operaciones/capacidades con evidencia propia. Un paquete puede reutilizar datos y componentes de otro, pero no hereda automáticamente su aprobación científica ni su prueba MCP.

## Mínimo para admitir una capacidad

La unidad operativa es una **capacidad demostrada en un caso municipal**, no un repositorio instalado. Una biblioteca auxiliar se comprueba dentro del caso del paquete que la usa, sin inventar otro servidor/caso independiente por dependencia.

1. **Pregunta y territorio:** municipio/identificador, límite versionado, usuario, propósito y criterio de éxito. Mostrar un mapa no basta.
2. **Fuentes comprobadas:** inventario por insumo y asset/query exactos, versión/snapshot/hash, cobertura, derechos y atribución. Distinguir datos abiertos, datos del operador y supuestos. Un portal no equivale a un dataset admitido.
3. **Harvest reproducible:** comando/configuración, filtros, paginación, límites, caché y recibo de datos obtenidos/faltantes/fallidos. Reejecutar no duplica registros ni cambia silenciosamente una versión anterior.
4. **Preparación y binding:** transformaciones/versiones/parámetros, CRS/unidades, joins/IDs, pérdidas y mapping al archivo/API/argumento original. No rellenar parámetros físicos desconocidos silenciosamente.
5. **Resultado nativo comprobado:** original ejecutado con versión/recursos, contraste apropiado y criterio/tolerancia declarado. No hay un porcentaje universal de aceptación para todas las disciplinas.
6. **Mismo caso por MCP:** entradas idénticas y comprobación de resultado, artefactos, errores relevantes y ciclo de vida. `tools/list` y exit code cero no son aceptación final.
7. **Paquete de conocimiento:** guía, comando reproducible, fuentes/asset lock, calidad/faltantes, salidas, método de verificación, límites y skill/runbook.
8. **Reproducción independiente:** otra persona o agente repite sin esta conversación; registra entorno/diferencias y explica qué cambia para otro municipio.

Un caso con datos de un municipio no implica contratación, aprobación o aval institucional del ayuntamiento. Con datos restringidos se registra esa limitación; no se publican para aparentar apertura. El escaparate abierto requiere un caso cuya reproducción sea permitida mediante datos redistribuibles o adquisición legítima desde su fuente.

## Estados y puerta de publicación

- **Laboratorio / referencia:** prueba pequeña o sintética de formato, binding, motor o transporte. Necesaria, pero no aceptación municipal.
- **Caso municipal demostrado:** pregunta territorial, datos, preparación, resultado y evidencia delimitados; registrar acceso público o restringido.
- **Caso municipal público reproducible:** otra persona puede obtener insumos permitidos y repetir; no depende de credenciales del autor ni de memoria de conversación.
- **Transferencia a otro municipio:** hito posterior que identifica fuentes, parámetros y diferencias; un municipio no acredita cobertura universal.

`case.ready_to_run` puede indicar que una referencia técnica se puede ejecutar. El catálogo no promoverá `tool.ready_to_run` a capacidad admitida por esa referencia: necesita alcance municipal verificado y un caso municipal público con referencias a evidencias. Los campos no prueban por sí mismos corrección científica; hacen revisable el expediente.

En `case.json`, el bloque opcional `municipal_case` identifica territorio/pregunta y acceso (`public_reproducible` o `restricted_operator`), más rutas a `harvest_manifest`, `native_evidence`, `mcp_evidence` y `reproduction_evidence`. Al promover el caso, deben existir esos archivos en el expediente público. Las evidencias contienen método, resultados y recibos permitidos; los datasets grandes permanecen en almacenamiento adecuado o en su fuente. La revisión humana/disciplinaria comprueba su contenido: la existencia de un archivo no certifica un análisis.

## Cómo crece libre

Publicar cosecha, decisiones, preparación, comprobaciones y errores útiles, además del resultado. Una persona debe poder estudiar, ejecutar, corregir y aportar sin contratar el servicio del autor. Documentar interfaces/formatos y una ruta de reproducción sin proveedor LLM de pago obligatorio.

El código mantiene su licencia y motores/datos/pesos conservan las suyas. No aplicar MIT a assets ajenos por inercia. Compartir snapshots permitidos, recetas de adquisición y atribuciones. Los datos del operador que no puedan publicarse permanecen fuera de Git y se etiquetan como restringidos.

Las contribuciones pequeñas cuentan: admitir una fuente, reproducir un fallo de paginación, traducir una entrada, comprobar unidades, mejorar una explicación o adaptar un caso a otro municipio. El avance se mide por casos reproducibles, no por conectores sin datos.

## Separar las comprobaciones

| Comprobación | Qué acredita |
|---|---|
| CI pequeña con snapshot permitido/fixture | Regresión de preparación, contrato y cálculo en ese conjunto. |
| Cosecha desde fuente con límites y recibo | Adquisición y diferencias de versión en la fecha observada. |
| Reproducción completa desde los manifiestos | Recorrido del caso: adquisición, preparación, original, MCP y artefactos. |
| Revisión de utilidad municipal | Que responde la pregunta dentro del alcance y calidad disponibles. |

Una fuente modificada genera nueva versión/diff y no reescribe automáticamente la baseline. Definir tamaños/costes/límites por caso; no descargar regiones completas en cada PR si una muestra conserva el criterio de prueba.

## Fuentes iniciales por evaluar

- [Marco Geoestadístico](https://www.inegi.org.mx/temas/mg/) y [Censo 2020](https://www.inegi.org.mx/programas/ccpv/2020/): edición, agregación e IDs compatibles.
- [DENUE API](https://www.inegi.org.mx/servicios/api_denue.html) y [descarga](https://www.inegi.org.mx/app/descarga/): API con token; evaluar descarga pública. Cosechar solo campos necesarios para el análisis, sin incorporar teléfonos/correos/contactos que no requiera.
- [Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/): revisar versión, modo y cobertura; no inferir conectividad peatonal completa.
- [Extractos OSM de México](https://download.geofabrik.de/north-america/mexico.html): seleccionar región/fecha y registrar cobertura/faltantes.
- [GeoPandas](https://geopandas.org/en/stable/), [OSMnx](https://osmnx.readthedocs.io/en/stable/) y [WorldCover](https://esa-worldcover.org/en): capacidades/formato y periodos del original; seleccionar versiones y assets al implementar.

Estos son canales candidatos. Este documento no informa que ya se hayan cosechado datos municipales ni ejecutado esos análisis.
