# Respuesta final del ensayo Hermes

```text
All three failures confirmed precisely as expected. Now I have everything needed to write the full Spanish report.

---

## INFORME FINAL EN ESPANOL

---

INVENTARIO MUNICIPAL HELSINKI - BIBLIOTECAS PUBLICAS Y ESTACIONES DE SALUD
Analista: hermes | Snapshot: 20261110T112344Z-500b5c | Poblacion: 31-dic-2025

===========================================================================
1. ADQUISICION Y PREPARACION DE DATOS
===========================================================================

Estado inicial: inputs ausentes. Se adquirio el snapshot publico fijado:
  Snapshot ID : 20261110T112344Z-500b5c
  Recibo      : /data/sources/20261110T112344Z-500b5c/harvest.json

Preparacion ejecutada (prepare_municipal_data):
  Unidades en registro        : 12 455
  Unidades con geometria valida: 12 423
  Unidades rechazadas (nulas) : 32
  Unidades sin distrito       : 26
  Unidades ambiguas           : 0
  Distritos                   : 34
  Poblacion municipal 2025    : 694 392 hab.
  Suma filas distritales      : 680 710 hab.
  Diferencia (reconciliacion) : 13 682 hab.

NOTA CRITICA sobre reconciliacion: Los 13 682 son la diferencia aritmetica
entre el total municipal y la suma de las 34 filas estadisticas distritales.
NO es un resultado de punto-en-poligono. No se adquirieron coordenadas de
residentes. No se puede inferir que esos habitantes vivan fuera de los
poligonos ni que carezcan de servicios.

===========================================================================
2. TAXONOMIA DE SERVICIOS ENCONTRADA (busqueda exacta por substring)
===========================================================================

Busqueda "librar" -> 15 coincidencias. ID seleccionado para analisis:
  ID 813  "public libraries" / "yleiset kirjastot" / "allmanna bibliotek"

Razon de exclusion de otras categorias: son entidades distintas en el
taxonomia fuente (bibliotecas universitarias ID 879, politecnicas ID 880,
moviles ID 312, paradas de movil ID 311, educacion de adultos ID 313,
institucionales ID 368, especiales ID 155, articulos de kiertotalous
IDs 926-958). No se expande jerarquia silenciosamente.

Busqueda "health station" -> 1 coincidencia:
  ID 703  "health stations" / "terveysasemat" / "halsosstationer"

===========================================================================
3. INVENTARIOS POR DISTRITO
===========================================================================

Run IDs usados: hermes-libraries  y  hermes-healthstations

--- BIBLIOTECAS PUBLICAS (ID 813) ---
  Total unidades asignadas  : 46
  Unidades sin distrito     : 0
  Output dir: /data/results/hermes-libraries/

Distritos SIN ninguna unidad registrada (4 de 34):
  302 Alppiharju | 402 Länsi-Pakila | 405 Itä-Pakila | 601 Kulosaari

Los TRES menores ratios por 10 000 habitantes (excluidos ceros):
  1. Kampinmalmi  (103)  : 1 unidad / 46 874 hab.  -> 0.213 por 10 000
  2. Vuosaari     (704)  : 1 unidad / 40 014 hab.  -> 0.250 por 10 000
  3. Mellunkyla   (703)  : 2 unidades / 40 906 hab. -> 0.489 por 10 000

El mayor ratio observado: Ostersundom (801) con 5.692 por 10 000
(poblacion muy pequena: 1 757 hab. -- indicador altamente sensible).

--- ESTACIONES DE SALUD (ID 703) ---
  Total unidades asignadas  : 23
  Unidades sin distrito     : 0
  Output dir: /data/results/hermes-healthstations/

Distritos SIN ninguna unidad registrada (13 de 34):
  101 Vironniemi | 201 Reijola | 302 Alppiharju | 303 Vallila |
  304 Pasila     | 305 Vanhakaupunki | 402 Länsi-Pakila | 405 Ita-Pakila |
  502 Pukinmaki  | 601 Kulosaari | 602 Herttoniemi | 701 Vartiokyla |
  801 Ostersundom

Los TRES menores ratios por 10 000 hab. (excluidos ceros):
  1. Kampinmalmi  (103)  : 1 unidad / 46 874 hab.  -> 0.213 por 10 000
  2. Vuosaari     (704)  : 1 unidad / 40 014 hab.  -> 0.250 por 10 000
  3. Kallio       (301)  : 1 unidad / 38 626 hab.  -> 0.259 por 10 000

ADVERTENCIA CRITICA: Cero unidades registradas NO equivale a ausencia de
acceso ni a necesidad de planificacion. Una estacion puede servir varios
distritos adyacentes. Los conteos son entradas de registro; no constituyen
un censo de capacidad ni de accesibilidad.

===========================================================================
4. ARTEFACTOS GENERADOS
===========================================================================

Bibliotecas (/data/results/hermes-libraries/):
  summary.json
  district_inventory.csv
  district_inventory.geojson
  selected_units.geojson              (46 puntos, EPSG:4326)
  report.html
  selected_units_3067.gpkg            (46 puntos reproyectados, EPSG:3067)
  libraries_buffer500m.gpkg           (46 circulos euclideos r=500 m)

Estaciones (/data/results/hermes-healthstations/):
  summary.json
  district_inventory.csv
  district_inventory.geojson
  selected_units.geojson              (23 puntos, EPSG:4326)
  report.html

Datos preparados (/data/prepared/):
  units.geojson | districts.geojson | units_metric.gpkg | districts_metric.gpkg
  district_ids.tif | services.json | rejected.json

===========================================================================
5. REPROYECCION Y BUFFERS (solo bibliotecas)
===========================================================================

JUSTIFICACION CRS (registrada en store_justification):
  Intencion  : Distancia metrica precisa para buffer euclidiano en Finlandia
  Elegido    : EPSG:3067 (ETRS89 / TM35FIN)
  Razon      : Es la proyeccion nacional oficial de Finlandia, Mercator
               transversa sobre elipsoide GRS80. Minimiza distorsion para
               el territorio finlandes y es el CRS de analisis ya usado en
               todos los datasets preparados (units_metric.gpkg, etc.).
  Descartado : EPSG:4326 (grados, inutilizable para buffer metrico)
               EPSG:3857 (distorsion severa a ~60 N)
               EPSG:32635 (UTM 35N, valido pero no es el estandar nacional)
  Limitacion : Los buffers son circulos planos euclidianos, NO redes de
               caminos ni accesibilidad peatonal. No se calcularon
               solapamientos entre zonas.
  Confianza  : alta

Resultado reproyeccion:
  Entrada  : selected_units.geojson (EPSG:4326, 46 puntos)
  Salida   : selected_units_3067.gpkg (EPSG:3067, 46 puntos, 106 KB)
  Bounds   : [380 942, 6 669 455, 401 047, 6 683 865] metros ETRS-TM35FIN

Resultado buffer:
  Salida   : libraries_buffer500m.gpkg (EPSG:3067, 46 poligonos, 164 KB)
  Radio    : 500 m (euclidiano en espacio proyectado)
  Bounds   : [380 442, 6 668 955, 401 547, 6 684 365]

===========================================================================
6. RASTER DE IDs DE DISTRITO (district_ids.tif)
===========================================================================

Metadatos:
  Archivo   : /data/prepared/district_ids.tif
  CRS       : EPSG:3067
  Tamano    : 268 x 414 pixeles @ 100 m de resolucion
  Tipo      : uint16, 1 banda
  Nodata    : 0
  Bounds    : [376 719, 6 644 495, 403 519, 6 685 895] m
  Etiqueta  : "Cartographic district identifier; categorical, not population.
               Cell-centre rasterization at 100 m."

Estadisticas banda 1:
  Min: 101 | Max: 801 | Valid: 71 496 px | Nodata: 39 456 px
  Los valores son IDs numericos de distrito (ej. 101, 203, 603, 801...)
  no magnitudes continuas: la media (472) y la desviacion tipica (226)
  no tienen significado fisico.

QUE REPRESENTA: Es una rasterizacion cartografica de los poligonos
  distritales a 100 m de celda. Cada pixel contiene el ID entero del
  distrito al que pertenece su centro geometrico. Permite overlay rapido
  de puntos con distritos sin un join vectorial.

QUE NO PUEDE INFERIRSE:
  - No es una cuadricula de poblacion. Los pixeles no codifican habitantes.
  - La nota oficial del servidor lo confirma: "cartographic test derivative,
    not a population grid."
  - El area de cada pixel (1 ha) no representa el area habitada del distrito.
  - Los 39 456 pixeles nodata (zona maritima / fuera del municipio) no
    implican area sin cobertura de servicio.
  - El histograma muestra agrupaciones de IDs (ej. 36 226 pixeles de distritos
    del grupo 600, que son los mas extensos geograficamente), pero eso
    refleja area, no poblacion.
  - No es apropiado para interpolar estadisticas de poblacion ni para
    calcular distancias de acceso.

===========================================================================
7. PRUEBAS DE RECHAZO DELIBERADO (confirmadas, sin resultados fabricados)
===========================================================================

TEST A - ID de servicio inexistente (99999):
  Herramienta : inventory_by_district, service_ids=[99999]
  Rechazo     : "Choose at most 100 existing numeric IDs from service_catalog;
                 unknown IDs are not silently ignored"
  Fabricado   : NO. Rechazo confirmado por el servidor.

TEST B - Archivo vectorial inexistente:
  Herramienta : vector_info, uri=/data/results/hermes-libraries/NONEXISTENT_FILE.geojson
  Rechazo     : "Cannot open vector dataset at '.../NONEXISTENT_FILE.geojson'.
                 Ensure the file exists and is a supported vector format."
  Fabricado   : NO. Error de acceso confirmado.

TEST C - Distancia de buffer negativa (-500 m):
  Herramienta : vector_buffer, distance=-500
  Rechazo     : "1 validation error for Params / distance / Input should be
                 greater than 0 [type=greater_than, input_value=-500.0]"
  Fabricado   : NO. Validacion Pydantic del servidor rechaza el parametro.

===========================================================================
8. LIMITACIONES TECNICAS Y TEMPORALES
===========================================================================

a) Las unidades del Service Map son entradas de registro; pueden incluir
   elementos exteriores, servicios moviles o unidades no operativas.
   No son un censo de edificios ni de capacidad de servicio.

b) La poblacion es a 31-dic-2025. Los snapshots de servicios y distritos
   pueden tener fechas de observacion distintas (desfase temporal).

c) Los ratios por 10 000 habitantes son indicadores descriptivos, no de
   accesibilidad. Un distrito con cero unidades puede estar cubierto por
   instalaciones de distritos vecinos.

d) 26 unidades del universo general no pudieron asignarse a ningun distrito
   (geometria valida pero fuera del limite poligonal); 32 unidades rechazadas
   por geometria nula. Para las categorias analizadas (813 y 703) todas las
   unidades se asignaron correctamente (unmatched=0).

e) La diferencia de 13 682 hab. entre total municipal y suma distrital es
   una diferencia de filas estadisticas, NO un resultado espacial de
   residentes sin cobertura.

f) Los buffers euclidianos de 500 m NO representan accesibilidad peatonal
   ni de transporte. No se calculo solapamiento de zonas de influencia.

g) No se reivindica disponibilidad permanente de la API ni comparacion
   global con otras ciudades. El snapshot fijado permite reproduccion offline.

h) Licencias: datos del Service Map (CC-BY-4.0, City of Helsinki);
   estadisticas de poblacion (CC-BY-4.0, City of Helsinki / Statistics Finland).
   Este analisis no implica endorsement institucional.

===========================================================================
FIN DEL INFORME
===========================================================================
```
