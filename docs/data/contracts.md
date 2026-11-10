# Contrato de fuentes, preparación y entradas

## Fuente no es asset

Una fuente es un canal de adquisición. El asset es el archivo, respuesta o snapshot específico utilizado. Registrar por asset: proveedor y URL/query; versión/fecha de adquisición; SHA-256 o fingerprint de snapshot; licencia y atribución aplicables; tamaño/formato; extensión y periodo; CRS horizontal/vertical/época; unidades; resolución/timestep; observación/modelo/supuesto; restricciones de distribución y credencial requerida, sin guardar su valor.

Un endpoint vivo requiere una regla de snapshot y watermark; no basta fijar la URL. Una licencia de código no se propaga automáticamente a datos o pesos. Registrar lo revisado y dejar explícito lo pendiente.

## Receta y recibo de cosecha municipal

Cada paquete declara una receta de adquisición ejecutable y un recibo versionado. Reutilizar descarga/API/binding soportados por la fuente; un conector nuevo se justifica por una brecha concreta. El contrato es común, pero no se exige un framework único para todos los publicadores.

| Parte | Mínimo documentado |
|---|---|
| Selección | Municipio/clave, extensión, periodo, categorías/campos y versión de la receta; query/asset exactos con secretos omitidos. |
| Adquisición | Comando y entorno, autenticación requerida sin valor, paginación/particiones, cuotas, timeout/reintentos acotados y regla de caché/reanudación. |
| Recibo | Fecha, fuente/edición, archivos/bytes/hashes, peticiones/páginas y registros obtenidos, duplicados, rechazados, fallidos y faltantes. Registrar evidencia de fin de paginación o dejar cobertura incompleta. |
| Calidad | Cobertura temporal/espacial, esquema/campos, IDs únicos, CRS/unidades, joins sin correspondencia y pruebas de completitud apropiadas. Descargar sin errores no garantiza exhaustividad de la fuente. |
| Actualización | Reproducir el snapshot fijado y cosechar una nueva edición son operaciones distintas. Nueva adquisición produce nuevo manifiesto/diff; no sobrescribir silenciosamente originales o baseline. |

No registrar URLs completas que contengan tokens, cabeceras de autenticación ni datos del operador no publicables. Un snapshot que ya no pueda adquirirse necesita un archivo permitido o debe declarar la limitación de reproducción. Los datos grandes no necesitan estar en Git; sí deben estar las recetas, manifiestos y evidencias permitidas.

## Contrato por operación

Los perfiles de este PR describen primeros casos representativos. La contribución por operación debe declarar:

- Entradas obligatorias, opcionales, condicionales y embebidas en otro archivo.
- Tipos/unidades/CRS, campos requeridos y relaciones entre IDs.
- Fuentes admitidas y faltantes que requieren operador/modelador.
- Transformaciones exactas, herramienta/versión/parámetros y pérdidas.
- Binding a ruta, sección, campo, API o argumento nativo y esquema MCP real.
- Validaciones que bloquean ejecución y advertencias de calidad que limitan interpretación.
- Artefactos de salida con escenario/revisión, source assets, unidades y diagnósticos.

Ejemplo: `network.osm.pbf → netconvert → network.net.xml → <net-file>` no resuelve `demand.rou.xml`. La demanda necesita su fuente o un escenario sintético explícito. Tampoco todos los cálculos de una herramienta necesitan el mismo conjunto de datos.

## Preparación propuesta

1. Inspeccionar requisitos del caso/capacidad y el entorno disponible.
2. Seleccionar fuentes permitidas y registrar acceso/costes/límites.
3. Obtener/copiar assets, verificar integridad y conservar originales.
4. Preparar en workspace aislado con transformaciones reproducibles.
5. Validar estructura y semántica; devolver faltantes con explicación concreta.
6. Solo entonces permitir ejecución admitida del original/MCP.

`data.prepare` no debe inventar diámetros, materiales, ocupación, demanda o calibración. Puede materializar supuestos de un escenario si el usuario los proporcionó/aceptó y se conservan como supuestos. Un caso de prueba no se convierte por eso en evidencia urbana real.

## Límites ya detectados en las fuentes

- [Geofabrik](https://download.geofabrik.de/) ofrece extractos OSM: sirven de insumo cartográfico, no contienen todo el modelo de transporte o hidráulica.
- [Overture](https://docs.overturemaps.org/getting-data/) permite selección por área/release; preservar atribución y revisar tema/asset.
- [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM) es un modelo de superficie. El proyecto debe justificar su aptitud; no sustituirlo silenciosamente por terreno o cotas de tubería.
- [ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview) es reanálisis; no observación local ni inicialización atmosférica completa para cualquier solver.
- [Climate.OneBuilding](https://climate.onebuilding.org/) publica archivos de clima para edificios, incluidos años típicos; revisar periodo, estación y derechos del archivo elegido. La ruta histórica `energyplus.net/weather` devolvió 404 en esta revisión.
- [Mobility Database](https://mobilitydatabase.org/) ayuda a localizar feeds; revisar al publicador original, fechas de servicio y condiciones del feed.
- [SoilGrids](https://isric.org/explore/soilgrids) anuncia pausada su API REST en la consulta de 2026-11-10. Investigar descargas/mirrors y admitir un asset concreto antes de depender de ese canal.

El catálogo de fuentes no implementa todavía estos conectores. La [matriz por herramienta](tool-data-matrix.md) vincula requisitos, preparación y bloqueos; sus fuentes siguen siendo candidatas.
