Generé y leí ambos inventarios de **34 distritos**, usando exclusivamente el MCP de Helsinki. Los insumos estaban ausentes: adquirí el snapshot fijado `20261110T112344Z-500b5c` y preparé los datos con verificación de hashes.

Seleccioné las categorías descubiertas **813, “public libraries”**, y **703, “health stations”**, sin expandir jerarquías.

| Inventario | Ubicaciones registradas | Asignadas a distrito | Distritos con cero |
|---|---:|---:|---:|
| Bibliotecas públicas | 46 | 46 | 4 |
| Centros de salud | 23 | 23 | 13 |

Los distritos sin una ubicación seleccionada son:

- **Bibliotecas:** Alppiharju (302), Länsi-Pakila (402), Itä-Pakila (405) y Kulosaari (601).
- **Salud:** Vironniemi (101), Reijola (201), Alppiharju (302), Vallila (303), Pasila (304), Vanhakaupunki (305), Länsi-Pakila (402), Itä-Pakila (405), Pukinmäki (502), Kulosaari (601), Herttoniemi (602), Vartiokylä (701) y Östersundom (801).

Todos empatan en **0 por 10 000 residentes**. Tomando ID ascendente como desempate explícito, los tres mínimos son 302/402/405 para bibliotecas y 101/201/302 para salud. Las tres tasas **positivas** más bajas son:

| Bibliotecas | Por 10 000 | Salud | Por 10 000 |
|---|---:|---|---:|
| Kampinmalmi | 0,213338 | Kampinmalmi | 0,213338 |
| Vuosaari | 0,249913 | Vuosaari | 0,249913 |
| Lauttasaari | 0,392896 | Kallio | 0,258893 |

Cada fila anterior registra una ubicación.

La población distrital suma **680 710**, frente al total municipal de **694 392**. La diferencia de **13 682** es una reconciliación entre filas estadísticas: **no se adquirieron coordenadas de residentes** ni se clasificaron espacialmente esas personas. La población corresponde al 31/12/2025; servicios y límites tienen otra fecha de observación. El registro completo reporta 32 unidades rechazadas, 26 puntos sin distrito y ninguna ambigüedad; las selecciones utilizadas no tienen puntos sin asignar. Son entradas registrales, no necesariamente edificios únicos, capacidad o calidad. **Un cero no demuestra falta de acceso ni necesidad de intervención.**

Inspeccioné los 46 puntos bibliotecarios en EPSG:4326 y reproyecté únicamente esa selección a **EPSG:3067**, adecuado para distancias métricas locales. Creé 46 buffers euclidianos de **500 m**, con 32 segmentos por cuadrante. Son una capa cartográfica exploratoria; no representan accesibilidad caminando, barreras ni población cubierta. El preflight bloqueó inicialmente la reproyección; registré una justificación aceptada mediante `store_justification`. El host no expone la invocación del prompt recomendado, por lo que no afirmo haberlo ejecutado.

El ráster `/data/prepared/district_ids.tif` es una rasterización categórica por centro de celda: EPSG:3067, celdas de 100 m, 268×414, una banda `uint16`, NoData=0. Tiene **71 496 celdas válidas**, **39 456 NoData** y códigos entre 101 y 801. Sus medias y percentiles numéricos carecen de interpretación demográfica; no permite inferir residentes, densidad o cobertura.

Los artefactos quedaron en el servidor:

- `/data/results/codex-public-libraries/`
- `/data/results/codex-health-stations/`

Ambos contienen `district_inventory.csv`, `district_inventory.geojson`, `selected_units.geojson`, `summary.json` y `report.html`. El directorio bibliotecario también contiene `selected_units_epsg3067.gpkg` y `library_buffers_500m.gpkg`/`.geojson`.

Confirmé estos rechazos deliberados, sin resultados exitosos:

- ID `999999`: `unknown IDs are not silently ignored`.
- `/data/prepared/codex_missing_input.geojson`: `Cannot open vector dataset… Ensure the file exists and is a supported vector format`.
- Buffer `-500`: `Input should be greater than 0 [type=greater_than]`.

No modifiqué software. No ejecuté cosecha en vivo, análisis de redes ni las restantes operaciones o familias de recursos/prompts; estos resultados no implican aval institucional.