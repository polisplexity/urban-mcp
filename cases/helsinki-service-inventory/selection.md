# Selección: Helsinki como ciudad de referencia abierta

Se eligió por la combinación comprobable de servicios públicos, divisiones territoriales y población con interfaces abiertas, y una ruta municipal publicada hacia edificios, territorio y modelos 3D. No se afirma un ranking universal de «la más abierta del mundo» ni disponibilidad perpetua.

| Opción considerada | Observación verificable | Decisión para este caso |
|---|---|---|
| Guanajuato / León / Silao | INEGI respondió con geometría, población y localidades; DENUE y Censo se podían descargar. | La selección inicial por tamaño no respondía al criterio del usuario de una ciudad de referencia con un ecosistema amplio para gemelos abiertos. No se implementó el caso mexicano. |
| Amsterdam | El endpoint público de buurten respondió; la ciudad documenta su plataforma de datos/API. | Candidata para transferencia; no se ejecutó aquí la cadena completa ni se le atribuye menor calidad. |
| Helsinki | Se cosecharon Service Map (12,455 registros, 34 distritos, 1,113 categorías) y PxWeb con 35 filas agregadas de población de 2025. La ciudad publica Helsinki 3D y servicios geográficos abiertos. | Primer caso reproducible; reutilizar esta base para nuevas herramientas/casos. |
| Zúrich | Se consideró su oferta 3D, pero el acceso al catálogo concreto consultado falló en esta sesión. | Sin comparación completa ni conclusión de falta de datos. |

Fuentes: [Helsinki 3D](https://www.hel.fi/en/decision-making/information-on-helsinki/maps-and-geospatial-data/helsinki-3d), [datos geográficos municipales](https://www.hel.fi/en/decision-making/information-on-helsinki/maps-and-geospatial-data/make-better-use-of-geospatial-data/open-geographic-data), [Service Map](https://www.hel.fi/palvelukarttaws/restpages/index_en.html), [PxWeb Helsinki](https://stat.hel.fi/Resources/Images/PxWebAPI_Help_Helsinki_en.pdf), [Amsterdam APIs](https://api.data.amsterdam.nl/api/).

La continuidad operativa se construye con recetas, snapshots permitidos, huellas, diferencias de versión y pruebas. La existencia de un portal, un modelo 3D o una API no prueba que estén disponibles las entradas de SUMO, SWMM o EnergyPlus. Cada herramienta siguiente requiere su propio caso, binding y evaluación.
