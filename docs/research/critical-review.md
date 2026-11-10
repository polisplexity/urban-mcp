# Análisis crítico de integraciones urbanas: herramienta por herramienta

Fecha: 10 de noviembre de 2026. Documento de análisis y propuesta; no es una autorización de implementación ni una lista de integraciones disponibles.

## 1. Qué se está decidiendo

El producto propuesto mantiene cómo una IA o agente utiliza herramientas urbanas existentes: sus interfaces, instalación, arranque, datos, operaciones y pruebas. La decisión de incluir una herramienta viene antes de escoger un framework común.

Este análisis separa **motor o aplicación original**, **bibliotecas y formatos auxiliares**, **MCP de terceros ya disponibles**, **código de integración que realmente haría falta** y **producto propio**. Un repositorio en el inventario no equivale a un servidor MCP pendiente de construir. Hay dependencias que deben ir dentro de otro paquete, alternativas entre las que hay que elegir, ejemplos que solo sirven de fixture y candidatos que todavía no justifican implementación.

El prototipo `urban-mcp-toolkit` fue descartado por instrucción del usuario. No es la arquitectura de referencia de este documento. No se arrastran como requisitos su ejecutor Python, sus perfiles ni la decisión de un gateway global.

## 2. Alcance y límites de la evidencia

- Se incluye una ficha individual para cada uno de los **226 repositorios** identificados en el inventario del 9 de noviembre, y fichas separadas de **PALM, openTELEMAC-MASCARET y SimStadt**, alojados fuera de GitHub.
- Los **986 enlaces pendientes** del registro de descubrimiento no se convierten en fichas técnicas ficticias: todavía no hay evidencia suficiente de identidad, pertinencia, licencia o interfaz. Son una cola de investigación distinta.
- Se consultó nuevamente el árbol de código de los 226 repositorios el 10 de noviembre y se registró el commit observado. Se recuperaron archivos candidatos de código donde existían, con lectura limitada; después se hizo una pasada dirigida sobre rutas de interfaz concretas. **Descargar o leer parcialmente un archivo no prueba que se pueda instalar o usar una herramienta.** Los archivos auxiliares, de pruebas o históricos no se aceptan como evidencia suficiente del API.
- Las entradas MCP inspeccionadas permiten detectar funciones ya expuestas. Esa evidencia no demuestra que todos los servidores funcionen, que su transporte sea compatible con todos los clientes, o que sus resultados sean correctos.
- En este trabajo no se instalaron ni validaron científicamente los 229 proyectos. Cada ficha indica una **prueba de admisión pendiente**, no una prueba ya aprobada.
- El commit observado identifica la fuente revisada, **no una versión de producto admitida**. Antes de mantener una receta hay que elegir release/commit, dependencias, plataforma y licencia de distribución.
- La detección de licencia del inventario es preliminar. Un `NOASSERTION`, una licencia no estándar o un archivo no localizado requieren revisión específica; ni la visibilidad pública ni una etiqueta de GitHub autorizan por sí solas redistribuir motores, datasets o pesos.

### 2.1 Qué significa «construir algo que no tenga el original»

Se distinguen tres situaciones:

1. **Función ya disponible:** se reutiliza. Cargar un IDF, ejecutar SWMM, controlar una sesión QGIS o gestionar un job no son aportes nuestros cuando el proyecto ya lo implementa.
2. **Integración de nuestro producto:** identificación de proyectos y revisiones, traducción de entradas entre herramientas, contratos para agentes, instalación reproducible y comprobación de resultados. Puede requerir código nuestro, pero no se presenta como algoritmo científico nuevo.
3. **Brecha todavía no demostrada:** se propone una necesidad y se identifica qué hay que inspeccionar/probar. No se afirma que una función esté ausente del original solo porque no apareció en el README o en un fragmento de código.

La línea «construir» de cada ficha describe una **propuesta condicionada a comprobar esa brecha**. Si una interfaz o MCP existente la cubre, el trabajo se reduce a receta, configuración y pruebas, o se elimina. Una búsqueda parcial tampoco permite afirmar que no exista otra implementación fuera del inventario.

## 3. Cómo leer las fichas

Cada ficha separa: qué se trae, por dónde se usa el original, qué adaptación se propone, con qué se implementaría y por qué, qué no se reconstruye, su crítica y la prueba que permitiría admitirla. Las decisiones son propuestas de alcance; no compromisos de construir 226 conectores.

- **Base:** capacidad candidata útil para varios flujos; no implica admisión automática.
- **Opcional:** se incorpora por un caso concreto.
- **Alternativa:** se compara con equivalentes; no se despliegan todas por defecto.
- **Dependencia:** biblioteca, plugin o formato de un paquete padre; no otro servidor.
- **Especialista:** requiere modelo, datos, calibración o infraestructura que un MCP no aporta por sí solo.
- **Comparar MCP:** primero evaluar servidores existentes; no comenzar uno nuevo.
- **Investigar / no ejecutable:** no escribir una receta que aparente soporte hasta resolver la incertidumbre.
- **Referencia / diferir:** documentación, fixture o trabajo fuera del alcance inicial.

### 3.1 La tecnología se decide por la frontera real

**Python** se propone donde el API y las estructuras del original ya son Python; **R** donde hay modelos/paquetes R; **Java/JVM** donde el ejecutor lo exige; **JavaScript/TypeScript** dentro de un visor web; y **Go** como candidato para puentes HTTP o de procesos que no necesitan bibliotecas Python. Ninguna elección implica portar el motor.

En las bibliotecas Python, decidir la fachada entre SDK oficial y FastMCP requiere probar el contrato seleccionado. FastMCP puede ahorrar composición y proveedores; el SDK puede bastar para una fachada pequeña. No hay evidencia de rendimiento en estas fichas para declarar vencedor a uno. En un MCP existente se respeta primero su framework y versión: una clase llamada FastMCP puede pertenecer al SDK v1 y no al paquete independiente. La uniformidad se exige en el contrato y las pruebas, no en reescribir todos los runtimes.

Los perfiles de implementación son **propuestas justificadas**, sujetas a la prueba individual. Si el servicio ya administra trabajos, autenticación o archivos, el adaptador utiliza esas funciones antes de crear otra cola o almacén. Un proceso externo no es automáticamente un sandbox; los límites de recursos y el alcance de archivos deben comprobarse.

## 4. Duplicidades que deben resolverse antes de construir

| Familia | Separación y decisión necesaria |
|---|---|
| QGIS / UMEP / plugins / MCP QGIS | Mantener QGIS y sus proveedores; comparar los MCP existentes. No crear un servidor por cada algoritmo/plugin. |
| GDAL / PROJ / Rasterio / GeoPandas / Shapely | Separar drivers, transformaciones, ráster, tablas y geometría. Compartir dependencias compatibles sin duplicar la misma operación con nombres distintos. |
| SWMM / PySWMM / swmm_api / MCP SWMM | El motor calcula; los wrappers controlan o editan; un MCP existente puede exponer esas funciones. El producto no necesita tres motores SWMM. |
| EPANET / editor EPA / WNTR | Toolkit hidráulico, aplicación gráfica y análisis de resiliencia son componentes distintos. Elegir cada uno por su función. |
| EnergyPlus / OpenStudio / eppy / Honeybee / MCP energéticos | Separar motor, generadores/modelos, parsers y MCP. Comparar los servidores disponibles y sus versiones; no adoptar todos los forks. |
| CityEnergyAnalyst / URBANopt / EUReCA / MUBES / SimStock / SimStadt | Son flujos de modelado con supuestos/datos diferentes. No existe equivalencia universal de entradas o resultados. |
| R5 / r5py / r5r / Conveyal | Motor, bindings y servicio de análisis. Seleccionar el perfil del usuario y reutilizar el wrapper/servicio. |
| OSRM / Valhalla / OpenRouteService / OpenTripPlanner | Elegir según modo, perfiles, transporte público, datos y operación. No instalar todos como si fueran intercambiables. |
| PDAL / binding Python / CloudCompare / Open3D / Potree | Procesamiento, binding, aplicación, algoritmos 3D y visualización cumplen funciones distintas. |
| Cesium / MapLibre / iTowns / Terria / deck.gl / kepler.gl | Son hosts, motores o componentes visuales. No todos necesitan MCP propio. El árbol actual de kepler.gl ya contiene un componente MCP. |
| Orion / Orion-LD / Scorpio / FROST / Ditto | Protocolos y modelos distintos; un broker no elimina diferencias semánticas ni reemplaza todos los demás. |
| Mesa / GAMA / NetLogo / AgentSociety | Frameworks/entornos de modelos, no modelos urbanos calibrados por el hecho de instalarlos. |

## 5. Índice de decisiones por repositorio

| Ficha | Repositorio | Dictamen propuesto |
|---|---|---|
| [001](#tool-deltares--delft3d) | `Deltares/Delft3D` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [002](#tool-deltares--hydromt) | `Deltares/hydromt` | Dependencia de otro paquete; no construir servidor independiente |
| [003](#tool-deltares--hydromt_sfincs) | `Deltares/hydromt_sfincs` | Dependencia de otro paquete; no construir servidor independiente |
| [004](#tool-deltares--hydromt_wflow) | `Deltares/hydromt_wflow` | Dependencia de otro paquete; no construir servidor independiente |
| [005](#tool-deltares--sfincs) | `Deltares/SFINCS` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [006](#tool-geoscienceaustralia--anuga_core) | `GeoscienceAustralia/anuga_core` | Módulo opcional, solo si el caso lo requiere |
| [007](#tool-markuspic--swmm_api) | `MarkusPic/swmm_api` | Dependencia de otro paquete; no construir servidor independiente |
| [008](#tool-openstreams--wflow) | `openstreams/wflow` | Investigar antes de diseñar o admitir implementación |
| [009](#tool-openwateranalytics--epanet) | `OpenWaterAnalytics/EPANET` | Candidato a capacidad base; admisión técnica pendiente |
| [010](#tool-pyswmm--pyswmm) | `pyswmm/pyswmm` | Candidato a capacidad base; admisión técnica pendiente |
| [011](#tool-usepa--epanet2.2) | `USEPA/EPANET2.2` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [012](#tool-usepa--stormwater-management-model) | `USEPA/Stormwater-Management-Model` | Candidato a capacidad base; admisión técnica pendiente |
| [013](#tool-usepa--wntr) | `USEPA/WNTR` | Módulo opcional, solo si el caso lo requiere |
| [014](#tool-blender--blender) | `blender/blender` | Módulo opcional, solo si el caso lo requiere |
| [015](#tool-buildingsmart--bcf-xml) | `buildingSMART/BCF-XML` | Dependencia de otro paquete; no construir servidor independiente |
| [016](#tool-buildingsmart--ids) | `buildingSMART/IDS` | Dependencia de otro paquete; no construir servidor independiente |
| [017](#tool-compas-dev--compas) | `compas-dev/compas` | Módulo opcional, solo si el caso lo requiere |
| [018](#tool-compas-dev--compas_fab) | `compas-dev/compas_fab` | Fuera del alcance inicial; no construir ahora |
| [019](#tool-dynamods--dynamo) | `DynamoDS/Dynamo` | Investigar antes de diseñar o admitir implementación |
| [020](#tool-freecad--freecad) | `FreeCAD/FreeCAD` | Módulo opcional, solo si el caso lo requiere |
| [021](#tool-ifcopenshell--ifcopenshell) | `IfcOpenShell/IfcOpenShell` | Candidato a capacidad base; admisión técnica pendiente |
| [022](#tool-openscad--openscad) | `openscad/openscad` | Módulo opcional, solo si el caso lo requiere |
| [023](#tool-pixaranimationstudios--openusd) | `PixarAnimationStudios/OpenUSD` | Dependencia de otro paquete; no construir servidor independiente |
| [024](#tool-specklesystems--speckle-server) | `specklesystems/speckle-server` | Módulo opcional, solo si el caso lo requiere |
| [025](#tool-specklesystems--specklepy) | `specklesystems/specklepy` | Dependencia de otro paquete; no construir servidor independiente |
| [026](#tool-apa-technology-division--urban-and-regional-planning-resources) | `APA-Technology-Division/urban-and-regional-planning-resources` | Referencia, especificación o fixture; no integración ejecutable autónoma |
| [027](#tool-durbanitas--awesome-urban-planning) | `durbanitas/awesome-urban-planning` | Referencia, especificación o fixture; no integración ejecutable autónoma |
| [028](#tool-ireliya--awesome-urban-planning-agents) | `Ireliya/Awesome-Urban-Planning-Agents` | Referencia, especificación o fixture; no integración ejecutable autónoma |
| [029](#tool-sacridini--awesome-geospatial) | `sacridini/Awesome-Geospatial` | Referencia, especificación o fixture; no integración ejecutable autónoma |
| [030](#tool-kunifujiwara--voxcity) | `kunifujiwara/VoxCity` | Módulo opcional, solo si el caso lo requiere |
| [031](#tool-ladybug-tools--uwg) | `ladybug-tools/uwg` | Módulo opcional, solo si el caso lo requiere |
| [032](#tool-openfoam--openfoam-dev) | `OpenFOAM/OpenFOAM-dev` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [033](#tool-udales--u-dales) | `uDALES/u-dales` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [034](#tool-umep-dev--solweig) | `UMEP-dev/solweig` | Módulo opcional, solo si el caso lo requiere |
| [035](#tool-umep-dev--suews) | `UMEP-dev/SUEWS` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [036](#tool-umep-dev--umep) | `UMEP-dev/UMEP` | Dependencia de otro paquete; no construir servidor independiente |
| [037](#tool-umep-dev--umep-processing) | `UMEP-dev/UMEP-processing` | Candidato a capacidad base; admisión técnica pendiente |
| [038](#tool-usepa--cmaq) | `USEPA/CMAQ` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [039](#tool-wrf-model--wrf) | `wrf-model/WRF` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [040](#tool-eclipse-ditto--ditto) | `eclipse-ditto/ditto` | Módulo opcional, solo si el caso lo requiere |
| [041](#tool-fiware--context.orion-ld) | `FIWARE/context.Orion-LD` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [042](#tool-fiware--tutorials.step-by-step) | `FIWARE/tutorials.Step-by-Step` | Referencia, especificación o fixture; no integración ejecutable autónoma |
| [043](#tool-fraunhoferiosb--frost-server) | `FraunhoferIOSB/FROST-Server` | Candidato a capacidad base; admisión técnica pendiente |
| [044](#tool-scorpiobroker--scorpiobroker) | `ScorpioBroker/ScorpioBroker` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [045](#tool-smart-data-models--data-models) | `smart-data-models/data-models` | Dependencia de otro paquete; no construir servidor independiente |
| [046](#tool-telefonicaid--fiware-orion) | `telefonicaid/fiware-orion` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [047](#tool-thingsboard--thingsboard) | `thingsboard/thingsboard` | Módulo opcional, solo si el caso lo requiere |
| [048](#tool-hpscil--open-space-cellular_automata) | `HPSCIL/Open-Space-Cellular_Automata` | Investigar antes de diseñar o admitir implementación |
| [049](#tool-johanlahti--urban-lu-model) | `johanlahti/urban-lu-model` | Investigar antes de diseñar o admitir implementación |
| [050](#tool-landinsightlab--muse) | `LandInsightLab/MUSE` | Investigar antes de diseñar o admitir implementación |
| [051](#tool-udst--choicemodels) | `UDST/choicemodels` | Dependencia de otro paquete; no construir servidor independiente |
| [052](#tool-udst--developer) | `UDST/developer` | Dependencia de otro paquete; no construir servidor independiente |
| [053](#tool-udst--orca) | `UDST/orca` | Dependencia de otro paquete; no construir servidor independiente |
| [054](#tool-udst--urbansim) | `UDST/urbansim` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [055](#tool-udst--urbansim_defaults) | `UDST/urbansim_defaults` | Dependencia de otro paquete; no construir servidor independiente |
| [056](#tool-udst--urbansim_templates) | `UDST/urbansim_templates` | Dependencia de otro paquete; no construir servidor independiente |
| [057](#tool-cityscope--cs_cityio) | `CityScope/CS_CityIO` | Módulo opcional, solo si el caso lo requiere |
| [058](#tool-cityscope--cs_cityscopejs) | `CityScope/CS_cityscopeJS` | Dependencia de otro paquete; no construir servidor independiente |
| [059](#tool-cityscope--cs_cityscopy) | `CityScope/CS_CityScoPy` | Dependencia de otro paquete; no construir servidor independiente |
| [060](#tool-cityscope--cs_mobility_service) | `CityScope/CS_Mobility_Service` | Investigar antes de diseñar o admitir implementación |
| [061](#tool-cityscope--cs_simulation_gama) | `CityScope/CS_Simulation_GAMA` | Dependencia de otro paquete; no construir servidor independiente |
| [062](#tool-consuldemocracy--consuldemocracy) | `consuldemocracy/consuldemocracy` | Módulo opcional, solo si el caso lo requiere |
| [063](#tool-decidim--decidim) | `decidim/decidim` | Módulo opcional, solo si el caso lo requiere |
| [064](#tool-umap-project--umap) | `umap-project/umap` | Módulo opcional, solo si el caso lo requiere |
| [065](#tool-martibosch--pylandstats) | `martibosch/pylandstats` | Módulo opcional, solo si el caso lo requiere |
| [066](#tool-natcap--invest) | `natcap/invest` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [067](#tool-natcap--pygeoprocessing) | `natcap/pygeoprocessing` | Dependencia de otro paquete; no construir servidor independiente |
| [068](#tool-r-spatialecology--landscapemetrics) | `r-spatialecology/landscapemetrics` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [069](#tool-architecture-building-systems--cityenergyanalyst) | `architecture-building-systems/CityEnergyAnalyst` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [070](#tool-betalab-team--eureca) | `BETALAB-team/EUReCA` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [071](#tool-kth-urbant--mubes-ubem) | `KTH-UrbanT/mubes-ubem` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [072](#tool-ladybug-tools--dragonfly-core) | `ladybug-tools/dragonfly-core` | Dependencia de otro paquete; no construir servidor independiente |
| [073](#tool-ladybug-tools--dragonfly-energy) | `ladybug-tools/dragonfly-energy` | Módulo opcional, solo si el caso lo requiere |
| [074](#tool-ladybug-tools--honeybee-core) | `ladybug-tools/honeybee-core` | Dependencia de otro paquete; no construir servidor independiente |
| [075](#tool-ladybug-tools--honeybee-energy) | `ladybug-tools/honeybee-energy` | Módulo opcional, solo si el caso lo requiere |
| [076](#tool-ladybug-tools--honeybee-radiance) | `ladybug-tools/honeybee-radiance` | Módulo opcional, solo si el caso lo requiere |
| [077](#tool-ladybug-tools--ladybug) | `ladybug-tools/ladybug` | Dependencia de otro paquete; no construir servidor independiente |
| [078](#tool-natlabrockies--comstock) | `NatLabRockies/ComStock` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [079](#tool-natlabrockies--energyplus) | `NatLabRockies/EnergyPlus` | Candidato a capacidad base; admisión técnica pendiente |
| [080](#tool-natlabrockies--openstudio) | `NatLabRockies/OpenStudio` | Dependencia de otro paquete; no construir servidor independiente |
| [081](#tool-natlabrockies--openstudio-hpxml) | `NatLabRockies/OpenStudio-HPXML` | Dependencia de otro paquete; no construir servidor independiente |
| [082](#tool-natlabrockies--resstock) | `NatLabRockies/resstock` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [083](#tool-rwth-ebc--teaser) | `RWTH-EBC/TEASER` | Módulo opcional, solo si el caso lo requiere |
| [084](#tool-samuelduchesne--archetypal) | `samuelduchesne/archetypal` | Dependencia de otro paquete; no construir servidor independiente |
| [085](#tool-samuelduchesne--geomeppy) | `samuelduchesne/geomeppy` | Dependencia de otro paquete; no construir servidor independiente |
| [086](#tool-santoshphilip--eppy) | `santoshphilip/eppy` | Dependencia de otro paquete; no construir servidor independiente |
| [087](#tool-ucl--simstock) | `UCL/simstock` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [088](#tool-urbanopt--urbanopt-cli) | `urbanopt/urbanopt-cli` | Módulo opcional, solo si el caso lo requiere |
| [089](#tool-urbanopt--urbanopt-example-geojson-project) | `urbanopt/urbanopt-example-geojson-project` | Referencia, especificación o fixture; no integración ejecutable autónoma |
| [090](#tool-urbanopt--urbanopt-reopt-gem) | `urbanopt/urbanopt-reopt-gem` | Dependencia de otro paquete; no construir servidor independiente |
| [091](#tool-cloudcompare--cloudcompare) | `CloudCompare/CloudCompare` | Módulo opcional, solo si el caso lo requiere |
| [092](#tool-isl-org--open3d) | `isl-org/Open3D` | Módulo opcional, solo si el caso lo requiere |
| [093](#tool-pdal--pdal) | `PDAL/PDAL` | Candidato a capacidad base; admisión técnica pendiente |
| [094](#tool-pdal--python) | `PDAL/python` | Dependencia de otro paquete; no construir servidor independiente |
| [095](#tool-potree--potree) | `potree/potree` | Módulo opcional, solo si el caso lo requiere |
| [096](#tool-anandb--energyplus-mcp-java) | `anandb/energyplus-mcp-java` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [097](#tool-bonninr--freecad_mcp) | `bonninr/freecad_mcp` | Investigar antes de diseñar o admitir implementación |
| [098](#tool-contextform--freecad-mcp) | `contextform/freecad-mcp` | Investigar antes de diseñar o admitir implementación |
| [099](#tool-ericmartinpe--energyplus-mcp-epjson) | `ericmartinpe/EnergyPlus-MCP-epjson` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [100](#tool-gaopengbin--cesium-mcp) | `gaopengbin/cesium-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [101](#tool-idfkit--idfkit-mcp) | `idfkit/idfkit-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [102](#tool-jagan-shanmugam--open-streetmap-mcp) | `jagan-shanmugam/open-streetmap-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [103](#tool-jjsantos01--qgis_mcp) | `jjsantos01/qgis_mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [104](#tool-jordangunn--gdal-mcp) | `JordanGunn/gdal-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [105](#tool-klabum--swmm-mcp-pub) | `kLabUM/SWMM-MCP-PUB` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [106](#tool-lbnl-eta--energyplus-mcp) | `LBNL-ETA/EnergyPlus-MCP` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [107](#tool-mahdin75--gis-mcp) | `mahdin75/gis-mcp` | Investigar antes de diseñar o admitir implementación |
| [108](#tool-msradam--osmnx-mcp) | `msradam/osmnx-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [109](#tool-neka-nat--freecad-mcp) | `neka-nat/freecad-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [110](#tool-nkarasiak--qgis-mcp) | `nkarasiak/qgis-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [111](#tool-osgeo--grass-mcp) | `OSGeo/grass-mcp` | No hay implementación ejecutable acreditada; no anunciar integración |
| [112](#tool-piatkowski--qgis-mcp) | `piatkowski/qgis-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [113](#tool-profrino--bonsai-bim-skills) | `ProfRino/bonsai-bim-skills` | Referencia, especificación o fixture; no integración ejecutable autónoma |
| [114](#tool-rainergaier--energyplus-mcp-server) | `RainerGaier/energyplus-mcp-server` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [115](#tool-salog0d--urbanplannermcp) | `salog0d/UrbanPlannerMCP` | Investigar antes de diseñar o admitir implementación |
| [116](#tool-show2instruct--ifc-bonsai-mcp) | `Show2Instruct/ifc-bonsai-mcp` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [117](#tool-sparkgeo--geo-mcp-servers) | `sparkgeo/geo-mcp-servers` | Investigar antes de diseñar o admitir implementación |
| [118](#tool-spkane--freecad-addon-robust-mcp-server) | `spkane/freecad-addon-robust-mcp-server` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [119](#tool-xrds76354--sumo-mcp-server) | `XRDS76354/SUMO-MCP-Server` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [120](#tool-zhonghao1995--agentic-swmm-workflow) | `Zhonghao1995/agentic-swmm-workflow` | Investigar antes de diseñar o admitir implementación |
| [121](#tool-3dcitydb--3dcitydb) | `3dcitydb/3dcitydb` | Módulo opcional, solo si el caso lo requiere |
| [122](#tool-3dcitydb--citydb-tool) | `3dcitydb/citydb-tool` | Dependencia de otro paquete; no construir servidor independiente |
| [123](#tool-citygml4j--citygml-tools) | `citygml4j/citygml-tools` | Módulo opcional, solo si el caso lo requiere |
| [124](#tool-citygml4j--citygml4j) | `citygml4j/citygml4j` | Dependencia de otro paquete; no construir servidor independiente |
| [125](#tool-cityjson--cjio) | `cityjson/cjio` | Candidato a capacidad base; admisión técnica pendiente |
| [126](#tool-dtcc-platform--dtcc-core) | `dtcc-platform/dtcc-core` | Dependencia de otro paquete; no construir servidor independiente |
| [127](#tool-dtcc-platform--dtcc-sim) | `dtcc-platform/dtcc-sim` | Investigar antes de diseñar o admitir implementación |
| [128](#tool-dtcc-platform--dtcc-viewer) | `dtcc-platform/dtcc-viewer` | Módulo opcional, solo si el caso lo requiere |
| [129](#tool-project-plateau--plateau-builder) | `Project-PLATEAU/PLATEAU-Builder` | Investigar antes de diseñar o admitir implementación |
| [130](#tool-project-plateau--plateau-gis-converter) | `Project-PLATEAU/PLATEAU-GIS-Converter` | Módulo opcional, solo si el caso lo requiere |
| [131](#tool-reearth--reearth-flow) | `reearth/reearth-flow` | Módulo opcional, solo si el caso lo requiere |
| [132](#tool-tudelft3d--3dcitydb-tools-for-qgis) | `tudelft3d/3DCityDB-Tools-for-QGIS` | Dependencia de otro paquete; no construir servidor independiente |
| [133](#tool-tudelft3d--3dfier) | `tudelft3d/3dfier` | Módulo opcional, solo si el caso lo requiere |
| [134](#tool-tudelft3d--city4cfd) | `tudelft3d/City4CFD` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [135](#tool-vcityteam--ud-viz) | `VCityTeam/UD-Viz` | Módulo opcional, solo si el caso lo requiere |
| [136](#tool-benchmark-urbanism--cityseer-api) | `benchmark-urbanism/cityseer-api` | Candidato a capacidad base; admisión técnica pendiente |
| [137](#tool-gboeing--osmnx) | `gboeing/osmnx` | Candidato a capacidad base; admisión técnica pendiente |
| [138](#tool-pysal--esda) | `pysal/esda` | Módulo opcional, solo si el caso lo requiere |
| [139](#tool-pysal--inequality) | `pysal/inequality` | Módulo opcional, solo si el caso lo requiere |
| [140](#tool-pysal--libpysal) | `pysal/libpysal` | Dependencia de otro paquete; no construir servidor independiente |
| [141](#tool-pysal--mgwr) | `pysal/mgwr` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [142](#tool-pysal--momepy) | `pysal/momepy` | Candidato a capacidad base; admisión técnica pendiente |
| [143](#tool-pysal--segregation) | `pysal/segregation` | Módulo opcional, solo si el caso lo requiere |
| [144](#tool-pysal--spopt) | `pysal/spopt` | Módulo opcional, solo si el caso lo requiere |
| [145](#tool-pysal--spreg) | `pysal/spreg` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [146](#tool-spacegroupucl--depthmapx) | `SpaceGroupUCL/depthmapX` | Módulo opcional, solo si el caso lo requiere |
| [147](#tool-a-b-street--abstreet) | `a-b-street/abstreet` | Investigar antes de diseñar o admitir implementación |
| [148](#tool-activitysim--activitysim) | `ActivitySim/activitysim` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [149](#tool-activitysim--populationsim) | `ActivitySim/populationsim` | Dependencia de otro paquete; no construir servidor independiente |
| [150](#tool-aequilibrae--aequilibrae) | `AequilibraE/aequilibrae` | Módulo opcional, solo si el caso lo requiere |
| [151](#tool-conveyal--analysis-backend) | `conveyal/analysis-backend` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [152](#tool-conveyal--r5) | `conveyal/r5` | Dependencia de otro paquete; no construir servidor independiente |
| [153](#tool-eclipse-sumo--sumo) | `eclipse-sumo/sumo` | Candidato a capacidad base; admisión técnica pendiente |
| [154](#tool-giscience--openrouteservice) | `GIScience/openrouteservice` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [155](#tool-ipea--accessibility) | `ipea/accessibility` | Módulo opcional, solo si el caso lo requiere |
| [156](#tool-ipea--r5r) | `ipea/r5r` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [157](#tool-matsim-org--matsim-libs) | `matsim-org/matsim-libs` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [158](#tool-mobilitydata--gtfs-validator) | `MobilityData/gtfs-validator` | Dependencia de otro paquete; no construir servidor independiente |
| [159](#tool-opentripplanner--opentripplanner) | `opentripplanner/OpenTripPlanner` | Candidato a capacidad base; admisión técnica pendiente |
| [160](#tool-project-osrm--osrm-backend) | `Project-OSRM/osrm-backend` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [161](#tool-r5py--r5py) | `r5py/r5py` | Módulo opcional, solo si el caso lo requiere |
| [162](#tool-ropensci--stplanr) | `ropensci/stplanr` | Módulo opcional, solo si el caso lo requiere |
| [163](#tool-udst--synthpop) | `UDST/synthpop` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [164](#tool-valhalla--valhalla) | `valhalla/valhalla` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [165](#tool-azavea--raster-vision) | `azavea/raster-vision` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [166](#tool-open-eo--openeo-processes) | `Open-EO/openeo-processes` | Dependencia de otro paquete; no construir servidor independiente |
| [167](#tool-open-eo--openeo-python-client) | `Open-EO/openeo-python-client` | Candidato a capacidad base; admisión técnica pendiente |
| [168](#tool-opendatacube--datacube-core) | `opendatacube/datacube-core` | Módulo opcional, solo si el caso lo requiere |
| [169](#tool-opengeos--geoai) | `opengeos/geoai` | Investigar antes de diseñar o admitir implementación |
| [170](#tool-opengeos--segment-geospatial) | `opengeos/segment-geospatial` | Módulo opcional, solo si el caso lo requiere |
| [171](#tool-orfeotoolbox--otb) | `orfeotoolbox/OTB` | Módulo opcional, solo si el caso lo requiere |
| [172](#tool-orfeotoolbox--pyotb) | `orfeotoolbox/pyotb` | Dependencia de otro paquete; no construir servidor independiente |
| [173](#tool-sentinel-hub--sentinelhub-py) | `sentinel-hub/sentinelhub-py` | Módulo opcional, solo si el caso lo requiere |
| [174](#tool-stac-utils--pystac) | `stac-utils/pystac` | Dependencia de otro paquete; no construir servidor independiente |
| [175](#tool-stac-utils--pystac-client) | `stac-utils/pystac-client` | Candidato a capacidad base; admisión técnica pendiente |
| [176](#tool-stac-utils--stac-fastapi) | `stac-utils/stac-fastapi` | Módulo opcional, solo si el caso lo requiere |
| [177](#tool-torchgeo--torchgeo) | `torchgeo/torchgeo` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [178](#tool-crowddynamics--crowddynamics) | `crowddynamics/crowddynamics` | Investigar antes de diseñar o admitir implementación |
| [179](#tool-mengecrowdsim--menge) | `MengeCrowdSim/Menge` | Módulo opcional, solo si el caso lo requiere |
| [180](#tool-pedestriandynamics--jupedsim) | `PedestrianDynamics/jupedsim` | Candidato a capacidad base; admisión técnica pendiente |
| [181](#tool-svenkreiss--socialforce) | `svenkreiss/socialforce` | Investigar antes de diseñar o admitir implementación |
| [182](#tool-dss-extensions--opendssdirect.py) | `dss-extensions/OpenDSSDirect.py` | Módulo opcional, solo si el caso lo requiere |
| [183](#tool-e2niee--pandapower) | `e2nIEE/pandapower` | Candidato a capacidad base; admisión técnica pendiente |
| [184](#tool-natlabrockies--reopt_api) | `NatLabRockies/REopt_API` | Módulo opcional, solo si el caso lo requiere |
| [185](#tool-oemof--oemof-solph) | `oemof/oemof-solph` | Módulo opcional, solo si el caso lo requiere |
| [186](#tool-pypsa--pypsa) | `PyPSA/PyPSA` | Módulo opcional, solo si el caso lo requiere |
| [187](#tool-rwth-ebc--uesgraphs) | `RWTH-EBC/uesgraphs` | Dependencia de otro paquete; no construir servidor independiente |
| [188](#tool-climada-project--climada_petals) | `CLIMADA-project/climada_petals` | Dependencia de otro paquete; no construir servidor independiente |
| [189](#tool-climada-project--climada_python) | `CLIMADA-project/climada_python` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [190](#tool-gem--oq-engine) | `gem/oq-engine` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [191](#tool-universite-gustave-eiffel--noisemodelling) | `Universite-Gustave-Eiffel/NoiseModelling` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [192](#tool-duckdb--duckdb-spatial) | `duckdb/duckdb-spatial` | Módulo opcional, solo si el caso lo requiere |
| [193](#tool-geopandas--geopandas) | `geopandas/geopandas` | Candidato a capacidad base; admisión técnica pendiente |
| [194](#tool-geotools--geotools) | `geotools/geotools` | Dependencia de otro paquete; no construir servidor independiente |
| [195](#tool-jblindsay--whitebox-tools) | `jblindsay/whitebox-tools` | Módulo opcional, solo si el caso lo requiere |
| [196](#tool-locationtech--jts) | `locationtech/jts` | Dependencia de otro paquete; no construir servidor independiente |
| [197](#tool-opengeos--whitebox-python) | `opengeos/whitebox-python` | Dependencia de otro paquete; no construir servidor independiente |
| [198](#tool-osgeo--gdal) | `OSGeo/gdal` | Candidato a capacidad base; admisión técnica pendiente |
| [199](#tool-osgeo--grass) | `OSGeo/grass` | Candidato a capacidad base; admisión técnica pendiente |
| [200](#tool-osgeo--proj) | `OSGeo/PROJ` | Dependencia de otro paquete; no construir servidor independiente |
| [201](#tool-postgis--postgis) | `postgis/postgis` | Candidato a capacidad base; admisión técnica pendiente |
| [202](#tool-qgis--qgis) | `qgis/QGIS` | Candidato a capacidad base; admisión técnica pendiente |
| [203](#tool-r-spatial--sf) | `r-spatial/sf` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [204](#tool-rasterio--rasterio) | `rasterio/rasterio` | Candidato a capacidad base; admisión técnica pendiente |
| [205](#tool-rspatial--terra) | `rspatial/terra` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [206](#tool-saga-gis--saga-gis) | `saga-gis/saga-gis` | Módulo opcional, solo si el caso lo requiere |
| [207](#tool-shapely--shapely) | `shapely/shapely` | Dependencia de otro paquete; no construir servidor independiente |
| [208](#tool-ckan--ckan) | `ckan/ckan` | Módulo opcional, solo si el caso lo requiere |
| [209](#tool-geonetwork--core-geonetwork) | `geonetwork/core-geonetwork` | Módulo opcional, solo si el caso lo requiere |
| [210](#tool-geonode--geonode) | `GeoNode/geonode` | Módulo opcional, solo si el caso lo requiere |
| [211](#tool-geopython--pygeoapi) | `geopython/pygeoapi` | Candidato a capacidad base; admisión técnica pendiente |
| [212](#tool-geoserver--geoserver) | `geoserver/geoserver` | Módulo opcional, solo si el caso lo requiere |
| [213](#tool-mapserver--mapserver) | `MapServer/MapServer` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [214](#tool-gama-platform--gama) | `gama-platform/gama` | Módulo para casos expertos; requiere datos, validación y recursos propios |
| [215](#tool-mesa--mesa) | `mesa/mesa` | Módulo opcional, solo si el caso lo requiere |
| [216](#tool-metadriverse--metaurban) | `metadriverse/metaurban` | Investigar antes de diseñar o admitir implementación |
| [217](#tool-netlogo--netlogo) | `NetLogo/NetLogo` | Módulo opcional, solo si el caso lo requiere |
| [218](#tool-tsinghua-fib-lab--agentsociety) | `tsinghua-fib-lab/AgentSociety` | Investigar antes de diseñar o admitir implementación |
| [219](#tool-tsinghua-fib-lab--citybench) | `tsinghua-fib-lab/CityBench` | Referencia, especificación o fixture; no integración ejecutable autónoma |
| [220](#tool-cesiumgs--3d-tiles-tools) | `CesiumGS/3d-tiles-tools` | Módulo opcional, solo si el caso lo requiere |
| [221](#tool-cesiumgs--cesium) | `CesiumGS/cesium` | Módulo opcional, solo si el caso lo requiere |
| [222](#tool-itowns--itowns) | `iTowns/itowns` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [223](#tool-keplergl--kepler.gl) | `keplergl/kepler.gl` | Comparar/reutilizar MCP existente antes de escribir uno nuevo |
| [224](#tool-maplibre--maplibre-gl-js) | `maplibre/maplibre-gl-js` | Módulo opcional, solo si el caso lo requiere |
| [225](#tool-terriajs--terriajs) | `TerriaJS/terriajs` | Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes |
| [226](#tool-visgl--deck.gl) | `visgl/deck.gl` | Dependencia de otro paquete; no construir servidor independiente |

## 6. Fichas individuales del inventario GitHub


### Familia: Agua drenaje e inundaciones

<a id="tool-deltares--delft3d"></a>

#### 001. Deltares/Delft3D

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Núcleos hidrodinámicos y sus modelos.
- **Puerta de integración propuesta:** Archivos de caso y ejecutables originales.
- **Construir nosotros, solo si falta:** Preparación de corrida, recursos, seguimiento y lectura de resultados por escenario.
- **Con qué y por qué:** conservar compilación Fortran/C++ y control por procesos; el cálculo permanece fuera del servidor MCP. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No reconstruir solver ni inferir batimetría o condiciones de borde.
- **Prueba de admisión pendiente:** Caso de referencia con balance y resultado iguales al ejecutable directo.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/engines_gpl/dsle/packages/wrappers/python/src/pydsle/__init__.py](https://github.com/Deltares/Delft3D/blob/0ee3890e6a81fe0b1587417b9b713b69d1c5f35a/src/engines_gpl/dsle/packages/wrappers/python/src/pydsle/__init__.py); 4/4 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Deltares/Delft3D), [documentación recuperada](https://github.com/Deltares/Delft3D/blob/main/README.md). Commit observado: `0ee3890e6a81fe0b1587417b9b713b69d1c5f35a`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-deltares--hydromt"></a>

#### 002. Deltares/hydromt

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Preparación reproducible de modelos y catálogo de datos.
- **Puerta de integración propuesta:** API y CLI HydroMT.
- **Construir nosotros, solo si falta:** Traducir selección de ciudad a configuración validada y registrar fuentes exactas.
- **Con qué y por qué:** su ecosistema de plugins y preparación de datos ya es Python. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No presentarlo como solver; los plugins tienen versiones y requisitos propios.
- **Prueba de admisión pendiente:** Construir el mismo modelo con API directa y mediante el conector.
- **Evidencia y alcance:** Archivo candidato recuperado: [hydromt/cli/__init__.py](https://github.com/Deltares/hydromt/blob/d64ed50dd89b02df7e590eb08134b73c38623f0e/hydromt/cli/__init__.py); 2/2 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Deltares/hydromt), [documentación recuperada](https://github.com/Deltares/hydromt/blob/main/README.rst), [pyproject.toml](https://github.com/Deltares/hydromt/blob/main/pyproject.toml). Commit observado: `d64ed50dd89b02df7e590eb08134b73c38623f0e`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-deltares--hydromt_sfincs"></a>

#### 003. Deltares/hydromt_sfincs

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Plugin de preparación de SFINCS.
- **Puerta de integración propuesta:** Configuración HydroMT y API del plugin.
- **Construir nosotros, solo si falta:** Mapear insumos municipales y revisar cobertura antes de generar un caso.
- **Con qué y por qué:** reutilizar el plugin, no generar archivos SFINCS a mano. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No atribuirle ejecución ni calibración del solver SFINCS.
- **Prueba de admisión pendiente:** Modelo preparado con rasters, CRS y fronteras comprobados.
- **Evidencia y alcance:** Archivo candidato recuperado: [hydromt_sfincs/__init__.py](https://github.com/Deltares/hydromt_sfincs/blob/d9ae46c170642c71e28cf0294d60f0a575e2d14a/hydromt_sfincs/__init__.py); 14/14 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Deltares/hydromt_sfincs), [documentación recuperada](https://github.com/Deltares/hydromt_sfincs/blob/main/README.rst), [environment.yml](https://github.com/Deltares/hydromt_sfincs/blob/main/environment.yml). Commit observado: `d9ae46c170642c71e28cf0294d60f0a575e2d14a`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-deltares--hydromt_wflow"></a>

#### 004. Deltares/hydromt_wflow

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Plugin de configuración de wflow.
- **Puerta de integración propuesta:** HydroMT y configuración del plugin.
- **Construir nosotros, solo si falta:** Vincular cuencas, forzamientos y fuentes al escenario de ejecución.
- **Con qué y por qué:** conservar contrato y dependencias del plugin. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No duplicar el modelo hidrológico ni asumir que datos globales lo calibran.
- **Prueba de admisión pendiente:** Comparar configuración y rejilla con ejemplo upstream.
- **Evidencia y alcance:** Archivo candidato recuperado: [hydromt_wflow/cli.py](https://github.com/Deltares/hydromt_wflow/blob/566af3b0e70b69dfb3daf35cf7ec40388d3c1471/hydromt_wflow/cli.py); 117/117 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Deltares/hydromt_wflow), [documentación recuperada](https://github.com/Deltares/hydromt_wflow/blob/main/README.rst), [pyproject.toml](https://github.com/Deltares/hydromt_wflow/blob/main/pyproject.toml). Commit observado: `566af3b0e70b69dfb3daf35cf7ec40388d3c1471`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-deltares--sfincs"></a>

#### 005. Deltares/SFINCS

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Motor de inundación y formatos propios.
- **Puerta de integración propuesta:** Ejecutable y archivos de caso; preparación separada.
- **Construir nosotros, solo si falta:** Encolar corridas, conservar diagnósticos y devolver mapas con unidades.
- **Con qué y por qué:** proceso nativo separado; escoger CPU/GPU según compilación admitida. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No inventar datos de terreno, lluvia o fronteras; validar distribución binaria.
- **Prueba de admisión pendiente:** Caso pequeño con profundidades y balance contrastados.
- **Evidencia y alcance:** Archivo candidato recuperado: [source/src/sfincs.f90](https://github.com/Deltares/SFINCS/blob/7500849d1175c1314847af99c5a54b8c18d4b5c0/source/src/sfincs.f90); 73/73 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Deltares/SFINCS), [documentación recuperada](https://github.com/Deltares/SFINCS/blob/main/README.rst). Commit observado: `7500849d1175c1314847af99c5a54b8c18d4b5c0`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-geoscienceaustralia--anuga_core"></a>

#### 006. GeoscienceAustralia/anuga_core

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Modelado hidrodinámico sobre malla.
- **Puerta de integración propuesta:** API Python ANUGA y extensiones compiladas.
- **Construir nosotros, solo si falta:** Registrar malla, fronteras y escenario; exponer corrida acotada y resultados.
- **Con qué y por qué:** la definición del problema ya usa objetos Python y código nativo. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No reconstruir esquema numérico ni vender una malla como modelo calibrado.
- **Prueba de admisión pendiente:** Ejemplo hidráulico conocido y sensibilidad al paso/malla.
- **Evidencia y alcance:** Archivo candidato recuperado: [anuga/utilities/model_tools.py](https://github.com/GeoscienceAustralia/anuga_core/blob/a10ac78fc7b68ae6af84d82a8f65f3b1c38ca0af/anuga/utilities/model_tools.py); 420/684 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/GeoscienceAustralia/anuga_core), [documentación recuperada](https://github.com/GeoscienceAustralia/anuga_core/blob/main/README.rst), [pyproject.toml](https://github.com/GeoscienceAustralia/anuga_core/blob/main/pyproject.toml). Commit observado: `a10ac78fc7b68ae6af84d82a8f65f3b1c38ca0af`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-markuspic--swmm_api"></a>

#### 007. MarkusPic/swmm_api

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Lectura, edición y análisis de archivos SWMM.
- **Puerta de integración propuesta:** API Python de archivos INP, reportes y salidas.
- **Construir nosotros, solo si falta:** Cambios tipados sobre copias y comparación documentada de entradas.
- **Con qué y por qué:** conservar sus parsers; complementar el paquete SWMM. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No duplicar PySWMM ni prometer control temporal por editar un archivo.
- **Prueba de admisión pendiente:** Editar un parámetro y verificar preservación de secciones no tocadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [setup.py](https://github.com/MarkusPic/swmm_api/blob/21b9d72f59303e5650b2fe806d064743cc3ecab2/setup.py); 5/5 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/MarkusPic/swmm_api), [documentación recuperada](https://github.com/MarkusPic/swmm_api/blob/main/README.md), [pyproject.toml](https://github.com/MarkusPic/swmm_api/blob/main/pyproject.toml). Commit observado: `21b9d72f59303e5650b2fe806d064743cc3ecab2`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-openstreams--wflow"></a>

#### 008. openstreams/wflow

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Reserva de mantenimiento:** el repositorio figura archivado en el corte. No admitirlo como base nueva sin justificar dependencia, sucesor y mantenimiento.
- **Traer del original:** Modelo hidrológico de la línea de este repositorio.
- **Puerta de integración propuesta:** Scripts y configuraciones propios; verificar versión vigente.
- **Construir nosotros, solo si falta:** Solo receta y adaptación si existe un caso que requiera esta línea.
- **Con qué y por qué:** respetar su runtime; contrastar con HydroMT/wflow antes de incorporarlo. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No confundir este repositorio con todas las versiones actuales de wflow.
- **Prueba de admisión pendiente:** Caso upstream ejecutado con dependencias realmente disponibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [openda_bmi/openda/bmi/__init__.py](https://github.com/openstreams/wflow/blob/416af957b268370e829af49824f9a5ad9125b4ed/openda_bmi/openda/bmi/__init__.py); 0/0 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/openstreams/wflow), [documentación recuperada](https://github.com/openstreams/wflow/blob/master/README.rst), [Dockerfile](https://github.com/openstreams/wflow/blob/master/Dockerfile). Commit observado: `416af957b268370e829af49824f9a5ad9125b4ed`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-openwateranalytics--epanet"></a>

#### 009. OpenWaterAnalytics/EPANET

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Toolkit hidráulico y de calidad de agua.
- **Puerta de integración propuesta:** Biblioteca C/toolkit y distribuciones originales.
- **Construir nosotros, solo si falta:** Operaciones tipadas de red y corridas con escenarios aislados.
- **Con qué y por qué:** usar un binding existente admitido; escogerlo por cobertura del toolkit. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No reescribir hidráulica; distinguir binding, motor y editor gráfico.
- **Prueba de admisión pendiente:** Red pequeña con caudales, presión y balance conocidos.
- **Evidencia y alcance:** Archivo candidato recuperado: [run/main.c](https://github.com/OpenWaterAnalytics/EPANET/blob/57d8bd8ad60e89b57f2a1ac591f05c8e13589866/run/main.c); 93/93 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/OpenWaterAnalytics/EPANET), [documentación recuperada](https://github.com/OpenWaterAnalytics/EPANET/blob/dev/README.md), [CMakeLists.txt](https://github.com/OpenWaterAnalytics/EPANET/blob/dev/CMakeLists.txt). Commit observado: `57d8bd8ad60e89b57f2a1ac591f05c8e13589866`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pyswmm--pyswmm"></a>

#### 010. pyswmm/pyswmm

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Control programático de SWMM y lectura por paso.
- **Puerta de integración propuesta:** API Python y motor asociado.
- **Construir nosotros, solo si falta:** Fachada de operaciones hidráulicas, estado de corrida y contexto de modelo.
- **Con qué y por qué:** API nativa evita un puente C construido por nosotros. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No duplicar simulación ni elegirlo además de otro wrapper sin necesidad.
- **Prueba de admisión pendiente:** Mismo INP, versión y lluvia producen mismas series directas y por MCP.
- **Evidencia y alcance:** Archivo candidato recuperado: [pyswmm/toolkitapi.py](https://github.com/pyswmm/pyswmm/blob/97cb36ff7820ba23ed6c09d9a38551aa619ea88a/pyswmm/toolkitapi.py); 420/580 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pyswmm/pyswmm), [documentación recuperada](https://github.com/pyswmm/pyswmm/blob/main/README.md), [pyproject.toml](https://github.com/pyswmm/pyswmm/blob/main/pyproject.toml). Commit observado: `97cb36ff7820ba23ed6c09d9a38551aa619ea88a`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-usepa--epanet2.2"></a>

#### 011. USEPA/EPANET2.2

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Aplicación y fuentes de la distribución EPANET 2.2.
- **Puerta de integración propuesta:** Ejecutable/editor y archivos INP.
- **Construir nosotros, solo si falta:** Receta de esa distribución y compatibilidad de importación, si es requerida.
- **Con qué y por qué:** conservar aplicación; preferir toolkit para automatización. Aplicación/binario y bibliotecas de su distribución. Seleccionar CLI o binding solo después de probar qué operación funciona fuera del escritorio.
- **No reconstruir / crítica:** No sumar otro motor hidráulico por confundir editor con toolkit.
- **Prueba de admisión pendiente:** Abrir/exportar INP y contrastarlo con OpenWaterAnalytics/EPANET.
- **Evidencia y alcance:** Archivo candidato recuperado: [SRC_engines/src/run/main.c](https://github.com/USEPA/EPANET2.2/blob/598ee6cd214de07a0d62e7dafc1bdbf09173645a/SRC_engines/src/run/main.c); 93/93 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/USEPA/EPANET2.2), [documentación recuperada](https://github.com/USEPA/EPANET2.2/blob/master/README.md). Commit observado: `598ee6cd214de07a0d62e7dafc1bdbf09173645a`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-usepa--stormwater-management-model"></a>

#### 012. USEPA/Stormwater-Management-Model

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Motor SWMM y formatos de entrada/salida.
- **Puerta de integración propuesta:** Toolkit o ejecutable nativo.
- **Construir nosotros, solo si falta:** Receta versionada y fachada de corrida cuando no alcance un MCP existente.
- **Con qué y por qué:** mantener motor C; evaluar PySWMM y MCP SWMM antes de escribir puente. Aplicación/binario y bibliotecas de su distribución. Seleccionar CLI o binding solo después de probar qué operación funciona fuera del escritorio.
- **No reconstruir / crítica:** No construir un segundo solver; no duplicar la envoltura si ya cubre el caso.
- **Prueba de admisión pendiente:** Caso oficial con reporte y errores contrastados.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/run/main.c](https://github.com/USEPA/Stormwater-Management-Model/blob/07c371f8a0d477da1d9d4e7c0d75719664f62fec/src/run/main.c); 104/104 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/USEPA/Stormwater-Management-Model), [documentación recuperada](https://github.com/USEPA/Stormwater-Management-Model/blob/develop/README.md), [CMakeLists.txt](https://github.com/USEPA/Stormwater-Management-Model/blob/develop/CMakeLists.txt). Commit observado: `07c371f8a0d477da1d9d4e7c0d75719664f62fec`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-usepa--wntr"></a>

#### 013. USEPA/WNTR

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Análisis de resiliencia y escenarios de redes de agua.
- **Puerta de integración propuesta:** API Python y conexión EPANET.
- **Construir nosotros, solo si falta:** Escenarios de perturbación con supuestos, métricas y procedencia explícitos.
- **Con qué y por qué:** conservar modelos de red y análisis de WNTR. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No confundir sus simuladores ni presentar fallas hipotéticas como observaciones.
- **Prueba de admisión pendiente:** Red conocida, perturbación reproducible y unidades verificadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [wntr/sim/models/__init__.py](https://github.com/USEPA/WNTR/blob/a91e6f26e992d04a9c874102c1434433ef7965a4/wntr/sim/models/__init__.py); 3/3 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/USEPA/WNTR), [documentación recuperada](https://github.com/USEPA/WNTR/blob/main/README.md), [pyproject.toml](https://github.com/USEPA/WNTR/blob/main/pyproject.toml). Commit observado: `a91e6f26e992d04a9c874102c1434433ef7965a4`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.


### Familia: BIM CAD y diseño computacional

<a id="tool-blender--blender"></a>

#### 014. blender/blender

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Modelado, escena y renderizado.
- **Puerta de integración propuesta:** API bpy en Blender y ejecución por proceso/plugin.
- **Construir nosotros, solo si falta:** Comandos de escena acotados y vínculo entre objetos urbanos y artefactos.
- **Con qué y por qué:** Python dentro de Blender; puente externo solo para MCP. Plugin o componente en el runtime de la aplicación anfitriona y un puente tipado externo cuando se requiera MCP. Debe respetar el hilo de interfaz, documento y sesión de la aplicación.
- **No reconstruir / crítica:** No reconstruir editor; geometría visual no equivale a BIM ni simulación física.
- **Prueba de admisión pendiente:** Crear, guardar y reabrir escena; verificar identidad y dimensiones.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [source/creator/creator.cc](https://github.com/blender/blender/blob/4c2757a939480c99ab7dfd7fa01cbe727f212d80/source/creator/creator.cc); lectura parcial de 600/687 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/blender/blender), [documentación recuperada](https://github.com/blender/blender/blob/main/README.md), [CMakeLists.txt](https://github.com/blender/blender/blob/main/CMakeLists.txt). Commit observado: `4c2757a939480c99ab7dfd7fa01cbe727f212d80`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-buildingsmart--bcf-xml"></a>

#### 015. buildingSMART/BCF-XML

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Formato de incidencias y coordinación BIM.
- **Puerta de integración propuesta:** Esquemas BCF y archivos de intercambio.
- **Construir nosotros, solo si falta:** Vincular incidencias a objetos/versiones y validar paquetes antes de intercambiarlos.
- **Con qué y por qué:** reutilizar esquemas y parser mantenido dentro del conector BIM. Reutilizar esquemas, formatos y validadores concretos; fijar sus versiones. No hay un motor científico que desplegar por el mero hecho de existir una especificación.
- **No reconstruir / crítica:** No convertir una especificación en motor ni duplicar gestión de incidencias existente.
- **Prueba de admisión pendiente:** Paquete BCF válido, referencia resuelta y caso con identificador roto.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/buildingSMART/BCF-XML), [documentación recuperada](https://github.com/buildingSMART/BCF-XML/blob/release_3_0/README.md). Commit observado: `bc48611d0d7a1587f028a2b69677a1aafd5cd0a8`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-buildingsmart--ids"></a>

#### 016. buildingSMART/IDS

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Especificación de requisitos de información BIM.
- **Puerta de integración propuesta:** XML y validadores compatibles por seleccionar.
- **Construir nosotros, solo si falta:** Preparar requisitos del proyecto y asociar resultados a la revisión IFC.
- **Con qué y por qué:** delegar validación en implementación existente, no solo leer XML. Reutilizar esquemas, formatos y validadores concretos; fijar sus versiones. No hay un motor científico que desplegar por el mero hecho de existir una especificación.
- **No reconstruir / crítica:** No afirmar cumplimiento normativo general por pasar un IDS.
- **Prueba de admisión pendiente:** IFC con requisito cumplido e incumplido y reporte trazable.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/buildingSMART/IDS), [documentación recuperada](https://github.com/buildingSMART/IDS/blob/development/README.md). Commit observado: `870f9c4e6e8f414e737b4d84ca1aa9b46fc6c8f3`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-compas-dev--compas"></a>

#### 017. compas-dev/compas

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Geometría y estructuras para diseño computacional.
- **Puerta de integración propuesta:** API Python COMPAS.
- **Construir nosotros, solo si falta:** Traducir operaciones de diseño seleccionadas y conservar parámetros/identidades.
- **Con qué y por qué:** sus objetos y extensiones se consumen directamente. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No publicar toda la API ni atribuirle validación estructural universal.
- **Prueba de admisión pendiente:** Operación geométrica conocida con tolerancias explícitas.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/compas/__main__.py](https://github.com/compas-dev/compas/blob/0c2d98df24047b5f8c58ad3a3e5dbb45d753c18d/src/compas/__main__.py); 30/30 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/compas-dev/compas), [documentación recuperada](https://github.com/compas-dev/compas/blob/main/README.md), [pyproject.toml](https://github.com/compas-dev/compas/blob/main/pyproject.toml). Commit observado: `0c2d98df24047b5f8c58ad3a3e5dbb45d753c18d`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-compas-dev--compas_fab"></a>

#### 018. compas-dev/compas_fab

- **Dictamen:** Fuera del alcance inicial; no construir ahora.
- **Traer del original:** Planificación e interfaces para fabricación robótica.
- **Puerta de integración propuesta:** API Python y backends de robótica.
- **Construir nosotros, solo si falta:** Solo adaptar un flujo de fabricación expresamente requerido.
- **Con qué y por qué:** mantener clientes/backends COMPAS FAB en entorno específico. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No añadir operación de robots al alcance urbano por compartir geometría.
- **Prueba de admisión pendiente:** Planificación simulada contra backend de prueba, sin accionar hardware.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/compas_fab/backends/interfaces/__init__.py](https://github.com/compas-dev/compas_fab/blob/ad53bb74462d040751a616e1cf1829565e8332fb/src/compas_fab/backends/interfaces/__init__.py); 38/38 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/compas-dev/compas_fab), [documentación recuperada](https://github.com/compas-dev/compas_fab/blob/main/README.md), [pyproject.toml](https://github.com/compas-dev/compas_fab/blob/main/pyproject.toml). Commit observado: `ad53bb74462d040751a616e1cf1829565e8332fb`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-dynamods--dynamo"></a>

#### 019. DynamoDS/Dynamo

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Programación visual y ejecución de grafos de diseño.
- **Puerta de integración propuesta:** Host de Dynamo y grafos; verificar ejecución automatizable.
- **Construir nosotros, solo si falta:** Catálogo de grafos admitidos, parámetros y salidas, condicionado al host.
- **Con qué y por qué:** usar runtime de Dynamo/.NET, sin traducir grafos a Python o Go. Plugin o componente en el runtime de la aplicación anfitriona y un puente tipado externo cuando se requiera MCP. Debe respetar el hilo de interfaz, documento y sesión de la aplicación.
- **No reconstruir / crítica:** No asumir que todo nodo funciona fuera de su aplicación anfitriona.
- **Prueba de admisión pendiente:** Grafo pequeño con mismos resultados dentro y fuera del puente.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/Engine/ProtoCore/Parser/Parser.h](https://github.com/DynamoDS/Dynamo/blob/a6a335702c3887fb50c901f9475d29a5b25b046a/src/Engine/ProtoCore/Parser/Parser.h); 152/152 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/DynamoDS/Dynamo), [documentación recuperada](https://github.com/DynamoDS/Dynamo/blob/master/README.md). Commit observado: `a6a335702c3887fb50c901f9475d29a5b25b046a`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-freecad--freecad"></a>

#### 020. FreeCAD/FreeCAD

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** CAD paramétrico y objetos de documento.
- **Puerta de integración propuesta:** API Python, FreeCADCmd y sesión gráfica.
- **Construir nosotros, solo si falta:** Recetas y comandos paramétricos solo si un MCP existente no los cubre.
- **Con qué y por qué:** API Python del propio FreeCAD y adaptador existente candidato. Plugin o componente en el runtime de la aplicación anfitriona y un puente tipado externo cuando se requiera MCP. Debe respetar el hilo de interfaz, documento y sesión de la aplicación.
- **No reconstruir / crítica:** No reconstruir CAD; modelado libre y referencias topológicas requieren control.
- **Prueba de admisión pendiente:** Modificar parámetro, recomputar, guardar y reabrir documento.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/Tools/bindings/model/__init__.py](https://github.com/FreeCAD/FreeCAD/blob/64c74e404e0778db9c11103b332695351ea39b6c/src/Tools/bindings/model/__init__.py); 1/1 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/FreeCAD/FreeCAD), [documentación recuperada](https://github.com/FreeCAD/FreeCAD/blob/main/README.md), [CMakeLists.txt](https://github.com/FreeCAD/FreeCAD/blob/main/CMakeLists.txt). Commit observado: `64c74e404e0778db9c11103b332695351ea39b6c`. Licencia en el inventario: `LGPL-2.1` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ifcopenshell--ifcopenshell"></a>

#### 021. IfcOpenShell/IfcOpenShell

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Lectura, edición y geometría IFC; herramientas relacionadas.
- **Puerta de integración propuesta:** API Python/C++ y utilidades existentes.
- **Construir nosotros, solo si falta:** Consultas BIM tipadas, revisiones y vínculo estable con objetos urbanos.
- **Con qué y por qué:** bindings existentes; preservar semántica IFC y unidades. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No reimplementar parser IFC ni inferir propiedades técnicas faltantes.
- **Prueba de admisión pendiente:** IFC pequeño con GUID, unidades y geometría preservados tras edición.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/ifcopenshell-python/ifcopenshell/api/__init__.py](https://github.com/IfcOpenShell/IfcOpenShell/blob/ba5f43c13af5dd5da69e04c6eed45d99ec718b58/src/ifcopenshell-python/ifcopenshell/api/__init__.py); 314/314 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/IfcOpenShell/IfcOpenShell), [documentación recuperada](https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.9.0/README.md), [Dockerfile](https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.9.0/Dockerfile). Commit observado: `ba5f43c13af5dd5da69e04c6eed45d99ec718b58`. Licencia en el inventario: `LGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-openscad--openscad"></a>

#### 022. openscad/openscad

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Modelado paramétrico mediante lenguaje OpenSCAD.
- **Puerta de integración propuesta:** CLI y archivos de modelo.
- **Construir nosotros, solo si falta:** Ejecutar plantillas admitidas con parámetros y artefactos identificables.
- **Con qué y por qué:** el límite natural es un ejecutable; no requiere incrustar C++. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No generar código irrestricto ni tratar sólidos como objetos BIM completos.
- **Prueba de admisión pendiente:** Plantilla con volumen/dimensiones esperadas y parámetro inválido.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/openscad.cc](https://github.com/openscad/openscad/blob/df091e896a1fe87655065b0859239db0d36d250a/src/openscad.cc); lectura parcial de 600/1240 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/openscad/openscad), [documentación recuperada](https://github.com/openscad/openscad/blob/master/README.md), [CMakeLists.txt](https://github.com/openscad/openscad/blob/master/CMakeLists.txt). Commit observado: `df091e896a1fe87655065b0859239db0d36d250a`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pixaranimationstudios--openusd"></a>

#### 023. PixarAnimationStudios/OpenUSD

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Composición e intercambio de escenas USD.
- **Puerta de integración propuesta:** Bibliotecas y bindings USD.
- **Construir nosotros, solo si falta:** Conversión y mapeo de IDs únicamente cuando un consumidor lo necesite.
- **Con qué y por qué:** dependencia del exportador/visor, no servidor MCP separado. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No convertir USD en modelo de autoridad urbana o inventar semántica IFC.
- **Prueba de admisión pendiente:** Escena con transformaciones y unidades conservadas en ida y vuelta.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [pxr/usd/usd/stage.h](https://github.com/PixarAnimationStudios/OpenUSD/blob/aaf0a1150211969d7f743676b230233b550b9d21/pxr/usd/usd/stage.h); lectura parcial de 600/2344 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/PixarAnimationStudios/OpenUSD), [documentación recuperada](https://github.com/PixarAnimationStudios/OpenUSD/blob/dev/README.md), [CMakeLists.txt](https://github.com/PixarAnimationStudios/OpenUSD/blob/dev/CMakeLists.txt). Commit observado: `aaf0a1150211969d7f743676b230233b550b9d21`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-specklesystems--speckle-server"></a>

#### 024. specklesystems/speckle-server

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Servidor colaborativo de objetos, versiones y proyectos.
- **Puerta de integración propuesta:** API de la instancia y autenticación correspondiente.
- **Construir nosotros, solo si falta:** Selección de proyecto, lectura de versiones y publicación autorizada de resultados.
- **Con qué y por qué:** cliente tipado; mantener servidor y permisos originales. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No reconstruir colaboración; verificar API y conectores de la versión instalada.
- **Prueba de admisión pendiente:** Publicar y recuperar objeto en proyecto de prueba con misma identidad.
- **Evidencia y alcance:** Archivo candidato recuperado: [packages/monitor-deployment/src/server/routes/index.ts](https://github.com/specklesystems/speckle-server/blob/51d43b91c4681a75bff8b285da7f443a4599da67/packages/monitor-deployment/src/server/routes/index.ts); 13/13 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/specklesystems/speckle-server), [documentación recuperada](https://github.com/specklesystems/speckle-server/blob/main/README.md), [docker-compose-deps.yml](https://github.com/specklesystems/speckle-server/blob/main/docker-compose-deps.yml). Commit observado: `51d43b91c4681a75bff8b285da7f443a4599da67`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-specklesystems--specklepy"></a>

#### 025. specklesystems/specklepy

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Cliente Python de Speckle y conversión de objetos.
- **Puerta de integración propuesta:** SDK Python.
- **Construir nosotros, solo si falta:** Serialización y traducción de nuestros artefactos a objetos Speckle.
- **Con qué y por qué:** usar dentro del adaptador Speckle, porque ya encapsula el protocolo. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No crear otra plataforma ni servidor MCP por cada SDK.
- **Prueba de admisión pendiente:** Enviar/recibir objeto de prueba sin perder propiedades acordadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/specklepy/api/__init__.py](https://github.com/specklesystems/specklepy/blob/d998c479578976bb34c85b3abbd37200598c93e8/src/specklepy/api/__init__.py); 0/0 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/specklesystems/specklepy), [documentación recuperada](https://github.com/specklesystems/specklepy/blob/main/README.md), [docker-compose-internal.yml](https://github.com/specklesystems/specklepy/blob/main/docker-compose-internal.yml). Commit observado: `d998c479578976bb34c85b3abbd37200598c93e8`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Catálogos de descubrimiento

<a id="tool-apa-technology-division--urban-and-regional-planning-resources"></a>

#### 026. APA-Technology-Division/urban-and-regional-planning-resources

- **Dictamen:** Referencia, especificación o fixture; no integración ejecutable autónoma.
- **Traer del original:** Índice de herramientas y referencias urbanísticas.
- **Puerta de integración propuesta:** Documentos y enlaces del catálogo.
- **Construir nosotros, solo si falta:** Actualizar procedencia y detectar enlaces/entradas duplicadas.
- **Con qué y por qué:** ingestión documental; no tiene ejecución científica que envolver. Solo incorporación documental o fixture a la investigación/pruebas. No instalar ni publicar un servidor MCP para este repositorio.
- **No reconstruir / crítica:** No anunciar cada enlace como integración disponible.
- **Prueba de admisión pendiente:** Enlace vigente y clasificación correcta de una muestra revisada.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/APA-Technology-Division/urban-and-regional-planning-resources), [documentación recuperada](https://github.com/APA-Technology-Division/urban-and-regional-planning-resources/blob/main/README.md). Commit observado: `8ae1ea59ad29a9f4180a34c2041a24ad19de14ff`. Licencia en el inventario: `CC0-1.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-durbanitas--awesome-urban-planning"></a>

#### 027. durbanitas/awesome-urban-planning

- **Dictamen:** Referencia, especificación o fixture; no integración ejecutable autónoma.
- **Traer del original:** Listado de recursos de planificación.
- **Puerta de integración propuesta:** Archivos documentales.
- **Construir nosotros, solo si falta:** Descubrimiento y revisión humana de candidatos.
- **Con qué y por qué:** fuente del inventario, sin servicio MCP por repositorio. Solo incorporación documental o fixture a la investigación/pruebas. No instalar ni publicar un servidor MCP para este repositorio.
- **No reconstruir / crítica:** No equiparar popularidad o inclusión en la lista con aptitud técnica.
- **Prueba de admisión pendiente:** Comprobar identidad, licencia y propósito de candidatos nuevos.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/durbanitas/awesome-urban-planning), [documentación recuperada](https://github.com/durbanitas/awesome-urban-planning/blob/master/readme.md). Commit observado: `88c129dde859d1db40470a09b3d3e9532b912b8d`. Licencia en el inventario: `CC0-1.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ireliya--awesome-urban-planning-agents"></a>

#### 028. Ireliya/Awesome-Urban-Planning-Agents

- **Dictamen:** Referencia, especificación o fixture; no integración ejecutable autónoma.
- **Traer del original:** Referencias sobre agentes para planificación urbana.
- **Puerta de integración propuesta:** Catálogo y enlaces a implementaciones.
- **Construir nosotros, solo si falta:** Distinguir artículos, demos, agentes y herramientas ejecutables.
- **Con qué y por qué:** solo investigación hasta inspeccionar cada implementación. Solo incorporación documental o fixture a la investigación/pruebas. No instalar ni publicar un servidor MCP para este repositorio.
- **No reconstruir / crítica:** No confundir un agente completo con una herramienta neutral para cualquier IA.
- **Prueba de admisión pendiente:** Verificar que una entrada tenga código y una interfaz real.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/Ireliya/Awesome-Urban-Planning-Agents), [documentación recuperada](https://github.com/Ireliya/Awesome-Urban-Planning-Agents/blob/main/README.md). Commit observado: `876a3df4572b3310e8f116bcf84dacf15bdce082`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-sacridini--awesome-geospatial"></a>

#### 029. sacridini/Awesome-Geospatial

- **Dictamen:** Referencia, especificación o fixture; no integración ejecutable autónoma.
- **Traer del original:** Índice geoespacial amplio.
- **Puerta de integración propuesta:** Documentos y enlaces.
- **Construir nosotros, solo si falta:** Ampliar búsqueda y detectar alternativas, sin instalaciones automáticas.
- **Con qué y por qué:** mantener fuente y fecha de revisión. Solo incorporación documental o fixture a la investigación/pruebas. No instalar ni publicar un servidor MCP para este repositorio.
- **No reconstruir / crítica:** No prometer cobertura operativa de todos sus enlaces.
- **Prueba de admisión pendiente:** Resolver y clasificar nuevos repositorios antes de admitirlos.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/sacridini/Awesome-Geospatial), [documentación recuperada](https://github.com/sacridini/Awesome-Geospatial/blob/master/README.md). Commit observado: `b3309282cfe938df9e16bd9255f289d4201320eb`. Licencia en el inventario: `CC0-1.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Clima urbano y atmósfera

<a id="tool-kunifujiwara--voxcity"></a>

#### 030. kunifujiwara/VoxCity

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Preparación de representación urbana voxelizada y análisis asociados.
- **Puerta de integración propuesta:** API Python y proveedores de datos.
- **Construir nosotros, solo si falta:** Escenarios con insumos fijados y extracción de productos identificables.
- **Con qué y por qué:** preservar estructuras y pipeline del proyecto. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No convertir estimaciones de geometría o vegetación en levantamiento observado.
- **Prueba de admisión pendiente:** Área sintética o conocida con resolución, CRS y cobertura declarados.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/voxcity/cli.py](https://github.com/kunifujiwara/VoxCity/blob/61ff5547e6fa9079dcd23c1cb4d37ec793194277/src/voxcity/cli.py); 301/301 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/kunifujiwara/VoxCity), [documentación recuperada](https://github.com/kunifujiwara/VoxCity/blob/main/README.md), [pyproject.toml](https://github.com/kunifujiwara/VoxCity/blob/main/pyproject.toml). Commit observado: `61ff5547e6fa9079dcd23c1cb4d37ec793194277`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ladybug-tools--uwg"></a>

#### 031. ladybug-tools/uwg

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Modelo Urban Weather Generator.
- **Puerta de integración propuesta:** API Python y archivos meteorológicos.
- **Construir nosotros, solo si falta:** Escenarios parametrizados de modificación meteorológica y comparación de EPW.
- **Con qué y por qué:** reutilizar modelo y lector/escritor meteorológico. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No presentarlo como CFD ni clima local validado sin parámetros adecuados.
- **Prueba de admisión pendiente:** EPW de prueba, parámetros fijados y salida comparada con ejecución directa.
- **Evidencia y alcance:** Archivo candidato recuperado: [uwg/cli/__init__.py](https://github.com/ladybug-tools/uwg/blob/ddedeac65df06126eb8edc0d2f150b30ff399ea2/uwg/cli/__init__.py); 67/67 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ladybug-tools/uwg), [documentación recuperada](https://github.com/ladybug-tools/uwg/blob/master/README.md), [cli-requirements.txt](https://github.com/ladybug-tools/uwg/blob/master/cli-requirements.txt). Commit observado: `ddedeac65df06126eb8edc0d2f150b30ff399ea2`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-openfoam--openfoam-dev"></a>

#### 032. OpenFOAM/OpenFOAM-dev

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Solvers CFD, malla y utilidades de OpenFOAM.
- **Puerta de integración propuesta:** Casos, diccionarios y ejecutables nativos.
- **Construir nosotros, solo si falta:** Plantillas expertas de caso, trabajos aislados y extracción de resultados.
- **Con qué y por qué:** conservar toolchain C++ y ejecución paralela; controlar procesos externos. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No generar un CFD defendible solo a partir de edificios OSM.
- **Prueba de admisión pendiente:** Caso de referencia, convergencia y comparación de campo/condiciones de borde.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/twoPhaseModels/interfaceProperties/interfaceProperties.C](https://github.com/OpenFOAM/OpenFOAM-dev/blob/fae12b3bcfd2d0c8075c7fe1f9982a47ea9a7a41/src/twoPhaseModels/interfaceProperties/interfaceProperties.C); 242/242 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/OpenFOAM/OpenFOAM-dev), [documentación recuperada](https://github.com/OpenFOAM/OpenFOAM-dev/blob/master/README.org). Commit observado: `fae12b3bcfd2d0c8075c7fe1f9982a47ea9a7a41`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-udales--u-dales"></a>

#### 033. uDALES/u-dales

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelo atmosférico LES y tratamiento urbano.
- **Puerta de integración propuesta:** Compilación y configuración del modelo.
- **Construir nosotros, solo si falta:** Preparar expedientes de corrida y registrar forzamientos, malla y recursos.
- **Con qué y por qué:** mantener Fortran/MPI y scripts oficiales. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No confundir simulación de alta resolución con datos disponibles para cualquier ciudad.
- **Prueba de admisión pendiente:** Caso LES upstream, configuración documentada y conservación verificada.
- **Evidencia y alcance:** Archivo candidato recuperado: [tools/python/udgeom/__init__.py](https://github.com/uDALES/u-dales/blob/f5801c3c7319ff75bffe1610642b2b239fed3af8/tools/python/udgeom/__init__.py); 91/91 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/uDALES/u-dales), [documentación recuperada](https://github.com/uDALES/u-dales/blob/master/README.md), [CMakeLists.txt](https://github.com/uDALES/u-dales/blob/master/CMakeLists.txt). Commit observado: `f5801c3c7319ff75bffe1610642b2b239fed3af8`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-umep-dev--solweig"></a>

#### 034. UMEP-dev/solweig

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Modelo radiativo y confort asociado a SOLWEIG.
- **Puerta de integración propuesta:** Entradas y ejecutor del proyecto; contrastar ruta UMEP.
- **Construir nosotros, solo si falta:** Normalizar paquetes meteorológicos y rasters para una corrida trazable.
- **Con qué y por qué:** compartir entorno compatible con la implementación SOLWEIG seleccionada. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No mantener dos versiones de SOLWEIG por separado sin necesidad.
- **Prueba de admisión pendiente:** Caso con rasters de referencia y resultado radiativo contrastado.
- **Evidencia y alcance:** Archivo candidato recuperado: [pysrc/solweig/models/__init__.py](https://github.com/UMEP-dev/solweig/blob/813876f78f90f033bc5ea57b1d942a04ff793a82/pysrc/solweig/models/__init__.py); 46/46 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UMEP-dev/solweig), [documentación recuperada](https://github.com/UMEP-dev/solweig/blob/main/README.md), [pyproject.toml](https://github.com/UMEP-dev/solweig/blob/main/pyproject.toml). Commit observado: `813876f78f90f033bc5ea57b1d942a04ff793a82`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-umep-dev--suews"></a>

#### 035. UMEP-dev/SUEWS

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelo de balance de agua y energía superficial.
- **Puerta de integración propuesta:** Configuración, forzamientos y wrapper admitido.
- **Construir nosotros, solo si falta:** Validación de cobertura temporal y escenarios de superficies urbanas.
- **Con qué y por qué:** usar ejecutor/wrapper soportado, preservando núcleo y versiones. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No sustituir calibración, meteorología ni parámetros de superficie.
- **Prueba de admisión pendiente:** Serie de referencia con balances y frecuencia temporal verificados.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/supy/data_model/validation/pipeline/__init__.py](https://github.com/UMEP-dev/SUEWS/blob/b63f8652ccf92413fda1326d9867821c26da0cc7/src/supy/data_model/validation/pipeline/__init__.py); 25/25 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UMEP-dev/SUEWS), [documentación recuperada](https://github.com/UMEP-dev/SUEWS/blob/master/README.md), [pyproject.toml](https://github.com/UMEP-dev/SUEWS/blob/master/pyproject.toml). Commit observado: `b63f8652ccf92413fda1326d9867821c26da0cc7`. Licencia en el inventario: `MPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-umep-dev--umep"></a>

#### 036. UMEP-dev/UMEP

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Herramientas climáticas integradas con QGIS.
- **Puerta de integración propuesta:** Plugin y algoritmos que exponga la versión instalada.
- **Construir nosotros, solo si falta:** Descubrimiento y operación de algoritmos seleccionados desde el conector QGIS.
- **Con qué y por qué:** reutilizar proveedor/plugin; no copiar sus modelos al nuevo producto. Plugin o componente en el runtime de la aplicación anfitriona y un puente tipado externo cuando se requiera MCP. Debe respetar el hilo de interfaz, documento y sesión de la aplicación.
- **No reconstruir / crítica:** No asumir que todos los módulos corren sin escritorio.
- **Prueba de admisión pendiente:** Ejecutar algoritmo con el mismo dataset desde QGIS y desde el puente.
- **Evidencia y alcance:** Archivo candidato recuperado: [SUEWSPrepare/tabs/main_tab.py](https://github.com/UMEP-dev/UMEP/blob/0a4b7f97391ac1b9188ee49aa76f078bb3d389de/SUEWSPrepare/tabs/main_tab.py); 42/42 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UMEP-dev/UMEP), [documentación recuperada](https://github.com/UMEP-dev/UMEP/blob/master/README.md). Commit observado: `0a4b7f97391ac1b9188ee49aa76f078bb3d389de`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-umep-dev--umep-processing"></a>

#### 037. UMEP-dev/UMEP-processing

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Algoritmos UMEP publicados mediante Processing.
- **Puerta de integración propuesta:** Registro de algoritmos QGIS Processing.
- **Construir nosotros, solo si falta:** Parámetros tipados, preflight y archivos de resultados por corrida.
- **Con qué y por qué:** usar qgis_process/PyQGIS con proveedor instalado. Plugin o componente en el runtime de la aplicación anfitriona y un puente tipado externo cuando se requiera MCP. Debe respetar el hilo de interfaz, documento y sesión de la aplicación.
- **No reconstruir / crítica:** No construir un MCP climático paralelo si el conector QGIS ya sirve el algoritmo.
- **Prueba de admisión pendiente:** Mismo ID de algoritmo y parámetros producen mismo resultado.
- **Evidencia y alcance:** Archivo candidato recuperado: [processing_umep.py](https://github.com/UMEP-dev/UMEP-processing/blob/a7798db1698c29fa5ba667e082e7ad564c20e8e8/processing_umep.py); 60/60 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UMEP-dev/UMEP-processing), [documentación recuperada](https://github.com/UMEP-dev/UMEP-processing/blob/main/README.md). Commit observado: `a7798db1698c29fa5ba667e082e7ad564c20e8e8`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-usepa--cmaq"></a>

#### 038. USEPA/CMAQ

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelado de química y calidad del aire.
- **Puerta de integración propuesta:** Compilación, casos y forzamientos del sistema.
- **Construir nosotros, solo si falta:** Envío de trabajos y consulta de salidas en infraestructura experta.
- **Con qué y por qué:** conservar Fortran, MPI y preprocesadores originales. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No simular calidad de aire sin inventarios de emisiones y meteorología compatibles.
- **Prueba de admisión pendiente:** Benchmark oficial y diagnóstico de emisiones/meteorología faltantes.
- **Evidencia y alcance:** Archivo candidato recuperado: [CCTM/src/PARIO/alloc_data_mod.f](https://github.com/USEPA/CMAQ/blob/13c473c8e834ca6ee5fcff468e16b015362e83be/CCTM/src/PARIO/alloc_data_mod.f); 38/38 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/USEPA/CMAQ), [documentación recuperada](https://github.com/USEPA/CMAQ/blob/main/README.md). Commit observado: `13c473c8e834ca6ee5fcff468e16b015362e83be`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-wrf-model--wrf"></a>

#### 039. wrf-model/WRF

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelo meteorológico y sus configuraciones.
- **Puerta de integración propuesta:** Ejecutables WRF y cadena de preprocesamiento correspondiente.
- **Construir nosotros, solo si falta:** Expediente de corrida, recursos y consulta de variables/resultados.
- **Con qué y por qué:** el adaptador controla el trabajo; no incorpora el solver al servidor MCP. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No prometer predicción urbana lista sin condiciones iniciales y configuración física.
- **Prueba de admisión pendiente:** Caso oficial con dominios y forzamientos fijados.
- **Evidencia y alcance:** Archivo candidato recuperado: [main/convert_em.F](https://github.com/wrf-model/WRF/blob/06d4240ae989cc3e50af412bb472df3d9048783c/main/convert_em.F); 167/167 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/wrf-model/WRF), [documentación recuperada](https://github.com/wrf-model/WRF/blob/master/README.md), [CMakeLists.txt](https://github.com/wrf-model/WRF/blob/master/CMakeLists.txt). Commit observado: `06d4240ae989cc3e50af412bb472df3d9048783c`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.


### Familia: Contexto urbano IoT e interoperabilidad

<a id="tool-eclipse-ditto--ditto"></a>

#### 040. eclipse-ditto/ditto

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Gestión de digital twins, conectividad y autorización.
- **Puerta de integración propuesta:** API HTTP/WebSocket de una instancia Ditto.
- **Construir nosotros, solo si falta:** Mapear IDs y capacidades de objetos seleccionados al contexto urbano.
- **Con qué y por qué:** cliente del servicio existente, sin reescribir el backend Java. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No sustituir su política ni confundir twin IoT con modelo urbano geográfico.
- **Prueba de admisión pendiente:** Lectura/actualización autorizada de un twin y rechazo de acceso cruzado.
- **Evidencia y alcance:** Archivo candidato recuperado: [documentation/src/main/resources/_plugins/llms_markdown_generator.rb](https://github.com/eclipse-ditto/ditto/blob/e6ef869b8093a13f05157e132d4afa2b30bc5cd1/documentation/src/main/resources/_plugins/llms_markdown_generator.rb); 311/311 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/eclipse-ditto/ditto), [documentación recuperada](https://github.com/eclipse-ditto/ditto/blob/master/README.md), [dockerfile-release](https://github.com/eclipse-ditto/ditto/blob/master/dockerfile-release). Commit observado: `e6ef869b8093a13f05157e132d4afa2b30bc5cd1`. Licencia en el inventario: `EPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-fiware--context.orion-ld"></a>

#### 041. FIWARE/context.Orion-LD

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Context broker NGSI-LD y sus operaciones.
- **Puerta de integración propuesta:** API NGSI-LD de una instancia.
- **Construir nosotros, solo si falta:** Consultas urbanas tipadas y mapeos explícitos de entidades/contextos.
- **Con qué y por qué:** cliente del broker; mantener JSON-LD y semántica originales. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No inventar un broker ni convertir automáticamente modelos incompatibles.
- **Prueba de admisión pendiente:** Entidad con contexto, relaciones y suscripción verificadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/lib/apiTypesV2/Attribute.cpp](https://github.com/FIWARE/context.Orion-LD/blob/4a2083e73072fa2e93b582b454cac26daa135187/src/lib/apiTypesV2/Attribute.cpp); 149/149 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/FIWARE/context.Orion-LD), [documentación recuperada](https://github.com/FIWARE/context.Orion-LD/blob/develop/README.md), [CMakeLists.txt](https://github.com/FIWARE/context.Orion-LD/blob/develop/CMakeLists.txt). Commit observado: `4a2083e73072fa2e93b582b454cac26daa135187`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-fiware--tutorials.step-by-step"></a>

#### 042. FIWARE/tutorials.Step-by-Step

- **Dictamen:** Referencia, especificación o fixture; no integración ejecutable autónoma.
- **Traer del original:** Ejemplos de configuración e integración FIWARE.
- **Puerta de integración propuesta:** Documentos, ejemplos y recetas.
- **Construir nosotros, solo si falta:** Seleccionar ejemplos aplicables y convertirlos en recetas mantenidas nuestras.
- **Con qué y por qué:** documentación de apoyo, no un motor instalable adicional. Solo incorporación documental o fixture a la investigación/pruebas. No instalar ni publicar un servidor MCP para este repositorio.
- **No reconstruir / crítica:** No contar cada tutorial como producto integrado ni copiar secretos de ejemplo.
- **Prueba de admisión pendiente:** Reproducir el tutorial elegido en entorno desechable.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/FIWARE/tutorials.Step-by-Step), [documentación recuperada](https://github.com/FIWARE/tutorials.Step-by-Step/blob/master/README.md). Commit observado: `af03ef0d8ce804c63e5d9719b06735aded2f086a`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-fraunhoferiosb--frost-server"></a>

#### 043. FraunhoferIOSB/FROST-Server

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Servicio OGC SensorThings para observaciones.
- **Puerta de integración propuesta:** API SensorThings de la instancia.
- **Construir nosotros, solo si falta:** Consulta espacial/temporal, paginación y resultados con unidad y calidad.
- **Con qué y por qué:** aprovechar protocolo existente; conector desacoplado de Java. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No duplicar almacenamiento ni perder relaciones Sensor/Datastream/Observation.
- **Prueba de admisión pendiente:** Observaciones paginadas con tiempos y unidades conservados.
- **Evidencia y alcance:** Archivo candidato recuperado: [FROST-Server.HTTP/src/main/java/de/fraunhofer/iosb/ilt/frostserver/ContextListener.java](https://github.com/FraunhoferIOSB/FROST-Server/blob/6343da7ac76557999190bd4af7be1d3b61c854e4/FROST-Server.HTTP/src/main/java/de/fraunhofer/iosb/ilt/frostserver/ContextListener.java); 38/38 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/FraunhoferIOSB/FROST-Server), [documentación recuperada](https://github.com/FraunhoferIOSB/FROST-Server/blob/v2.x/README.md), [pom.xml](https://github.com/FraunhoferIOSB/FROST-Server/blob/v2.x/pom.xml). Commit observado: `6343da7ac76557999190bd4af7be1d3b61c854e4`. Licencia en el inventario: `LGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-scorpiobroker--scorpiobroker"></a>

#### 044. ScorpioBroker/ScorpioBroker

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Implementación de broker NGSI-LD.
- **Puerta de integración propuesta:** API de la instancia Scorpio.
- **Construir nosotros, solo si falta:** Mismo contrato urbano de broker con perfil de compatibilidad Scorpio.
- **Con qué y por qué:** integrar API; no elegir stack por el lenguaje dominante de GitHub. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No instalarlo junto con Orion-LD por defecto; evaluar capacidades requeridas.
- **Prueba de admisión pendiente:** Consultas y temporalidad del caso frente a su versión concreta.
- **Evidencia y alcance:** Archivo candidato recuperado: [Commons/src/main/java/com/github/jsonldjava/core/Constants.java](https://github.com/ScorpioBroker/ScorpioBroker/blob/ca019cf5f13654aa5723462369b195bcc3ac30c2/Commons/src/main/java/com/github/jsonldjava/core/Constants.java); 182/182 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ScorpioBroker/ScorpioBroker), [documentación recuperada](https://github.com/ScorpioBroker/ScorpioBroker/blob/development-quarkus/README.md), [pom.xml](https://github.com/ScorpioBroker/ScorpioBroker/blob/development-quarkus/pom.xml). Commit observado: `ca019cf5f13654aa5723462369b195bcc3ac30c2`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-smart-data-models--data-models"></a>

#### 045. smart-data-models/data-models

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Modelos y definiciones de datos para dominios urbanos.
- **Puerta de integración propuesta:** Esquemas y contextos seleccionados.
- **Construir nosotros, solo si falta:** Mapeos explícitos desde cada fuente y validación de campos acordados.
- **Con qué y por qué:** conservar IDs/versiones de esquemas, como dependencia de conectores. Reutilizar esquemas, formatos y validadores concretos; fijar sus versiones. No hay un motor científico que desplegar por el mero hecho de existir una especificación.
- **No reconstruir / crítica:** No tratar nombres de entidades iguales como equivalencia semántica garantizada.
- **Prueba de admisión pendiente:** Dato válido, unidad incompatible y relación a entidad ausente.
- **Evidencia y alcance:** Archivo candidato recuperado: [pysmartdatamodels/__init__.py](https://github.com/smart-data-models/data-models/blob/325ea7069e4c3bd73d1000339ff0ecdf0310365b/pysmartdatamodels/__init__.py); 1/1 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/smart-data-models/data-models), [documentación recuperada](https://github.com/smart-data-models/data-models/blob/master/README.md), [package.json](https://github.com/smart-data-models/data-models/blob/master/package.json). Commit observado: `325ea7069e4c3bd73d1000339ff0ecdf0310365b`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-telefonicaid--fiware-orion"></a>

#### 046. telefonicaid/fiware-orion

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Context broker de la línea NGSIv2.
- **Puerta de integración propuesta:** API NGSIv2.
- **Construir nosotros, solo si falta:** Perfil de compatibilidad para instalaciones que ya usan esta versión.
- **Con qué y por qué:** conservar servicio y definir traducción solo donde sea demostrable. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No etiquetar NGSIv2 como NGSI-LD ni ocultar pérdida semántica.
- **Prueba de admisión pendiente:** Lectura/escritura de entidad y prueba de transformación limitada.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/lib/apiTypesV2/BatchQuery.cpp](https://github.com/telefonicaid/fiware-orion/blob/538766b5382c070517a6dcf17ed3d50e1d4a52ce/src/lib/apiTypesV2/BatchQuery.cpp); 64/64 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/telefonicaid/fiware-orion), [documentación recuperada](https://github.com/telefonicaid/fiware-orion/blob/master/README.md), [CMakeLists.txt](https://github.com/telefonicaid/fiware-orion/blob/master/CMakeLists.txt). Commit observado: `538766b5382c070517a6dcf17ed3d50e1d4a52ce`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-thingsboard--thingsboard"></a>

#### 047. thingsboard/thingsboard

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Plataforma IoT, dispositivos, telemetría y paneles.
- **Puerta de integración propuesta:** REST/telemetría de la instalación; revisar edición.
- **Construir nosotros, solo si falta:** Consultar activos y series autorizadas con su identidad y unidades.
- **Con qué y por qué:** usar APIs existentes; no copiar paneles ni reglas del backend. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No mezclar funciones de ediciones distintas ni eludir permisos de dispositivo.
- **Prueba de admisión pendiente:** Serie de prueba y separación entre activos/proyectos.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [application/src/main/java/org/thingsboard/server/controller/DeviceController.java](https://github.com/thingsboard/thingsboard/blob/cd259892925ff3cc6709dae021c0d619cfdfbaea/application/src/main/java/org/thingsboard/server/controller/DeviceController.java); lectura parcial de 600/763 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/thingsboard/thingsboard), [documentación recuperada](https://github.com/thingsboard/thingsboard/blob/master/README.md), [pom.xml](https://github.com/thingsboard/thingsboard/blob/master/pom.xml). Commit observado: `cd259892925ff3cc6709dae021c0d619cfdfbaea`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Desarrollo urbano y uso del suelo

<a id="tool-hpscil--open-space-cellular_automata"></a>

#### 048. HPSCIL/Open-Space-Cellular_Automata

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Material de autómatas celulares sobre espacio abierto.
- **Puerta de integración propuesta:** Código/datos reales pendientes de identificar.
- **Construir nosotros, solo si falta:** Ningún adaptador hasta localizar ejecutor, entradas y licencia utilizables.
- **Con qué y por qué:** la referencia no basta para escoger runtime o framework. No fijar lenguaje, framework ni receta ejecutable todavía. Falta acreditar una implementación/interfaz utilizable; crear código ahora asumiría una arquitectura sin evidencia.
- **No reconstruir / crítica:** No vender una referencia académica como motor mantenible.
- **Prueba de admisión pendiente:** Reproducir un ejemplo publicado con código disponible.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/HPSCIL/Open-Space-Cellular_Automata), [documentación recuperada](https://github.com/HPSCIL/Open-Space-Cellular_Automata/blob/master/README.md). Commit observado: `fe3876b575e96aaed5f9a0c6bd8876796f5e6b94`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-johanlahti--urban-lu-model"></a>

#### 049. johanlahti/urban-lu-model

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Modelo de cambio de uso de suelo del repositorio.
- **Puerta de integración propuesta:** Scripts, configuración y datos del proyecto.
- **Construir nosotros, solo si falta:** Escenario versionado y lectura de cambios solo después de reproducibilidad básica.
- **Con qué y por qué:** conservar implementación y sus dependencias históricas. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No inferir aptitud actual ni extrapolar parámetros de otra ciudad.
- **Prueba de admisión pendiente:** Reproducción de ejemplo y evaluación de dependencias obsoletas.
- **Evidencia y alcance:** Archivo candidato recuperado: [script/Main.py](https://github.com/johanlahti/urban-lu-model/blob/a8f7419b6f13bc4c273f1c0c6262a5daf4f87deb/script/Main.py); 39/39 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/johanlahti/urban-lu-model), [documentación recuperada](https://github.com/johanlahti/urban-lu-model/blob/master/README.md). Commit observado: `a8f7419b6f13bc4c273f1c0c6262a5daf4f87deb`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-landinsightlab--muse"></a>

#### 050. LandInsightLab/MUSE

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Modelo de simulación de evolución urbana del proyecto.
- **Puerta de integración propuesta:** Interfaz y configuraciones Python por revisar.
- **Construir nosotros, solo si falta:** Empaquetar un escenario reproducible y resultados de uso del suelo.
- **Con qué y por qué:** mantener modelo; fijar datos y parámetros antes de definir herramientas MCP. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No confundir simulación de uso del suelo con resultado normativo o causal.
- **Prueba de admisión pendiente:** Caso conocido y comparación con escenario base.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/mainwindow.py](https://github.com/LandInsightLab/MUSE/blob/09cfb9004d9cbdc5dd60dd08f90395cbbc074957/src/mainwindow.py); 420/1022 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/LandInsightLab/MUSE), [documentación recuperada](https://github.com/LandInsightLab/MUSE/blob/master/README.md), [requirements.txt](https://github.com/LandInsightLab/MUSE/blob/master/requirements.txt). Commit observado: `09cfb9004d9cbdc5dd60dd08f90395cbbc074957`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-udst--choicemodels"></a>

#### 051. UDST/choicemodels

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Estimación y aplicación de modelos de elección.
- **Puerta de integración propuesta:** API Python.
- **Construir nosotros, solo si falta:** Expediente de variables, muestra y modelo dentro del flujo UrbanSim.
- **Con qué y por qué:** biblioteca de estimación, no MCP independiente. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No atribuir causalidad ni validez local por ajustar un modelo.
- **Prueba de admisión pendiente:** Datos sintéticos con elección y parámetros verificables.
- **Evidencia y alcance:** Archivo candidato recuperado: [choicemodels/__init__.py](https://github.com/UDST/choicemodels/blob/80b1bac2757ccda4164b5bbeb73a014c1294996d/choicemodels/__init__.py); 6/6 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UDST/choicemodels), [documentación recuperada](https://github.com/UDST/choicemodels/blob/main/README.md), [pyproject.toml](https://github.com/UDST/choicemodels/blob/main/pyproject.toml). Commit observado: `80b1bac2757ccda4164b5bbeb73a014c1294996d`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-udst--developer"></a>

#### 052. UDST/developer

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Componentes de modelado de desarrollo inmobiliario.
- **Puerta de integración propuesta:** API Python y tablas del modelo.
- **Construir nosotros, solo si falta:** Configuración explícita de factibilidad dentro de un escenario urbano.
- **Con qué y por qué:** conservar componente bajo el adaptador del modelo padre. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No presentar supuestos de factibilidad como valuación o permisos aprobados.
- **Prueba de admisión pendiente:** Caso pequeño con restricciones y unidades comprobadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [developer/__init__.py](https://github.com/UDST/developer/blob/749acb15442b2387dea2e0539c9ef9186f6a83c1/developer/__init__.py); 1/1 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UDST/developer), [documentación recuperada](https://github.com/UDST/developer/blob/master/README.md), [setup.py](https://github.com/UDST/developer/blob/master/setup.py). Commit observado: `749acb15442b2387dea2e0539c9ef9186f6a83c1`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-udst--orca"></a>

#### 053. UDST/orca

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Orquestación de tablas, inyecciones y pasos de modelos.
- **Puerta de integración propuesta:** API y registro de pasos Orca.
- **Construir nosotros, solo si falta:** Seleccionar pasos admitidos y registrar entradas/salidas del escenario.
- **Con qué y por qué:** reutilizar orquestación nativa del modelo UrbanSim. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No desarrollar otro scheduler que replique los pasos internos.
- **Prueba de admisión pendiente:** Pipeline mínimo con dependencias resueltas y resultados iguales.
- **Evidencia y alcance:** Archivo candidato recuperado: [orca/__init__.py](https://github.com/UDST/orca/blob/880d1dd9ba71b28bac43a1533792b695613baa64/orca/__init__.py); 5/5 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UDST/orca), [documentación recuperada](https://github.com/UDST/orca/blob/main/README.rst), [pyproject.toml](https://github.com/UDST/orca/blob/main/pyproject.toml). Commit observado: `880d1dd9ba71b28bac43a1533792b695613baa64`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-udst--urbansim"></a>

#### 054. UDST/urbansim

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelado de desarrollo y uso del suelo.
- **Puerta de integración propuesta:** API Python y configuración de modelos.
- **Construir nosotros, solo si falta:** Fachada de escenarios, datasets, corrida y comparación de indicadores.
- **Con qué y por qué:** conservar tablas y componentes del ecosistema UDST. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No crear un modelo de ciudad sin población, parcelas, estimación y calibración.
- **Prueba de admisión pendiente:** Modelo de ejemplo reproducido y sensibilidad de supuestos documentada.
- **Evidencia y alcance:** Archivo candidato recuperado: [urbansim/models/__init__.py](https://github.com/UDST/urbansim/blob/1a9a68e9bfe34dd31c68bf9480c4fc65334663e0/urbansim/models/__init__.py); 8/8 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UDST/urbansim), [documentación recuperada](https://github.com/UDST/urbansim/blob/main/README.rst), [pyproject.toml](https://github.com/UDST/urbansim/blob/main/pyproject.toml). Commit observado: `1a9a68e9bfe34dd31c68bf9480c4fc65334663e0`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-udst--urbansim_defaults"></a>

#### 055. UDST/urbansim_defaults

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Configuraciones y componentes de referencia UrbanSim.
- **Puerta de integración propuesta:** Paquetes/tablas del proyecto.
- **Construir nosotros, solo si falta:** Elegir componentes compatibles y registrar su procedencia en el escenario.
- **Con qué y por qué:** dependencia opcional de una versión concreta de UrbanSim. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No instalar defaults como modelo válido de cualquier municipio.
- **Prueba de admisión pendiente:** Ejemplo con versiones compatibles y campos requeridos presentes.
- **Evidencia y alcance:** Archivo candidato recuperado: [urbansim_defaults/models.py](https://github.com/UDST/urbansim_defaults/blob/466c8b4ddd4d2cbfa81c5e6b6fe0b8825c8cb323/urbansim_defaults/models.py); 258/258 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UDST/urbansim_defaults), [documentación recuperada](https://github.com/UDST/urbansim_defaults/blob/master/README.md), [setup.py](https://github.com/UDST/urbansim_defaults/blob/master/setup.py). Commit observado: `466c8b4ddd4d2cbfa81c5e6b6fe0b8825c8cb323`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-udst--urbansim_templates"></a>

#### 056. UDST/urbansim_templates

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Plantillas de modelado para el ecosistema UrbanSim.
- **Puerta de integración propuesta:** API/configuraciones de plantillas.
- **Construir nosotros, solo si falta:** Parametrizar una plantilla concreta con validación de variables.
- **Con qué y por qué:** usar en el paquete UrbanSim que lo requiera. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No crear otra herramienta por cada plantilla ni prometer interoperabilidad entre versiones.
- **Prueba de admisión pendiente:** Plantilla mínima con entrenamiento/aplicación reproducibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [urbansim_templates/models/__init__.py](https://github.com/UDST/urbansim_templates/blob/35cf5df511eff1db586add32fa6a92602546c70e/urbansim_templates/models/__init__.py); 6/6 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UDST/urbansim_templates), [documentación recuperada](https://github.com/UDST/urbansim_templates/blob/main/README.md), [pyproject.toml](https://github.com/UDST/urbansim_templates/blob/main/pyproject.toml). Commit observado: `35cf5df511eff1db586add32fa6a92602546c70e`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Diseño urbano participativo

<a id="tool-cityscope--cs_cityio"></a>

#### 057. CityScope/CS_CityIO

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Servicio de intercambio de estado de mesas/escenarios CityScope.
- **Puerta de integración propuesta:** API del servidor CityIO.
- **Construir nosotros, solo si falta:** Mapear tablas y revisiones a escenarios, conservando identidades y autoría.
- **Con qué y por qué:** integrar servicio Rust por API; no reescribirlo. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No asumir que todas las tablas comparten esquema o que una propuesta es dato observado.
- **Prueba de admisión pendiente:** Leer/modificar mesa de prueba y comprobar revisión y estado previo.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/main.rs](https://github.com/CityScope/CS_CityIO/blob/0cacb158240385fbfede5fedee6edf236b45db81/src/main.rs); 66/66 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CityScope/CS_CityIO), [Cargo.toml](https://github.com/CityScope/CS_CityIO/blob/main/Cargo.toml). Commit observado: `0cacb158240385fbfede5fedee6edf236b45db81`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-cityscope--cs_cityscopejs"></a>

#### 058. CityScope/CS_cityscopeJS

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Cliente y visualización JavaScript de CityScope.
- **Puerta de integración propuesta:** Componentes y API del cliente.
- **Construir nosotros, solo si falta:** Integración visual de escenario y eventos solo en un cliente elegido.
- **Con qué y por qué:** JavaScript en navegador; puente de comandos tipados si hace falta. JavaScript/TypeScript en el host del visor y un contrato de comandos/eventos de navegador. Un servidor MCP, si falta, usaría el SDK TypeScript y un puente explícito con esa sesión.
- **No reconstruir / crítica:** No duplicar CityIO ni añadir un visor obligatorio al producto MCP.
- **Prueba de admisión pendiente:** Evento de edición produce cambio de estado correcto y recuperable.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/App.js](https://github.com/CityScope/CS_cityscopeJS/blob/1cb2e63cbcdc794a6fb5da9fbc60537289e319a1/src/App.js); 69/69 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CityScope/CS_cityscopeJS), [documentación recuperada](https://github.com/CityScope/CS_cityscopeJS/blob/master/README.md), [package.json](https://github.com/CityScope/CS_cityscopeJS/blob/master/package.json). Commit observado: `1cb2e63cbcdc794a6fb5da9fbc60537289e319a1`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-cityscope--cs_cityscopy"></a>

#### 059. CityScope/CS_CityScoPy

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Cliente Python de CityScope.
- **Puerta de integración propuesta:** SDK/API Python.
- **Construir nosotros, solo si falta:** Lectura y envío de datos como parte del conector CityIO.
- **Con qué y por qué:** reutilizar SDK si es compatible con la instancia. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No desplegar otro servidor solo por existir un cliente Python.
- **Prueba de admisión pendiente:** Ida y vuelta de mesa con esquema e IDs preservados.
- **Evidencia y alcance:** Archivo candidato recuperado: [cityscopy/__init__.py](https://github.com/CityScope/CS_CityScoPy/blob/12defc13eea0b3de7a91dc11a1ca08f96250b567/cityscopy/__init__.py); 0/0 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CityScope/CS_CityScoPy), [documentación recuperada](https://github.com/CityScope/CS_CityScoPy/blob/master/README.md). Commit observado: `12defc13eea0b3de7a91dc11a1ca08f96250b567`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-cityscope--cs_mobility_service"></a>

#### 060. CityScope/CS_Mobility_Service

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Servicio/experimentos de movilidad para CityScope.
- **Puerta de integración propuesta:** Código y contratos de la versión elegida.
- **Construir nosotros, solo si falta:** Adaptar únicamente indicadores y escenario que logren reproducirse.
- **Con qué y por qué:** conservar implementación; revisar notebooks frente a servicio ejecutable. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No llamar servicio productivo a un notebook ni inventar demanda.
- **Prueba de admisión pendiente:** Ejemplo CityScope reproducido con entrada y métrica conocidas.
- **Evidencia y alcance:** Archivo candidato recuperado: [scripts/activity_scheduler.py](https://github.com/CityScope/CS_Mobility_Service/blob/1e273ed56470f7223887f4d8ae7b93288e2b1477/scripts/activity_scheduler.py); 236/236 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CityScope/CS_Mobility_Service), [documentación recuperada](https://github.com/CityScope/CS_Mobility_Service/blob/master/README.md), [requirements.txt](https://github.com/CityScope/CS_Mobility_Service/blob/master/requirements.txt). Commit observado: `1e273ed56470f7223887f4d8ae7b93288e2b1477`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-cityscope--cs_simulation_gama"></a>

#### 061. CityScope/CS_Simulation_GAMA

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Modelo/conexión CityScope con GAMA.
- **Puerta de integración propuesta:** Modelos GAML y ruta de intercambio CityScope.
- **Construir nosotros, solo si falta:** Receta conjunta y correspondencia entre objetos de mesa y agentes.
- **Con qué y por qué:** usar ejecutor GAMA existente; no traducir GAML. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No atribuir resultados de ese modelo a toda ciudad o a cualquier versión GAMA.
- **Prueba de admisión pendiente:** Escenario de ejemplo con ida y vuelta de indicadores.
- **Evidencia y alcance:** Archivo candidato recuperado: [CS_CityScope_GAMA/models/CityScope/CityScope_Custom_Template.gaml](https://github.com/CityScope/CS_Simulation_GAMA/blob/f64b17f0be21feffdc196a07aab7c3067df96ba6/CS_CityScope_GAMA/models/CityScope/CityScope_Custom_Template.gaml); 44/44 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CityScope/CS_Simulation_GAMA), [documentación recuperada](https://github.com/CityScope/CS_Simulation_GAMA/blob/master/README.md). Commit observado: `f64b17f0be21feffdc196a07aab7c3067df96ba6`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-consuldemocracy--consuldemocracy"></a>

#### 062. consuldemocracy/consuldemocracy

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Plataforma de participación y sus procesos.
- **Puerta de integración propuesta:** APIs y extensiones admitidas por la instalación.
- **Construir nosotros, solo si falta:** Consulta de procesos y envío autorizado a una instancia de prueba.
- **Con qué y por qué:** integrar API; plugin Ruby solo si falta una operación verificable. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No automatizar identidad, voto o decisiones ciudadanas ni reemplazar el proceso.
- **Prueba de admisión pendiente:** Publicación de contribución de prueba con recibo y permisos verificados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [config/routes.rb](https://github.com/consuldemocracy/consuldemocracy/blob/3bbddbc3828fb0637242178817684e7698fb1135/config/routes.rb); lectura parcial de 92/92 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/consuldemocracy/consuldemocracy), [documentación recuperada](https://github.com/consuldemocracy/consuldemocracy/blob/master/README.md), [Dockerfile](https://github.com/consuldemocracy/consuldemocracy/blob/master/Dockerfile). Commit observado: `3bbddbc3828fb0637242178817684e7698fb1135`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-decidim--decidim"></a>

#### 063. decidim/decidim

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Procesos participativos, propuestas y reglas de la instancia.
- **Puerta de integración propuesta:** API disponible y extensiones Rails específicas.
- **Construir nosotros, solo si falta:** Conector de lectura y contribuciones explícitas vinculadas a escenarios.
- **Con qué y por qué:** conservar Decidim; extensión Ruby solo para una brecha identificada. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No inventar receptor ni pasar propuestas del agente por opiniones ciudadanas.
- **Prueba de admisión pendiente:** Contribución en proceso de prueba y lectura posterior del recibo.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [decidim-api/lib/decidim/api/query_type.rb](https://github.com/decidim/decidim/blob/9fd2a688cc3d357a5a9db710aafc86d3860cdaae/decidim-api/lib/decidim/api/query_type.rb); lectura parcial de 103/103 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/decidim/decidim), [documentación recuperada](https://github.com/decidim/decidim/blob/develop/README.adoc), [decidim.gemspec](https://github.com/decidim/decidim/blob/develop/decidim.gemspec). Commit observado: `9fd2a688cc3d357a5a9db710aafc86d3860cdaae`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-umap-project--umap"></a>

#### 064. umap-project/umap

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Edición y publicación colaborativa de mapas.
- **Puerta de integración propuesta:** API/exportaciones de la instancia y GeoJSON.
- **Construir nosotros, solo si falta:** Intercambio de capas y vínculo con mapas/proyectos autorizados.
- **Con qué y por qué:** reutilizar servicio; validar qué escrituras admite la versión. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No duplicar editor ni asumir API de edición pública por tener exportación.
- **Prueba de admisión pendiente:** Exportar/reimportar capa con estilos y propiedades acordados.
- **Evidencia y alcance:** Archivo candidato recuperado: [umap/models.py](https://github.com/umap-project/umap/blob/8c20f55ba00e0d63bd46a013e46e7f812a44e9ca/umap/models.py); 420/675 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/umap-project/umap), [documentación recuperada](https://github.com/umap-project/umap/blob/master/README.md), [Dockerfile](https://github.com/umap-project/umap/blob/master/Dockerfile). Commit observado: `8c20f55ba00e0d63bd46a013e46e7f812a44e9ca`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Ecología paisaje y naturaleza urbana

<a id="tool-martibosch--pylandstats"></a>

#### 065. martibosch/pylandstats

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Métricas de paisaje sobre rasters categóricos.
- **Puerta de integración propuesta:** API Python.
- **Construir nosotros, solo si falta:** Análisis reproducible con clases, resolución y área de estudio explícitas.
- **Con qué y por qué:** usar métricas nativas y conservar definición de clases. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No convertir métricas de patrón espacial en biodiversidad observada.
- **Prueba de admisión pendiente:** Raster sintético con composición y conectividad calculables.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/pylandstats/landscape.py](https://github.com/martibosch/pylandstats/blob/a7c3840086e2dd19b75f357c6e4e0ff0a4264d6f/src/pylandstats/landscape.py); lectura parcial de 600/4037 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/martibosch/pylandstats), [documentación recuperada](https://github.com/martibosch/pylandstats/blob/main/README.md), [pyproject.toml](https://github.com/martibosch/pylandstats/blob/main/pyproject.toml). Commit observado: `a7c3840086e2dd19b75f357c6e4e0ff0a4264d6f`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-natcap--invest"></a>

#### 066. natcap/invest

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelos de servicios ecosistémicos de InVEST.
- **Puerta de integración propuesta:** API/modelos y paquetes de datos específicos.
- **Construir nosotros, solo si falta:** Seleccionar modelo, validar parámetros e insumos y conservar escenarios.
- **Con qué y por qué:** un adaptador por familia de modelos, usando ejecución upstream. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No generar servicios ecosistémicos sin coeficientes/datos locales ni duplicar modelos.
- **Prueba de admisión pendiente:** Ejemplo oficial por modelo con resultados contrastados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/natcap/invest/cli.py](https://github.com/natcap/invest/blob/f02f5e20d2d3f46f69f4a6785d032659e2cf318d/src/natcap/invest/cli.py); lectura parcial de 501/501 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/natcap/invest), [documentación recuperada](https://github.com/natcap/invest/blob/main/README.md), [.readthedocs_environment.yml](https://github.com/natcap/invest/blob/main/.readthedocs_environment.yml). Commit observado: `f02f5e20d2d3f46f69f4a6785d032659e2cf318d`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-natcap--pygeoprocessing"></a>

#### 067. natcap/pygeoprocessing

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Operaciones ráster de soporte a modelos.
- **Puerta de integración propuesta:** API Python y dependencias GDAL.
- **Construir nosotros, solo si falta:** Utilizar operaciones como dependencia de InVEST u otro paquete definido.
- **Con qué y por qué:** evitar otro catálogo de geoprocesamiento superpuesto a GDAL. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No crear un MCP separado por una biblioteca auxiliar.
- **Prueba de admisión pendiente:** Operación ráster mínima con nodata, resolución y CRS comprobados.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/pygeoprocessing/__init__.py](https://github.com/natcap/pygeoprocessing/blob/17fde868d10d4eef45c3d023ea25a0ef0673f8bb/src/pygeoprocessing/__init__.py); 91/91 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/natcap/pygeoprocessing), [documentación recuperada](https://github.com/natcap/pygeoprocessing/blob/main/README.rst), [pyproject.toml](https://github.com/natcap/pygeoprocessing/blob/main/pyproject.toml). Commit observado: `17fde868d10d4eef45c3d023ea25a0ef0673f8bb`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-r-spatialecology--landscapemetrics"></a>

#### 068. r-spatialecology/landscapemetrics

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Métricas de paisaje en R.
- **Puerta de integración propuesta:** API R.
- **Construir nosotros, solo si falta:** Operaciones seleccionadas cuando el flujo de trabajo del usuario sea R.
- **Con qué y por qué:** Rscript con intercambio estructurado; conservar implementación estadística. Rscript y paquetes R originales, con intercambio por JSON/tablas/archivos. Si hace falta un servidor MCP externo, una fachada Go puede administrar el proceso sin traducir el cálculo estadístico.
- **No reconstruir / crítica:** No exponer simultáneamente métricas homónimas de otra biblioteca como equivalentes.
- **Prueba de admisión pendiente:** Raster de clases con resultados y vecindad declarados.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/RcppExports.cpp](https://github.com/r-spatialecology/landscapemetrics/blob/0f8c05188a3ca49b1d3bac948fb243d21052db71/src/RcppExports.cpp); 229/229 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/r-spatialecology/landscapemetrics), [documentación recuperada](https://github.com/r-spatialecology/landscapemetrics/blob/main/README.md). Commit observado: `0f8c05188a3ca49b1d3bac948fb243d21052db71`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Energía urbana y edificios

<a id="tool-architecture-building-systems--cityenergyanalyst"></a>

#### 069. architecture-building-systems/CityEnergyAnalyst

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Simulación y análisis energético urbano por escenarios.
- **Puerta de integración propuesta:** Scripts/API CEA y estructura de escenario.
- **Construir nosotros, solo si falta:** Selección de escenarios, validación de insumos y publicación trazable de indicadores.
- **Con qué y por qué:** respetar entorno científico y ejecutores de CEA. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No crear otro UBEM ni asumir edificios y usos completos en cualquier ciudad.
- **Prueba de admisión pendiente:** Escenario de referencia con mismos indicadores por ejecución directa.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [cea/api.py](https://github.com/architecture-building-systems/CityEnergyAnalyst/blob/05210726cff4de7f217a7a695be06d7dc5b5aa59/cea/api.py); lectura parcial de 104/104 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/architecture-building-systems/CityEnergyAnalyst), [documentación recuperada](https://github.com/architecture-building-systems/CityEnergyAnalyst/blob/master/README.rst), [Dockerfile](https://github.com/architecture-building-systems/CityEnergyAnalyst/blob/master/Dockerfile). Commit observado: `05210726cff4de7f217a7a695be06d7dc5b5aa59`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-betalab-team--eureca"></a>

#### 070. BETALAB-team/EUReCA

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Modelado energético de edificios y distritos.
- **Puerta de integración propuesta:** API/ejecutor Python EUReCA.
- **Construir nosotros, solo si falta:** Preparación de entradas e intercambio de resultados para un escenario validado.
- **Con qué y por qué:** mantener modelo y dependencias nativas del proyecto. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No tratar aproximaciones de arquetipos como datos observados ni duplicar CEA sin caso.
- **Prueba de admisión pendiente:** Edificio pequeño con meteorología y demanda contrastadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [eureca_ubem/Input/Main.py](https://github.com/BETALAB-team/EUReCA/blob/aa46bb3711366c0bbc6069af899aa138e6af62b3/eureca_ubem/Input/Main.py); 59/59 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/BETALAB-team/EUReCA), [documentación recuperada](https://github.com/BETALAB-team/EUReCA/blob/main/README.md), [pyproject.toml](https://github.com/BETALAB-team/EUReCA/blob/main/pyproject.toml). Commit observado: `aa46bb3711366c0bbc6069af899aa138e6af62b3`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-kth-urbant--mubes-ubem"></a>

#### 071. KTH-UrbanT/mubes-ubem

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Flujo de modelado energético urbano.
- **Puerta de integración propuesta:** Ejecutor Python y EnergyPlus de la versión elegida.
- **Construir nosotros, solo si falta:** Expediente de corrida y mapeo de edificios al flujo MUBES.
- **Con qué y por qué:** envolver su ejecutor; conservar generación de modelos upstream. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No sumar otro frontend energético antes de demostrar diferencia frente a CEA/URBANopt.
- **Prueba de admisión pendiente:** Ejemplo reproducido, versión EnergyPlus y consumo comparados.
- **Evidencia y alcance:** Archivo candidato recuperado: [bin/mubes_run.py](https://github.com/KTH-UrbanT/mubes-ubem/blob/faca419b67c93fcace84b915a9239a27c8407d3a/bin/mubes_run.py); 237/237 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/KTH-UrbanT/mubes-ubem), [documentación recuperada](https://github.com/KTH-UrbanT/mubes-ubem/blob/main/README.md), [requirements.txt](https://github.com/KTH-UrbanT/mubes-ubem/blob/main/requirements.txt). Commit observado: `faca419b67c93fcace84b915a9239a27c8407d3a`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ladybug-tools--dragonfly-core"></a>

#### 072. ladybug-tools/dragonfly-core

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Modelo de distrito/edificios y serialización Dragonfly.
- **Puerta de integración propuesta:** API Python y formatos nativos.
- **Construir nosotros, solo si falta:** Mapeo explícito de objetos urbanos a modelo Dragonfly.
- **Con qué y por qué:** componente geométrico del flujo energético elegido. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No vender conversión geométrica como simulación energética.
- **Prueba de admisión pendiente:** Distrito sintético con unidades, plantas e IDs preservados.
- **Evidencia y alcance:** Archivo candidato recuperado: [dragonfly/cli/__init__.py](https://github.com/ladybug-tools/dragonfly-core/blob/3f1dd0489d8ab5ac986170e912f1504cd7c10952/dragonfly/cli/__init__.py); 75/75 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ladybug-tools/dragonfly-core), [documentación recuperada](https://github.com/ladybug-tools/dragonfly-core/blob/master/README.md), [dev-requirements.txt](https://github.com/ladybug-tools/dragonfly-core/blob/master/dev-requirements.txt). Commit observado: `3f1dd0489d8ab5ac986170e912f1504cd7c10952`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ladybug-tools--dragonfly-energy"></a>

#### 073. ladybug-tools/dragonfly-energy

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Traducción y flujos energéticos para modelos Dragonfly.
- **Puerta de integración propuesta:** API y CLI de Dragonfly Energy.
- **Construir nosotros, solo si falta:** Operaciones de preparación/ejecución de un escenario energético de distrito.
- **Con qué y por qué:** conservar traductores y compatibilidad con Honeybee/OpenStudio. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No reconstruir traductor ni ocultar pérdida de detalle entre representaciones.
- **Prueba de admisión pendiente:** Modelo pequeño traducido y ejecutado con igual configuración.
- **Evidencia y alcance:** Archivo candidato recuperado: [dragonfly_energy/cli/__init__.py](https://github.com/ladybug-tools/dragonfly-energy/blob/9ac42871aa713374db84318dc20f6a3079959137/dragonfly_energy/cli/__init__.py); 22/22 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ladybug-tools/dragonfly-energy), [documentación recuperada](https://github.com/ladybug-tools/dragonfly-energy/blob/master/README.md), [Dockerfile](https://github.com/ladybug-tools/dragonfly-energy/blob/master/Dockerfile). Commit observado: `9ac42871aa713374db84318dc20f6a3079959137`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ladybug-tools--honeybee-core"></a>

#### 074. ladybug-tools/honeybee-core

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Modelo de edificios y geometría Honeybee.
- **Puerta de integración propuesta:** API Python y HBJSON.
- **Construir nosotros, solo si falta:** Conversión validada desde el modelo urbano/BIM del proyecto.
- **Con qué y por qué:** dependencia del paquete Honeybee correspondiente. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No duplicar esquema de edificios ni tratar toda geometría IFC como térmica.
- **Prueba de admisión pendiente:** Habitación cerrada, unidades y adyacencias verificadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [honeybee/cli/__init__.py](https://github.com/ladybug-tools/honeybee-core/blob/4c7d41dccfcc9c175d6860c5f4f4af414c2debb0/honeybee/cli/__init__.py); 118/118 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ladybug-tools/honeybee-core), [documentación recuperada](https://github.com/ladybug-tools/honeybee-core/blob/master/README.md), [dev-requirements.txt](https://github.com/ladybug-tools/honeybee-core/blob/master/dev-requirements.txt). Commit observado: `4c7d41dccfcc9c175d6860c5f4f4af414c2debb0`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ladybug-tools--honeybee-energy"></a>

#### 075. ladybug-tools/honeybee-energy

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Modelo y flujos de simulación energética Honeybee.
- **Puerta de integración propuesta:** API/CLI y herramientas energéticas admitidas.
- **Construir nosotros, solo si falta:** Preparación parametrizada de casos y resultados con procedencia.
- **Con qué y por qué:** mantener plantillas y traducción energética de Honeybee. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No atribuir certificación o calibración por lograr una corrida.
- **Prueba de admisión pendiente:** Modelo oficial con EPW y resultados contrastados.
- **Evidencia y alcance:** Archivo candidato recuperado: [honeybee_energy/cli/__init__.py](https://github.com/ladybug-tools/honeybee-energy/blob/49956e396900fd8641e4a7a7b386b902aa6ca585/honeybee_energy/cli/__init__.py); 68/68 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ladybug-tools/honeybee-energy), [documentación recuperada](https://github.com/ladybug-tools/honeybee-energy/blob/master/README.md), [Dockerfile](https://github.com/ladybug-tools/honeybee-energy/blob/master/Dockerfile). Commit observado: `49956e396900fd8641e4a7a7b386b902aa6ca585`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ladybug-tools--honeybee-radiance"></a>

#### 076. ladybug-tools/honeybee-radiance

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Flujos de iluminación y radiación con Radiance.
- **Puerta de integración propuesta:** API/CLI de recetas y motor Radiance externo.
- **Construir nosotros, solo si falta:** Lanzar receta admitida, validar materiales y devolver resultados identificables.
- **Con qué y por qué:** conservar recetas; aislar ejecutables y archivos Radiance. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No reimplementar trazado ni reutilizar parámetros entre estudios sin validación.
- **Prueba de admisión pendiente:** Escena mínima con sensores, unidades y referencia lumínica.
- **Evidencia y alcance:** Archivo candidato recuperado: [honeybee_radiance/cli/__init__.py](https://github.com/ladybug-tools/honeybee-radiance/blob/ade258f57dd10a00debbb85623ed496946cbec49/honeybee_radiance/cli/__init__.py); 88/88 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ladybug-tools/honeybee-radiance), [documentación recuperada](https://github.com/ladybug-tools/honeybee-radiance/blob/master/README.md), [Dockerfile](https://github.com/ladybug-tools/honeybee-radiance/blob/master/Dockerfile). Commit observado: `ade258f57dd10a00debbb85623ed496946cbec49`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ladybug-tools--ladybug"></a>

#### 077. ladybug-tools/ladybug

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Datos climáticos, sol y utilidades ambientales.
- **Puerta de integración propuesta:** API Python y estructuras meteorológicas.
- **Construir nosotros, solo si falta:** Lectura normalizada de EPW y cálculos auxiliares en paquetes climáticos.
- **Con qué y por qué:** dependencia de los adaptadores ambientales. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No crear otra API meteorológica superpuesta ni inferir confort completo con una métrica.
- **Prueba de admisión pendiente:** EPW con periodo, unidad y trayectoria solar conocidos.
- **Evidencia y alcance:** Archivo candidato recuperado: [ladybug/cli/__init__.py](https://github.com/ladybug-tools/ladybug/blob/b184357d4fca1fe46cbd180496af441e57f103e8/ladybug/cli/__init__.py); 103/103 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ladybug-tools/ladybug), [documentación recuperada](https://github.com/ladybug-tools/ladybug/blob/master/README.md), [Dockerfile](https://github.com/ladybug-tools/ladybug/blob/master/Dockerfile). Commit observado: `b184357d4fca1fe46cbd180496af441e57f103e8`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-natlabrockies--comstock"></a>

#### 078. NatLabRockies/ComStock

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelos y flujos de stock de edificios comerciales.
- **Puerta de integración propuesta:** Workflows, medidas y datos propios del proyecto.
- **Construir nosotros, solo si falta:** Seleccionar subconjuntos y ejecutar escenarios explícitamente compatibles.
- **Con qué y por qué:** mantener OpenStudio/Ruby y pipeline upstream. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No trasladar stock/arquetipos estadounidenses como representación de otra ciudad.
- **Prueba de admisión pendiente:** Muestra reproducible con ponderaciones y motor fijados.
- **Evidencia y alcance:** Archivo candidato recuperado: [postprocessing/comstockpostproc/__init__.py](https://github.com/NatLabRockies/ComStock/blob/45aadab506b3513bde9bbfb6d22d32eaea104df2/postprocessing/comstockpostproc/__init__.py); 35/35 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/NatLabRockies/ComStock), [documentación recuperada](https://github.com/NatLabRockies/ComStock/blob/main/README.md). Commit observado: `45aadab506b3513bde9bbfb6d22d32eaea104df2`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-natlabrockies--energyplus"></a>

#### 079. NatLabRockies/EnergyPlus

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Motor de simulación energética de edificios.
- **Puerta de integración propuesta:** Ejecutable y API oficial de EnergyPlus.
- **Construir nosotros, solo si falta:** Receta de motor y contrato de corrida; reutilizar MCP energético existente cuando cubra el caso.
- **Con qué y por qué:** la API Python/CLI evita reescribir el motor C++; evaluar MCP antes del puente. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No crear simulador propio ni usar un IDF incompatible con su versión.
- **Prueba de admisión pendiente:** Caso oficial con EPW y SQL/reportes idénticos.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/EnergyPlus/api/api.py](https://github.com/NatLabRockies/EnergyPlus/blob/613b9a754fa075716dbdd6358842e87f0d51064e/src/EnergyPlus/api/api.py); lectura parcial de 159/159 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/NatLabRockies/EnergyPlus), [documentación recuperada](https://github.com/NatLabRockies/EnergyPlus/blob/develop/README.md), [CMakeLists.txt](https://github.com/NatLabRockies/EnergyPlus/blob/develop/CMakeLists.txt). Commit observado: `613b9a754fa075716dbdd6358842e87f0d51064e`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-natlabrockies--openstudio"></a>

#### 080. NatLabRockies/OpenStudio

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** SDK y herramientas para modelos y workflows energéticos.
- **Puerta de integración propuesta:** CLI, bindings y medidas compatibles.
- **Construir nosotros, solo si falta:** Seleccionar workflow y exponer parámetros/resultados de forma trazable.
- **Con qué y por qué:** respetar CLI/bindings Ruby o Python de esa distribución. Aplicación/binario y bibliotecas de su distribución. Seleccionar CLI o binding solo después de probar qué operación funciona fuera del escritorio.
- **No reconstruir / crítica:** No reconstruir SDK ni asumir compatibilidad entre cualquier OpenStudio y EnergyPlus.
- **Prueba de admisión pendiente:** Workflow mínimo y versiones de ambos motores verificadas.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/cli/main.cpp](https://github.com/NatLabRockies/OpenStudio/blob/3f640c31ff0656718a22c53f2b12894518a1d491/src/cli/main.cpp); lectura parcial de 379/379 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/NatLabRockies/OpenStudio), [documentación recuperada](https://github.com/NatLabRockies/OpenStudio/blob/develop/README.md), [CMakeLists.txt](https://github.com/NatLabRockies/OpenStudio/blob/develop/CMakeLists.txt). Commit observado: `3f640c31ff0656718a22c53f2b12894518a1d491`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-natlabrockies--openstudio-hpxml"></a>

#### 081. NatLabRockies/OpenStudio-HPXML

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Conversión y simulación de modelos residenciales HPXML.
- **Puerta de integración propuesta:** Medidas Ruby y ejecutor OpenStudio.
- **Construir nosotros, solo si falta:** Validar HPXML y registrar supuestos del escenario residencial.
- **Con qué y por qué:** componente del paquete residencial, usando sus medidas originales. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No rehacer conversor ni confundir cumplimiento XML con validez del edificio.
- **Prueba de admisión pendiente:** HPXML de referencia con conversión y consumo contrastados.
- **Evidencia y alcance:** Archivo candidato recuperado: [HPXMLtoOpenStudio/resources/model.rb](https://github.com/NatLabRockies/OpenStudio-HPXML/blob/493de26db0f34aed16648c971679af9b3adbed37/HPXMLtoOpenStudio/resources/model.rb); 420/1471 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/NatLabRockies/OpenStudio-HPXML), [documentación recuperada](https://github.com/NatLabRockies/OpenStudio-HPXML/blob/master/README.md). Commit observado: `493de26db0f34aed16648c971679af9b3adbed37`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-natlabrockies--resstock"></a>

#### 082. NatLabRockies/resstock

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Flujos de simulación de stock residencial.
- **Puerta de integración propuesta:** Workflows y muestreo del proyecto.
- **Construir nosotros, solo si falta:** Corridas de subconjuntos y expediente de arquetipos/ponderaciones.
- **Con qué y por qué:** mantener pipeline residencial y medidas OpenStudio. Compilación y ejecutores originales en un trabajador separado; utilizar el planificador existente si lo hay. El adaptador entrega configuración, estado y artefactos, sin ejecutar el solver dentro de una petición MCP.
- **No reconstruir / crítica:** No extrapolar stock estadounidense a cualquier municipio sin adaptación científica.
- **Prueba de admisión pendiente:** Muestra pequeña con pesos y escenarios reproducibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [measures/ServerDirectoryCleanup/measure.rb](https://github.com/NatLabRockies/resstock/blob/33433157aa52d1a97f35b9640bdf7a2c46f5d908/measures/ServerDirectoryCleanup/measure.rb); 215/215 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/NatLabRockies/resstock), [documentación recuperada](https://github.com/NatLabRockies/resstock/blob/develop/README.md). Commit observado: `33433157aa52d1a97f35b9640bdf7a2c46f5d908`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-rwth-ebc--teaser"></a>

#### 083. RWTH-EBC/TEASER

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Generación de modelos energéticos simplificados de edificios.
- **Puerta de integración propuesta:** API Python y exportaciones Modelica.
- **Construir nosotros, solo si falta:** Configurar arquetipos y enlazar exportación con simulador admitido.
- **Con qué y por qué:** usar generador existente y tratar Modelica como dependencia separada. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No afirmar que exportar Modelica ya ejecuta o valida el modelo.
- **Prueba de admisión pendiente:** Edificio conocido exportado y simulado con herramienta identificada.
- **Evidencia y alcance:** Archivo candidato recuperado: [teaser/data/output/modelica_output.py](https://github.com/RWTH-EBC/TEASER/blob/92ec587c7cb25837879db52e2cd0cd46763ceaf4/teaser/data/output/modelica_output.py); 82/82 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/RWTH-EBC/TEASER), [documentación recuperada](https://github.com/RWTH-EBC/TEASER/blob/main/README.md), [setup.py](https://github.com/RWTH-EBC/TEASER/blob/main/setup.py). Commit observado: `92ec587c7cb25837879db52e2cd0cd46763ceaf4`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-samuelduchesne--archetypal"></a>

#### 084. samuelduchesne/archetypal

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Gestión y análisis de arquetipos/modelos energéticos.
- **Puerta de integración propuesta:** API/CLI Python y dependencia EnergyPlus.
- **Construir nosotros, solo si falta:** Seleccionar operaciones de biblioteca/arquetipo dentro de un flujo energético.
- **Con qué y por qué:** conservar lectores y objetos nativos. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No mantener otro simulador; comprobar compatibilidad del paquete con EnergyPlus.
- **Prueba de admisión pendiente:** Modelo pequeño con metadatos y resultados recuperables.
- **Evidencia y alcance:** Archivo candidato recuperado: [archetypal/cli.py](https://github.com/samuelduchesne/archetypal/blob/4c13297f1acbe8bcf0982b8c862a76fee6fbea01/archetypal/cli.py); 382/382 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/samuelduchesne/archetypal), [documentación recuperada](https://github.com/samuelduchesne/archetypal/blob/main/README.md), [Dockerfile](https://github.com/samuelduchesne/archetypal/blob/main/Dockerfile). Commit observado: `4c13297f1acbe8bcf0982b8c862a76fee6fbea01`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-samuelduchesne--geomeppy"></a>

#### 085. samuelduchesne/geomeppy

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Edición geométrica de modelos IDF.
- **Puerta de integración propuesta:** API Python sobre eppy.
- **Construir nosotros, solo si falta:** Cambios geométricos tipados con copia, validación y diferencias.
- **Con qué y por qué:** utilidad del adaptador EnergyPlus, no MCP autónomo. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No convertir geometría sintética en envolvente térmica completa.
- **Prueba de admisión pendiente:** Cambio de volumen/superficie con topología y modelo preservados.
- **Evidencia y alcance:** Archivo candidato recuperado: [geomeppy/geom/clippers.py](https://github.com/samuelduchesne/geomeppy/blob/f2677b6cf1bf1390d4316262e7f06355a207c582/geomeppy/geom/clippers.py); 144/144 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/samuelduchesne/geomeppy), [documentación recuperada](https://github.com/samuelduchesne/geomeppy/blob/master/README.md), [pyproject.toml](https://github.com/samuelduchesne/geomeppy/blob/master/pyproject.toml). Commit observado: `f2677b6cf1bf1390d4316262e7f06355a207c582`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-santoshphilip--eppy"></a>

#### 086. santoshphilip/eppy

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Lectura y edición de objetos EnergyPlus IDF.
- **Puerta de integración propuesta:** API Python y diccionario de versión.
- **Construir nosotros, solo si falta:** Edición acotada por esquema, manteniendo trazabilidad del cambio.
- **Con qué y por qué:** emplear parser dentro del adaptador energético seleccionado. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No reescribir lector IDF ni usar diccionario de otra versión.
- **Prueba de admisión pendiente:** Lectura/edición/serialización de un objeto con IDD correcto.
- **Evidencia y alcance:** Archivo candidato recuperado: [main.py](https://github.com/santoshphilip/eppy/blob/3323849be84bf48c1b7c99c760f93bed80564ca5/main.py); 6/6 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/santoshphilip/eppy), [documentación recuperada](https://github.com/santoshphilip/eppy/blob/master/README.rst), [pyproject.toml](https://github.com/santoshphilip/eppy/blob/master/pyproject.toml). Commit observado: `3323849be84bf48c1b7c99c760f93bed80564ca5`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ucl--simstock"></a>

#### 087. UCL/simstock

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Preparación/modelado energético de stock de edificios.
- **Puerta de integración propuesta:** API Python y pipeline SimStock.
- **Construir nosotros, solo si falta:** Mapear geometrías y atributos a un caso de stock verificable.
- **Con qué y por qué:** conservar preprocesamiento y ejecución del proyecto. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No asumir que huellas urbanas bastan para deducir usos y construcciones.
- **Prueba de admisión pendiente:** Muestra de edificios con pérdidas de información explícitas.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/simstock/__init__.py](https://github.com/UCL/simstock/blob/8f8889ba990cd3111c41c4022de962a59d7ec0ad/src/simstock/__init__.py); 27/27 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UCL/simstock), [documentación recuperada](https://github.com/UCL/simstock/blob/main/README.md), [environment.yaml](https://github.com/UCL/simstock/blob/main/environment.yaml). Commit observado: `8f8889ba990cd3111c41c4022de962a59d7ec0ad`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-urbanopt--urbanopt-cli"></a>

#### 088. urbanopt/urbanopt-cli

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Orquestación de proyectos energéticos distritales.
- **Puerta de integración propuesta:** CLI Ruby y estructura GeoJSON/workflows.
- **Construir nosotros, solo si falta:** Receta del proyecto, parámetros admitidos y seguimiento de resultados.
- **Con qué y por qué:** envolver CLI existente; no reproducir orquestación Ruby. Aplicación/binario y bibliotecas de su distribución. Seleccionar CLI o binding solo después de probar qué operación funciona fuera del escritorio.
- **No reconstruir / crítica:** No ejecutar cualquier proyecto descargado ni duplicar CityEnergyAnalyst sin requisito.
- **Prueba de admisión pendiente:** Proyecto de ejemplo con workflow y resultados equivalentes.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [bin/uo](https://github.com/urbanopt/urbanopt-cli/blob/fbebeae3389201ec5db47cdce0274ca1b8f97299/bin/uo); lectura parcial de 5/5 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/urbanopt/urbanopt-cli), [documentación recuperada](https://github.com/urbanopt/urbanopt-cli/blob/develop/README.md), [CMakeLists.txt](https://github.com/urbanopt/urbanopt-cli/blob/develop/CMakeLists.txt). Commit observado: `fbebeae3389201ec5db47cdce0274ca1b8f97299`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-urbanopt--urbanopt-example-geojson-project"></a>

#### 089. urbanopt/urbanopt-example-geojson-project

- **Dictamen:** Referencia, especificación o fixture; no integración ejecutable autónoma.
- **Traer del original:** Proyecto de ejemplo y recursos URBANopt.
- **Puerta de integración propuesta:** Archivos GeoJSON, workflows y medidas de ejemplo.
- **Construir nosotros, solo si falta:** Fixture documentada para probar el conector URBANopt.
- **Con qué y por qué:** datos/ejemplo del paquete padre, sin adaptador independiente. Solo incorporación documental o fixture a la investigación/pruebas. No instalar ni publicar un servidor MCP para este repositorio.
- **No reconstruir / crítica:** No contar el ejemplo como otro motor o como escenario real de una ciudad.
- **Prueba de admisión pendiente:** Ejemplo intacto ejecutado con la versión admitida del CLI.
- **Evidencia y alcance:** Archivo candidato recuperado: [example_project/resources/residential-measures/measures/ServerDirectoryCleanup/measure.rb](https://github.com/urbanopt/urbanopt-example-geojson-project/blob/46d70351e308c8da210b42e6baf57f8180d2c189/example_project/resources/residential-measures/measures/ServerDirectoryCleanup/measure.rb); 188/188 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/urbanopt/urbanopt-example-geojson-project), [documentación recuperada](https://github.com/urbanopt/urbanopt-example-geojson-project/blob/develop/README.md). Commit observado: `46d70351e308c8da210b42e6baf57f8180d2c189`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-urbanopt--urbanopt-reopt-gem"></a>

#### 090. urbanopt/urbanopt-reopt-gem

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Conexión de URBANopt con optimización REopt.
- **Puerta de integración propuesta:** Gem Ruby y servicio/ejecutor REopt correspondiente.
- **Construir nosotros, solo si falta:** Enlace entre escenarios y resultados de optimización con supuestos económicos.
- **Con qué y por qué:** conservar integración Ruby; las credenciales pertenecen al servicio autorizado. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No duplicar REopt ni atribuir rentabilidad cierta a un escenario.
- **Prueba de admisión pendiente:** Ejemplo reducido con tarifas, restricciones y respuesta reproducible.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [lib/urbanopt/reopt.rb](https://github.com/urbanopt/urbanopt-reopt-gem/blob/e72772a341c06fbc18457cebaa60be87d686cd2b/lib/urbanopt/reopt.rb); lectura parcial de 16/16 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/urbanopt/urbanopt-reopt-gem), [documentación recuperada](https://github.com/urbanopt/urbanopt-reopt-gem/blob/develop/README.md), [urbanopt-reopt.gemspec](https://github.com/urbanopt/urbanopt-reopt-gem/blob/develop/urbanopt-reopt.gemspec). Commit observado: `e72772a341c06fbc18457cebaa60be87d686cd2b`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.


### Familia: LiDAR y nubes de puntos

<a id="tool-cloudcompare--cloudcompare"></a>

#### 091. CloudCompare/CloudCompare

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Procesamiento y comparación de nubes de puntos.
- **Puerta de integración propuesta:** CLI y herramientas de la aplicación.
- **Construir nosotros, solo si falta:** Operaciones por lotes con archivos aislados, parámetros y métricas trazables.
- **Con qué y por qué:** controlar proceso nativo; usar GUI solo cuando la operación lo exija. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No reconstruir registro de nubes ni perder CRS/escalas globales.
- **Prueba de admisión pendiente:** Dos nubes sintéticas con transformación/distancia conocidas.
- **Evidencia y alcance:** Archivo candidato recuperado: [ccViewer/main.cpp](https://github.com/CloudCompare/CloudCompare/blob/1b4b15697c0ea2e285edd4c86ca7ececd92c75d3/ccViewer/main.cpp); 193/193 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CloudCompare/CloudCompare), [documentación recuperada](https://github.com/CloudCompare/CloudCompare/blob/master/README.md), [CMakeLists.txt](https://github.com/CloudCompare/CloudCompare/blob/master/CMakeLists.txt). Commit observado: `1b4b15697c0ea2e285edd4c86ca7ececd92c75d3`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-isl-org--open3d"></a>

#### 092. isl-org/Open3D

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Geometría 3D, nubes y algoritmos de reconstrucción.
- **Puerta de integración propuesta:** API Python/C++ de Open3D.
- **Construir nosotros, solo si falta:** Operaciones seleccionadas y resultados con transformación/procedencia.
- **Con qué y por qué:** bindings nativos evitan otra capa C++ propia. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No presentar registro aproximado como levantamiento topográfico certificado.
- **Prueba de admisión pendiente:** Nube sintética con registro y error de referencia.
- **Evidencia y alcance:** Archivo candidato recuperado: [python/tools/cli.py](https://github.com/isl-org/Open3D/blob/b6c5e196384ad71e75b6e6f9c5da22d046221f1d/python/tools/cli.py); 420/447 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/isl-org/Open3D), [documentación recuperada](https://github.com/isl-org/Open3D/blob/main/README.md), [CMakeLists.txt](https://github.com/isl-org/Open3D/blob/main/CMakeLists.txt). Commit observado: `b6c5e196384ad71e75b6e6f9c5da22d046221f1d`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-pdal--pdal"></a>

#### 093. PDAL/PDAL

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Pipelines de lectura y procesamiento de nubes.
- **Puerta de integración propuesta:** CLI y pipelines JSON PDAL.
- **Construir nosotros, solo si falta:** Construir pipelines admitidos, validar etapas y producir artefactos/versiones.
- **Con qué y por qué:** JSON y proceso son frontera estable; no incrustar PDAL en el controlador. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No reescribir formatos LAS/LAZ ni publicar filtros sin unidades y CRS.
- **Prueba de admisión pendiente:** LAS pequeño con recuento, escala y filtro esperados.
- **Evidencia y alcance:** Archivo candidato recuperado: [kernels/PipelineKernel.cpp](https://github.com/PDAL/PDAL/blob/d04b9017f8b3a4675937ff28614d879509a63a74/kernels/PipelineKernel.cpp); 187/187 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/PDAL/PDAL), [documentación recuperada](https://github.com/PDAL/PDAL/blob/master/README.md), [CMakeLists.txt](https://github.com/PDAL/PDAL/blob/master/CMakeLists.txt). Commit observado: `d04b9017f8b3a4675937ff28614d879509a63a74`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-pdal--python"></a>

#### 094. PDAL/python

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Bindings Python de PDAL.
- **Puerta de integración propuesta:** API Python y biblioteca PDAL compatible.
- **Construir nosotros, solo si falta:** Usarlo solo cuando un adaptador Python necesite ejecutar/inspeccionar pipelines.
- **Con qué y por qué:** binding opcional del paquete PDAL. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No mantener dos instalaciones PDAL incompatibles ni otro servidor equivalente.
- **Prueba de admisión pendiente:** Mismo pipeline por binding y CLI produce mismo resultado.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/pdal/__main__.py](https://github.com/PDAL/python/blob/c963beb9bcf1830cc8b81fa19e1deb14e1aa1906/src/pdal/__main__.py); 79/79 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/PDAL/python), [documentación recuperada](https://github.com/PDAL/python/blob/main/README.rst), [CMakeLists.txt](https://github.com/PDAL/python/blob/main/CMakeLists.txt). Commit observado: `c963beb9bcf1830cc8b81fa19e1deb14e1aa1906`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-potree--potree"></a>

#### 095. potree/potree

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Visualización web de nubes de puntos.
- **Puerta de integración propuesta:** API JavaScript y formato servido por el visor.
- **Construir nosotros, solo si falta:** Vínculo con artefactos y comandos de cámara/selección si se elige este visor.
- **Con qué y por qué:** puente en navegador; conversión de nubes es componente aparte. JavaScript/TypeScript en el host del visor y un contrato de comandos/eventos de navegador. Un servidor MCP, si falta, usaría el SDK TypeScript y un puente explícito con esa sesión.
- **No reconstruir / crítica:** No asumir que el visor convierte LAS ni duplicar un visor ya seleccionado.
- **Prueba de admisión pendiente:** Cargar nube acotada y verificar extensión/selección.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/utils/ClipVolume.js](https://github.com/potree/potree/blob/5636cd471d9eb464969e758be45c44d7613d3859/src/utils/ClipVolume.js); 290/290 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/potree/potree), [documentación recuperada](https://github.com/potree/potree/blob/develop/README.md), [package.json](https://github.com/potree/potree/blob/develop/package.json). Commit observado: `5636cd471d9eb464969e758be45c44d7613d3859`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.


### Familia: MCP geoespacial y urbano existente

<a id="tool-anandb--energyplus-mcp-java"></a>

#### 096. anandb/energyplus-mcp-java

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP EnergyPlus implementado en Java.
- **Puerta de integración propuesta:** Servidor y herramientas upstream.
- **Construir nosotros, solo si falta:** Receta y pruebas de capacidades necesarias; modificaciones solo si una brecha queda demostrada.
- **Con qué y por qué:** conservar Java y su framework MCP, sin traducción automática a Python. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No construir otro MCP EnergyPlus por preferencia de lenguaje.
- **Framework/interfaz original:** No se identifica con certeza el framework del servidor a partir de la entrada recuperada; no inferirlo por el nombre del repositorio.
- **Prueba de admisión pendiente:** Ejecutar caso conocido y comparar salidas con motor directo.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/main/java/io/github/anandb/energyplus/EmcpApplication.java](https://github.com/anandb/energyplus-mcp-java/blob/35ac70762157b2e566425e83c82b70b2762d35d7/src/main/java/io/github/anandb/energyplus/EmcpApplication.java); 22/22 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/anandb/energyplus-mcp-java), [documentación recuperada](https://github.com/anandb/energyplus-mcp-java/blob/main/README.md), [Dockerfile](https://github.com/anandb/energyplus-mcp-java/blob/main/Dockerfile). Commit observado: `35ac70762157b2e566425e83c82b70b2762d35d7`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-bonninr--freecad_mcp"></a>

#### 097. bonninr/freecad_mcp

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Integración anunciada para FreeCAD; implementación aún por acreditar funcionalmente.
- **Puerta de integración propuesta:** main.py remite a blender_mcp.server; comprobar paquete y bridge efectivos.
- **Construir nosotros, solo si falta:** Ningún puente nuevo hasta resolver qué aplicación controla realmente esta entrada.
- **Con qué y por qué:** revisar runtime y plugin antes de seleccionar o portar implementación. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** El nombre del repositorio no acredita control FreeCAD; el namespace observado requiere investigación.
- **Framework/interfaz original:** No se identifica con certeza el framework del servidor a partir de la entrada recuperada; no inferirlo por el nombre del repositorio.
- **Prueba de admisión pendiente:** Cliente externo crea/reabre documento FreeCAD y recupera el objeto correcto.
- **Evidencia y alcance:** Archivo candidato recuperado: [main.py](https://github.com/bonninr/freecad_mcp/blob/54f150377097426864d418169fa431db40e0c157/main.py); 8/8 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/bonninr/freecad_mcp), [documentación recuperada](https://github.com/bonninr/freecad_mcp/blob/main/README.md), [pyproject.toml](https://github.com/bonninr/freecad_mcp/blob/main/pyproject.toml). Commit observado: `54f150377097426864d418169fa431db40e0c157`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-contextform--freecad-mcp"></a>

#### 098. contextform/freecad-mcp

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Integración FreeCAD con contexto/observadores identificados.
- **Puerta de integración propuesta:** Servidor y material histórico del repositorio.
- **Construir nosotros, solo si falta:** Solo mantener integración si se identifica ruta vigente fuera de archivos históricos.
- **Con qué y por qué:** respetar puente original; revisión de arquitectura antes de adoptar. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** La inspección encontró código en archive; eso no acredita un servidor vigente.
- **Framework/interfaz original:** No se identifica con certeza el framework del servidor a partir de la entrada recuperada; no inferirlo por el nombre del repositorio.
- **Prueba de admisión pendiente:** Arranque documentado desde checkout limpio y operación paramétrica.
- **Evidencia y alcance:** El barrido automático recuperó código auxiliar, histórico o de pruebas, no una interfaz suficiente para sustentar el conector. Se requiere inspección dirigida del API/CLI antes de implementar; no se usa ese archivo como prueba de operabilidad.
- **Identificación:** [repositorio](https://github.com/contextform/freecad-mcp), [documentación recuperada](https://github.com/contextform/freecad-mcp/blob/main/README.md). Commit observado: `de4fed2a7a4352fcb0de60d2b784063c54eeb812`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-ericmartinpe--energyplus-mcp-epjson"></a>

#### 099. ericmartinpe/EnergyPlus-MCP-epjson

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP con operaciones sobre modelos epJSON.
- **Puerta de integración propuesta:** Servidor Python y conversión IDF/epJSON existentes.
- **Construir nosotros, solo si falta:** Receta, validación de compatibilidad y mapeo de escenarios.
- **Con qué y por qué:** conservar servidor y dependencias; comparar con LBNL/idfkit. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No reconstruir inspección/edición ya expuestas ni adoptar todos los forks.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1. Hay imports de la API v1: fijar dependencias compatibles o verificar una migración; no instalar automáticamente la última versión del SDK.
- **Prueba de admisión pendiente:** Modificar objeto epJSON y verificar corrida y conversión de versión.
- **Evidencia y alcance:** Archivo candidato recuperado: [energyplus-mcp-server/energyplus_mcp_server/server.py](https://github.com/ericmartinpe/EnergyPlus-MCP-epjson/blob/09b419bb07e816491086bf705e5719b5babca7b7/energyplus-mcp-server/energyplus_mcp_server/server.py); 420/1992 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ericmartinpe/EnergyPlus-MCP-epjson), [documentación recuperada](https://github.com/ericmartinpe/EnergyPlus-MCP-epjson/blob/main/README.md). Commit observado: `09b419bb07e816491086bf705e5719b5babca7b7`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-gaopengbin--cesium-mcp"></a>

#### 100. gaopengbin/cesium-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** Contratos y servidor MCP para Cesium.
- **Puerta de integración propuesta:** Paquetes TypeScript de servidor/contratos y conexión a visor.
- **Construir nosotros, solo si falta:** Receta del visor y pruebas de cámara/objetos con IDs urbanos.
- **Con qué y por qué:** conservar TypeScript y puente de navegador del upstream. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No reemplazar renderizador ni asumir un visor conectado por iniciar el servidor.
- **Framework/interfaz original:** Imports observados: SDK MCP TypeScript/JavaScript.
- **Prueba de admisión pendiente:** Listar y enfocar objeto en visor real; leer estado final.
- **Evidencia y alcance:** Archivo candidato recuperado: [packages/cesium-mcp-dev/src/server.ts](https://github.com/gaopengbin/cesium-mcp/blob/6572b727ff86aa28f1ddfd234539dd82af2fcd33/packages/cesium-mcp-dev/src/server.ts); 149/149 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/gaopengbin/cesium-mcp), [documentación recuperada](https://github.com/gaopengbin/cesium-mcp/blob/main/README.md), [Dockerfile](https://github.com/gaopengbin/cesium-mcp/blob/main/Dockerfile). Commit observado: `6572b727ff86aa28f1ddfd234539dd82af2fcd33`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-idfkit--idfkit-mcp"></a>

#### 101. idfkit/idfkit-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** Servidor MCP sobre herramientas de modelado EnergyPlus.
- **Puerta de integración propuesta:** Entradas del paquete idfkit-mcp.
- **Construir nosotros, solo si falta:** Evaluar cobertura y mantener receta/contratos si sustituye otra integración energética.
- **Con qué y por qué:** preservar su implementación y motor compatible. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No sumar otro servidor energético sin diferencia funcional probada.
- **Framework/interfaz original:** Imports observados: paquete FastMCP independiente.
- **Prueba de admisión pendiente:** Inspección/edición y corrida mínima frente a EnergyPlus directo.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/idfkit_mcp/server.py](https://github.com/idfkit/idfkit-mcp/blob/97c76475281e3681f8cc9966b078045928d370f1/src/idfkit_mcp/server.py); 180/180 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/idfkit/idfkit-mcp), [documentación recuperada](https://github.com/idfkit/idfkit-mcp/blob/main/README.md), [Dockerfile](https://github.com/idfkit/idfkit-mcp/blob/main/Dockerfile). Commit observado: `97c76475281e3681f8cc9966b078045928d370f1`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-jagan-shanmugam--open-streetmap-mcp"></a>

#### 102. jagan-shanmugam/open-streetmap-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP de geocodificación, rutas y búsqueda de lugares.
- **Puerta de integración propuesta:** Herramientas upstream y servicios externos que invocan.
- **Construir nosotros, solo si falta:** Configuración explícita de proveedores, cobertura, procedencia y límites.
- **Con qué y por qué:** reutilizar servidor; distinguir servicio público y motor propio. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No presentarlo como servidor OSM autosuficiente ni inventar disponibilidad de proveedores.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1. Hay imports de la API v1: fijar dependencias compatibles o verificar una migración; no instalar automáticamente la última versión del SDK.
- **Prueba de admisión pendiente:** Consulta conocida y comportamiento ante proveedor no disponible.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/osm_mcp_server/server.py](https://github.com/jagan-shanmugam/open-streetmap-mcp/blob/4319f9f0744f089209081e8c20fc854db7a1a43c/src/osm_mcp_server/server.py); 420/1599 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/jagan-shanmugam/open-streetmap-mcp), [documentación recuperada](https://github.com/jagan-shanmugam/open-streetmap-mcp/blob/main/README.md), [pyproject.toml](https://github.com/jagan-shanmugam/open-streetmap-mcp/blob/main/pyproject.toml). Commit observado: `4319f9f0744f089209081e8c20fc854db7a1a43c`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-jjsantos01--qgis_mcp"></a>

#### 103. jjsantos01/qgis_mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** Servidor MCP y conexión a plugin QGIS.
- **Puerta de integración propuesta:** Herramientas para proyectos, capas y operaciones de sesión.
- **Construir nosotros, solo si falta:** Receta conjunta, perfil de permisos y pruebas de proyecto.
- **Con qué y por qué:** conservar Python y puente QGIS; comparar con otras implementaciones. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No rehacer carga/edición existentes ni confundir conexión con validez de Processing.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1. Hay imports de la API v1: fijar dependencias compatibles o verificar una migración; no instalar automáticamente la última versión del SDK.
- **Prueba de admisión pendiente:** Abrir proyecto, ejecutar operación y comprobar capa guardada.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/qgis_mcp/qgis_mcp_server.py](https://github.com/jjsantos01/qgis_mcp/blob/e37bf6f095e1658a8939cb7d8467c1e61d138bd2/src/qgis_mcp/qgis_mcp_server.py); 270/270 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/jjsantos01/qgis_mcp), [documentación recuperada](https://github.com/jjsantos01/qgis_mcp/blob/main/README.md), [pyproject.toml](https://github.com/jjsantos01/qgis_mcp/blob/main/pyproject.toml). Commit observado: `e37bf6f095e1658a8939cb7d8467c1e61d138bd2`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-jordangunn--gdal-mcp"></a>

#### 104. JordanGunn/gdal-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** Servidor MCP y registro de herramientas GDAL.
- **Puerta de integración propuesta:** Servidor y módulos upstream.
- **Construir nosotros, solo si falta:** Receta de drivers/versiones y pruebas de las operaciones que necesitamos.
- **Con qué y por qué:** conservar MCP; extender solo una operación ausente demostrada. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No construir otro GDAL MCP sin contrastar catálogo, límites y salidas.
- **Framework/interfaz original:** Imports observados: paquete FastMCP independiente.
- **Prueba de admisión pendiente:** Reproyección/recorte conocidos y rechazo de entrada incompatible.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/server.py](https://github.com/JordanGunn/gdal-mcp/blob/418f401c7987e388eaaee6ad13289798a1ff69b6/src/server.py); 94/94 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/JordanGunn/gdal-mcp), [documentación recuperada](https://github.com/JordanGunn/gdal-mcp/blob/main/README.md), [Dockerfile](https://github.com/JordanGunn/gdal-mcp/blob/main/Dockerfile). Commit observado: `418f401c7987e388eaaee6ad13289798a1ff69b6`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-klabum--swmm-mcp-pub"></a>

#### 105. kLabUM/SWMM-MCP-PUB

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP SWMM con carga, edición, corrida y reportes.
- **Puerta de integración propuesta:** Herramientas list_models, duplicate_model, run_model y reportes identificadas.
- **Construir nosotros, solo si falta:** Receta, espacio de modelos por proyecto y pruebas hidráulicas de contrato.
- **Con qué y por qué:** conservar servidor y motor; investigar extensiones solo por brecha concreta. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No proponer como nuevo un run_model ya implementado; revisar unidades de edición.
- **Framework/interfaz original:** Imports observados: paquete FastMCP independiente.
- **Prueba de admisión pendiente:** Modelo duplicado y corrida con reporte/series iguales al SWMM directo.
- **Evidencia y alcance:** Archivo candidato recuperado: [server.py](https://github.com/kLabUM/SWMM-MCP-PUB/blob/0c299b24196d1c8c32e92e8d4437958f237e4a88/server.py); 420/491 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/kLabUM/SWMM-MCP-PUB), [documentación recuperada](https://github.com/kLabUM/SWMM-MCP-PUB/blob/main/README.md), [pyproject.toml](https://github.com/kLabUM/SWMM-MCP-PUB/blob/main/pyproject.toml). Commit observado: `0c299b24196d1c8c32e92e8d4437958f237e4a88`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-lbnl-eta--energyplus-mcp"></a>

#### 106. LBNL-ETA/EnergyPlus-MCP

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP de inspección, edición y simulación EnergyPlus.
- **Puerta de integración propuesta:** Servidor Python, configuración y receta de contenedor upstream.
- **Construir nosotros, solo si falta:** Perfil reproducible de motor/modelos y pruebas de escenarios propios.
- **Con qué y por qué:** reutilizar servidor antes de escribir fachada energética. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No atribuir como aporte propio cargar/validar/simular si ya está expuesto.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1. Hay imports de la API v1: fijar dependencias compatibles o verificar una migración; no instalar automáticamente la última versión del SDK.
- **Prueba de admisión pendiente:** Caso de referencia, cambio acotado y reporte de motor verificados.
- **Evidencia y alcance:** Archivo candidato recuperado: [energyplus-mcp-server/energyplus_mcp_server/server.py](https://github.com/LBNL-ETA/EnergyPlus-MCP/blob/5a7d3bb1d2e537ba329d3412c8b79d22cedd7c70/energyplus-mcp-server/energyplus_mcp_server/server.py); 420/1431 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/LBNL-ETA/EnergyPlus-MCP), [documentación recuperada](https://github.com/LBNL-ETA/EnergyPlus-MCP/blob/main/README.md). Commit observado: `5a7d3bb1d2e537ba329d3412c8b79d22cedd7c70`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-mahdin75--gis-mcp"></a>

#### 107. mahdin75/gis-mcp

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Proyecto de integración GIS/MCP y agentes asociados.
- **Puerta de integración propuesta:** Servidor real y separación frente a agentes por localizar.
- **Construir nosotros, solo si falta:** Evaluación de herramientas reutilizables sin importar su agente completo.
- **Con qué y por qué:** seleccionar únicamente componente MCP autónomo si existe. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** Una prueba de herramientas en LangChain no demuestra el punto de arranque del servidor.
- **Framework/interfaz original:** No se identifica con certeza el framework del servidor a partir de la entrada recuperada; no inferirlo por el nombre del repositorio.
- **Prueba de admisión pendiente:** Cliente MCP externo enumera e invoca una herramienta sin agente propietario.
- **Evidencia y alcance:** Archivo candidato recuperado: [agents/Langchain/verify_tools.py](https://github.com/mahdin75/gis-mcp/blob/be8a33d25aefccf256136f3de0f18124f6efa16f/agents/Langchain/verify_tools.py); 193/193 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/mahdin75/gis-mcp), [documentación recuperada](https://github.com/mahdin75/gis-mcp/blob/main/README.md), [Dockerfile](https://github.com/mahdin75/gis-mcp/blob/main/Dockerfile). Commit observado: `be8a33d25aefccf256136f3de0f18124f6efa16f`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-msradam--osmnx-mcp"></a>

#### 108. msradam/osmnx-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP con gestión de grafos OSMnx y montaje de herramientas.
- **Puerta de integración propuesta:** create_server y registro de grafos identificados.
- **Construir nosotros, solo si falta:** Receta, persistencia/recuperación requerida y pruebas de grafos por proyecto.
- **Con qué y por qué:** conservar wrapper; comprobar operaciones antes de escribir OSMnx MCP propio. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No reinventar registro de grafos; un grafo activo global puede requerir revisar aislamiento.
- **Framework/interfaz original:** Imports observados: paquete FastMCP independiente.
- **Prueba de admisión pendiente:** Dos grafos distintos sin confundir resultados ni selección activa.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/osmnx_mcp/server.py](https://github.com/msradam/osmnx-mcp/blob/be547a94038b7b3fa353615381a330b94e2b0b7c/src/osmnx_mcp/server.py); 68/68 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/msradam/osmnx-mcp), [pyproject.toml](https://github.com/msradam/osmnx-mcp/blob/main/pyproject.toml). Commit observado: `be547a94038b7b3fa353615381a330b94e2b0b7c`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-neka-nat--freecad-mcp"></a>

#### 109. neka-nat/freecad-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP/bridge FreeCAD con operaciones y trabajos asíncronos.
- **Puerta de integración propuesta:** Servidor Python y RPC del addon.
- **Construir nosotros, solo si falta:** Receta compatible y selección de herramientas paramétricas admitidas.
- **Con qué y por qué:** conservar bridge y trabajos que ya ofrece. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No construir otro sistema de jobs sin probar el existente; no publicar ejecución libre por defecto.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1; API MCPServer del SDK Python v2. El código incluye rutas alternativas v1/v2: comprobar la combinación instalada, sin asumir que requiere una reescritura.
- **Prueba de admisión pendiente:** Documento, trabajo asíncrono y recuperación de estado tras error.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/freecad_mcp/server.py](https://github.com/neka-nat/freecad-mcp/blob/ec8abf21fb9e9ed4bbcbba497515e088423ad251/src/freecad_mcp/server.py); 420/860 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/neka-nat/freecad-mcp), [documentación recuperada](https://github.com/neka-nat/freecad-mcp/blob/main/README.md), [pyproject.toml](https://github.com/neka-nat/freecad-mcp/blob/main/pyproject.toml). Commit observado: `ec8abf21fb9e9ed4bbcbba497515e088423ad251`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-nkarasiak--qgis-mcp"></a>

#### 110. nkarasiak/qgis-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP QGIS con registro/conexión de instancias.
- **Puerta de integración propuesta:** Servidor, plugin y resolución de instancias identificados.
- **Construir nosotros, solo si falta:** Receta, selección explícita de instancia y pruebas de aislamiento.
- **Con qué y por qué:** conservar lógica de conexión/reintentos existente. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No proponer descubrimiento multiinstancia como novedad si ya está implementado.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1; API MCPServer del SDK Python v2. El código incluye rutas alternativas v1/v2: comprobar la combinación instalada, sin asumir que requiere una reescritura.
- **Prueba de admisión pendiente:** Dos sesiones QGIS identificadas y operación en la sesión correcta.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/qgis_mcp/server.py](https://github.com/nkarasiak/qgis-mcp/blob/dae432367fcb2873a151b94c4faaadef2033cf9f/src/qgis_mcp/server.py); 420/3591 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/nkarasiak/qgis-mcp), [documentación recuperada](https://github.com/nkarasiak/qgis-mcp/blob/main/README.md), [pyproject.toml](https://github.com/nkarasiak/qgis-mcp/blob/main/pyproject.toml). Commit observado: `dae432367fcb2873a151b94c4faaadef2033cf9f`. Licencia en el inventario: `GPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-osgeo--grass-mcp"></a>

#### 111. OSGeo/grass-mcp

- **Dictamen:** No hay implementación ejecutable acreditada; no anunciar integración.
- **Traer del original:** Repositorio que anuncia integración MCP para GRASS.
- **Puerta de integración propuesta:** README/licencia; no se localizaron archivos de implementación.
- **Construir nosotros, solo si falta:** Ninguna reutilización de servidor hasta que exista código; evaluar GRASS nativo aparte.
- **Con qué y por qué:** no hay base ejecutable acreditada sobre la que elegir framework. No fijar lenguaje, framework ni receta ejecutable todavía. Falta acreditar una implementación/interfaz utilizable; crear código ahora asumiría una arquitectura sin evidencia.
- **No reconstruir / crítica:** No presentarlo como MCP instalable ni contar una prueba aprobada inexistente.
- **Framework/interfaz original:** No se identifica con certeza el framework del servidor a partir de la entrada recuperada; no inferirlo por el nombre del repositorio.
- **Prueba de admisión pendiente:** Aparición de implementación, instalación limpia y llamada real.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/OSGeo/grass-mcp), [documentación recuperada](https://github.com/OSGeo/grass-mcp/blob/main/README.md). Commit observado: `83ec0d4dabd1416dca2a9bddcc6a37d6843c6bf1`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-piatkowski--qgis-mcp"></a>

#### 112. piatkowski/qgis-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP QGIS con operaciones geográficas tipadas.
- **Puerta de integración propuesta:** Herramientas de capa, reproyección, recorte, estadísticas y exportación identificadas.
- **Construir nosotros, solo si falta:** Receta, pruebas de procesamiento y compatibilidad con proyectos reales.
- **Con qué y por qué:** reutilizar operaciones; no portar por uniformidad. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No reconstruir funciones ya expuestas; medir diferencias frente a otros QGIS MCP.
- **Framework/interfaz original:** Imports observados: paquete FastMCP independiente.
- **Prueba de admisión pendiente:** Operación con CRS conocido y salida reabierta en QGIS.
- **Evidencia y alcance:** Archivo candidato recuperado: [server/tools.py](https://github.com/piatkowski/qgis-mcp/blob/f23312bff5f6a09def134f88006bfaceda723430/server/tools.py); 187/187 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/piatkowski/qgis-mcp), [documentación recuperada](https://github.com/piatkowski/qgis-mcp/blob/main/README.md), [pyproject.toml](https://github.com/piatkowski/qgis-mcp/blob/main/pyproject.toml). Commit observado: `f23312bff5f6a09def134f88006bfaceda723430`. Licencia en el inventario: `GPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-profrino--bonsai-bim-skills"></a>

#### 113. ProfRino/bonsai-bim-skills

- **Dictamen:** Referencia, especificación o fixture; no integración ejecutable autónoma.
- **Traer del original:** Skills y helpers para Bonsai BIM.
- **Puerta de integración propuesta:** Instrucciones y funciones Python del proyecto.
- **Construir nosotros, solo si falta:** Reutilizar conocimiento/helpers comprobados dentro del paquete BIM elegido.
- **Con qué y por qué:** skill no equivale a servidor MCP; revisar funciones antes de incorporarlas. Solo incorporación documental o fixture a la investigación/pruebas. No instalar ni publicar un servidor MCP para este repositorio.
- **No reconstruir / crítica:** No anunciar skills como endpoint MCP ni copiar instrucciones como código de confianza.
- **Framework/interfaz original:** No se identifica con certeza el framework del servidor a partir de la entrada recuperada; no inferirlo por el nombre del repositorio.
- **Prueba de admisión pendiente:** Helper sobre IFC pequeño con resultado comprobable y dependencia explícita.
- **Evidencia y alcance:** Archivo candidato recuperado: [canonical/bonsai_bim_helpers.py](https://github.com/ProfRino/bonsai-bim-skills/blob/cc51dd8a7bc0d7443235439adf998baa6b4e9008/canonical/bonsai_bim_helpers.py); 420/5871 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ProfRino/bonsai-bim-skills), [documentación recuperada](https://github.com/ProfRino/bonsai-bim-skills/blob/main/README.md). Commit observado: `cc51dd8a7bc0d7443235439adf998baa6b4e9008`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-rainergaier--energyplus-mcp-server"></a>

#### 114. RainerGaier/energyplus-mcp-server

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP y API con generación/ejecución y consulta de simulaciones.
- **Puerta de integración propuesta:** Servidor MCP y rutas HTTP identificadas.
- **Construir nosotros, solo si falta:** Receta y pruebas de plantillas, meteorología y estado de corrida existentes.
- **Con qué y por qué:** conservar implementación; comparar antes de elegir paquete energético. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No crear otra API de jobs o generación si sus rutas ya cubren la necesidad.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1. Hay imports de la API v1: fijar dependencias compatibles o verificar una migración; no instalar automáticamente la última versión del SDK.
- **Prueba de admisión pendiente:** Caso completo con plantilla, EPW y consulta de estado/resultados.
- **Evidencia y alcance:** Archivo candidato recuperado: [energyplus-mcp-server/energyplus_mcp_server/server.py](https://github.com/RainerGaier/energyplus-mcp-server/blob/ec0c43421ae51f044d403cfa802bd4ec7c39b56c/energyplus-mcp-server/energyplus_mcp_server/server.py); 420/1739 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/RainerGaier/energyplus-mcp-server), [documentación recuperada](https://github.com/RainerGaier/energyplus-mcp-server/blob/main/README.md). Commit observado: `ec0c43421ae51f044d403cfa802bd4ec7c39b56c`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-salog0d--urbanplannermcp"></a>

#### 115. salog0d/UrbanPlannerMCP

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** MCP con modelos urbanos específicos de población/infraestructura.
- **Puerta de integración propuesta:** run_city_infra_model y run_population_inequalities_model identificadas.
- **Construir nosotros, solo si falta:** Examinar fórmulas, entradas y alcance antes de considerar su exposición.
- **Con qué y por qué:** reutilizar solo modelos científicamente admitidos, no el nombre genérico. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No tratar UrbanPlanner como cobertura de todo urbanismo ni convertir estimaciones en hechos.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1. Hay imports de la API v1: fijar dependencias compatibles o verificar una migración; no instalar automáticamente la última versión del SDK.
- **Prueba de admisión pendiente:** Caso numérico documentado y revisión de supuestos del modelo.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/server.py](https://github.com/salog0d/UrbanPlannerMCP/blob/730f0659dff05142bff834b8ce96215ee54cf2cf/src/server.py); 39/39 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/salog0d/UrbanPlannerMCP), [documentación recuperada](https://github.com/salog0d/UrbanPlannerMCP/blob/main/README.md), [pyproject.toml](https://github.com/salog0d/UrbanPlannerMCP/blob/main/pyproject.toml). Commit observado: `730f0659dff05142bff834b8ce96215ee54cf2cf`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-show2instruct--ifc-bonsai-mcp"></a>

#### 116. Show2Instruct/ifc-bonsai-mcp

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** Bridge MCP para Blender/Bonsai y servicios auxiliares.
- **Puerta de integración propuesta:** Servidor, addon y servicio de embeddings separado.
- **Construir nosotros, solo si falta:** Receta de componentes imprescindibles y operaciones BIM con identificación estable.
- **Con qué y por qué:** conservar bridge; embeddings solo si la función elegida los necesita. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No convertir el stack completo en requisito de leer un IFC; revisar código ejecutable expuesto.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1. Hay imports de la API v1: fijar dependencias compatibles o verificar una migración; no instalar automáticamente la última versión del SDK.
- **Prueba de admisión pendiente:** Consulta/edición IFC con GUID preservado y prueba de dependencia ausente.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/blender_mcp/server.py](https://github.com/Show2Instruct/ifc-bonsai-mcp/blob/62154932f99d8bff8494c51ddb0b16840fac8fec/src/blender_mcp/server.py); 172/172 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Show2Instruct/ifc-bonsai-mcp), [documentación recuperada](https://github.com/Show2Instruct/ifc-bonsai-mcp/blob/main/README.md), [pyproject.toml](https://github.com/Show2Instruct/ifc-bonsai-mcp/blob/main/pyproject.toml). Commit observado: `62154932f99d8bff8494c51ddb0b16840fac8fec`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-sparkgeo--geo-mcp-servers"></a>

#### 117. sparkgeo/geo-mcp-servers

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Colección de servidores geoespaciales.
- **Puerta de integración propuesta:** Subpaquetes y puntos de arranque por identificar individualmente.
- **Construir nosotros, solo si falta:** Evaluar cada servidor como candidato, no incorporar el monorepo entero.
- **Con qué y por qué:** usar runtime de cada subpaquete y recetas separadas. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** Un healthcheck del repositorio no acredita todas sus herramientas.
- **Framework/interfaz original:** No se identifica con certeza el framework del servidor a partir de la entrada recuperada; no inferirlo por el nombre del repositorio.
- **Prueba de admisión pendiente:** Listar y ejecutar una operación por subpaquete realmente seleccionado.
- **Evidencia y alcance:** Archivo candidato recuperado: [scripts/check_health.py](https://github.com/sparkgeo/geo-mcp-servers/blob/386098e0a704db584929cce89036ae1666d93752/scripts/check_health.py); 183/183 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/sparkgeo/geo-mcp-servers), [documentación recuperada](https://github.com/sparkgeo/geo-mcp-servers/blob/main/README.md), [requirements.txt](https://github.com/sparkgeo/geo-mcp-servers/blob/main/requirements.txt). Commit observado: `386098e0a704db584929cce89036ae1666d93752`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-spkane--freecad-addon-robust-mcp-server"></a>

#### 118. spkane/freecad-addon-robust-mcp-server

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** Servidor y bridge FreeCAD con manejo de ejecución/seguridad propios.
- **Puerta de integración propuesta:** MCPServer, registro de componentes y bridge de FreeCAD.
- **Construir nosotros, solo si falta:** Receta y pruebas de compatibilidad, permisos y resultados de comandos necesarios.
- **Con qué y por qué:** conservar SDK/bridge upstream y sus límites operativos. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No reimplementar timeouts o bridge sin identificar falla; distinguir timeout de detener cálculo.
- **Framework/interfaz original:** Imports observados: API MCPServer del SDK Python v2.
- **Prueba de admisión pendiente:** Trabajo válido, timeout y sesión FreeCAD utilizable después.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/freecad_mcp/server.py](https://github.com/spkane/freecad-addon-robust-mcp-server/blob/b076fa67b0fd6867527ba3a85552219be1d2b4c3/src/freecad_mcp/server.py); 420/545 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/spkane/freecad-addon-robust-mcp-server), [documentación recuperada](https://github.com/spkane/freecad-addon-robust-mcp-server/blob/main/README.md), [Dockerfile](https://github.com/spkane/freecad-addon-robust-mcp-server/blob/main/Dockerfile). Commit observado: `b076fa67b0fd6867527ba3a85552219be1d2b4c3`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-xrds76354--sumo-mcp-server"></a>

#### 119. XRDS76354/SUMO-MCP-Server

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** MCP de redes, demanda, control y consultas SUMO.
- **Puerta de integración propuesta:** manage_network, control_simulation y query_simulation_state identificadas.
- **Construir nosotros, solo si falta:** Receta y contrato del subconjunto admitido; validar estado por escenario.
- **Con qué y por qué:** conservar servidor y TraCI; ampliar solo brechas verificadas. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No vender sus comandos de optimización como mejora garantizada; revisar estado compartido.
- **Framework/interfaz original:** Imports observados: API FastMCP del SDK Python v1. Hay imports de la API v1: fijar dependencias compatibles o verificar una migración; no instalar automáticamente la última versión del SDK.
- **Prueba de admisión pendiente:** Red/demanda fijas, pasos reproducibles y cierre limpio de simulación.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/server.py](https://github.com/XRDS76354/SUMO-MCP-Server/blob/6b62a25c1b13751d636309a03e4388594fcd7620/src/server.py); 420/514 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/XRDS76354/SUMO-MCP-Server), [documentación recuperada](https://github.com/XRDS76354/SUMO-MCP-Server/blob/main/README.md), [pyproject.toml](https://github.com/XRDS76354/SUMO-MCP-Server/blob/main/pyproject.toml). Commit observado: `6b62a25c1b13751d636309a03e4388594fcd7620`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-zhonghao1995--agentic-swmm-workflow"></a>

#### 120. Zhonghao1995/agentic-swmm-workflow

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Workflow con componentes MCP SWMM/GIS y gráficos.
- **Puerta de integración propuesta:** Servidores JavaScript identificados y orquestador del proyecto.
- **Construir nosotros, solo si falta:** Separar componentes utilizables por cualquier cliente del agente/orquestación propia.
- **Con qué y por qué:** conservar cada runtime; no trasladar el agente entero al producto. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** No confundir workflow agentic con motor hidráulico ni duplicar herramientas ya disponibles.
- **Framework/interfaz original:** Imports observados: SDK MCP TypeScript/JavaScript.
- **Prueba de admisión pendiente:** Cliente MCP externo ejecuta caso sin depender del agente original.
- **Evidencia y alcance:** Archivo candidato recuperado: [mcp/swmm-gis/server.js](https://github.com/Zhonghao1995/agentic-swmm-workflow/blob/a3bf4f23469cf4252955901176c86b9c94578963/mcp/swmm-gis/server.js); 420/628 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Zhonghao1995/agentic-swmm-workflow), [documentación recuperada](https://github.com/Zhonghao1995/agentic-swmm-workflow/blob/main/README.md), [Dockerfile](https://github.com/Zhonghao1995/agentic-swmm-workflow/blob/main/Dockerfile). Commit observado: `a3bf4f23469cf4252955901176c86b9c94578963`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Modelos urbanos 3D y reconstrucción

<a id="tool-3dcitydb--3dcitydb"></a>

#### 121. 3dcitydb/3dcitydb

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Modelo y funciones de base de datos urbana 3D.
- **Puerta de integración propuesta:** Esquema SQL y herramientas de su versión.
- **Construir nosotros, solo si falta:** Receta de esquema, catálogo de objetos y permisos mínimos de consulta.
- **Con qué y por qué:** usar funciones/tablas originales; conector de aplicación sin acceso SQL irrestricto del agente. SQL y funciones originales tras una API de aplicación con rol acotado. Si falta la fachada MCP, implementarla con un cliente PostgreSQL/DuckDB tipado; no ofrecer SQL libre al agente.
- **No reconstruir / crítica:** No duplicar base 3D ni confundir v4/v5 y sus herramientas compatibles.
- **Prueba de admisión pendiente:** Importar/exportar CityGML pequeño con IDs y CRS preservados.
- **Evidencia y alcance:** No se recuperó un punto de entrada de código en esta revisión; la interfaz indicada sigue siendo hipótesis documental hasta verificarla.
- **Identificación:** [repositorio](https://github.com/3dcitydb/3dcitydb), [documentación recuperada](https://github.com/3dcitydb/3dcitydb/blob/master/README.md), [Dockerfile](https://github.com/3dcitydb/3dcitydb/blob/master/Dockerfile). Commit observado: `3fb6a9a36c067d8f9a06fef9e4a4cbdc5466af51`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-3dcitydb--citydb-tool"></a>

#### 122. 3dcitydb/citydb-tool

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Herramientas de importación/exportación y gestión CityDB.
- **Puerta de integración propuesta:** CLI Java y conexión a esquema compatible.
- **Construir nosotros, solo si falta:** Operaciones por trabajos y expedientes de importación/exportación.
- **Con qué y por qué:** envolver CLI del tool, preservando compatibilidad de esquema. JVM y CLI/biblioteca originales. El adaptador puede controlar el CLI como proceso o consumir un servicio existente; no hace falta portar el algoritmo a Go o Python.
- **No reconstruir / crítica:** No desarrollar importador CityGML propio ni lanzar migraciones como consulta ordinaria.
- **Prueba de admisión pendiente:** Round trip de ejemplo con recuento, identidad y geometría.
- **Evidencia y alcance:** Archivo candidato recuperado: [citydb-cli/src/main/java/module-info.java](https://github.com/3dcitydb/citydb-tool/blob/dcb4a8a159d06b164732dbd93990eee79f064f91/citydb-cli/src/main/java/module-info.java); 63/63 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/3dcitydb/citydb-tool), [documentación recuperada](https://github.com/3dcitydb/citydb-tool/blob/main/README.md), [Dockerfile](https://github.com/3dcitydb/citydb-tool/blob/main/Dockerfile). Commit observado: `dcb4a8a159d06b164732dbd93990eee79f064f91`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-citygml4j--citygml-tools"></a>

#### 123. citygml4j/citygml-tools

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Transformación y utilidades CityGML.
- **Puerta de integración propuesta:** CLI Java del proyecto.
- **Construir nosotros, solo si falta:** Recetas de conversión con declaración de pérdidas y versiones.
- **Con qué y por qué:** conservar ejecutable y parsers CityGML. JVM y CLI/biblioteca originales. El adaptador puede controlar el CLI como proceso o consumir un servicio existente; no hace falta portar el algoritmo a Go o Python.
- **No reconstruir / crítica:** No crear otra implementación de cada versión del formato.
- **Prueba de admisión pendiente:** Convertir ejemplo y validar geometría, IDs y propiedades conservadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/main/java/org/citygml4j/tools/CityGMLTools.java](https://github.com/citygml4j/citygml-tools/blob/cd59a8276821c4ee0a410c045880d4ff69563776/src/main/java/org/citygml4j/tools/CityGMLTools.java); 336/336 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/citygml4j/citygml-tools), [documentación recuperada](https://github.com/citygml4j/citygml-tools/blob/master/README.md), [Dockerfile](https://github.com/citygml4j/citygml-tools/blob/master/Dockerfile). Commit observado: `cd59a8276821c4ee0a410c045880d4ff69563776`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-citygml4j--citygml4j"></a>

#### 124. citygml4j/citygml4j

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Biblioteca Java para CityGML/CityJSON y sus modelos.
- **Puerta de integración propuesta:** API Java.
- **Construir nosotros, solo si falta:** Usarla en un conector que requiera acceso estructurado al formato.
- **Con qué y por qué:** dependencia del paquete 3D, no nuevo servidor MCP. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No mantener parser propio ni un servicio por cada biblioteca.
- **Prueba de admisión pendiente:** Lectura/escritura del mismo modelo sin cambios semánticos acordados.
- **Evidencia y alcance:** Archivo candidato recuperado: [citygml4j-cityjson/src/main/java/module-info.java](https://github.com/citygml4j/citygml4j/blob/f3295d7d8fcf56c4768bfc20286e4128b6b53b3d/citygml4j-cityjson/src/main/java/module-info.java); 44/44 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/citygml4j/citygml4j), [documentación recuperada](https://github.com/citygml4j/citygml4j/blob/master/README.md). Commit observado: `f3295d7d8fcf56c4768bfc20286e4128b6b53b3d`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-cityjson--cjio"></a>

#### 125. cityjson/cjio

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Manipulación y validación de CityJSON.
- **Puerta de integración propuesta:** API/CLI Python cjio.
- **Construir nosotros, solo si falta:** Operaciones acotadas de validación, selección y exportación con procedencia.
- **Con qué y por qué:** reutilizar CLI/API y conservar la versión CityJSON. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No convertir toda ciudad a GeoJSON perdiendo superficies y semántica.
- **Prueba de admisión pendiente:** CityJSON pequeño con índices de vértices, transform y semántica preservados.
- **Evidencia y alcance:** Archivo candidato recuperado: [cjio/__init__.py](https://github.com/cityjson/cjio/blob/35728539127f71b1d5ae458169ff84050e5e20ad/cjio/__init__.py); 18/18 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/cityjson/cjio), [documentación recuperada](https://github.com/cityjson/cjio/blob/master/README.rst), [Dockerfile](https://github.com/cityjson/cjio/blob/master/Dockerfile). Commit observado: `35728539127f71b1d5ae458169ff84050e5e20ad`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-dtcc-platform--dtcc-core"></a>

#### 126. dtcc-platform/dtcc-core

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Modelos de datos y operaciones geométricas DTCC.
- **Puerta de integración propuesta:** API Python y extensiones del proyecto.
- **Construir nosotros, solo si falta:** Mapeo controlado a objetos DTCC si se selecciona esa familia.
- **Con qué y por qué:** usar modelo nativo en paquete DTCC. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No añadir una representación urbana universal sin probar correspondencia.
- **Prueba de admisión pendiente:** Objeto conocido con coordenadas y propiedades preservadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [dtcc_core/model/__init__.py](https://github.com/dtcc-platform/dtcc-core/blob/aee72fd40f1e55018ccc5fd85b40249b7e6ca452/dtcc_core/model/__init__.py); 23/23 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/dtcc-platform/dtcc-core), [documentación recuperada](https://github.com/dtcc-platform/dtcc-core/blob/develop/README.md), [CMakeLists.txt](https://github.com/dtcc-platform/dtcc-core/blob/develop/CMakeLists.txt). Commit observado: `aee72fd40f1e55018ccc5fd85b40249b7e6ca452`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-dtcc-platform--dtcc-sim"></a>

#### 127. dtcc-platform/dtcc-sim

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Componentes de simulación de la plataforma DTCC.
- **Puerta de integración propuesta:** Servicio/ejecutor y contratos de esa versión.
- **Construir nosotros, solo si falta:** Receta y operaciones de las simulaciones realmente reproducibles.
- **Con qué y por qué:** conservar servicio Python si está operativo; evitar rehacer el motor. API/cliente Python o HTTP nativo existente, con el servicio original como dueño de trabajos y estado. El nuevo código se limita al contrato de integración que falte.
- **No reconstruir / crítica:** No atribuir cobertura científica al nombre sim sin identificar modelos y datos.
- **Prueba de admisión pendiente:** Ejemplo de simulación con salidas y parámetros conocidos.
- **Evidencia y alcance:** Archivo candidato recuperado: [service/main.py](https://github.com/dtcc-platform/dtcc-sim/blob/4322b6fedb702336db14e2068481028b4ae702eb/service/main.py); 53/53 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/dtcc-platform/dtcc-sim), [documentación recuperada](https://github.com/dtcc-platform/dtcc-sim/blob/develop/README.md), [Dockerfile](https://github.com/dtcc-platform/dtcc-sim/blob/develop/Dockerfile). Commit observado: `4322b6fedb702336db14e2068481028b4ae702eb`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-dtcc-platform--dtcc-viewer"></a>

#### 128. dtcc-platform/dtcc-viewer

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Visualización de objetos DTCC.
- **Puerta de integración propuesta:** API y ejecutor del visor.
- **Construir nosotros, solo si falta:** Enlace opcional entre resultados DTCC y selección visual.
- **Con qué y por qué:** conservar mecanismo de visualización del proyecto; verificar si es web o local. JavaScript/TypeScript en el host del visor y un contrato de comandos/eventos de navegador. Un servidor MCP, si falta, usaría el SDK TypeScript y un puente explícito con esa sesión.
- **No reconstruir / crítica:** No crear otro visor obligatorio ni confundir mostrar con validar simulación.
- **Prueba de admisión pendiente:** Abrir escena de referencia y comprobar extensión/selección.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/dtcc_viewer/scripts/main.py](https://github.com/dtcc-platform/dtcc-viewer/blob/234f0c6703549470e35918b1638698311ffdfa68/src/dtcc_viewer/scripts/main.py); 420/556 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/dtcc-platform/dtcc-viewer), [documentación recuperada](https://github.com/dtcc-platform/dtcc-viewer/blob/develop/README.md), [pyproject.toml](https://github.com/dtcc-platform/dtcc-viewer/blob/develop/pyproject.toml). Commit observado: `234f0c6703549470e35918b1638698311ffdfa68`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-project-plateau--plateau-builder"></a>

#### 129. Project-PLATEAU/PLATEAU-Builder

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Editor y herramientas para modelos urbanos PLATEAU.
- **Puerta de integración propuesta:** Aplicación Java y formatos de proyecto.
- **Construir nosotros, solo si falta:** Importación/exportación y tareas admitidas si existe automatización verificable.
- **Con qué y por qué:** conservar Java; no asumir API de control remoto por ser código abierto. Plugin o componente en el runtime de la aplicación anfitriona y un puente tipado externo cuando se requiera MCP. Debe respetar el hilo de interfaz, documento y sesión de la aplicación.
- **No reconstruir / crítica:** No reconstruir editor ni prometer headless sin interfaz probada.
- **Prueba de admisión pendiente:** Abrir, modificar y guardar ejemplo con identidad CityGML.
- **Evidencia y alcance:** Archivo candidato recuperado: [plateaubuilder-core/src/main/java/module-info.java](https://github.com/Project-PLATEAU/PLATEAU-Builder/blob/b2086799d523fb5745b2615dd63001b63708f513/plateaubuilder-core/src/main/java/module-info.java); 71/71 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Project-PLATEAU/PLATEAU-Builder), [documentación recuperada](https://github.com/Project-PLATEAU/PLATEAU-Builder/blob/main/README.md). Commit observado: `b2086799d523fb5745b2615dd63001b63708f513`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-project-plateau--plateau-gis-converter"></a>

#### 130. Project-PLATEAU/PLATEAU-GIS-Converter

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Conversión de modelos PLATEAU a productos GIS/3D.
- **Puerta de integración propuesta:** CLI y configuración Rust.
- **Construir nosotros, solo si falta:** Recetas de formatos admitidos y registro de pérdidas de transformación.
- **Con qué y por qué:** controlar binario Rust existente, sin portar el conversor. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No duplicar conversión ni asumir que cualquier CityGML es perfil PLATEAU.
- **Prueba de admisión pendiente:** Modelo de referencia convertido con recuento y CRS comprobados.
- **Evidencia y alcance:** Archivo candidato recuperado: [nusamai-czml/src/models/mod.rs](https://github.com/Project-PLATEAU/PLATEAU-GIS-Converter/blob/e1c8feff7d8ff3e132230d6c21eaed4879e4a235/nusamai-czml/src/models/mod.rs); 77/77 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Project-PLATEAU/PLATEAU-GIS-Converter), [documentación recuperada](https://github.com/Project-PLATEAU/PLATEAU-GIS-Converter/blob/main/README.md), [Cargo.toml](https://github.com/Project-PLATEAU/PLATEAU-GIS-Converter/blob/main/Cargo.toml). Commit observado: `e1c8feff7d8ff3e132230d6c21eaed4879e4a235`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-reearth--reearth-flow"></a>

#### 131. reearth/reearth-flow

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Plataforma de procesamiento y workflows geoespaciales.
- **Puerta de integración propuesta:** Ejecutor/API y grafos de acciones Re:Earth Flow.
- **Construir nosotros, solo si falta:** Lanzar workflows aprobados y relacionar resultados con escenario.
- **Con qué y por qué:** conservar orquestación existente y consumir API/CLI admitida. Cliente del API o ejecutor admitido por upstream; preferir la ruta que ya resuelva estado y trabajos. No implementar ambas antes de comprobar la necesidad.
- **No reconstruir / crítica:** No construir otro motor de grafos ni exponer todas las acciones como herramientas sin control.
- **Prueba de admisión pendiente:** Workflow pequeño reproducible y recuperación de un error de etapa.
- **Evidencia y alcance:** Archivo candidato recuperado: [engine/runtime/action-python-processor/src/lib.rs](https://github.com/reearth/reearth-flow/blob/aafa4e61461438e144529914719ea53c9b5f0c5e/engine/runtime/action-python-processor/src/lib.rs); 11/11 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/reearth/reearth-flow), [documentación recuperada](https://github.com/reearth/reearth-flow/blob/main/README.md). Commit observado: `aafa4e61461438e144529914719ea53c9b5f0c5e`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-tudelft3d--3dcitydb-tools-for-qgis"></a>

#### 132. tudelft3d/3DCityDB-Tools-for-QGIS

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Plugin de integración 3DCityDB y QGIS.
- **Puerta de integración propuesta:** Plugin/PyQGIS y esquema compatible.
- **Construir nosotros, solo si falta:** Receta de instalación y acciones dentro de la sesión QGIS elegida.
- **Con qué y por qué:** reutilizar plugin; compartir instancia con conector QGIS. Plugin o componente en el runtime de la aplicación anfitriona y un puente tipado externo cuando se requiera MCP. Debe respetar el hilo de interfaz, documento y sesión de la aplicación.
- **No reconstruir / crítica:** No duplicar importadores ni montar otro servicio por ser un plugin.
- **Prueba de admisión pendiente:** Cargar/editar capa 3D de prueba y verificar persistencia en CityDB.
- **Evidencia y alcance:** Archivo candidato recuperado: [__init__.py](https://github.com/tudelft3d/3DCityDB-Tools-for-QGIS/blob/3f96cca2a9a3c6497a9e5977b59ce8e690d6fcbf/__init__.py); 43/43 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/tudelft3d/3DCityDB-Tools-for-QGIS), [documentación recuperada](https://github.com/tudelft3d/3DCityDB-Tools-for-QGIS/blob/master/README.md). Commit observado: `3f96cca2a9a3c6497a9e5977b59ce8e690d6fcbf`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-tudelft3d--3dfier"></a>

#### 133. tudelft3d/3dfier

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Reconstrucción 3D a partir de datos geográficos y elevación.
- **Puerta de integración propuesta:** Ejecutable C++ y configuración.
- **Construir nosotros, solo si falta:** Preparar expediente de datos y ejecutar reconstrucción con diagnóstico.
- **Con qué y por qué:** mantener algoritmo compilado como proceso aislado. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No presentar reconstrucción inferida como medición ni ocultar calidad de elevación.
- **Prueba de admisión pendiente:** Caso pequeño con fuentes y comparación de alturas/geometría.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/main.cpp](https://github.com/tudelft3d/3dfier/blob/9f7fece6bb2624095dc7e7059defa1a9dbd4276e/src/main.cpp); 420/1287 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/tudelft3d/3dfier), [documentación recuperada](https://github.com/tudelft3d/3dfier/blob/master/README.md), [3dfier.dockerfile](https://github.com/tudelft3d/3dfier/blob/master/3dfier.dockerfile). Commit observado: `9f7fece6bb2624095dc7e7059defa1a9dbd4276e`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-tudelft3d--city4cfd"></a>

#### 134. tudelft3d/City4CFD

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Preparación/reconstrucción de modelos para CFD.
- **Puerta de integración propuesta:** CLI y configuración de caso.
- **Construir nosotros, solo si falta:** Receta de preparación y comprobación del producto para un solver elegido.
- **Con qué y por qué:** conservar C++ y cadena de geometría. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No confundir geometría preparada con malla CFD validada o simulación ejecutada.
- **Prueba de admisión pendiente:** Geometría de referencia con superficies y requisitos del consumidor verificados.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/main.cpp](https://github.com/tudelft3d/City4CFD/blob/450cbae89a4b640b39b2bd8e328ed52ed8ab5881/src/main.cpp); 147/147 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/tudelft3d/City4CFD), [documentación recuperada](https://github.com/tudelft3d/City4CFD/blob/main/README.md), [CMakeLists.txt](https://github.com/tudelft3d/City4CFD/blob/main/CMakeLists.txt). Commit observado: `450cbae89a4b640b39b2bd8e328ed52ed8ab5881`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-vcityteam--ud-viz"></a>

#### 135. VCityTeam/UD-Viz

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Componentes web de visualización e interacción urbana 3D.
- **Puerta de integración propuesta:** API JavaScript/TypeScript.
- **Construir nosotros, solo si falta:** Host visual opcional y puente de selección/cámara a objetos de escenario.
- **Con qué y por qué:** usar componentes existentes y estado del navegador. JavaScript/TypeScript en el host del visor y un contrato de comandos/eventos de navegador. Un servidor MCP, si falta, usaría el SDK TypeScript y un puente explícito con esa sesión.
- **No reconstruir / crítica:** No reconstruir motor ni obligar todos los agentes a una UI concreta.
- **Prueba de admisión pendiente:** Selección de objeto con ID y escena recuperada tras recarga.
- **Evidencia y alcance:** Archivo candidato recuperado: [packages/visualizer/src/ClippingPlane.js](https://github.com/VCityTeam/UD-Viz/blob/87812dcac1444c132c1a425986279eb740875d45/packages/visualizer/src/ClippingPlane.js); 151/151 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/VCityTeam/UD-Viz), [documentación recuperada](https://github.com/VCityTeam/UD-Viz/blob/master/Readme.md), [package.json](https://github.com/VCityTeam/UD-Viz/blob/master/package.json). Commit observado: `87812dcac1444c132c1a425986279eb740875d45`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Morfología y estadística espacial

<a id="tool-benchmark-urbanism--cityseer-api"></a>

#### 136. benchmark-urbanism/cityseer-api

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Análisis de redes, centralidad y accesibilidad.
- **Puerta de integración propuesta:** API Python con extensión Rust.
- **Construir nosotros, solo si falta:** Operaciones tipadas sobre red versionada y vinculación de resultados a segmentos.
- **Con qué y por qué:** usar binding existente; no portar Rust ni sustituir algoritmo. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No convertir distancia de red o mezcla de usos en impacto causal.
- **Prueba de admisión pendiente:** Red pequeña con centralidad/distancias verificables y CRS métrico.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [pysrc/cityseer/metrics/networks.py](https://github.com/benchmark-urbanism/cityseer-api/blob/0e321c180dc311804bb28673e9dde248f233949b/pysrc/cityseer/metrics/networks.py); lectura parcial de 600/1239 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/benchmark-urbanism/cityseer-api), [documentación recuperada](https://github.com/benchmark-urbanism/cityseer-api/blob/master/README.md), [pyproject.toml](https://github.com/benchmark-urbanism/cityseer-api/blob/master/pyproject.toml). Commit observado: `0e321c180dc311804bb28673e9dde248f233949b`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-gboeing--osmnx"></a>

#### 137. gboeing/osmnx

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Descarga, construcción y análisis de grafos OSM.
- **Puerta de integración propuesta:** API Python; comparar MCP OSMnx existente.
- **Construir nosotros, solo si falta:** Preparación de red con filtros, fecha, cobertura y procedencia.
- **Con qué y por qué:** conservar OSMnx o adoptar su MCP si cubre operaciones. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No rehacer descarga/topología ni asumir OSM completo o apto para cada simulador.
- **Prueba de admisión pendiente:** Grafo de fixture con sentidos, proyección y atributos conservados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [osmnx/graph.py](https://github.com/gboeing/osmnx/blob/5f3b46f048f9f0a693702cea5f29f2eaad840204/osmnx/graph.py); lectura parcial de 600/863 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/gboeing/osmnx), [documentación recuperada](https://github.com/gboeing/osmnx/blob/main/README.md), [pyproject.toml](https://github.com/gboeing/osmnx/blob/main/pyproject.toml). Commit observado: `5f3b46f048f9f0a693702cea5f29f2eaad840204`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pysal--esda"></a>

#### 138. pysal/esda

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Estadística espacial exploratoria.
- **Puerta de integración propuesta:** API Python.
- **Construir nosotros, solo si falta:** Seleccionar estadísticos con pesos y permutaciones explícitos.
- **Con qué y por qué:** usar implementación PySAL y objetos de pesos originales. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No interpretar autocorrelación como causalidad ni ocultar elección de vecindad.
- **Prueba de admisión pendiente:** Datos sintéticos con pesos y semilla conocidos.
- **Evidencia y alcance:** Archivo candidato recuperado: [esda/__init__.py](https://github.com/pysal/esda/blob/7d4a8ba04e5c7bd02b7639838f364a21a9b106ff/esda/__init__.py); 49/49 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pysal/esda), [documentación recuperada](https://github.com/pysal/esda/blob/main/README.md), [environment.yml](https://github.com/pysal/esda/blob/main/environment.yml). Commit observado: `7d4a8ba04e5c7bd02b7639838f364a21a9b106ff`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pysal--inequality"></a>

#### 139. pysal/inequality

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Métricas de desigualdad.
- **Puerta de integración propuesta:** API Python.
- **Construir nosotros, solo si falta:** Indicadores definidos sobre población/área y ponderaciones declaradas.
- **Con qué y por qué:** conservar definición matemática y tratamiento de datos. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No confundir desigualdad agregada con desigualdad individual ni mezclar unidades.
- **Prueba de admisión pendiente:** Distribución pequeña con indicador calculable manualmente.
- **Evidencia y alcance:** Archivo candidato recuperado: [inequality/__init__.py](https://github.com/pysal/inequality/blob/77d802d6b85728e6fddb3f8871c2fa9ba72ae237/inequality/__init__.py); 39/39 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pysal/inequality), [documentación recuperada](https://github.com/pysal/inequality/blob/main/README.md), [pyproject.toml](https://github.com/pysal/inequality/blob/main/pyproject.toml). Commit observado: `77d802d6b85728e6fddb3f8871c2fa9ba72ae237`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pysal--libpysal"></a>

#### 140. pysal/libpysal

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Pesos y utilidades base de análisis espacial.
- **Puerta de integración propuesta:** API Python de pesos/estructuras.
- **Construir nosotros, solo si falta:** Normalización de identificadores y pesos dentro del paquete estadístico.
- **Con qué y por qué:** dependencia compartida; no publicar un MCP adicional. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No inventar vecindades ni perder alineación entre tabla y matriz de pesos.
- **Prueba de admisión pendiente:** Pesos pequeños con orden de IDs y conectividad comprobados.
- **Evidencia y alcance:** Archivo candidato recuperado: [libpysal/__init__.py](https://github.com/pysal/libpysal/blob/06834ad0b71c9f53dcae8c113f466275b0b2a9c4/libpysal/__init__.py); 30/30 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pysal/libpysal), [documentación recuperada](https://github.com/pysal/libpysal/blob/main/README.md), [environment.yml](https://github.com/pysal/libpysal/blob/main/environment.yml). Commit observado: `06834ad0b71c9f53dcae8c113f466275b0b2a9c4`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-pysal--mgwr"></a>

#### 141. pysal/mgwr

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Regresión geográficamente ponderada y multiescala.
- **Puerta de integración propuesta:** API Python de ajuste y selección de parámetros.
- **Construir nosotros, solo si falta:** Expediente de variables, escala, diagnósticos y resultados.
- **Con qué y por qué:** conservar modelo estadístico y sus selectores. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No presentar coeficientes locales como causalidad ni ignorar colinealidad/escala.
- **Prueba de admisión pendiente:** Dataset sintético con ajuste y diagnósticos reproducibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [mgwr/__init__.py](https://github.com/pysal/mgwr/blob/49d99aa2f2aa22707499fbf42986cdb9f86db5d8/mgwr/__init__.py); 10/10 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pysal/mgwr), [documentación recuperada](https://github.com/pysal/mgwr/blob/main/README.md), [pyproject.toml](https://github.com/pysal/mgwr/blob/main/pyproject.toml). Commit observado: `49d99aa2f2aa22707499fbf42986cdb9f86db5d8`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pysal--momepy"></a>

#### 142. pysal/momepy

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Morfometría urbana y análisis de formas/redes.
- **Puerta de integración propuesta:** API Python y datos geoespaciales nativos.
- **Construir nosotros, solo si falta:** Operaciones de morfología con identificadores, CRS y escala explícitos.
- **Con qué y por qué:** conservar métricas y objetos GeoPandas/PySAL. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No rehacer indicadores ni tratar resultados homónimos de versiones distintas como iguales.
- **Prueba de admisión pendiente:** Manzana sintética con áreas, relaciones y red conocidas.
- **Evidencia y alcance:** Archivo candidato recuperado: [momepy/__init__.py](https://github.com/pysal/momepy/blob/e720ac89cfe1f1f9a3cecc692abbcc455eebb327/momepy/__init__.py); 22/22 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pysal/momepy), [documentación recuperada](https://github.com/pysal/momepy/blob/main/README.md), [environment.yml](https://github.com/pysal/momepy/blob/main/environment.yml). Commit observado: `e720ac89cfe1f1f9a3cecc692abbcc455eebb327`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pysal--segregation"></a>

#### 143. pysal/segregation

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Medición y análisis de segregación.
- **Puerta de integración propuesta:** API Python.
- **Construir nosotros, solo si falta:** Seleccionar métricas y universo poblacional con procedencia y restricciones de datos.
- **Con qué y por qué:** preservar implementaciones y ponderaciones del paquete. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No producir inferencias individuales ni comparar métricas con universos incompatibles.
- **Prueba de admisión pendiente:** Ejemplo agregado con grupos y métrica calculables.
- **Evidencia y alcance:** Archivo candidato recuperado: [segregation/__init__.py](https://github.com/pysal/segregation/blob/9f9ce950549a0eeb98877804208feb95676fa66d/segregation/__init__.py); 23/23 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pysal/segregation), [documentación recuperada](https://github.com/pysal/segregation/blob/main/README.md), [environment.yml](https://github.com/pysal/segregation/blob/main/environment.yml). Commit observado: `9f9ce950549a0eeb98877804208feb95676fa66d`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pysal--spopt"></a>

#### 144. pysal/spopt

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Optimización espacial y regionalización.
- **Puerta de integración propuesta:** API Python y solvers configurados.
- **Construir nosotros, solo si falta:** Definir problema admitido, restricciones y devolución de soluciones/diagnósticos.
- **Con qué y por qué:** conservar formulación y solver; registrar versión y estado de optimalidad. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No llamar óptima una solución factible ni inventar objetivos del proyecto.
- **Prueba de admisión pendiente:** Instancia pequeña con óptimo conocido y caso infactible.
- **Evidencia y alcance:** Archivo candidato recuperado: [spopt/__init__.py](https://github.com/pysal/spopt/blob/aeea0e690ef68193d439a42a8ec6f84470bdfb8c/spopt/__init__.py); 7/7 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pysal/spopt), [documentación recuperada](https://github.com/pysal/spopt/blob/main/README.md), [environment.yml](https://github.com/pysal/spopt/blob/main/environment.yml). Commit observado: `aeea0e690ef68193d439a42a8ec6f84470bdfb8c`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pysal--spreg"></a>

#### 145. pysal/spreg

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Regresión espacial y sus diagnósticos.
- **Puerta de integración propuesta:** API Python.
- **Construir nosotros, solo si falta:** Operaciones de estimación con variables, pesos y supuestos registrados.
- **Con qué y por qué:** mantener estimadores originales. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No automatizar selección causal ni ocultar supuestos del modelo espacial.
- **Prueba de admisión pendiente:** Datos sintéticos con coeficientes y orden de observaciones fijados.
- **Evidencia y alcance:** Archivo candidato recuperado: [spreg/__init__.py](https://github.com/pysal/spreg/blob/13c4f29d0ff056523d2df55ddd1e0076f33134f4/spreg/__init__.py); 46/46 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/pysal/spreg), [documentación recuperada](https://github.com/pysal/spreg/blob/main/README.md), [environment.yml](https://github.com/pysal/spreg/blob/main/environment.yml). Commit observado: `13c4f29d0ff056523d2df55ddd1e0076f33134f4`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-spacegroupucl--depthmapx"></a>

#### 146. SpaceGroupUCL/depthmapX

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Análisis de sintaxis espacial y visibilidad.
- **Puerta de integración propuesta:** CLI o aplicación; verificar automatización de la versión.
- **Construir nosotros, solo si falta:** Preparar/redescubrir un flujo de análisis con entradas y métricas definidas.
- **Con qué y por qué:** conservar C++ y ejecutor existente; no traducir sus algoritmos. Aplicación/binario y bibliotecas de su distribución. Seleccionar CLI o binding solo después de probar qué operación funciona fuera del escritorio.
- **No reconstruir / crítica:** No sumar centralidades homónimas sin explicar diferencia frente a cityseer/OSMnx.
- **Prueba de admisión pendiente:** Plano/red pequeña con métrica contrastada en aplicación original.
- **Evidencia y alcance:** Archivo candidato recuperado: [GuiUnitTest/main.cpp](https://github.com/SpaceGroupUCL/depthmapX/blob/6ea9755efe30d51603b99b842898b62a2591b850/GuiUnitTest/main.cpp); 18/18 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/SpaceGroupUCL/depthmapX), [documentación recuperada](https://github.com/SpaceGroupUCL/depthmapX/blob/master/README.md), [CMakeLists.txt](https://github.com/SpaceGroupUCL/depthmapX/blob/master/CMakeLists.txt). Commit observado: `6ea9755efe30d51603b99b842898b62a2591b850`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.


### Familia: Movilidad y transporte

<a id="tool-a-b-street--abstreet"></a>

#### 147. a-b-street/abstreet

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Simulación y edición de escenarios de movilidad.
- **Puerta de integración propuesta:** Herramientas/formatos de A/B Street y ejecutores disponibles.
- **Construir nosotros, solo si falta:** Paquetes de escenario y consulta de métricas solo donde exista entrada automatizable.
- **Con qué y por qué:** conservar Rust y formatos; comprobar modo batch antes de ofrecer MCP. Aplicación/binario y bibliotecas de su distribución. Seleccionar CLI o binding solo después de probar qué operación funciona fuera del escritorio.
- **No reconstruir / crítica:** No tratar un simulador interactivo como servicio estable por defecto.
- **Prueba de admisión pendiente:** Escenario de ejemplo con demanda y semilla reproducibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [abstutil/src/cli.rs](https://github.com/a-b-street/abstreet/blob/0964f29315820c91b171b585eb51e300164e9197/abstutil/src/cli.rs); 64/64 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/a-b-street/abstreet), [documentación recuperada](https://github.com/a-b-street/abstreet/blob/main/README.md), [Cargo.toml](https://github.com/a-b-street/abstreet/blob/main/Cargo.toml). Commit observado: `0964f29315820c91b171b585eb51e300164e9197`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-activitysim--activitysim"></a>

#### 148. ActivitySim/activitysim

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelado de demanda de viajes basada en actividades.
- **Puerta de integración propuesta:** CLI, configuraciones y tablas ActivitySim.
- **Construir nosotros, solo si falta:** Corridas reproducibles con muestra, configuración y salidas identificables.
- **Con qué y por qué:** usar pipeline de ActivitySim, sin reescribir modelos de elección. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No simular demanda creíble sin encuestas, población y estimación compatibles.
- **Prueba de admisión pendiente:** Ejemplo oficial reducido con semilla y tablas contrastadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [activitysim/cli/__init__.py](https://github.com/ActivitySim/activitysim/blob/4916024bd75400e856d142f487d0b61af5768ead/activitysim/cli/__init__.py); 2/2 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ActivitySim/activitysim), [documentación recuperada](https://github.com/ActivitySim/activitysim/blob/main/README.md), [pyproject.toml](https://github.com/ActivitySim/activitysim/blob/main/pyproject.toml). Commit observado: `4916024bd75400e856d142f487d0b61af5768ead`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-activitysim--populationsim"></a>

#### 149. ActivitySim/populationsim

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Síntesis de población para modelos de demanda.
- **Puerta de integración propuesta:** CLI Python y tablas de controles.
- **Construir nosotros, solo si falta:** Validar controles y devolver población sintética con diagnóstico de ajuste.
- **Con qué y por qué:** conservar balanceo/síntesis original. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No presentar población sintética como padrón de personas reales.
- **Prueba de admisión pendiente:** Controles pequeños con totales y diagnóstico esperados.
- **Evidencia y alcance:** Archivo candidato recuperado: [populationsim/__main__.py](https://github.com/ActivitySim/populationsim/blob/64449c8a0c345d654a1f30fa4cd237abea67656f/populationsim/__main__.py); 40/40 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ActivitySim/populationsim), [documentación recuperada](https://github.com/ActivitySim/populationsim/blob/master/README.md), [pyproject.toml](https://github.com/ActivitySim/populationsim/blob/master/pyproject.toml). Commit observado: `64449c8a0c345d654a1f30fa4cd237abea67656f`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-aequilibrae--aequilibrae"></a>

#### 150. AequilibraE/aequilibrae

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Asignación y análisis de transporte sobre proyectos/redes.
- **Puerta de integración propuesta:** API Python y proyecto de datos.
- **Construir nosotros, solo si falta:** Operaciones de demanda/asignación con unidades, zonas y restricciones explícitas.
- **Con qué y por qué:** usar API y estructuras nativas, conservando librerías numéricas. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No generar OD o calibración de red automáticamente a partir de calles.
- **Prueba de admisión pendiente:** Red pequeña con matriz OD y flujos de referencia.
- **Evidencia y alcance:** Archivo candidato recuperado: [aequilibrae/utils/interface/__init__.py](https://github.com/AequilibraE/aequilibrae/blob/2fe3537715f9e5ae191112a98915cec620c707a5/aequilibrae/utils/interface/__init__.py); 0/0 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/AequilibraE/aequilibrae), [documentación recuperada](https://github.com/AequilibraE/aequilibrae/blob/develop/README.md), [pyproject.toml](https://github.com/AequilibraE/aequilibrae/blob/develop/pyproject.toml). Commit observado: `2fe3537715f9e5ae191112a98915cec620c707a5`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-conveyal--analysis-backend"></a>

#### 151. conveyal/analysis-backend

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Reserva de mantenimiento:** el repositorio figura archivado en el corte. No admitirlo como base nueva sin justificar dependencia, sucesor y mantenimiento.
- **Traer del original:** Servicio de análisis de accesibilidad y ejecución de tareas.
- **Puerta de integración propuesta:** API/arquitectura del backend y workers.
- **Construir nosotros, solo si falta:** Conector de proyectos/análisis con límites y estado de trabajos.
- **Con qué y por qué:** consumir servicio existente; no reemplazar cola y workers si ya resuelven el caso. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No asumir autorización multiusuario o despliegue listo por inspeccionar el repo.
- **Prueba de admisión pendiente:** Análisis pequeño con estado, artefacto y permisos por proyecto.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/main/java/com/conveyal/analysis/BackendMain.java](https://github.com/conveyal/analysis-backend/blob/d14d1a2375f1596d29d6706b40bb02bd15a07614/src/main/java/com/conveyal/analysis/BackendMain.java); lectura parcial de 175/175 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/conveyal/analysis-backend), [documentación recuperada](https://github.com/conveyal/analysis-backend/blob/dev/README.md), [pom.xml](https://github.com/conveyal/analysis-backend/blob/dev/pom.xml). Commit observado: `d14d1a2375f1596d29d6706b40bb02bd15a07614`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-conveyal--r5"></a>

#### 152. conveyal/r5

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Motor de enrutamiento/accesibilidad multimodal.
- **Puerta de integración propuesta:** Biblioteca Java y wrappers existentes.
- **Construir nosotros, solo si falta:** Preparación de red y consulta vía wrapper admitido, con fechas/horarios.
- **Con qué y por qué:** preferir r5py/r5r si cubren el flujo; no escribir otro binding sin motivo. JVM y CLI/biblioteca originales. El adaptador puede controlar el CLI como proceso o consumir un servicio existente; no hace falta portar el algoritmo a Go o Python.
- **No reconstruir / crítica:** No duplicar r5r/r5py ni comparar resultados con fechas GTFS distintas.
- **Prueba de admisión pendiente:** Red/GTFS de fixture con itinerario o matriz conocida.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/main/java/com/conveyal/r5/analyst/TravelTimeComputer.java](https://github.com/conveyal/r5/blob/f5c6414b61482d81fdd71ca665d10f0eaa5d86cd/src/main/java/com/conveyal/r5/analyst/TravelTimeComputer.java); lectura parcial de 446/446 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/conveyal/r5), [documentación recuperada](https://github.com/conveyal/r5/blob/dev/README.md), [Dockerfile](https://github.com/conveyal/r5/blob/dev/Dockerfile). Commit observado: `f5c6414b61482d81fdd71ca665d10f0eaa5d86cd`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-eclipse-sumo--sumo"></a>

#### 153. eclipse-sumo/sumo

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Simulación de tráfico, construcción de redes y TraCI/libsumo.
- **Puerta de integración propuesta:** TraCI, libsumo y CLI; comparar MCP SUMO existente.
- **Construir nosotros, solo si falta:** Escenarios tipados, ciclo de vida y resultados solo para brechas del MCP elegido.
- **Con qué y por qué:** TraCI/libsumo ya controlan el motor; mantener proceso aislado por simulación. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No reimplementar control ni optimización existente; red sin demanda no basta.
- **Prueba de admisión pendiente:** Red y demanda fijas, semilla, flujos y cierre de proceso comprobados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [tools/traci/main.py](https://github.com/eclipse-sumo/sumo/blob/9a562c33fc452272ccd1fe5790632ae4e5ba7dc3/tools/traci/main.py); lectura parcial de 292/292 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/eclipse-sumo/sumo), [documentación recuperada](https://github.com/eclipse-sumo/sumo/blob/main/README.md), [CMakeLists.txt](https://github.com/eclipse-sumo/sumo/blob/main/CMakeLists.txt). Commit observado: `9a562c33fc452272ccd1fe5790632ae4e5ba7dc3`. Licencia en el inventario: `EPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-giscience--openrouteservice"></a>

#### 154. GIScience/openrouteservice

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Servicio de rutas y análisis sobre red.
- **Puerta de integración propuesta:** API HTTP y perfiles del servidor.
- **Construir nosotros, solo si falta:** Consultas tipadas y registro de perfil/dataset/fecha utilizados.
- **Con qué y por qué:** conservar motor Java y solicitar operaciones por protocolo. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No instalarlo junto con OSRM/Valhalla por defecto ni asumir servicios públicos ilimitados.
- **Prueba de admisión pendiente:** Ruta conocida, perfil distinto y error de cobertura de red.
- **Evidencia y alcance:** Archivo candidato recuperado: [ors-api/src/main/java/org/heigit/ors/api/APIEnums.java](https://github.com/GIScience/openrouteservice/blob/1bd30615e7747ed54adc4b0224aa3b23c100c04e/ors-api/src/main/java/org/heigit/ors/api/APIEnums.java); 420/529 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/GIScience/openrouteservice), [documentación recuperada](https://github.com/GIScience/openrouteservice/blob/main/README.md), [Dockerfile](https://github.com/GIScience/openrouteservice/blob/main/Dockerfile). Commit observado: `1bd30615e7747ed54adc4b0224aa3b23c100c04e`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-ipea--accessibility"></a>

#### 155. ipea/accessibility

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Métricas de accesibilidad sobre matrices de viaje.
- **Puerta de integración propuesta:** API R.
- **Construir nosotros, solo si falta:** Definir oportunidades, umbrales y población para indicadores comparables.
- **Con qué y por qué:** preservar implementación y mantener matriz como entrada explícita. Rscript y paquetes R originales, con intercambio por JSON/tablas/archivos. Si hace falta un servidor MCP externo, una fachada Go puede administrar el proceso sin traducir el cálculo estadístico.
- **No reconstruir / crítica:** No confundir cálculo de indicador con generación de tiempos de viaje.
- **Prueba de admisión pendiente:** Matriz pequeña con accesibilidad acumulada verificable.
- **Evidencia y alcance:** Archivo candidato recuperado: [R/accessibility-package.R](https://github.com/ipea/accessibility/blob/f54fd4f1945c53c3aebed448420b2ef3d3643343/R/accessibility-package.R); 115/115 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ipea/accessibility), [documentación recuperada](https://github.com/ipea/accessibility/blob/main/README.md). Commit observado: `f54fd4f1945c53c3aebed448420b2ef3d3643343`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-ipea--r5r"></a>

#### 156. ipea/r5r

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Acceso R a motor R5 y análisis multimodal.
- **Puerta de integración propuesta:** API R y runtime Java.
- **Construir nosotros, solo si falta:** Escenarios de horarios, red y matriz con procedencia.
- **Con qué y por qué:** mantener wrapper existente y JVM compatible. Rscript y paquetes R originales, con intercambio por JSON/tablas/archivos. Si hace falta un servidor MCP externo, una fachada Go puede administrar el proceso sin traducir el cálculo estadístico.
- **No reconstruir / crítica:** No construir otro cliente Java si el usuario trabaja en R; no duplicar r5py en el mismo perfil.
- **Prueba de admisión pendiente:** GTFS/red de fixture con fecha y matriz contrastadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [java-r5rcore/src/org/ipea/r5r/JsonUtil.java](https://github.com/ipea/r5r/blob/1ca392e5eb9d3e9a98dbabc0702c1fe97bd926ec/java-r5rcore/src/org/ipea/r5r/JsonUtil.java); 15/15 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ipea/r5r), [documentación recuperada](https://github.com/ipea/r5r/blob/master/README.md), [Dockerfile](https://github.com/ipea/r5r/blob/master/Dockerfile). Commit observado: `1ca392e5eb9d3e9a98dbabc0702c1fe97bd926ec`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-matsim-org--matsim-libs"></a>

#### 157. matsim-org/matsim-libs

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Simulación de movilidad basada en agentes.
- **Puerta de integración propuesta:** Configuraciones, modelos y ejecutor Java MATSim.
- **Construir nosotros, solo si falta:** Recetas de escenarios admitidos, recursos y lectura de eventos/indicadores.
- **Con qué y por qué:** conservar configuraciones y motor; controlar corrida como trabajo externo. JVM y CLI/biblioteca originales. El adaptador puede controlar el CLI como proceso o consumir un servicio existente; no hace falta portar el algoritmo a Go o Python.
- **No reconstruir / crítica:** No generar planes de actividad calibrados desde una red OSM solamente.
- **Prueba de admisión pendiente:** Ejemplo de escenario con semilla, población y eventos comprobados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [matsim/src/main/java/org/matsim/core/controler/Controler.java](https://github.com/matsim-org/matsim-libs/blob/dbee7ca8edc3b9443b21dfe3047143f819fde70c/matsim/src/main/java/org/matsim/core/controler/Controler.java); lectura parcial de 554/554 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/matsim-org/matsim-libs), [documentación recuperada](https://github.com/matsim-org/matsim-libs/blob/main/README.md), [pom.xml](https://github.com/matsim-org/matsim-libs/blob/main/pom.xml). Commit observado: `dbee7ca8edc3b9443b21dfe3047143f819fde70c`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-mobilitydata--gtfs-validator"></a>

#### 158. MobilityData/gtfs-validator

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Validación de feeds GTFS.
- **Puerta de integración propuesta:** CLI/servicio y reportes del validador.
- **Construir nosotros, solo si falta:** Preflight de feeds y enlace de incidencias a tareas del proyecto.
- **Con qué y por qué:** usar CLI existente; no crear un validador GTFS propio. JVM y CLI/biblioteca originales. El adaptador puede controlar el CLI como proceso o consumir un servicio existente; no hace falta portar el algoritmo a Go o Python.
- **No reconstruir / crítica:** No interpretar feed válido como servicio vigente o cobertura adecuada.
- **Prueba de admisión pendiente:** Feed válido y feed con error conocido producen diagnóstico correcto.
- **Evidencia y alcance:** Archivo candidato recuperado: [web/client/src/app.d.ts](https://github.com/MobilityData/gtfs-validator/blob/c4c9e89a2b31aaa6603ae1be41968a8c3438aacb/web/client/src/app.d.ts); 5/5 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/MobilityData/gtfs-validator), [documentación recuperada](https://github.com/MobilityData/gtfs-validator/blob/master/README.md), [Dockerfile](https://github.com/MobilityData/gtfs-validator/blob/master/Dockerfile). Commit observado: `c4c9e89a2b31aaa6603ae1be41968a8c3438aacb`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-opentripplanner--opentripplanner"></a>

#### 159. opentripplanner/OpenTripPlanner

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Planificación multimodal de viajes.
- **Puerta de integración propuesta:** API de la versión instalada y construcción de grafo.
- **Construir nosotros, solo si falta:** Consultas de itinerario con fecha, zona horaria y cobertura explícitas.
- **Con qué y por qué:** conservar JVM/servidor; validar versión de API antes de tipar operaciones. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No sustituir operador de transporte ni inventar datos en tiempo real.
- **Prueba de admisión pendiente:** Viaje en red/GTFS de prueba y fuera de servicio.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [application/src/main/java/org/opentripplanner/standalone/OTPMain.java](https://github.com/opentripplanner/OpenTripPlanner/blob/9353c8caba506cfbdab1ac8be8cf9442df137ff4/application/src/main/java/org/opentripplanner/standalone/OTPMain.java); lectura parcial de 272/272 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/opentripplanner/OpenTripPlanner), [documentación recuperada](https://github.com/opentripplanner/OpenTripPlanner/blob/dev-2.x/README.md), [pom.xml](https://github.com/opentripplanner/OpenTripPlanner/blob/dev-2.x/pom.xml). Commit observado: `9353c8caba506cfbdab1ac8be8cf9442df137ff4`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-project-osrm--osrm-backend"></a>

#### 160. Project-OSRM/osrm-backend

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Motor y servicio de rutas sobre red vial.
- **Puerta de integración propuesta:** HTTP y herramientas de preparación de datos.
- **Construir nosotros, solo si falta:** Perfil de rutas/tablas con versión y cobertura de red identificadas.
- **Con qué y por qué:** cliente ligero sobre servicio C++ separado. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No construir routing ni sumar todos los motores de rutas al perfil base.
- **Prueba de admisión pendiente:** Ruta/tabla de fixture con perfil y distancias comprobados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/tools/routed.cpp](https://github.com/Project-OSRM/osrm-backend/blob/746c97c1c8ef7ebeb7acb9b986cf6c4e04f82caf/src/tools/routed.cpp); lectura parcial de 458/458 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/Project-OSRM/osrm-backend), [documentación recuperada](https://github.com/Project-OSRM/osrm-backend/blob/master/README.md), [CMakeLists.txt](https://github.com/Project-OSRM/osrm-backend/blob/master/CMakeLists.txt). Commit observado: `746c97c1c8ef7ebeb7acb9b986cf6c4e04f82caf`. Licencia en el inventario: `BSD-2-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-r5py--r5py"></a>

#### 161. r5py/r5py

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Wrapper Python de R5.
- **Puerta de integración propuesta:** API Python y JVM compatible.
- **Construir nosotros, solo si falta:** Consultas de accesibilidad/tiempos con red y horarios fijados.
- **Con qué y por qué:** reutilizar binding existente en vez de mantener Java puente propio. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No publicar otro R5 MCP si la fachada del wrapper ya cubre el caso.
- **Prueba de admisión pendiente:** Matriz pequeña con fecha, ventana y modo declarados.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/r5py/__main__.py](https://github.com/r5py/r5py/blob/59c97d0a65f9b0dfd9488d0084613c96e0d92c45/src/r5py/__main__.py); 3/3 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/r5py/r5py), [documentación recuperada](https://github.com/r5py/r5py/blob/main/README.md), [pyproject.toml](https://github.com/r5py/r5py/blob/main/pyproject.toml). Commit observado: `59c97d0a65f9b0dfd9488d0084613c96e0d92c45`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-ropensci--stplanr"></a>

#### 162. ropensci/stplanr

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Análisis y preparación de transporte sostenible en R.
- **Puerta de integración propuesta:** API R y servicios que cada función utilice.
- **Construir nosotros, solo si falta:** Operaciones seleccionadas sobre redes/líneas de deseo con proveedor explícito.
- **Con qué y por qué:** mantener algoritmos y conversiones existentes. Rscript y paquetes R originales, con intercambio por JSON/tablas/archivos. Si hace falta un servidor MCP externo, una fachada Go puede administrar el proceso sin traducir el cálculo estadístico.
- **No reconstruir / crítica:** No asumir que toda función es local ni duplicar servicios de rutas externos.
- **Prueba de admisión pendiente:** OD pequeña y asignación/ruta contrastada con dependencia identificada.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [R/route.R](https://github.com/ropensci/stplanr/blob/c7fd7f0a5c67b4ef448ed4d1275bdd8d97562d79/R/route.R); lectura parcial de 250/250 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/ropensci/stplanr), [documentación recuperada](https://github.com/ropensci/stplanr/blob/master/README.md). Commit observado: `c7fd7f0a5c67b4ef448ed4d1275bdd8d97562d79`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-udst--synthpop"></a>

#### 163. UDST/synthpop

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Síntesis de población del ecosistema UDST.
- **Puerta de integración propuesta:** API Python y tablas de controles.
- **Construir nosotros, solo si falta:** Receta si un modelo existente depende de esta implementación concreta.
- **Con qué y por qué:** conservar biblioteca solo con dependencias reproducibles. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No elegirla además de PopulationSim por inercia; revisar mantenimiento y compatibilidad.
- **Prueba de admisión pendiente:** Controles sintéticos con totales y error de ajuste conocidos.
- **Evidencia y alcance:** Archivo candidato recuperado: [synthpop/__init__.py](https://github.com/UDST/synthpop/blob/6fb13991c9d3ede2d8cf80512bd1102e37b98971/synthpop/__init__.py); 2/2 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/UDST/synthpop), [documentación recuperada](https://github.com/UDST/synthpop/blob/develop/README.rst), [requirements-dev.txt](https://github.com/UDST/synthpop/blob/develop/requirements-dev.txt). Commit observado: `6fb13991c9d3ede2d8cf80512bd1102e37b98971`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-valhalla--valhalla"></a>

#### 164. valhalla/valhalla

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Motor de rutas multimodales y perfiles de coste.
- **Puerta de integración propuesta:** API HTTP y herramientas de preparación.
- **Construir nosotros, solo si falta:** Consultas tipadas con perfil y datos de red versionados.
- **Con qué y por qué:** conservar proceso C++; adaptar protocolo existente. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No reconstruir coste/routing ni prometer restricciones no soportadas por el perfil.
- **Prueba de admisión pendiente:** Ruta/matriz con perfil, restricciones y cobertura comprobados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/worker.cc](https://github.com/valhalla/valhalla/blob/9dd1f92f3cd36962ebb7f30f16ea8a9cf6445076/src/worker.cc); lectura parcial de 600/1772 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/valhalla/valhalla), [documentación recuperada](https://github.com/valhalla/valhalla/blob/master/README.md), [CMakeLists.txt](https://github.com/valhalla/valhalla/blob/master/CMakeLists.txt). Commit observado: `9dd1f92f3cd36962ebb7f30f16ea8a9cf6445076`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.


### Familia: Observación terrestre y GeoAI

<a id="tool-azavea--raster-vision"></a>

#### 165. azavea/raster-vision

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Pipeline de aprendizaje y predicción sobre imágenes geoespaciales.
- **Puerta de integración propuesta:** Configuraciones y ejecutores Python.
- **Construir nosotros, solo si falta:** Recetas de modelos admitidos, datos, pesos y resultados por corrida.
- **Con qué y por qué:** conservar pipeline y runtimes de aprendizaje. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No incorporar entrenamiento genérico ni considerar libre un peso por ser abierto el código.
- **Prueba de admisión pendiente:** Predicción sobre imagen pequeña con pesos fijados y métricas de referencia.
- **Evidencia y alcance:** Archivo candidato recuperado: [rastervision_pipeline/rastervision/pipeline/__init__.py](https://github.com/azavea/raster-vision/blob/fed86fb97ba522431cb12b32c356530695587dbf/rastervision_pipeline/rastervision/pipeline/__init__.py); 41/41 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/azavea/raster-vision), [documentación recuperada](https://github.com/azavea/raster-vision/blob/master/README.md), [Dockerfile](https://github.com/azavea/raster-vision/blob/master/Dockerfile). Commit observado: `fed86fb97ba522431cb12b32c356530695587dbf`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-open-eo--openeo-processes"></a>

#### 166. Open-EO/openeo-processes

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Definiciones de procesos openEO.
- **Puerta de integración propuesta:** Esquemas y especificación de procesos.
- **Construir nosotros, solo si falta:** Validación de grafos frente al backend elegido.
- **Con qué y por qué:** el catálogo describe procesos; el backend es otra pieza. Reutilizar esquemas, formatos y validadores concretos; fijar sus versiones. No hay un motor científico que desplegar por el mero hecho de existir una especificación.
- **No reconstruir / crítica:** No anunciar definiciones JSON como motor ejecutable ni asumir cobertura total del backend.
- **Prueba de admisión pendiente:** Grafo válido y proceso no soportado detectados antes de envío.
- **Evidencia y alcance:** Archivo candidato recuperado: [dev/check-tests.js](https://github.com/Open-EO/openeo-processes/blob/98ae0148287b6a59beaa9b00a506fdd6f725c098/dev/check-tests.js); 68/68 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Open-EO/openeo-processes), [documentación recuperada](https://github.com/Open-EO/openeo-processes/blob/master/README.md). Commit observado: `98ae0148287b6a59beaa9b00a506fdd6f725c098`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-open-eo--openeo-python-client"></a>

#### 167. Open-EO/openeo-python-client

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Cliente de backends openEO.
- **Puerta de integración propuesta:** API Python y conexión al backend.
- **Construir nosotros, solo si falta:** Operaciones de consulta/envío/estado usando capacidades del servidor real.
- **Con qué y por qué:** conservar cliente, autenticación y manejo de trabajos existentes. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No reconstruir el backend ni otra cola si openEO ya da jobs; revisar cuotas y costes.
- **Prueba de admisión pendiente:** Job pequeño con estado, descarga y error del backend conservados.
- **Evidencia y alcance:** Archivo candidato recuperado: [openeo/api/__init__.py](https://github.com/Open-EO/openeo-python-client/blob/39d5f5492198f23cfb70dad6790df5b7cf4b575b/openeo/api/__init__.py); 3/3 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Open-EO/openeo-python-client), [documentación recuperada](https://github.com/Open-EO/openeo-python-client/blob/master/README.md), [pyproject.toml](https://github.com/Open-EO/openeo-python-client/blob/master/pyproject.toml). Commit observado: `39d5f5492198f23cfb70dad6790df5b7cf4b575b`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-opendatacube--datacube-core"></a>

#### 168. opendatacube/datacube-core

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Indexación y consulta de datos de observación terrestre.
- **Puerta de integración propuesta:** API/CLI Python y catálogo de productos.
- **Construir nosotros, solo si falta:** Consultas acotadas de cubos y resultados con producto/CRS/tiempo explícitos.
- **Con qué y por qué:** mantener índice y objetos xarray del ecosistema. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No crear otro catálogo ni cargar conjuntos gigantes al contexto de un agente.
- **Prueba de admisión pendiente:** Ventana pequeña con bandas, fechas y nodata conocidos.
- **Evidencia y alcance:** Archivo candidato recuperado: [datacube/api/__init__.py](https://github.com/opendatacube/datacube-core/blob/dc1e8bd485dafe5c779b84c250753e2f8350df8e/datacube/api/__init__.py); 18/18 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/opendatacube/datacube-core), [documentación recuperada](https://github.com/opendatacube/datacube-core/blob/develop/README.rst), [conda-environment.yml](https://github.com/opendatacube/datacube-core/blob/develop/conda-environment.yml). Commit observado: `dc1e8bd485dafe5c779b84c250753e2f8350df8e`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-opengeos--geoai"></a>

#### 169. opengeos/geoai

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Herramientas de GeoAI e interfaces de automatización existentes.
- **Puerta de integración propuesta:** API Python y componentes de agente/CLI del repositorio.
- **Construir nosotros, solo si falta:** Seleccionar funciones específicas y revisar interfaces ya existentes antes de envolverlas.
- **Con qué y por qué:** conservar implementaciones/modelos; no imponer agente del upstream. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No convertir un paquete amplio de IA en una sola herramienta irrestricta.
- **Prueba de admisión pendiente:** Función admitida con dataset/pesos fijados y resultado espacial contrastado.
- **Evidencia y alcance:** Archivo candidato recuperado: [agent-harness/cli_anything/geoai/__init__.py](https://github.com/opengeos/geoai/blob/0b13f11f685e77853546223e4ee8bfafbea86f17/agent-harness/cli_anything/geoai/__init__.py); 1/1 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/opengeos/geoai), [documentación recuperada](https://github.com/opengeos/geoai/blob/main/README.md), [Dockerfile](https://github.com/opengeos/geoai/blob/main/Dockerfile). Commit observado: `0b13f11f685e77853546223e4ee8bfafbea86f17`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-opengeos--segment-geospatial"></a>

#### 170. opengeos/segment-geospatial

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Segmentación geoespacial y utilidades de modelos.
- **Puerta de integración propuesta:** API Python y automatizaciones ya presentes.
- **Construir nosotros, solo si falta:** Operaciones de segmentación con prompts/parámetros, pesos y cobertura definidos.
- **Con qué y por qué:** conservar modelos y dependencias GPU en proceso de trabajo separado. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No tratar segmentación como objeto urbano validado ni ignorar licencia de pesos.
- **Prueba de admisión pendiente:** Imagen pequeña con máscara georreferenciada y error conocido.
- **Evidencia y alcance:** Archivo candidato recuperado: [agent-harness/cli_anything/samgeo/__init__.py](https://github.com/opengeos/segment-geospatial/blob/826718cac3781614ef5eccd9acf7d7b5dfd06089/agent-harness/cli_anything/samgeo/__init__.py); 3/3 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/opengeos/segment-geospatial), [documentación recuperada](https://github.com/opengeos/segment-geospatial/blob/main/README.md), [Dockerfile](https://github.com/opengeos/segment-geospatial/blob/main/Dockerfile). Commit observado: `826718cac3781614ef5eccd9acf7d7b5dfd06089`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-orfeotoolbox--otb"></a>

#### 171. orfeotoolbox/OTB

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Aplicaciones de procesamiento de imágenes OTB.
- **Puerta de integración propuesta:** CLI/aplicaciones y bindings disponibles.
- **Construir nosotros, solo si falta:** Descubrir aplicaciones admitidas, tipar parámetros y mantener resultados.
- **Con qué y por qué:** ejecutar herramientas nativas sin reimplementar algoritmos. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No publicar todas las aplicaciones a ciegas ni confundir sus requisitos ráster.
- **Prueba de admisión pendiente:** Aplicación pequeña con metadatos, bandas y valores esperados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [Modules/Core/Wrappers/CommandLine/src/otbWrapperCommandLineLauncher.cxx](https://github.com/orfeotoolbox/OTB/blob/6cec51ca777e1122600c8034d50a0d7c1adafabf/Modules/Core/Wrappers/CommandLine/src/otbWrapperCommandLineLauncher.cxx); lectura parcial de 600/972 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/orfeotoolbox/OTB), [documentación recuperada](https://github.com/orfeotoolbox/OTB/blob/develop/README.md), [CMakeLists.txt](https://github.com/orfeotoolbox/OTB/blob/develop/CMakeLists.txt). Commit observado: `6cec51ca777e1122600c8034d50a0d7c1adafabf`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-orfeotoolbox--pyotb"></a>

#### 172. orfeotoolbox/pyotb

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** API Python de aplicaciones OTB.
- **Puerta de integración propuesta:** Binding/API Python y OTB compatible.
- **Construir nosotros, solo si falta:** Construcción de pipelines dentro de un adaptador Python que lo requiera.
- **Con qué y por qué:** dependencia opcional del paquete OTB. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No mantener dos OTB incompatibles ni otro servidor equivalente al CLI.
- **Prueba de admisión pendiente:** Mismo pipeline por pyotb y CLI produce mismo resultado.
- **Evidencia y alcance:** Archivo candidato recuperado: [pyotb/__init__.py](https://github.com/orfeotoolbox/pyotb/blob/d7fec19cbc4e61fdb1356c7872faede9aeac8607/pyotb/__init__.py); 24/24 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/orfeotoolbox/pyotb), [documentación recuperada](https://github.com/orfeotoolbox/pyotb/blob/develop/README.md), [pyproject.toml](https://github.com/orfeotoolbox/pyotb/blob/develop/pyproject.toml). Commit observado: `d7fec19cbc4e61fdb1356c7872faede9aeac8607`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-sentinel-hub--sentinelhub-py"></a>

#### 173. sentinel-hub/sentinelhub-py

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Cliente de servicios Sentinel Hub.
- **Puerta de integración propuesta:** SDK y API del proveedor configurado.
- **Construir nosotros, solo si falta:** Solicitudes con colección, periodo, resolución y procedencia fijados.
- **Con qué y por qué:** aprovechar SDK; servicio y credenciales quedan externos. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** El SDK abierto no garantiza acceso gratuito ni derechos sobre todos los datos.
- **Prueba de admisión pendiente:** Consulta de prueba o fixture con bandas y metadatos conservados.
- **Evidencia y alcance:** Archivo candidato recuperado: [sentinelhub/api/__init__.py](https://github.com/sentinel-hub/sentinelhub-py/blob/b466167df34d7010ff228686d962820e81bbb13f/sentinelhub/api/__init__.py); 22/22 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/sentinel-hub/sentinelhub-py), [documentación recuperada](https://github.com/sentinel-hub/sentinelhub-py/blob/master/README.md), [pyproject.toml](https://github.com/sentinel-hub/sentinelhub-py/blob/master/pyproject.toml). Commit observado: `b466167df34d7010ff228686d962820e81bbb13f`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-stac-utils--pystac"></a>

#### 174. stac-utils/pystac

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Modelo y serialización de objetos STAC.
- **Puerta de integración propuesta:** API Python.
- **Construir nosotros, solo si falta:** Validar y producir metadatos de artefactos cuando adoptemos STAC.
- **Con qué y por qué:** biblioteca del conector/catálogo, sin endpoint independiente. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No confundir un objeto STAC con un archivo ráster disponible.
- **Prueba de admisión pendiente:** Item con assets, geometría, tiempos y referencias válidos.
- **Evidencia y alcance:** Archivo candidato recuperado: [core/pystac/client.py](https://github.com/stac-utils/pystac/blob/9ea0cd1188de0652434d602f3050ce06730227af/core/pystac/client.py); 23/23 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/stac-utils/pystac), [documentación recuperada](https://github.com/stac-utils/pystac/blob/main/README.md), [pyproject.toml](https://github.com/stac-utils/pystac/blob/main/pyproject.toml). Commit observado: `9ea0cd1188de0652434d602f3050ce06730227af`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-stac-utils--pystac-client"></a>

#### 175. stac-utils/pystac-client

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Consulta de catálogos STAC API.
- **Puerta de integración propuesta:** API Python y capacidades del servidor.
- **Construir nosotros, solo si falta:** Búsquedas acotadas por espacio/tiempo y resultados con enlaces verificables.
- **Con qué y por qué:** usar cliente y paginación existentes. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No asumir todas las extensiones STAC ni descargar automáticamente cada asset.
- **Prueba de admisión pendiente:** Catálogo de fixture con paginación y filtros comprobados.
- **Evidencia y alcance:** Archivo candidato recuperado: [pystac_client/cli.py](https://github.com/stac-utils/pystac-client/blob/077d93b575b89345cacbcd2e24a59ebd493f208e/pystac_client/cli.py); 420/445 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/stac-utils/pystac-client), [documentación recuperada](https://github.com/stac-utils/pystac-client/blob/main/README.md), [pyproject.toml](https://github.com/stac-utils/pystac-client/blob/main/pyproject.toml). Commit observado: `077d93b575b89345cacbcd2e24a59ebd493f208e`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-stac-utils--stac-fastapi"></a>

#### 176. stac-utils/stac-fastapi

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Componentes para publicar STAC API.
- **Puerta de integración propuesta:** Servicio y backend de almacenamiento elegido.
- **Construir nosotros, solo si falta:** Solo desplegar catálogo propio si hace falta publicar nuestros assets.
- **Con qué y por qué:** conservar framework/backends originales y cliente separado. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No instalar un servidor STAC cuando solo necesitamos consultar uno.
- **Prueba de admisión pendiente:** Item de prueba publicado, consultado y aislado por permisos cuando aplique.
- **Evidencia y alcance:** Archivo candidato recuperado: [stac_fastapi/api/stac_fastapi/api/__init__.py](https://github.com/stac-utils/stac-fastapi/blob/02b0a19a4da9383e7fda6a81332e8ca67099d797/stac_fastapi/api/stac_fastapi/api/__init__.py); 1/1 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/stac-utils/stac-fastapi), [documentación recuperada](https://github.com/stac-utils/stac-fastapi/blob/main/README.md), [Dockerfile](https://github.com/stac-utils/stac-fastapi/blob/main/Dockerfile). Commit observado: `02b0a19a4da9383e7fda6a81332e8ca67099d797`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-torchgeo--torchgeo"></a>

#### 177. torchgeo/torchgeo

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Datasets, modelos y utilidades de aprendizaje geoespacial.
- **Puerta de integración propuesta:** API Python/PyTorch.
- **Construir nosotros, solo si falta:** Recetas cerradas de entrenamiento/inferencia, datos y evaluación.
- **Con qué y por qué:** conservar PyTorch y ejecución en trabajador GPU/CPU apropiado. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No convertir un framework de investigación en predicciones urbanas validadas por defecto.
- **Prueba de admisión pendiente:** Modelo y dataset fijados, métrica y georreferencia comprobadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [torchgeo/models/__init__.py](https://github.com/torchgeo/torchgeo/blob/7d50a08d1c7b652040921122bf36916aa5d16425/torchgeo/models/__init__.py); 195/195 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/torchgeo/torchgeo), [documentación recuperada](https://github.com/torchgeo/torchgeo/blob/main/README.md), [package.json](https://github.com/torchgeo/torchgeo/blob/main/package.json). Commit observado: `7d50a08d1c7b652040921122bf36916aa5d16425`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Peatones y multitudes

<a id="tool-crowddynamics--crowddynamics"></a>

#### 178. crowddynamics/crowddynamics

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Simulación de multitudes de esa implementación.
- **Puerta de integración propuesta:** CLI/API Python y configuración.
- **Construir nosotros, solo si falta:** Envolver un escenario reproducible solo tras revisar dependencias y mantenimiento.
- **Con qué y por qué:** mantener modelo; separar ejecución numérica del MCP. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No extrapolar comportamientos humanos ni asumir mantenimiento actual.
- **Prueba de admisión pendiente:** Escenario sencillo con semilla, trayectorias y colisiones comprobadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [crowddynamics/cli.py](https://github.com/crowddynamics/crowddynamics/blob/a5858c02c06ed72f49b7bd6aaabd7cf16b3054c3/crowddynamics/cli.py); 92/92 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/crowddynamics/crowddynamics), [documentación recuperada](https://github.com/crowddynamics/crowddynamics/blob/master/README.md), [environment.yml](https://github.com/crowddynamics/crowddynamics/blob/master/environment.yml). Commit observado: `a5858c02c06ed72f49b7bd6aaabd7cf16b3054c3`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-mengecrowdsim--menge"></a>

#### 179. MengeCrowdSim/Menge

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Framework de simulación de multitudes.
- **Puerta de integración propuesta:** Ejecutable, configuración y plugins admitidos.
- **Construir nosotros, solo si falta:** Receta de escenario y consulta de trayectorias/indicadores.
- **Con qué y por qué:** controlar proceso C++ y formatos nativos. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No inventar comportamiento o calibración ni cargar plugins no revisados.
- **Prueba de admisión pendiente:** Escenario de ejemplo con población y recorridos reproducibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/include/macros.h](https://github.com/MengeCrowdSim/Menge/blob/00f97eaec7650069d4c62afc03b46f7fa8d4bc43/src/include/macros.h); 104/104 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/MengeCrowdSim/Menge), [documentación recuperada](https://github.com/MengeCrowdSim/Menge/blob/master/README.md). Commit observado: `00f97eaec7650069d4c62afc03b46f7fa8d4bc43`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-pedestriandynamics--jupedsim"></a>

#### 180. PedestrianDynamics/jupedsim

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Motor de simulación peatonal y bindings.
- **Puerta de integración propuesta:** API Python y geometrías/modelos admitidos.
- **Construir nosotros, solo si falta:** Operaciones de escenario, corrida y artefactos de trayectorias.
- **Con qué y por qué:** bindings existentes; un contexto aislado por simulación. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No asumir evacuación validada ni traducir geometría urbana sin verificar transitabilidad.
- **Prueba de admisión pendiente:** Geometría pequeña con agentes, destinos y recuentos conocidos.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [python_modules/jupedsim/jupedsim/simulation.py](https://github.com/PedestrianDynamics/jupedsim/blob/75fdf5f43cf6042a983fd210dfd52f085118dac8/python_modules/jupedsim/jupedsim/simulation.py); lectura parcial de 600/622 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/PedestrianDynamics/jupedsim), [documentación recuperada](https://github.com/PedestrianDynamics/jupedsim/blob/master/README.md), [CMakeLists.txt](https://github.com/PedestrianDynamics/jupedsim/blob/master/CMakeLists.txt). Commit observado: `75fdf5f43cf6042a983fd210dfd52f085118dac8`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-svenkreiss--socialforce"></a>

#### 181. svenkreiss/socialforce

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Implementación/modelos de fuerzas sociales.
- **Puerta de integración propuesta:** API Python y ejemplos de simulación/ajuste.
- **Construir nosotros, solo si falta:** Uso experimental con parámetros y datos de evaluación explícitos.
- **Con qué y por qué:** conservar modelo y dependencia numérica real de la versión. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No presentarlo como motor peatonal universal o evidencia de conducta real.
- **Prueba de admisión pendiente:** Ejemplo reproducido y sensibilidad a parámetros documentada.
- **Evidencia y alcance:** Archivo candidato recuperado: [socialforce/__init__.py](https://github.com/svenkreiss/socialforce/blob/8d1fba69667f949175dc8575857fb4780afedb9a/socialforce/__init__.py); 8/8 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/svenkreiss/socialforce), [documentación recuperada](https://github.com/svenkreiss/socialforce/blob/main/README.md), [setup.py](https://github.com/svenkreiss/socialforce/blob/main/setup.py). Commit observado: `8d1fba69667f949175dc8575857fb4780afedb9a`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Redes eléctricas y optimización energética

<a id="tool-dss-extensions--opendssdirect.py"></a>

#### 182. dss-extensions/OpenDSSDirect.py

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Acceso Python al motor DSS de su distribución.
- **Puerta de integración propuesta:** API Python y motor nativo asociado.
- **Construir nosotros, solo si falta:** Escenarios de red, flujo y lectura de resultados con configuración aislada.
- **Con qué y por qué:** usar binding mantenido, sin portar solver eléctrico. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No confundir compatibilidad entre variantes DSS ni inferir red física desde mapas.
- **Prueba de admisión pendiente:** Circuito conocido con tensiones/potencias contrastadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [opendssdirect/__init__.py](https://github.com/dss-extensions/OpenDSSDirect.py/blob/d654af2055564881f10c343c94e640d0cfa6da4b/opendssdirect/__init__.py); 68/68 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/dss-extensions/OpenDSSDirect.py), [documentación recuperada](https://github.com/dss-extensions/OpenDSSDirect.py/blob/master/README.md), [pyproject.toml](https://github.com/dss-extensions/OpenDSSDirect.py/blob/master/pyproject.toml). Commit observado: `d654af2055564881f10c343c94e640d0cfa6da4b`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-e2niee--pandapower"></a>

#### 183. e2nIEE/pandapower

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Modelado y cálculo de redes eléctricas.
- **Puerta de integración propuesta:** API Python y solvers admitidos.
- **Construir nosotros, solo si falta:** Operaciones tipadas de escenarios y diagnóstico de convergencia.
- **Con qué y por qué:** conservar estructura de red y métodos numéricos. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No generar una red calibrada de datos incompletos ni ocultar falta de convergencia.
- **Prueba de admisión pendiente:** Red de prueba con balance y caso no convergente.
- **Evidencia y alcance:** Archivo candidato recuperado: [pandapower/converter/cim/interfaces.py](https://github.com/e2nIEE/pandapower/blob/cbaf33b77a408de5899eea56ea15233975cffe5b/pandapower/converter/cim/interfaces.py); 68/68 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/e2nIEE/pandapower), [documentación recuperada](https://github.com/e2nIEE/pandapower/blob/develop/README.rst), [pyproject.toml](https://github.com/e2nIEE/pandapower/blob/develop/pyproject.toml). Commit observado: `cbaf33b77a408de5899eea56ea15233975cffe5b`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-natlabrockies--reopt_api"></a>

#### 184. NatLabRockies/REopt_API

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** API y flujos asociados a optimización REopt.
- **Puerta de integración propuesta:** Servicio/API y motor de optimización correspondiente.
- **Construir nosotros, solo si falta:** Solicitud de escenarios con tarifas, restricciones y supuestos versionados.
- **Con qué y por qué:** integrar API existente; verificar despliegue local y solver por separado. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No confundir servidor API con todo el solver ni prometer ahorro económico cierto.
- **Prueba de admisión pendiente:** Escenario pequeño con objetivo, restricciones y respuesta comprobables.
- **Evidencia y alcance:** Archivo candidato recuperado: [futurecosts/api.py](https://github.com/NatLabRockies/REopt_API/blob/bbe45b5ee92138bce3e61c348ab80288bcfad4ed/futurecosts/api.py); 118/118 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/NatLabRockies/REopt_API), [documentación recuperada](https://github.com/NatLabRockies/REopt_API/blob/master/README.md), [Dockerfile](https://github.com/NatLabRockies/REopt_API/blob/master/Dockerfile). Commit observado: `bbe45b5ee92138bce3e61c348ab80288bcfad4ed`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-oemof--oemof-solph"></a>

#### 185. oemof/oemof-solph

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Modelado y optimización de sistemas energéticos.
- **Puerta de integración propuesta:** API Python y solver configurado.
- **Construir nosotros, solo si falta:** Formulaciones admitidas, ejecución y explicación del estado de solución.
- **Con qué y por qué:** mantener modelo y solucionador; no reescribir optimización. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No atribuir óptimo sin verificar estado, brecha y restricciones.
- **Prueba de admisión pendiente:** Sistema pequeño con solución conocida e instancia infactible.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/oemof/solph/processing.py](https://github.com/oemof/oemof-solph/blob/3846e3e46a003f2036710af464de556621047ac4/src/oemof/solph/processing.py); 420/1024 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/oemof/oemof-solph), [documentación recuperada](https://github.com/oemof/oemof-solph/blob/dev/README.rst), [pyproject.toml](https://github.com/oemof/oemof-solph/blob/dev/pyproject.toml). Commit observado: `3846e3e46a003f2036710af464de556621047ac4`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-pypsa--pypsa"></a>

#### 186. PyPSA/PyPSA

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Análisis y optimización de redes/sistemas energéticos.
- **Puerta de integración propuesta:** API Python y backend de optimización admitido.
- **Construir nosotros, solo si falta:** Escenarios con horizonte, resolución, restricciones y costes explícitos.
- **Con qué y por qué:** conservar modelo y estructuras temporales nativas. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No mezclar series o unidades ni presentar plan óptimo como decisión aprobada.
- **Prueba de admisión pendiente:** Red pequeña con balance temporal y objetivo contrastados.
- **Evidencia y alcance:** Archivo candidato recuperado: [pypsa/__init__.py](https://github.com/PyPSA/PyPSA/blob/aecef6ed32e512f31246eeaaad4c3b50e8930554/pypsa/__init__.py); 112/112 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/PyPSA/PyPSA), [documentación recuperada](https://github.com/PyPSA/PyPSA/blob/master/README.md), [pyproject.toml](https://github.com/PyPSA/PyPSA/blob/master/pyproject.toml). Commit observado: `aecef6ed32e512f31246eeaaad4c3b50e8930554`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-rwth-ebc--uesgraphs"></a>

#### 187. RWTH-EBC/uesgraphs

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Representación/generación de redes energéticas urbanas.
- **Puerta de integración propuesta:** API Python y exportaciones del paquete.
- **Construir nosotros, solo si falta:** Mapeo de topología y vínculo con simulador/optimizador elegido.
- **Con qué y por qué:** dependencia del flujo de redes; mantener exportador nativo. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No confundir un grafo con dimensionamiento o simulación ya ejecutados.
- **Prueba de admisión pendiente:** Grafo pequeño exportado sin perder conectividad y unidades.
- **Evidencia y alcance:** Archivo candidato recuperado: [uesgraphs/systemmodels/model_generation_pipeline.py](https://github.com/RWTH-EBC/uesgraphs/blob/b4a3e2fca9e04f32c92ac4e26f3a3531d4d7c0b6/uesgraphs/systemmodels/model_generation_pipeline.py); 420/1615 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/RWTH-EBC/uesgraphs), [documentación recuperada](https://github.com/RWTH-EBC/uesgraphs/blob/master/README.md), [pyproject.toml](https://github.com/RWTH-EBC/uesgraphs/blob/master/pyproject.toml). Commit observado: `b4a3e2fca9e04f32c92ac4e26f3a3531d4d7c0b6`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Riesgo y resiliencia

<a id="tool-climada-project--climada_petals"></a>

#### 188. CLIMADA-project/climada_petals

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Extensiones y modelos de peligro/impacto CLIMADA.
- **Puerta de integración propuesta:** API Python y módulos concretos.
- **Construir nosotros, solo si falta:** Receta del módulo realmente requerido y datos que necesita.
- **Con qué y por qué:** complemento del paquete CLIMADA con compatibilidad fijada. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No instalar todos los peligros ni atribuir validación a la familia completa.
- **Prueba de admisión pendiente:** Ejemplo de un módulo con entradas/resultados reproducibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [climada_petals/__init__.py](https://github.com/CLIMADA-project/climada_petals/blob/dcfcfeb12fef21b400453b305a203c98b116ee0d/climada_petals/__init__.py); 68/68 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CLIMADA-project/climada_petals), [documentación recuperada](https://github.com/CLIMADA-project/climada_petals/blob/main/README.md), [pyproject.toml](https://github.com/CLIMADA-project/climada_petals/blob/main/pyproject.toml). Commit observado: `dcfcfeb12fef21b400453b305a203c98b116ee0d`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-climada-project--climada_python"></a>

#### 189. CLIMADA-project/climada_python

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Cálculo de impactos/riesgo con peligro, exposición y vulnerabilidad.
- **Puerta de integración propuesta:** API Python y fuentes de datos del caso.
- **Construir nosotros, solo si falta:** Escenario de riesgo con los tres componentes trazables y resultados delimitados.
- **Con qué y por qué:** conservar modelo y tratamiento de eventos. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No producir pérdidas reales desde geometría sola ni omitir incertidumbre/vulnerabilidad.
- **Prueba de admisión pendiente:** Ejemplo pequeño con peligro y exposición fijados y cálculo contrastado.
- **Evidencia y alcance:** Archivo candidato recuperado: [climada/__init__.py](https://github.com/CLIMADA-project/climada_python/blob/cc0b21516a156384f718e328c59b60138dc1775c/climada/__init__.py); 120/120 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CLIMADA-project/climada_python), [documentación recuperada](https://github.com/CLIMADA-project/climada_python/blob/main/README.md), [pyproject.toml](https://github.com/CLIMADA-project/climada_python/blob/main/pyproject.toml). Commit observado: `cc0b21516a156384f718e328c59b60138dc1775c`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-gem--oq-engine"></a>

#### 190. gem/oq-engine

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Motor OpenQuake de peligro y riesgo sísmico.
- **Puerta de integración propuesta:** CLI/API del engine y archivos de configuración.
- **Construir nosotros, solo si falta:** Enviar/consultar trabajos existentes y registrar modelos, exposición y resultados.
- **Con qué y por qué:** reutilizar engine y sistema de trabajos; no crear otra cola innecesaria. API/cliente Python o HTTP nativo existente, con el servicio original como dueño de trabajos y estado. El nuevo código se limita al contrato de integración que falte.
- **No reconstruir / crítica:** No confundir mapa de peligro con pérdida urbana ni elegir modelos sin justificación.
- **Prueba de admisión pendiente:** Caso oficial con configuración, estado y resultados de referencia.
- **Evidencia y alcance:** Archivo candidato recuperado: [openquake/engine/__init__.py](https://github.com/gem/oq-engine/blob/205ba5f0fb1df88a283b142556218c62a50fbd2b/openquake/engine/__init__.py); 56/56 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/gem/oq-engine), [documentación recuperada](https://github.com/gem/oq-engine/blob/master/README.md), [pyproject.toml](https://github.com/gem/oq-engine/blob/master/pyproject.toml). Commit observado: `205ba5f0fb1df88a283b142556218c62a50fbd2b`. Licencia en el inventario: `AGPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Ruido ambiental

<a id="tool-universite-gustave-eiffel--noisemodelling"></a>

#### 191. Universite-Gustave-Eiffel/NoiseModelling

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Cálculo de propagación y mapas de ruido.
- **Puerta de integración propuesta:** Scripts/CLI Java y datos de emisión/escena.
- **Construir nosotros, solo si falta:** Paquetes de corrida con fuentes, meteorología y geometrías declaradas.
- **Con qué y por qué:** conservar librerías y ejecución NoiseModelling. JVM y CLI/biblioteca originales. El adaptador puede controlar el CLI como proceso o consumir un servicio existente; no hace falta portar el algoritmo a Go o Python.
- **No reconstruir / crítica:** No deducir emisión acústica solo de calles ni etiquetar resultado como medición.
- **Prueba de admisión pendiente:** Caso acústico conocido con receptores y niveles contrastados.
- **Evidencia y alcance:** Archivo candidato recuperado: [noisemodelling-scripts/src/main/java/org/noise_planet/noisemodelling/VersionUtils.java](https://github.com/Universite-Gustave-Eiffel/NoiseModelling/blob/62d60599061ce101f943c383581d057225f3d742/noisemodelling-scripts/src/main/java/org/noise_planet/noisemodelling/VersionUtils.java); 77/77 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/Universite-Gustave-Eiffel/NoiseModelling), [documentación recuperada](https://github.com/Universite-Gustave-Eiffel/NoiseModelling/blob/main/README.md), [Dockerfile](https://github.com/Universite-Gustave-Eiffel/NoiseModelling/blob/main/Dockerfile). Commit observado: `62d60599061ce101f943c383581d057225f3d742`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: SIG y geoprocesamiento

<a id="tool-duckdb--duckdb-spatial"></a>

#### 192. duckdb/duckdb-spatial

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Extensión espacial y consultas analíticas DuckDB.
- **Puerta de integración propuesta:** SQL y drivers de la extensión instalada.
- **Construir nosotros, solo si falta:** Consultas de dominio limitadas, catálogos de archivos y resultados por referencia.
- **Con qué y por qué:** usar cliente DuckDB y extensión exacta; evitar servidor nuevo por cada consulta. SQL y funciones originales tras una API de aplicación con rol acotado. Si falta la fachada MCP, implementarla con un cliente PostgreSQL/DuckDB tipado; no ofrecer SQL libre al agente.
- **No reconstruir / crítica:** No reconstruir funciones espaciales ni dar SQL/lectura de archivos irrestrictos al agente.
- **Prueba de admisión pendiente:** Consulta espacial sobre fixture con CRS y filas esperadas.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/spatial/modules/main/spatial_functions_aggregate.cpp](https://github.com/duckdb/duckdb-spatial/blob/d332807f4ffdcc4da0092fe760ef48266f548941/src/spatial/modules/main/spatial_functions_aggregate.cpp); 168/168 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/duckdb/duckdb-spatial), [documentación recuperada](https://github.com/duckdb/duckdb-spatial/blob/v2.0-cyanoptera/README.md), [CMakeLists.txt](https://github.com/duckdb/duckdb-spatial/blob/v2.0-cyanoptera/CMakeLists.txt). Commit observado: `d332807f4ffdcc4da0092fe760ef48266f548941`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-geopandas--geopandas"></a>

#### 193. geopandas/geopandas

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Tablas vectoriales y operaciones geoespaciales.
- **Puerta de integración propuesta:** API Python GeoDataFrame.
- **Construir nosotros, solo si falta:** Operaciones de tabla seleccionadas y contratos de CRS, columnas e identidad.
- **Con qué y por qué:** integración directa; comparte dependencias con paquetes de análisis. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No crear otra base GIS ni duplicar cada función de GDAL/QGIS.
- **Prueba de admisión pendiente:** Join/overlay pequeño con IDs, CRS y recuentos comprobados.
- **Evidencia y alcance:** Archivo candidato recuperado: [geopandas/tools/clip.py](https://github.com/geopandas/geopandas/blob/ead9a4fe380b3e5cb189fca03328af4e1db5fa33/geopandas/tools/clip.py); 268/268 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/geopandas/geopandas), [documentación recuperada](https://github.com/geopandas/geopandas/blob/main/README.md), [environment-dev.yml](https://github.com/geopandas/geopandas/blob/main/environment-dev.yml). Commit observado: `ead9a4fe380b3e5cb189fca03328af4e1db5fa33`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-geotools--geotools"></a>

#### 194. geotools/geotools

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Bibliotecas GIS del ecosistema Java.
- **Puerta de integración propuesta:** APIs Java y módulos requeridos.
- **Construir nosotros, solo si falta:** Usarlas solo dentro de un conector Java que ya las necesite.
- **Con qué y por qué:** dependencia de servicios como GeoServer; no trasladarla a Go/Python. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No publicar otro servidor GIS equivalente por existir una biblioteca amplia.
- **Prueba de admisión pendiente:** Lectura/transformación con módulos y CRS fijados.
- **Evidencia y alcance:** Archivo candidato recuperado: [modules/ogc/net.opengis.wmts/src/net/opengis/gml311/EngineeringCRSRefType.java](https://github.com/geotools/geotools/blob/f447d91381b9ba8b48dadd2b5b4a415a9aaf63b8/modules/ogc/net.opengis.wmts/src/net/opengis/gml311/EngineeringCRSRefType.java); 373/373 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/geotools/geotools), [documentación recuperada](https://github.com/geotools/geotools/blob/main/README.md), [pom.xml](https://github.com/geotools/geotools/blob/main/pom.xml). Commit observado: `f447d91381b9ba8b48dadd2b5b4a415a9aaf63b8`. Licencia en el inventario: `LGPL-2.1` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-jblindsay--whitebox-tools"></a>

#### 195. jblindsay/whitebox-tools

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Herramientas de terreno y análisis geoespacial.
- **Puerta de integración propuesta:** CLI y catálogo de herramientas del binario admitido.
- **Construir nosotros, solo si falta:** Operaciones seleccionadas de terreno con parámetros y artefactos trazables.
- **Con qué y por qué:** controlar binario Rust original y salida de cada comando. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No asumir que todas las extensiones/binarios tienen iguales condiciones de distribución.
- **Prueba de admisión pendiente:** DEM sintético con flujo o relieve esperado y nodata comprobado.
- **Evidencia y alcance:** Archivo candidato recuperado: [whitebox-runner/src/main.rs](https://github.com/jblindsay/whitebox-tools/blob/3d7c73cf562b6c58d2649c37f570e3e9a90322f2/whitebox-runner/src/main.rs); 420/965 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/jblindsay/whitebox-tools), [documentación recuperada](https://github.com/jblindsay/whitebox-tools/blob/master/README.md), [Cargo.toml](https://github.com/jblindsay/whitebox-tools/blob/master/Cargo.toml). Commit observado: `3d7c73cf562b6c58d2649c37f570e3e9a90322f2`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-locationtech--jts"></a>

#### 196. locationtech/jts

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Topología y geometría planar en Java.
- **Puerta de integración propuesta:** API Java JTS.
- **Construir nosotros, solo si falta:** Dependencia geométrica de un conector Java, cuando corresponda.
- **Con qué y por qué:** conservar biblioteca en el runtime del consumidor. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No añadir otro MCP de geometría además de GEOS/Shapely sin diferencia requerida.
- **Prueba de admisión pendiente:** Geometría pequeña con predicados y precisión declarados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [modules/core/src/main/java/org/locationtech/jts/geom/Geometry.java](https://github.com/locationtech/jts/blob/3460207216f3091cd7f72d48d6ddd1b561b2b8fd/modules/core/src/main/java/org/locationtech/jts/geom/Geometry.java); lectura parcial de 600/1839 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/locationtech/jts), [documentación recuperada](https://github.com/locationtech/jts/blob/master/README.md), [pom.xml](https://github.com/locationtech/jts/blob/master/pom.xml). Commit observado: `3460207216f3091cd7f72d48d6ddd1b561b2b8fd`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-opengeos--whitebox-python"></a>

#### 197. opengeos/whitebox-python

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Wrapper Python de WhiteboxTools.
- **Puerta de integración propuesta:** API Python y binario Whitebox compatible.
- **Construir nosotros, solo si falta:** Utilizarlo dentro de un adaptador Python si reduce el puente requerido.
- **Con qué y por qué:** conservar wrapper, no duplicar API del CLI en otro servicio. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No contar wrapper y binario como dos motores independientes.
- **Prueba de admisión pendiente:** Mismo DEM y parámetros por wrapper/CLI dan misma salida.
- **Evidencia y alcance:** Archivo candidato recuperado: [whitebox/cli.py](https://github.com/opengeos/whitebox-python/blob/1fcd8d2ca5c454b828e4ff2f05fea16a2432baed/whitebox/cli.py); 17/17 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/opengeos/whitebox-python), [documentación recuperada](https://github.com/opengeos/whitebox-python/blob/master/README.rst), [requirements_dev.txt](https://github.com/opengeos/whitebox-python/blob/master/requirements_dev.txt). Commit observado: `1fcd8d2ca5c454b828e4ff2f05fea16a2432baed`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-osgeo--gdal"></a>

#### 198. OSGeo/gdal

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Drivers y herramientas de transformación ráster/vector.
- **Puerta de integración propuesta:** CLI, API y bindings; comparar GDAL MCP existente.
- **Construir nosotros, solo si falta:** Receta de drivers/versiones y operaciones no cubiertas por MCP reutilizable.
- **Con qué y por qué:** usar CLI o binding admitido según operación; no reescribir C++. Aplicación/binario y bibliotecas de su distribución. Seleccionar CLI o binding solo después de probar qué operación funciona fuera del escritorio.
- **No reconstruir / crítica:** No inventar transformaciones ni exponer todos los drivers/accesos externos sin límites.
- **Prueba de admisión pendiente:** Raster/vector pequeño con CRS, nodata y atributos preservados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [apps/gdalinfo_bin.cpp](https://github.com/OSGeo/gdal/blob/8b3b63fb300935c55f546c0e24e4398cc21db71c/apps/gdalinfo_bin.cpp); lectura parcial de 244/244 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/OSGeo/gdal), [documentación recuperada](https://github.com/OSGeo/gdal/blob/master/README.md), [CMakeLists.txt](https://github.com/OSGeo/gdal/blob/master/CMakeLists.txt). Commit observado: `8b3b63fb300935c55f546c0e24e4398cc21db71c`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-osgeo--grass"></a>

#### 199. OSGeo/grass

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Motor GIS y módulos de GRASS.
- **Puerta de integración propuesta:** Sesión/mapset, CLI y API Python.
- **Construir nosotros, solo si falta:** Operaciones de módulos seleccionados con mapsets aislados y procedencia.
- **Con qué y por qué:** conservar gestión de sesión/mapset y módulos nativos. Python para preparar parámetros y llamar el ejecutor/API original con argumentos estructurados. Se conserva la estructura de configuración y archivos upstream.
- **No reconstruir / crítica:** No depender del grass-mcp anunciado sin código ni mezclar mapsets entre proyectos.
- **Prueba de admisión pendiente:** Módulo sobre fixture con región, resolución y mapset comprobados.
- **Evidencia y alcance:** Archivo candidato recuperado: [python/grass/pygrass/modules/interface/__init__.py](https://github.com/OSGeo/grass/blob/e228271fcaba86bd984e3ca71cd3b4507b3c8e2c/python/grass/pygrass/modules/interface/__init__.py); 23/23 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/OSGeo/grass), [documentación recuperada](https://github.com/OSGeo/grass/blob/main/README.md), [CMakeLists.txt](https://github.com/OSGeo/grass/blob/main/CMakeLists.txt). Commit observado: `e228271fcaba86bd984e3ca71cd3b4507b3c8e2c`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-osgeo--proj"></a>

#### 200. OSGeo/PROJ

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Transformaciones de coordenadas y bases geodésicas.
- **Puerta de integración propuesta:** Biblioteca/CLI y bindings ya usados por GIS.
- **Construir nosotros, solo si falta:** Registro de operación, rejillas y precisión dentro de otros conectores.
- **Con qué y por qué:** dependencia del stack GIS; no otro motor MCP independiente. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No aceptar solo un EPSG como garantía de datum/época/transformación adecuada.
- **Prueba de admisión pendiente:** Puntos de control con transformación y rejilla declaradas.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/apps/cct.cpp](https://github.com/OSGeo/PROJ/blob/be0df1e07a3ce21f3aafc29607b0a3295f588137/src/apps/cct.cpp); lectura parcial de 600/610 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/OSGeo/PROJ), [documentación recuperada](https://github.com/OSGeo/PROJ/blob/master/README.md), [CMakeLists.txt](https://github.com/OSGeo/PROJ/blob/master/CMakeLists.txt). Commit observado: `be0df1e07a3ce21f3aafc29607b0a3295f588137`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-postgis--postgis"></a>

#### 201. postgis/postgis

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Funciones espaciales y almacenamiento sobre PostgreSQL.
- **Puerta de integración propuesta:** SQL mediante API de aplicación y rol acotado.
- **Construir nosotros, solo si falta:** Consultas de dominio, selecciones persistentes y artefactos con permisos por proyecto.
- **Con qué y por qué:** mantener PostGIS como motor; el agente llama operaciones tipadas, no SQL libre. SQL y funciones originales tras una API de aplicación con rol acotado. Si falta la fachada MCP, implementarla con un cliente PostgreSQL/DuckDB tipado; no ofrecer SQL libre al agente.
- **No reconstruir / crítica:** No construir otra base espacial ni copiar bases de productos existentes.
- **Prueba de admisión pendiente:** Consulta conocida, CRS y aislamiento de datos entre proyectos.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [postgis/postgis.sql.in](https://github.com/postgis/postgis/blob/e55a99babec9ebca6048974840cc5fce979ef14c/postgis/postgis.sql.in); lectura parcial de 600/7297 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/postgis/postgis), [documentación recuperada](https://github.com/postgis/postgis/blob/master/README.md). Commit observado: `e55a99babec9ebca6048974840cc5fce979ef14c`. Licencia en el inventario: `GPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-qgis--qgis"></a>

#### 202. qgis/QGIS

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Aplicación GIS, proveedores y Processing.
- **Puerta de integración propuesta:** qgis_process/PyQGIS y plugin; comparar MCP QGIS existentes.
- **Construir nosotros, solo si falta:** Receta de distribución/proveedores y pruebas de operaciones elegidas.
- **Con qué y por qué:** API Python y CLI de QGIS; conservar puente MCP seleccionado. Plugin o componente en el runtime de la aplicación anfitriona y un puente tipado externo cuando se requiera MCP. Debe respetar el hilo de interfaz, documento y sesión de la aplicación.
- **No reconstruir / crítica:** No reconstruir GIS ni mezclar automatización headless con control de sesión gráfica.
- **Prueba de admisión pendiente:** Mismo algoritmo/proveedor sobre fixture da misma capa y metadatos.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/process/qgsprocess.cpp](https://github.com/qgis/QGIS/blob/bdf869bd700fbd6b47fa71855d301a3701881ab6/src/process/qgsprocess.cpp); lectura parcial de 600/1439 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/qgis/QGIS), [documentación recuperada](https://github.com/qgis/QGIS/blob/master/README.md), [CMakeLists.txt](https://github.com/qgis/QGIS/blob/master/CMakeLists.txt). Commit observado: `bdf869bd700fbd6b47fa71855d301a3701881ab6`. Licencia en el inventario: `GPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-r-spatial--sf"></a>

#### 203. r-spatial/sf

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Datos vectoriales y operaciones espaciales en R.
- **Puerta de integración propuesta:** API R y bibliotecas nativas de sf.
- **Construir nosotros, solo si falta:** Operaciones cuando un flujo R las requiera, con CRS/IDs explícitos.
- **Con qué y por qué:** mantener sf; no traducir algoritmos ni crear copia universal en Python. Rscript y paquetes R originales, con intercambio por JSON/tablas/archivos. Si hace falta un servidor MCP externo, una fachada Go puede administrar el proceso sin traducir el cálculo estadístico.
- **No reconstruir / crítica:** No asumir igualdad entre motores o semántica esférica/planar.
- **Prueba de admisión pendiente:** Overlay pequeño con motor geométrico y CRS declarados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [R/read.R](https://github.com/r-spatial/sf/blob/f93e9c6f003ec195d6e534868033dce20c2e7ace/R/read.R); lectura parcial de 600/832 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/r-spatial/sf), [documentación recuperada](https://github.com/r-spatial/sf/blob/main/README.md). Commit observado: `f93e9c6f003ec195d6e534868033dce20c2e7ace`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-rasterio--rasterio"></a>

#### 204. rasterio/rasterio

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Lectura/escritura y ventanas de datos ráster.
- **Puerta de integración propuesta:** API Python basada en GDAL.
- **Construir nosotros, solo si falta:** Operaciones por ventanas y referencias a artefactos georreferenciados.
- **Con qué y por qué:** conservar bindings y drivers compatibles. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No duplicar GDAL ni cargar rásters completos al contexto del agente.
- **Prueba de admisión pendiente:** Ventana de raster con transform, nodata y valores conocidos.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [rasterio/rio/main.py](https://github.com/rasterio/rasterio/blob/124e23f4060678460f39a0d838ac8c83b6fe2fe7/rasterio/rio/main.py); lectura parcial de 118/118 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/rasterio/rasterio), [documentación recuperada](https://github.com/rasterio/rasterio/blob/main/README.rst), [Dockerfile](https://github.com/rasterio/rasterio/blob/main/Dockerfile). Commit observado: `124e23f4060678460f39a0d838ac8c83b6fe2fe7`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-rspatial--terra"></a>

#### 205. rspatial/terra

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Procesamiento de rasters/vectores en R.
- **Puerta de integración propuesta:** API R y núcleo nativo.
- **Construir nosotros, solo si falta:** Operaciones específicas de flujos R con archivos y límites definidos.
- **Con qué y por qué:** conservar terra y sus clases; intercambio por artefactos cuando sea grande. Rscript y paquetes R originales, con intercambio por JSON/tablas/archivos. Si hace falta un servidor MCP externo, una fachada Go puede administrar el proceso sin traducir el cálculo estadístico.
- **No reconstruir / crítica:** No crear otro stack ráster general paralelo por uniformidad.
- **Prueba de admisión pendiente:** Raster pequeño con reproyección o agregado y metadatos comprobados.
- **Evidencia y alcance:** Archivo candidato recuperado: [R/click.R](https://github.com/rspatial/terra/blob/27420759a7a3c8f01c72e8a3bed3fb1028c33128/R/click.R); 159/159 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/rspatial/terra), [documentación recuperada](https://github.com/rspatial/terra/blob/master/README.md). Commit observado: `27420759a7a3c8f01c72e8a3bed3fb1028c33128`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-saga-gis--saga-gis"></a>

#### 206. saga-gis/saga-gis

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Herramientas de análisis geográfico SAGA.
- **Puerta de integración propuesta:** CLI y bibliotecas de herramientas de la distribución.
- **Construir nosotros, solo si falta:** Receta y selección de algoritmos por identificadores reales de esa versión.
- **Con qué y por qué:** usar saga_cmd y catálogo instalado; no incrustar C++. Go con el SDK MCP oficial para un adaptador de proceso: argumentos tipados, directorio de trabajo, terminación y referencias a archivos. El motor compilado se distribuye/instala aparte.
- **No reconstruir / crítica:** No fijar IDs de algoritmos sin versión ni reconstruir análisis de terreno existente.
- **Prueba de admisión pendiente:** Herramienta conocida con DEM sintético y parámetros contrastados.
- **Evidencia y alcance:** Archivo candidato recuperado: [saga-gis/src/saga_core/saga_api/api_callback.cpp](https://github.com/saga-gis/saga-gis/blob/24b7957d0edf0689ac531b5ce6752a7a2c6acb41/saga-gis/src/saga_core/saga_api/api_callback.cpp); 420/830 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/saga-gis/saga-gis). Commit observado: `24b7957d0edf0689ac531b5ce6752a7a2c6acb41`. Licencia en el inventario: `sin identificación SPDX` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-shapely--shapely"></a>

#### 207. shapely/shapely

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Geometría planar sobre GEOS.
- **Puerta de integración propuesta:** API Python Shapely.
- **Construir nosotros, solo si falta:** Operaciones geométricas acotadas con CRS/unidades y referencia de entrada explícitos.
- **Con qué y por qué:** usar API nativa; servidor propio solo si no basta un conector GIS existente. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No atribuirle manejo CRS completo, geodesia o simulación urbana; no duplicar GEOS.
- **Prueba de admisión pendiente:** Área/buffer conocido y rechazo de coordenadas/unidades incompatibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/shapely/__init__.py](https://github.com/shapely/shapely/blob/9ab6978eb2153a7781729fb303e0e35b119c1c2c/src/shapely/__init__.py); 54/54 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/shapely/shapely), [documentación recuperada](https://github.com/shapely/shapely/blob/main/README.rst), [pyproject.toml](https://github.com/shapely/shapely/blob/main/pyproject.toml). Commit observado: `9ab6978eb2153a7781729fb303e0e35b119c1c2c`. Licencia en el inventario: `BSD-3-Clause` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Servicios geoespaciales y catálogos

<a id="tool-ckan--ckan"></a>

#### 208. ckan/ckan

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Catálogo de datasets, organizaciones y recursos.
- **Puerta de integración propuesta:** Action API y permisos de una instancia.
- **Construir nosotros, solo si falta:** Búsqueda de recursos y vinculación con ingestión/versiones del proyecto.
- **Con qué y por qué:** consumir catálogo existente; publicación solo con credencial y alcance admitidos. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No duplicar catálogo ni considerar descargable cualquier recurso listado.
- **Prueba de admisión pendiente:** Búsqueda paginada y recurso con archivo/metadatos verificables.
- **Evidencia y alcance:** Archivo candidato recuperado: [ckan/cli/__init__.py](https://github.com/ckan/ckan/blob/fe279958910397c33dda5567719232be1639b35f/ckan/cli/__init__.py); 179/179 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/ckan/ckan), [documentación recuperada](https://github.com/ckan/ckan/blob/master/README.rst), [dev-requirements.txt](https://github.com/ckan/ckan/blob/master/dev-requirements.txt). Commit observado: `fe279958910397c33dda5567719232be1639b35f`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-geonetwork--core-geonetwork"></a>

#### 209. geonetwork/core-geonetwork

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Catálogo de metadatos geográficos.
- **Puerta de integración propuesta:** API de la versión instalada y estándares que publique.
- **Construir nosotros, solo si falta:** Búsqueda, lectura de fichas y resolución de enlaces/formatos.
- **Con qué y por qué:** integrar servicio Java sin importar su backend al adaptador. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No convertir metadatos en garantía de acceso, licencia o calidad del dataset.
- **Prueba de admisión pendiente:** Ficha conocida y enlace roto diagnosticado sin descarga ficticia.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [services/src/main/java/org/fao/geonet/api/records/CatalogApi.java](https://github.com/geonetwork/core-geonetwork/blob/6923928b9b290c8328a0ed21fd84b6a00f5bf237/services/src/main/java/org/fao/geonet/api/records/CatalogApi.java); lectura parcial de 600/704 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/geonetwork/core-geonetwork), [documentación recuperada](https://github.com/geonetwork/core-geonetwork/blob/main/README.md), [pom.xml](https://github.com/geonetwork/core-geonetwork/blob/main/pom.xml). Commit observado: `6923928b9b290c8328a0ed21fd84b6a00f5bf237`. Licencia en el inventario: `GPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-geonode--geonode"></a>

#### 210. GeoNode/geonode

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Gestión/publicación colaborativa de recursos geográficos.
- **Puerta de integración propuesta:** API GeoNode y servicios asociados de la instalación.
- **Construir nosotros, solo si falta:** Conector de recursos y publicación autorizada con identidad de proyecto.
- **Con qué y por qué:** conservar GeoNode y su stack; no asumir una sola API entre versiones. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No reconstruir portal ni publicar capas sin respetar permisos/procedencia.
- **Prueba de admisión pendiente:** Subir/leer capa de prueba con visibilidad y metadatos correctos.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [geonode/api/api.py](https://github.com/GeoNode/geonode/blob/c6aeb9784c94e2251dc7468c1f698b5d195ea0bd/geonode/api/api.py); lectura parcial de 600/758 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/GeoNode/geonode), [documentación recuperada](https://github.com/GeoNode/geonode/blob/master/README.md), [Dockerfile](https://github.com/GeoNode/geonode/blob/master/Dockerfile). Commit observado: `c6aeb9784c94e2251dc7468c1f698b5d195ea0bd`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-geopython--pygeoapi"></a>

#### 211. geopython/pygeoapi

- **Dictamen:** Candidato a capacidad base; admisión técnica pendiente.
- **Traer del original:** Implementación de APIs OGC y procesos configurables.
- **Puerta de integración propuesta:** OGC API de colecciones/procesos de la instancia.
- **Construir nosotros, solo si falta:** Descubrimiento y llamadas tipadas a procesos ya configurados.
- **Con qué y por qué:** reutilizar servicio y jobs si están disponibles en ese despliegue. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No crear otro adaptador por cada proceso OGC ni afirmar soporte de extensiones no configuradas.
- **Prueba de admisión pendiente:** Colección paginada y proceso pequeño con salida/estado verificables.
- **Evidencia y alcance:** Archivo candidato recuperado: [pygeoapi/api/__init__.py](https://github.com/geopython/pygeoapi/blob/133f077e11ffdd966c2f0117b7adcb1dca30f132/pygeoapi/api/__init__.py); 420/1334 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/geopython/pygeoapi), [documentación recuperada](https://github.com/geopython/pygeoapi/blob/master/README.md), [Dockerfile](https://github.com/geopython/pygeoapi/blob/master/Dockerfile). Commit observado: `133f077e11ffdd966c2f0117b7adcb1dca30f132`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-geoserver--geoserver"></a>

#### 212. geoserver/geoserver

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Publicación de mapas/capas y servicios geográficos.
- **Puerta de integración propuesta:** WMS/WFS/OGC y REST administrativo según instalación.
- **Construir nosotros, solo si falta:** Lectura de capas/capacidades; administración solo como operación separada autorizada.
- **Con qué y por qué:** conservar servidor Java; diferenciar consulta y configuración. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No reconstruir map server ni usar credenciales administrativas para consultas del agente.
- **Prueba de admisión pendiente:** Capa de prueba con filtros, CRS y autorización comprobados.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/restconfig/src/main/java/org/geoserver/rest/catalog/LayerController.java](https://github.com/geoserver/geoserver/blob/67ce637b71aa83df14e1dae61b21807279904e78/src/restconfig/src/main/java/org/geoserver/rest/catalog/LayerController.java); lectura parcial de 232/232 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/geoserver/geoserver), [documentación recuperada](https://github.com/geoserver/geoserver/blob/main/README.md), [requirements.txt](https://github.com/geoserver/geoserver/blob/main/requirements.txt). Commit observado: `67ce637b71aa83df14e1dae61b21807279904e78`. Licencia en el inventario: `NOASSERTION` / `open_source_license_text_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-mapserver--mapserver"></a>

#### 213. MapServer/MapServer

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Publicación cartográfica y servicios geográficos.
- **Puerta de integración propuesta:** Servicios OGC y configuración de mapfiles.
- **Construir nosotros, solo si falta:** Consulta de capacidades/capas; receta si el proyecto elige esta implementación.
- **Con qué y por qué:** integrar servicios y conservar renderizador nativo. Cliente HTTP tipado en Go con SDK MCP oficial cuando haga falta una fachada nueva. Se conserva el servidor original; usar una API ya existente evita cargar su runtime dentro del adaptador.
- **No reconstruir / crítica:** No instalarlo además de GeoServer sin motivo ni reescribir renderizado.
- **Prueba de admisión pendiente:** Mapa/capa de fixture con extensión, CRS y respuesta esperados.
- **Evidencia y alcance:** Archivo candidato recuperado: [msautotest/api/__init__.py](https://github.com/MapServer/MapServer/blob/8be067b074e46040ee5ba2bd1f2a9e03730decad/msautotest/api/__init__.py); 0/0 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/MapServer/MapServer), [documentación recuperada](https://github.com/MapServer/MapServer/blob/main/README.md), [CMakeLists.txt](https://github.com/MapServer/MapServer/blob/main/CMakeLists.txt). Commit observado: `8be067b074e46040ee5ba2bd1f2a9e03730decad`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.


### Familia: Simulación social y agentes

<a id="tool-gama-platform--gama"></a>

#### 214. gama-platform/gama

- **Dictamen:** Módulo para casos expertos; requiere datos, validación y recursos propios.
- **Traer del original:** Modelado y simulación basada en agentes.
- **Puerta de integración propuesta:** Modelos GAML y ejecutor headless admitido.
- **Construir nosotros, solo si falta:** Recetas de modelos concretos, parámetros, semillas y resultados por corrida.
- **Con qué y por qué:** conservar GAMA/GAML; controlar el ejecutor externo. JVM y CLI/biblioteca originales. El adaptador puede controlar el CLI como proceso o consumir un servicio existente; no hace falta portar el algoritmo a Go o Python.
- **No reconstruir / crítica:** No prometer un modelo social o urbano universal por tener un framework.
- **Prueba de admisión pendiente:** Modelo pequeño con semilla fija y resultados contrastados.
- **Evidencia y alcance:** Archivo candidato recuperado: [gama.api/src/gama/api/APIActivator.java](https://github.com/gama-platform/gama/blob/bfef64f890c67b971207770b80e37ff6765ecb03/gama.api/src/gama/api/APIActivator.java); 83/83 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/gama-platform/gama), [documentación recuperada](https://github.com/gama-platform/gama/blob/main/README.md). Commit observado: `bfef64f890c67b971207770b80e37ff6765ecb03`. Licencia en el inventario: `GPL-3.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-mesa--mesa"></a>

#### 215. mesa/mesa

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Framework de simulación basada en agentes en Python.
- **Puerta de integración propuesta:** Clases y API del modelo definido por su autor.
- **Construir nosotros, solo si falta:** Envolver modelos específicos con variables, semillas y criterios de parada.
- **Con qué y por qué:** compartir runtime del modelo y conservar sus reglas. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** La novedad del modelo pertenece a quien lo define; Mesa no trae una ciudad calibrada.
- **Prueba de admisión pendiente:** Modelo pequeño con número de agentes y evolución reproducibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [mesa/model.py](https://github.com/mesa/mesa/blob/1d3b61e2aa8d06b2c07f7c8efc146875512be3bb/mesa/model.py); 417/417 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/mesa/mesa), [documentación recuperada](https://github.com/mesa/mesa/blob/main/README.md), [pyproject.toml](https://github.com/mesa/mesa/blob/main/pyproject.toml). Commit observado: `1d3b61e2aa8d06b2c07f7c8efc146875512be3bb`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-metadriverse--metaurban"></a>

#### 216. metadriverse/metaurban

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Entorno de simulación urbana y agentes para investigación.
- **Puerta de integración propuesta:** API Python y motor/recursos del entorno.
- **Construir nosotros, solo si falta:** Recetas de escenarios experimentales y extracción de métricas identificadas.
- **Con qué y por qué:** conservar simulador y recursos; ejecución gráfica separada si se requiere. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No confundir benchmark de agentes con predicción de movilidad real.
- **Prueba de admisión pendiente:** Escenario fijado con seed, recursos y observaciones recuperables.
- **Evidencia y alcance:** Archivo candidato recuperado: [metaurban/engine/__init__.py](https://github.com/metadriverse/metaurban/blob/6b8ff9aa48dd27d5c57fa1c712db520732f11fa9/metaurban/engine/__init__.py); 5/5 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/metadriverse/metaurban), [documentación recuperada](https://github.com/metadriverse/metaurban/blob/main/README.md), [Dockerfile](https://github.com/metadriverse/metaurban/blob/main/Dockerfile). Commit observado: `6b8ff9aa48dd27d5c57fa1c712db520732f11fa9`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-netlogo--netlogo"></a>

#### 217. NetLogo/NetLogo

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Entorno y lenguaje de modelos basados en agentes.
- **Puerta de integración propuesta:** Ejecutor headless, modelos y BehaviorSpace según versión.
- **Construir nosotros, solo si falta:** Catálogo de modelos admitidos, parámetros y resultados de experimentos.
- **Con qué y por qué:** conservar runtime y modelos NetLogo; no traducirlos. JVM y CLI/biblioteca originales. El adaptador puede controlar el CLI como proceso o consumir un servicio existente; no hace falta portar el algoritmo a Go o Python.
- **No reconstruir / crítica:** No tomar modelos educativos como modelos de política pública validados.
- **Prueba de admisión pendiente:** Modelo de ejemplo y experimento con seed/resultados conocidos.
- **Evidencia y alcance:** Archivo candidato recuperado: [extensions/py/src/main/PythonExtension.scala](https://github.com/NetLogo/NetLogo/blob/931b3715e3b714d1cd8b7281f12434fd594a67d6/extensions/py/src/main/PythonExtension.scala); 256/256 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/NetLogo/NetLogo), [documentación recuperada](https://github.com/NetLogo/NetLogo/blob/main/README.md). Commit observado: `931b3715e3b714d1cd8b7281f12434fd594a67d6`. Licencia en el inventario: `GPL-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-tsinghua-fib-lab--agentsociety"></a>

#### 218. tsinghua-fib-lab/AgentSociety

- **Dictamen:** Investigar antes de diseñar o admitir implementación.
- **Traer del original:** Framework/plataforma de simulación social con agentes.
- **Puerta de integración propuesta:** APIs, modelos y proveedores de la versión elegida.
- **Construir nosotros, solo si falta:** Solo recetas experimentales con datos, costes y configuración explícitos.
- **Con qué y por qué:** conservar framework y backend; no mezclar su agente con el cliente MCP del usuario. Python con la API upstream y sus extensiones compiladas en un entorno de trabajo propio. Una fachada MCP sería fina y expondría operaciones elegidas, no ejecución Python arbitraria.
- **No reconstruir / crítica:** No equiparar conversación sintética con evidencia social ni disponibilidad libre de proveedores/datos.
- **Prueba de admisión pendiente:** Experimento pequeño reproducible con consumo y resultados registrados.
- **Evidencia y alcance:** Archivo candidato recuperado: [packages/agentsociety-benchmark/agentsociety_benchmark/cli/__init__.py](https://github.com/tsinghua-fib-lab/AgentSociety/blob/f70be25b9432a331c116db1301a796467dd8d2a8/packages/agentsociety-benchmark/agentsociety_benchmark/cli/__init__.py); 7/7 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/tsinghua-fib-lab/AgentSociety), [documentación recuperada](https://github.com/tsinghua-fib-lab/AgentSociety/blob/main/README.md), [Dockerfile](https://github.com/tsinghua-fib-lab/AgentSociety/blob/main/Dockerfile). Commit observado: `f70be25b9432a331c116db1301a796467dd8d2a8`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-tsinghua-fib-lab--citybench"></a>

#### 219. tsinghua-fib-lab/CityBench

- **Dictamen:** Referencia, especificación o fixture; no integración ejecutable autónoma.
- **Traer del original:** Benchmarks y tareas para evaluar modelos en entornos urbanos.
- **Puerta de integración propuesta:** Scripts, datasets y métricas de evaluación.
- **Construir nosotros, solo si falta:** Evaluación opcional de capacidades de agentes, no operación municipal.
- **Con qué y por qué:** mantener benchmark y dependencias separadas del catálogo operativo. Solo incorporación documental o fixture a la investigación/pruebas. No instalar ni publicar un servidor MCP para este repositorio.
- **No reconstruir / crítica:** No presentarlo como motor de planificación ni confundir puntuación con utilidad real.
- **Prueba de admisión pendiente:** Una tarea reproducida con dataset/modelo/versiones fijados.
- **Evidencia y alcance:** Archivo candidato recuperado: [config.py](https://github.com/tsinghua-fib-lab/CityBench/blob/37f3b0bc63fcfb259ee366cb43f098f3da5f6ad1/config.py); 289/289 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/tsinghua-fib-lab/CityBench), [documentación recuperada](https://github.com/tsinghua-fib-lab/CityBench/blob/main/README.md), [requirements.txt](https://github.com/tsinghua-fib-lab/CityBench/blob/main/requirements.txt). Commit observado: `37f3b0bc63fcfb259ee366cb43f098f3da5f6ad1`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.


### Familia: Visualización cartográfica y 3D

<a id="tool-cesiumgs--3d-tiles-tools"></a>

#### 220. CesiumGS/3d-tiles-tools

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Validación, conversión y utilidades de 3D Tiles.
- **Puerta de integración propuesta:** CLI/API TypeScript y dependencias específicas.
- **Construir nosotros, solo si falta:** Recetas de procesamiento y comprobación de artefactos 3D Tiles.
- **Con qué y por qué:** mantener herramientas Node; no reimplementar formatos/compresión. TypeScript/Node y CLI/API original. Reutilizar su modelo de objetos y ejecutor; una fachada MCP nueva usaría el SDK TypeScript solo para las operaciones seleccionadas.
- **No reconstruir / crítica:** No asumir que transforma cualquier modelo en tiles correctos ni duplicar conversores.
- **Prueba de admisión pendiente:** Tileset pequeño validado y reabierto sin pérdida de referencias.
- **Evidencia y alcance:** Archivo candidato recuperado: [src/cli/ToolsMain.ts](https://github.com/CesiumGS/3d-tiles-tools/blob/819213226c1e0a095ab0a35340456803ebb1356b/src/cli/ToolsMain.ts); 420/772 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/CesiumGS/3d-tiles-tools), [documentación recuperada](https://github.com/CesiumGS/3d-tiles-tools/blob/main/README.md), [package.json](https://github.com/CesiumGS/3d-tiles-tools/blob/main/package.json). Commit observado: `819213226c1e0a095ab0a35340456803ebb1356b`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-cesiumgs--cesium"></a>

#### 221. CesiumGS/cesium

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Motor de visualización geoespacial 3D.
- **Puerta de integración propuesta:** API JavaScript del visor; comparar MCP Cesium existente.
- **Construir nosotros, solo si falta:** Enlace de datasets/resultados y comandos visuales solo si hace falta una UI.
- **Con qué y por qué:** usar visor y puente MCP existente candidato. JavaScript/TypeScript en el host del visor y un contrato de comandos/eventos de navegador. Un servidor MCP, si falta, usaría el SDK TypeScript y un puente explícito con esa sesión.
- **No reconstruir / crítica:** No reconstruir globo/renderizador ni asumir credenciales de servicios asociados.
- **Prueba de admisión pendiente:** Objeto georreferenciado, cámara y selección verificados en navegador.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [packages/engine/Source/Scene/Scene.js](https://github.com/CesiumGS/cesium/blob/6bf9a21febc7e7271e3fd91fc4ed53958b26601f/packages/engine/Source/Scene/Scene.js); lectura parcial de 600/5580 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/CesiumGS/cesium), [documentación recuperada](https://github.com/CesiumGS/cesium/blob/main/README.md), [package.json](https://github.com/CesiumGS/cesium/blob/main/package.json). Commit observado: `6bf9a21febc7e7271e3fd91fc4ed53958b26601f`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-itowns--itowns"></a>

#### 222. iTowns/itowns

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Visualización geoespacial 3D web.
- **Puerta de integración propuesta:** API JavaScript y proveedores del visor.
- **Construir nosotros, solo si falta:** Host opcional y contrato de selección/artefactos si este visor es elegido.
- **Con qué y por qué:** conservar renderizador y estado de escena nativos. JavaScript/TypeScript en el host del visor y un contrato de comandos/eventos de navegador. Un servidor MCP, si falta, usaría el SDK TypeScript y un puente explícito con esa sesión.
- **No reconstruir / crítica:** No incluir todos los visores por defecto ni confundir captura con dato científico.
- **Prueba de admisión pendiente:** Capa de referencia con CRS, extensión y objeto seleccionado.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [packages/Main/src/Core/View.js](https://github.com/iTowns/itowns/blob/20ad0b23bd6a29a17f782aa142dfdbacea6d5a98/packages/Main/src/Core/View.js); lectura parcial de 600/1178 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/iTowns/itowns), [documentación recuperada](https://github.com/iTowns/itowns/blob/master/README.md), [Dockerfile](https://github.com/iTowns/itowns/blob/master/Dockerfile). Commit observado: `20ad0b23bd6a29a17f782aa142dfdbacea6d5a98`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-keplergl--kepler.gl"></a>

#### 223. keplergl/kepler.gl

- **Dictamen:** Comparar/reutilizar MCP existente antes de escribir uno nuevo.
- **Traer del original:** Visualización analítica y componente MCP presente en el árbol actual.
- **Puerta de integración propuesta:** API del visor y src/mcp/src/server/index.ts recuperado.
- **Construir nosotros, solo si falta:** Examinar primero su MCP nativo; receta y pruebas de integración con un host real.
- **Con qué y por qué:** conservar TypeScript y evaluar servidor MCP upstream antes de escribir otro. Conservar lenguaje, runtime, biblioteca MCP y bridge del upstream elegido. Nuestro código sería receta, configuración, prueba o extensión pequeña de una brecha demostrada; no una reescritura del servidor.
- **No reconstruir / crítica:** El catálogo anterior lo trataba solo como visor; no atribuirnos su MCP como novedad.
- **Framework/interfaz original:** No se identifica con certeza el framework del servidor a partir de la entrada recuperada; no inferirlo por el nombre del repositorio.
- **Prueba de admisión pendiente:** Cliente externo invoca una acción y el visor refleja/captura el estado correcto.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/mcp/src/server/bridge-server.ts](https://github.com/keplergl/kepler.gl/blob/6af0c1ed5b16d646544cad72805fa962eeaf887a/src/mcp/src/server/bridge-server.ts); lectura parcial de 293/293 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/keplergl/kepler.gl), [documentación recuperada](https://github.com/keplergl/kepler.gl/blob/master/README.md), [package.json](https://github.com/keplergl/kepler.gl/blob/master/package.json). Commit observado: `6af0c1ed5b16d646544cad72805fa962eeaf887a`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-maplibre--maplibre-gl-js"></a>

#### 224. maplibre/maplibre-gl-js

- **Dictamen:** Módulo opcional, solo si el caso lo requiere.
- **Traer del original:** Renderizador cartográfico web.
- **Puerta de integración propuesta:** API JavaScript del mapa.
- **Construir nosotros, solo si falta:** Puente de cámara, capas, selección y captura vinculado a objetos urbanos.
- **Con qué y por qué:** TypeScript en cliente y comandos tipados; no motor GIS nuevo. JavaScript/TypeScript en el host del visor y un contrato de comandos/eventos de navegador. Un servidor MCP, si falta, usaría el SDK TypeScript y un puente explícito con esa sesión.
- **No reconstruir / crítica:** No atribuir análisis espacial al renderizador ni convertir todo dataset en GeoJSON del agente.
- **Prueba de admisión pendiente:** Estado de mapa, capa y selección comprobados tras acción y recarga.
- **Evidencia y alcance:** Fuente de interfaz recuperada: [src/ui/map.ts](https://github.com/maplibre/maplibre-gl-js/blob/a5b3ed02bf0a87fff45a82b665a9d8a6e502c164/src/ui/map.ts); lectura parcial de 600/4791 líneas. La lectura no acredita instalación ni cobertura completa del API.
- **Identificación:** [repositorio](https://github.com/maplibre/maplibre-gl-js), [documentación recuperada](https://github.com/maplibre/maplibre-gl-js/blob/main/README.md), [docker-compose.yml](https://github.com/maplibre/maplibre-gl-js/blob/main/docker-compose.yml). Commit observado: `a5b3ed02bf0a87fff45a82b665a9d8a6e502c164`. Licencia en el inventario: `NOASSERTION` / `license_review_required`; revisión preliminar, no admisión de redistribución.

<a id="tool-terriajs--terriajs"></a>

#### 225. TerriaJS/terriajs

- **Dictamen:** Alternativa: comparar y elegir, no instalar por defecto junto a sus equivalentes.
- **Traer del original:** Plataforma de catálogo/visualización geoespacial.
- **Puerta de integración propuesta:** Modelos de catálogo y APIs de la aplicación.
- **Construir nosotros, solo si falta:** Integración con catálogos y estado compartido cuando se elija Terria como host.
- **Con qué y por qué:** conservar aplicación; comprobar interfaz de automatización real. JavaScript/TypeScript en el host del visor y un contrato de comandos/eventos de navegador. Un servidor MCP, si falta, usaría el SDK TypeScript y un puente explícito con esa sesión.
- **No reconstruir / crítica:** No reconstruir catálogo/visor ni asumir que todas sus fuentes tienen iguales permisos.
- **Prueba de admisión pendiente:** Catálogo de prueba cargado y selección/enlace compartido reproducibles.
- **Evidencia y alcance:** Archivo candidato recuperado: [packages/terriajs/lib/Models/ItemSearchProviders/Index.ts](https://github.com/TerriaJS/terriajs/blob/49f9b22c631148972b4d58a22e54af2f39d0abc0/packages/terriajs/lib/Models/ItemSearchProviders/Index.ts); 108/108 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/TerriaJS/terriajs), [documentación recuperada](https://github.com/TerriaJS/terriajs/blob/main/README.md), [package.json](https://github.com/TerriaJS/terriajs/blob/main/package.json). Commit observado: `49f9b22c631148972b4d58a22e54af2f39d0abc0`. Licencia en el inventario: `Apache-2.0` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

<a id="tool-visgl--deck.gl"></a>

#### 226. visgl/deck.gl

- **Dictamen:** Dependencia de otro paquete; no construir servidor independiente.
- **Traer del original:** Capas de visualización de datos con GPU.
- **Puerta de integración propuesta:** API JavaScript/TypeScript.
- **Construir nosotros, solo si falta:** Capas y selección de resultados dentro de un visor elegido.
- **Con qué y por qué:** componente del frontend; no crear servidor MCP por biblioteca de render. Integrar como dependencia del paquete padre, en su lenguaje nativo. No crear otro servicio, otra instalación o catálogo MCP por esta biblioteca.
- **No reconstruir / crítica:** No confundir visualización acelerada con análisis geográfico o almacenamiento.
- **Prueba de admisión pendiente:** Capa pequeña con coordenadas, picking y valores correctos.
- **Evidencia y alcance:** Archivo candidato recuperado: [modules/main/src/index.ts](https://github.com/visgl/deck.gl/blob/5d4ba6cd02b4742552bf4b5126ee8d418930aab5/modules/main/src/index.ts); 268/268 líneas. Es evidencia parcial de implementación, no comprobación exhaustiva de la puerta de integración propuesta.
- **Identificación:** [repositorio](https://github.com/visgl/deck.gl), [documentación recuperada](https://github.com/visgl/deck.gl/blob/master/README.md), [package.json](https://github.com/visgl/deck.gl/blob/master/package.json). Commit observado: `5d4ba6cd02b4742552bf4b5126ee8d418930aab5`. Licencia en el inventario: `MIT` / `open_source_license_detected`; revisión preliminar, no admisión de redistribución.

## 7. Proyectos fuera de GitHub

### E1. PALM Model System

- **Traer:** modelo LES y componentes de entorno urbano, superficies y atmósfera de PALM, junto con sus herramientas de configuración/ejecución.
- **Entrada original:** toolchain y casos PALM, compilación Fortran y ejecución paralela según la configuración admitida. La documentación `latest` redirigió a la versión `25.10.1` durante la consulta; eso no fija nuestra versión de soporte.
- **Construir propuesto:** expediente de caso con dominio, malla, forzamientos y recursos; envío/consulta de trabajo; recuperación de variables con referencias. Reutilizar las herramientas PALM y el planificador de la instalación.
- **Con qué y por qué:** trabajador con toolchain nativo y un conector de trabajos; no incluir el solver en el proceso MCP ni reescribirlo en Python/Go.
- **No reconstruir / crítica:** no crear solver LES, inventar meteorología, convertir huellas en un caso calibrado o presentar parámetros por defecto como validez para cualquier ciudad.
- **Prueba pendiente:** caso oficial pequeño con configuración/restart documentados, resultados y recursos contrastados.
- **Decisión:** módulo experto, sujeto a compilación, datos y licencia exacta de la revisión seleccionada. No instalado en esta revisión.
- **Fuentes:** [documentación de versión](https://docs.palm-model.com/25.10.1/), [repositorio](https://gitlab.palm-model.org/releases/palm_model_system). El repositorio/código completo no se auditó en esta pasada.

### E2. openTELEMAC-MASCARET

- **Traer:** solvers hidráulicos y utilidades de preparación/procesamiento del sistema.
- **Entrada original:** casos y ejecutores Fortran/Python, con configuración de compilador y MPI cuando corresponda. La ruta antigua `.org/index.php/installation` devolvió 404; se identificó la página oficial equivalente en `.com`.
- **Construir propuesto:** receta por módulo/versión y expediente de corrida; validación de malla, fronteras y datos; estado y resultados del trabajo. No otra implementación hidráulica.
- **Con qué y por qué:** usar scripts y ejecutables oficiales en trabajador separado. La fachada controla el caso y conversa con el scheduler existente, si lo hay.
- **No reconstruir / crítica:** no reducir todos los módulos a una operación genérica de inundación, ni prometer paralelismo o binarios sin validar la distribución elegida.
- **Prueba pendiente:** caso de referencia de un módulo, reproducción directa y por el conector, errores y balance comprobados.
- **Decisión:** investigación experta. El alojamiento de código devolvió 403 en esta consulta; no se fija licencia exacta, receta ni API como verificados.
- **Fuentes:** [instalación oficial](https://www.opentelemac.com/index.php/installation), [repositorio](https://gitlab.pam-retd.fr/otm/telemac-mascaret).

### E3. SimStadt

- **Traer:** entorno de simulación energética urbana y workflows sobre CityGML. No reconstruir cálculo energético, bibliotecas de edificios ni su sistema de workflows.
- **Entrada original:** aplicación/workflows Java y su CLI documentada; seleccionar versión, compilación y modelos requeridos antes de diseñar una fachada.
- **Construir propuesto:** mapeo de un escenario urbano a entradas SimStadt, receta del workflow elegido y recuperación de indicadores con revisión y supuestos.
- **Con qué y por qué:** mantener Java y herramientas originales; consumir CLI/API existente. Un adaptador externo solo cubre las operaciones que no pueda invocar ya un cliente.
- **No reconstruir / crítica:** no asumir que CityGML contiene usos, materiales y ocupación completos. Hay documentación rezagada: la guía Git todavía habla de repositorio privado, mientras la portada y una noticia institucional actual confirman apertura con MIT desde septiembre de 2026. La guía antigua no es motivo suficiente para declararlo cerrado.
- **Prueba pendiente:** obtener fuente/release públicas admitidas, comprobar licencia/dependencias reales y ejecutar un caso pequeño con meteorología y datos de edificios identificados.
- **Decisión:** candidato energético en revisión, no receta de compilación ya probada. Esta pasada verificó fuentes institucionales y ubicación del repositorio, no ejecutó ni auditó su código completo.
- **Fuentes:** [portada actual](https://simstadt.hft-stuttgart.de/), [noticia institucional](https://www.hft-stuttgart.com/research/news/simstadt-next), [repositorio identificado](https://transfer.hft-stuttgart.de/gitlab/simstadt/simstadt), [guía Git rezagada](https://simstadt.hft-stuttgart.de/developer-how-to/git/).

## 8. Componentes propuestos del producto: aporte propio y límites

| Componente | Qué se reutiliza | Qué habría que construir | Tecnología propuesta y razón | Lo que no queda decidido |
|---|---|---|---|---|
| Registro de capacidades | Metadatos y contratos upstream. | Identidad de herramienta/versión, capacidades admitidas y evidencia de soporte. | JSON/YAML versionados y validación; no requiere un servicio distribuido para empezar. | No convertir todos los candidatos en productos admitidos. |
| Recetas | Instaladores, imágenes, locks y comandos originales. | Matriz comprobada de instalación/arranque por plataforma y perfil; diagnóstico de requisitos. | El runtime de cada herramienta; ejecución de procesos con argumentos estructurados. | No se impone virtualenv a Java, R, contenedores o escritorio. |
| Fachada de biblioteca Python | Funciones y estructuras nativas. | Operaciones MCP seleccionadas, entradas/salidas y referencias. | Python evita reescribir bindings; comparar SDK oficial/FastMCP contra ese contrato. | Framework y versión no se fijan solo porque la biblioteca sea Python. |
| Fachada de CLI | Ejecutable y formatos originales. | Parámetros tipados, entorno de trabajo, terminación y resultados. | Go + SDK oficial es candidato porque controla procesos sin incrustar el runtime científico. | La prueba debe comparar coste/operación con un wrapper ya existente. |
| Fachada de servicio HTTP | API, autenticación y jobs del servicio. | Descubrimiento y operaciones de dominio que falten para MCP. | Cliente tipado independiente, Go como candidato; preservar el servicio original. | No rehacer API, autorización ni cola que ya existan. |
| Composición MCP | SDKs/frameworks y proxies mantenidos. | Selección de herramientas por proyecto, namespaces y compatibilidad si un caso exige agregación. | Evaluar FastMCP u otra implementación existente contra los MCP elegidos. | No es obligatorio un gateway global ni reescribir los backends. |
| Trabajos largos | Scheduler/jobs upstream cuando existan. | Traducción de estado, cancelación y resultados; cola propia solo para una brecha real. | Preferir API del scheduler o procesos aislados; estado persistente donde lo exija el caso. | No duplicar OpenQuake, openEO o servidores que ya dan jobs. |
| Intercambio semántico | Formatos y estándares de los dominios. | Mapeos explícitos de IDs, CRS, unidades, tiempo, variables y revisión. | Transformaciones y validadores de las bibliotecas originales. | No existe una conversión universal de cualquier resultado hacia cualquier motor. |
| Pruebas | Ejemplos y casos de referencia redistribuibles. | Prueba de instalación, contrato MCP, cálculo conocido y errores relevantes. | Clientes de prueba independientes del lenguaje del servidor; plataformas reales. | Que responda tools/list no acredita cálculo correcto. |
| Experiencia de usuario | Clientes MCP y herramientas de despliegue existentes. | Diagnóstico, configuración y selección entendible de capacidades. | Elegir empaquetado después de probar runtimes reales, locales/remotos. | No se promete un instalador universal antes de resolver las dependencias. |

### 8.1 Qué sí sería desarrollo científico adicional

Un modelo nuevo, una calibración para otra ciudad, una función de vulnerabilidad, una traducción semántica sin equivalente, un nuevo esquema de demanda o una evaluación causal son trabajo científico/sectorial separado. Deben tener datos, hipótesis, autoría y validación propias. No se financian ni se presentan como una consecuencia automática de «poner MCP» a un motor.

### 8.2 Criterio de admisión de una herramienta

1. Identificar operación útil y usuario; descartar duplicidad funcional.
2. Confirmar API/CLI y versión; buscar MCP/binding existente antes de escribir otro.
3. Separar motor, wrapper, datos, pesos y servicio externo, con sus condiciones de uso.
4. Reproducir ejemplo directo y registrar requisitos reales.
5. Definir exclusivamente el delta de integración y seleccionar su tecnología por esa frontera.
6. Ejecutar el mismo caso por MCP, incluidos errores y límites científicos relevantes.
7. Probar proyecto/usuario, archivos, recursos y ciclo de vida sin atribuir aislamiento que no se haya comprobado.
8. Admitir solo versiones/plataformas efectivamente probadas y describir límites en el catálogo.

El resultado de esta revisión es un mapa de decisiones y brechas. No autoriza construir todos los candidatos ni fija la arquitectura a partir del prototipo descartado.


## Procedencia de esta copia pública

Revisión de 226 repositorios públicos y tres proyectos externos al 10 de noviembre de 2026. Las fuentes y commits observados están enlazados en las fichas. Se excluyeron rutas locales, productos privados y archivos de evidencia internos. Ninguna revisión documental acredita instalación o validación científica. Las propuestas tecnológicas por herramienta permanecen sujetas a la RFC.
