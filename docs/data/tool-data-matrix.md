# Matriz inicial de datos por herramienta

**Estado: propuesta de requisitos, no disponibilidad operativa.** Cada fila tiene una ficha individual. Los perfiles agrupan datos de un primer caso representativo; cada operación necesita un binding nativo y puede requerir un subconjunto diferente. Las dependencias heredan datos del paquete padre. No se exige GTFS para una validación geométrica ni HVAC para un cálculo de iluminación.

Fuentes candidatas no equivalen a assets descargados, licenciados o adecuados. Las fuentes de operador necesitan proyecto y autorización concretos. `ready_to_run=false` en los 229 candidatos.

| Herramienta | Perfil propuesto | Estado |
|---|---|---|
| [Deltares/Delft3D](#data-deltares--delft3d) | `coastal` | candidate; binding pendiente |
| [Deltares/hydromt](#data-deltares--hydromt) | `flood` | dependency; binding pendiente |
| [Deltares/hydromt_sfincs](#data-deltares--hydromt_sfincs) | `flood` | dependency; binding pendiente |
| [Deltares/hydromt_wflow](#data-deltares--hydromt_wflow) | `hydrology` | dependency; binding pendiente |
| [Deltares/SFINCS](#data-deltares--sfincs) | `flood` | candidate; binding pendiente |
| [GeoscienceAustralia/anuga_core](#data-geoscienceaustralia--anuga_core) | `flood` | candidate; binding pendiente |
| [MarkusPic/swmm_api](#data-markuspic--swmm_api) | `swmm` | dependency; binding pendiente |
| [openstreams/wflow](#data-openstreams--wflow) | `hydrology` | candidate; binding pendiente |
| [OpenWaterAnalytics/EPANET](#data-openwateranalytics--epanet) | `epanet` | candidate; binding pendiente |
| [pyswmm/pyswmm](#data-pyswmm--pyswmm) | `swmm` | candidate; binding pendiente |
| [USEPA/EPANET2.2](#data-usepa--epanet2.2) | `epanet` | candidate; binding pendiente |
| [USEPA/Stormwater-Management-Model](#data-usepa--stormwater-management-model) | `swmm` | candidate; binding pendiente |
| [USEPA/WNTR](#data-usepa--wntr) | `epanet` | candidate; binding pendiente |
| [blender/blender](#data-blender--blender) | `cad` | candidate; binding pendiente |
| [buildingSMART/BCF-XML](#data-buildingsmart--bcf-xml) | `bcf` | dependency; binding pendiente |
| [buildingSMART/IDS](#data-buildingsmart--ids) | `bim` | dependency; binding pendiente |
| [compas-dev/compas](#data-compas-dev--compas) | `cad` | candidate; binding pendiente |
| [compas-dev/compas_fab](#data-compas-dev--compas_fab) | `cad` | candidate; binding pendiente |
| [DynamoDS/Dynamo](#data-dynamods--dynamo) | `cad` | candidate; binding pendiente |
| [FreeCAD/FreeCAD](#data-freecad--freecad) | `cad` | candidate; binding pendiente |
| [IfcOpenShell/IfcOpenShell](#data-ifcopenshell--ifcopenshell) | `bim` | candidate; binding pendiente |
| [openscad/openscad](#data-openscad--openscad) | `cad` | candidate; binding pendiente |
| [PixarAnimationStudios/OpenUSD](#data-pixaranimationstudios--openusd) | `scene` | dependency; binding pendiente |
| [specklesystems/speckle-server](#data-specklesystems--speckle-server) | `object-service` | candidate; binding pendiente |
| [specklesystems/specklepy](#data-specklesystems--specklepy) | `object-service` | dependency; binding pendiente |
| [APA-Technology-Division/urban-and-regional-planning-resources](#data-apa-technology-division--urban-and-regional-planning-resources) | `none` | reference; binding pendiente |
| [durbanitas/awesome-urban-planning](#data-durbanitas--awesome-urban-planning) | `none` | reference; binding pendiente |
| [Ireliya/Awesome-Urban-Planning-Agents](#data-ireliya--awesome-urban-planning-agents) | `none` | reference; binding pendiente |
| [sacridini/Awesome-Geospatial](#data-sacridini--awesome-geospatial) | `none` | reference; binding pendiente |
| [kunifujiwara/VoxCity](#data-kunifujiwara--voxcity) | `microclimate` | candidate; binding pendiente |
| [ladybug-tools/uwg](#data-ladybug-tools--uwg) | `weather` | candidate; binding pendiente |
| [OpenFOAM/OpenFOAM-dev](#data-openfoam--openfoam-dev) | `cfd` | candidate; binding pendiente |
| [uDALES/u-dales](#data-udales--u-dales) | `atmosphere` | candidate; binding pendiente |
| [UMEP-dev/solweig](#data-umep-dev--solweig) | `microclimate` | candidate; binding pendiente |
| [UMEP-dev/SUEWS](#data-umep-dev--suews) | `microclimate` | candidate; binding pendiente |
| [UMEP-dev/UMEP](#data-umep-dev--umep) | `microclimate` | dependency; binding pendiente |
| [UMEP-dev/UMEP-processing](#data-umep-dev--umep-processing) | `microclimate` | candidate; binding pendiente |
| [USEPA/CMAQ](#data-usepa--cmaq) | `air-quality` | candidate; binding pendiente |
| [wrf-model/WRF](#data-wrf-model--wrf) | `atmosphere` | candidate; binding pendiente |
| [eclipse-ditto/ditto](#data-eclipse-ditto--ditto) | `context` | candidate; binding pendiente |
| [FIWARE/context.Orion-LD](#data-fiware--context.orion-ld) | `context` | candidate; binding pendiente |
| [FIWARE/tutorials.Step-by-Step](#data-fiware--tutorials.step-by-step) | `none` | reference; binding pendiente |
| [FraunhoferIOSB/FROST-Server](#data-fraunhoferiosb--frost-server) | `context` | candidate; binding pendiente |
| [ScorpioBroker/ScorpioBroker](#data-scorpiobroker--scorpiobroker) | `context` | candidate; binding pendiente |
| [smart-data-models/data-models](#data-smart-data-models--data-models) | `schemas` | dependency; binding pendiente |
| [telefonicaid/fiware-orion](#data-telefonicaid--fiware-orion) | `context` | candidate; binding pendiente |
| [thingsboard/thingsboard](#data-thingsboard--thingsboard) | `context` | candidate; binding pendiente |
| [HPSCIL/Open-Space-Cellular_Automata](#data-hpscil--open-space-cellular_automata) | `land-use` | candidate; binding pendiente |
| [johanlahti/urban-lu-model](#data-johanlahti--urban-lu-model) | `land-use` | candidate; binding pendiente |
| [LandInsightLab/MUSE](#data-landinsightlab--muse) | `land-use` | candidate; binding pendiente |
| [UDST/choicemodels](#data-udst--choicemodels) | `land-use` | dependency; binding pendiente |
| [UDST/developer](#data-udst--developer) | `land-use` | dependency; binding pendiente |
| [UDST/orca](#data-udst--orca) | `land-use` | dependency; binding pendiente |
| [UDST/urbansim](#data-udst--urbansim) | `land-use` | candidate; binding pendiente |
| [UDST/urbansim_defaults](#data-udst--urbansim_defaults) | `land-use` | dependency; binding pendiente |
| [UDST/urbansim_templates](#data-udst--urbansim_templates) | `land-use` | dependency; binding pendiente |
| [CityScope/CS_CityIO](#data-cityscope--cs_cityio) | `context` | candidate; binding pendiente |
| [CityScope/CS_cityscopeJS](#data-cityscope--cs_cityscopejs) | `context` | dependency; binding pendiente |
| [CityScope/CS_CityScoPy](#data-cityscope--cs_cityscopy) | `context` | dependency; binding pendiente |
| [CityScope/CS_Mobility_Service](#data-cityscope--cs_mobility_service) | `demand` | candidate; binding pendiente |
| [CityScope/CS_Simulation_GAMA](#data-cityscope--cs_simulation_gama) | `context` | dependency; binding pendiente |
| [consuldemocracy/consuldemocracy](#data-consuldemocracy--consuldemocracy) | `participation` | candidate; binding pendiente |
| [decidim/decidim](#data-decidim--decidim) | `participation` | candidate; binding pendiente |
| [umap-project/umap](#data-umap-project--umap) | `participation` | candidate; binding pendiente |
| [martibosch/pylandstats](#data-martibosch--pylandstats) | `landscape` | candidate; binding pendiente |
| [natcap/invest](#data-natcap--invest) | `ecosystem` | candidate; binding pendiente |
| [natcap/pygeoprocessing](#data-natcap--pygeoprocessing) | `raster` | dependency; binding pendiente |
| [r-spatialecology/landscapemetrics](#data-r-spatialecology--landscapemetrics) | `landscape` | candidate; binding pendiente |
| [architecture-building-systems/CityEnergyAnalyst](#data-architecture-building-systems--cityenergyanalyst) | `urban-energy` | candidate; binding pendiente |
| [BETALAB-team/EUReCA](#data-betalab-team--eureca) | `urban-energy` | candidate; binding pendiente |
| [KTH-UrbanT/mubes-ubem](#data-kth-urbant--mubes-ubem) | `urban-energy` | candidate; binding pendiente |
| [ladybug-tools/dragonfly-core](#data-ladybug-tools--dragonfly-core) | `urban-energy` | dependency; binding pendiente |
| [ladybug-tools/dragonfly-energy](#data-ladybug-tools--dragonfly-energy) | `energy` | candidate; binding pendiente |
| [ladybug-tools/honeybee-core](#data-ladybug-tools--honeybee-core) | `energy` | dependency; binding pendiente |
| [ladybug-tools/honeybee-energy](#data-ladybug-tools--honeybee-energy) | `energy` | candidate; binding pendiente |
| [ladybug-tools/honeybee-radiance](#data-ladybug-tools--honeybee-radiance) | `daylight` | candidate; binding pendiente |
| [ladybug-tools/ladybug](#data-ladybug-tools--ladybug) | `weather` | dependency; binding pendiente |
| [NatLabRockies/ComStock](#data-natlabrockies--comstock) | `urban-energy` | candidate; binding pendiente |
| [NatLabRockies/EnergyPlus](#data-natlabrockies--energyplus) | `energy` | candidate; binding pendiente |
| [NatLabRockies/OpenStudio](#data-natlabrockies--openstudio) | `energy` | dependency; binding pendiente |
| [NatLabRockies/OpenStudio-HPXML](#data-natlabrockies--openstudio-hpxml) | `energy` | dependency; binding pendiente |
| [NatLabRockies/resstock](#data-natlabrockies--resstock) | `urban-energy` | candidate; binding pendiente |
| [RWTH-EBC/TEASER](#data-rwth-ebc--teaser) | `energy` | candidate; binding pendiente |
| [samuelduchesne/archetypal](#data-samuelduchesne--archetypal) | `energy` | dependency; binding pendiente |
| [samuelduchesne/geomeppy](#data-samuelduchesne--geomeppy) | `energy` | dependency; binding pendiente |
| [santoshphilip/eppy](#data-santoshphilip--eppy) | `energy` | dependency; binding pendiente |
| [UCL/simstock](#data-ucl--simstock) | `urban-energy` | candidate; binding pendiente |
| [urbanopt/urbanopt-cli](#data-urbanopt--urbanopt-cli) | `urban-energy` | candidate; binding pendiente |
| [urbanopt/urbanopt-example-geojson-project](#data-urbanopt--urbanopt-example-geojson-project) | `urban-energy` | reference; binding pendiente |
| [urbanopt/urbanopt-reopt-gem](#data-urbanopt--urbanopt-reopt-gem) | `electrical` | dependency; binding pendiente |
| [CloudCompare/CloudCompare](#data-cloudcompare--cloudcompare) | `lidar` | candidate; binding pendiente |
| [isl-org/Open3D](#data-isl-org--open3d) | `lidar` | candidate; binding pendiente |
| [PDAL/PDAL](#data-pdal--pdal) | `lidar` | candidate; binding pendiente |
| [PDAL/python](#data-pdal--python) | `lidar` | dependency; binding pendiente |
| [potree/potree](#data-potree--potree) | `scene` | candidate; binding pendiente |
| [anandb/energyplus-mcp-java](#data-anandb--energyplus-mcp-java) | `energy` | candidate; binding pendiente |
| [bonninr/freecad_mcp](#data-bonninr--freecad_mcp) | `cad` | candidate; binding pendiente |
| [contextform/freecad-mcp](#data-contextform--freecad-mcp) | `cad` | candidate; binding pendiente |
| [ericmartinpe/EnergyPlus-MCP-epjson](#data-ericmartinpe--energyplus-mcp-epjson) | `energy` | candidate; binding pendiente |
| [gaopengbin/cesium-mcp](#data-gaopengbin--cesium-mcp) | `scene` | candidate; binding pendiente |
| [idfkit/idfkit-mcp](#data-idfkit--idfkit-mcp) | `energy` | candidate; binding pendiente |
| [jagan-shanmugam/open-streetmap-mcp](#data-jagan-shanmugam--open-streetmap-mcp) | `roads` | candidate; binding pendiente |
| [jjsantos01/qgis_mcp](#data-jjsantos01--qgis_mcp) | `vector` | candidate; binding pendiente |
| [JordanGunn/gdal-mcp](#data-jordangunn--gdal-mcp) | `vector` | candidate; binding pendiente |
| [kLabUM/SWMM-MCP-PUB](#data-klabum--swmm-mcp-pub) | `swmm` | candidate; binding pendiente |
| [LBNL-ETA/EnergyPlus-MCP](#data-lbnl-eta--energyplus-mcp) | `energy` | candidate; binding pendiente |
| [mahdin75/gis-mcp](#data-mahdin75--gis-mcp) | `vector` | candidate; binding pendiente |
| [msradam/osmnx-mcp](#data-msradam--osmnx-mcp) | `roads` | candidate; binding pendiente |
| [neka-nat/freecad-mcp](#data-neka-nat--freecad-mcp) | `cad` | candidate; binding pendiente |
| [nkarasiak/qgis-mcp](#data-nkarasiak--qgis-mcp) | `vector` | candidate; binding pendiente |
| [OSGeo/grass-mcp](#data-osgeo--grass-mcp) | `vector` | reference; binding pendiente |
| [piatkowski/qgis-mcp](#data-piatkowski--qgis-mcp) | `vector` | candidate; binding pendiente |
| [ProfRino/bonsai-bim-skills](#data-profrino--bonsai-bim-skills) | `none` | reference; binding pendiente |
| [RainerGaier/energyplus-mcp-server](#data-rainergaier--energyplus-mcp-server) | `energy` | candidate; binding pendiente |
| [salog0d/UrbanPlannerMCP](#data-salog0d--urbanplannermcp) | `social` | candidate; binding pendiente |
| [Show2Instruct/ifc-bonsai-mcp](#data-show2instruct--ifc-bonsai-mcp) | `bim` | candidate; binding pendiente |
| [sparkgeo/geo-mcp-servers](#data-sparkgeo--geo-mcp-servers) | `stac` | candidate; binding pendiente |
| [spkane/freecad-addon-robust-mcp-server](#data-spkane--freecad-addon-robust-mcp-server) | `cad` | candidate; binding pendiente |
| [XRDS76354/SUMO-MCP-Server](#data-xrds76354--sumo-mcp-server) | `sumo` | candidate; binding pendiente |
| [Zhonghao1995/agentic-swmm-workflow](#data-zhonghao1995--agentic-swmm-workflow) | `swmm` | candidate; binding pendiente |
| [3dcitydb/3dcitydb](#data-3dcitydb--3dcitydb) | `city-model` | candidate; binding pendiente |
| [3dcitydb/citydb-tool](#data-3dcitydb--citydb-tool) | `city-model` | dependency; binding pendiente |
| [citygml4j/citygml-tools](#data-citygml4j--citygml-tools) | `city-model` | candidate; binding pendiente |
| [citygml4j/citygml4j](#data-citygml4j--citygml4j) | `city-model` | dependency; binding pendiente |
| [cityjson/cjio](#data-cityjson--cjio) | `city-model` | candidate; binding pendiente |
| [dtcc-platform/dtcc-core](#data-dtcc-platform--dtcc-core) | `city-model` | dependency; binding pendiente |
| [dtcc-platform/dtcc-sim](#data-dtcc-platform--dtcc-sim) | `cfd` | candidate; binding pendiente |
| [dtcc-platform/dtcc-viewer](#data-dtcc-platform--dtcc-viewer) | `scene` | candidate; binding pendiente |
| [Project-PLATEAU/PLATEAU-Builder](#data-project-plateau--plateau-builder) | `city-model` | candidate; binding pendiente |
| [Project-PLATEAU/PLATEAU-GIS-Converter](#data-project-plateau--plateau-gis-converter) | `city-model` | candidate; binding pendiente |
| [reearth/reearth-flow](#data-reearth--reearth-flow) | `city-model` | candidate; binding pendiente |
| [tudelft3d/3DCityDB-Tools-for-QGIS](#data-tudelft3d--3dcitydb-tools-for-qgis) | `city-model` | dependency; binding pendiente |
| [tudelft3d/3dfier](#data-tudelft3d--3dfier) | `reconstruction` | candidate; binding pendiente |
| [tudelft3d/City4CFD](#data-tudelft3d--city4cfd) | `cfd` | candidate; binding pendiente |
| [VCityTeam/UD-Viz](#data-vcityteam--ud-viz) | `scene` | candidate; binding pendiente |
| [benchmark-urbanism/cityseer-api](#data-benchmark-urbanism--cityseer-api) | `roads` | candidate; binding pendiente |
| [gboeing/osmnx](#data-gboeing--osmnx) | `roads` | candidate; binding pendiente |
| [pysal/esda](#data-pysal--esda) | `statistics` | candidate; binding pendiente |
| [pysal/inequality](#data-pysal--inequality) | `statistics` | candidate; binding pendiente |
| [pysal/libpysal](#data-pysal--libpysal) | `statistics` | dependency; binding pendiente |
| [pysal/mgwr](#data-pysal--mgwr) | `statistics` | candidate; binding pendiente |
| [pysal/momepy](#data-pysal--momepy) | `statistics` | candidate; binding pendiente |
| [pysal/segregation](#data-pysal--segregation) | `statistics` | candidate; binding pendiente |
| [pysal/spopt](#data-pysal--spopt) | `statistics` | candidate; binding pendiente |
| [pysal/spreg](#data-pysal--spreg) | `statistics` | candidate; binding pendiente |
| [SpaceGroupUCL/depthmapX](#data-spacegroupucl--depthmapx) | `roads` | candidate; binding pendiente |
| [a-b-street/abstreet](#data-a-b-street--abstreet) | `sumo` | candidate; binding pendiente |
| [ActivitySim/activitysim](#data-activitysim--activitysim) | `demand` | candidate; binding pendiente |
| [ActivitySim/populationsim](#data-activitysim--populationsim) | `demand` | dependency; binding pendiente |
| [AequilibraE/aequilibrae](#data-aequilibrae--aequilibrae) | `traffic-assignment` | candidate; binding pendiente |
| [conveyal/analysis-backend](#data-conveyal--analysis-backend) | `transit` | candidate; binding pendiente |
| [conveyal/r5](#data-conveyal--r5) | `transit` | dependency; binding pendiente |
| [eclipse-sumo/sumo](#data-eclipse-sumo--sumo) | `sumo` | candidate; binding pendiente |
| [GIScience/openrouteservice](#data-giscience--openrouteservice) | `roads` | candidate; binding pendiente |
| [ipea/accessibility](#data-ipea--accessibility) | `accessibility` | candidate; binding pendiente |
| [ipea/r5r](#data-ipea--r5r) | `transit` | candidate; binding pendiente |
| [matsim-org/matsim-libs](#data-matsim-org--matsim-libs) | `demand` | candidate; binding pendiente |
| [MobilityData/gtfs-validator](#data-mobilitydata--gtfs-validator) | `transit` | dependency; binding pendiente |
| [opentripplanner/OpenTripPlanner](#data-opentripplanner--opentripplanner) | `transit` | candidate; binding pendiente |
| [Project-OSRM/osrm-backend](#data-project-osrm--osrm-backend) | `roads` | candidate; binding pendiente |
| [r5py/r5py](#data-r5py--r5py) | `transit` | candidate; binding pendiente |
| [ropensci/stplanr](#data-ropensci--stplanr) | `traffic-assignment` | candidate; binding pendiente |
| [UDST/synthpop](#data-udst--synthpop) | `demand` | candidate; binding pendiente |
| [valhalla/valhalla](#data-valhalla--valhalla) | `roads` | candidate; binding pendiente |
| [azavea/raster-vision](#data-azavea--raster-vision) | `imagery` | candidate; binding pendiente |
| [Open-EO/openeo-processes](#data-open-eo--openeo-processes) | `schemas` | dependency; binding pendiente |
| [Open-EO/openeo-python-client](#data-open-eo--openeo-python-client) | `eo-process` | candidate; binding pendiente |
| [opendatacube/datacube-core](#data-opendatacube--datacube-core) | `data-cube` | candidate; binding pendiente |
| [opengeos/geoai](#data-opengeos--geoai) | `imagery` | candidate; binding pendiente |
| [opengeos/segment-geospatial](#data-opengeos--segment-geospatial) | `imagery` | candidate; binding pendiente |
| [orfeotoolbox/OTB](#data-orfeotoolbox--otb) | `imagery` | candidate; binding pendiente |
| [orfeotoolbox/pyotb](#data-orfeotoolbox--pyotb) | `imagery` | dependency; binding pendiente |
| [sentinel-hub/sentinelhub-py](#data-sentinel-hub--sentinelhub-py) | `imagery` | candidate; binding pendiente |
| [stac-utils/pystac](#data-stac-utils--pystac) | `stac` | dependency; binding pendiente |
| [stac-utils/pystac-client](#data-stac-utils--pystac-client) | `stac` | candidate; binding pendiente |
| [stac-utils/stac-fastapi](#data-stac-utils--stac-fastapi) | `stac` | candidate; binding pendiente |
| [torchgeo/torchgeo](#data-torchgeo--torchgeo) | `imagery` | candidate; binding pendiente |
| [crowddynamics/crowddynamics](#data-crowddynamics--crowddynamics) | `social` | candidate; binding pendiente |
| [MengeCrowdSim/Menge](#data-mengecrowdsim--menge) | `social` | candidate; binding pendiente |
| [PedestrianDynamics/jupedsim](#data-pedestriandynamics--jupedsim) | `social` | candidate; binding pendiente |
| [svenkreiss/socialforce](#data-svenkreiss--socialforce) | `social` | candidate; binding pendiente |
| [dss-extensions/OpenDSSDirect.py](#data-dss-extensions--opendssdirect.py) | `electrical` | candidate; binding pendiente |
| [e2nIEE/pandapower](#data-e2niee--pandapower) | `electrical` | candidate; binding pendiente |
| [NatLabRockies/REopt_API](#data-natlabrockies--reopt_api) | `electrical` | candidate; binding pendiente |
| [oemof/oemof-solph](#data-oemof--oemof-solph) | `electrical` | candidate; binding pendiente |
| [PyPSA/PyPSA](#data-pypsa--pypsa) | `electrical` | candidate; binding pendiente |
| [RWTH-EBC/uesgraphs](#data-rwth-ebc--uesgraphs) | `electrical` | dependency; binding pendiente |
| [CLIMADA-project/climada_petals](#data-climada-project--climada_petals) | `risk` | dependency; binding pendiente |
| [CLIMADA-project/climada_python](#data-climada-project--climada_python) | `risk` | candidate; binding pendiente |
| [gem/oq-engine](#data-gem--oq-engine) | `risk` | candidate; binding pendiente |
| [Universite-Gustave-Eiffel/NoiseModelling](#data-universite-gustave-eiffel--noisemodelling) | `noise` | candidate; binding pendiente |
| [duckdb/duckdb-spatial](#data-duckdb--duckdb-spatial) | `vector` | candidate; binding pendiente |
| [geopandas/geopandas](#data-geopandas--geopandas) | `vector` | candidate; binding pendiente |
| [geotools/geotools](#data-geotools--geotools) | `vector` | dependency; binding pendiente |
| [jblindsay/whitebox-tools](#data-jblindsay--whitebox-tools) | `raster` | candidate; binding pendiente |
| [locationtech/jts](#data-locationtech--jts) | `vector` | dependency; binding pendiente |
| [opengeos/whitebox-python](#data-opengeos--whitebox-python) | `raster` | dependency; binding pendiente |
| [OSGeo/gdal](#data-osgeo--gdal) | `vector` | candidate; binding pendiente |
| [OSGeo/grass](#data-osgeo--grass) | `vector` | candidate; binding pendiente |
| [OSGeo/PROJ](#data-osgeo--proj) | `vector` | dependency; binding pendiente |
| [postgis/postgis](#data-postgis--postgis) | `spatial-db` | candidate; binding pendiente |
| [qgis/QGIS](#data-qgis--qgis) | `vector` | candidate; binding pendiente |
| [r-spatial/sf](#data-r-spatial--sf) | `vector` | candidate; binding pendiente |
| [rasterio/rasterio](#data-rasterio--rasterio) | `raster` | candidate; binding pendiente |
| [rspatial/terra](#data-rspatial--terra) | `raster` | candidate; binding pendiente |
| [saga-gis/saga-gis](#data-saga-gis--saga-gis) | `raster` | candidate; binding pendiente |
| [shapely/shapely](#data-shapely--shapely) | `vector` | dependency; binding pendiente |
| [ckan/ckan](#data-ckan--ckan) | `resource-catalog` | candidate; binding pendiente |
| [geonetwork/core-geonetwork](#data-geonetwork--core-geonetwork) | `resource-catalog` | candidate; binding pendiente |
| [GeoNode/geonode](#data-geonode--geonode) | `resource-catalog` | candidate; binding pendiente |
| [geopython/pygeoapi](#data-geopython--pygeoapi) | `ogc-service` | candidate; binding pendiente |
| [geoserver/geoserver](#data-geoserver--geoserver) | `ogc-service` | candidate; binding pendiente |
| [MapServer/MapServer](#data-mapserver--mapserver) | `ogc-service` | candidate; binding pendiente |
| [gama-platform/gama](#data-gama-platform--gama) | `social` | candidate; binding pendiente |
| [mesa/mesa](#data-mesa--mesa) | `social` | candidate; binding pendiente |
| [metadriverse/metaurban](#data-metadriverse--metaurban) | `social` | candidate; binding pendiente |
| [NetLogo/NetLogo](#data-netlogo--netlogo) | `social` | candidate; binding pendiente |
| [tsinghua-fib-lab/AgentSociety](#data-tsinghua-fib-lab--agentsociety) | `social` | candidate; binding pendiente |
| [tsinghua-fib-lab/CityBench](#data-tsinghua-fib-lab--citybench) | `none` | reference; binding pendiente |
| [CesiumGS/3d-tiles-tools](#data-cesiumgs--3d-tiles-tools) | `scene` | candidate; binding pendiente |
| [CesiumGS/cesium](#data-cesiumgs--cesium) | `scene` | candidate; binding pendiente |
| [iTowns/itowns](#data-itowns--itowns) | `scene` | candidate; binding pendiente |
| [keplergl/kepler.gl](#data-keplergl--kepler.gl) | `scene` | candidate; binding pendiente |
| [maplibre/maplibre-gl-js](#data-maplibre--maplibre-gl-js) | `scene` | candidate; binding pendiente |
| [TerriaJS/terriajs](#data-terriajs--terriajs) | `scene` | candidate; binding pendiente |
| [visgl/deck.gl](#data-visgl--deck.gl) | `scene` | dependency; binding pendiente |
| [external:palm](#data-palm) | `microclimate` | candidate; binding pendiente |
| [external:telemac](#data-telemac) | `coastal` | candidate; binding pendiente |
| [external:simstadt](#data-simstadt) | `urban-energy` | candidate; binding pendiente |

<a id="data-deltares--delft3d"></a>

## Deltares/Delft3D

- **Interfaz original:** Archivos de caso y ejecutables originales.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| mesh | bathymetry and computational mesh | [GEBCO bathymetry catalog](https://www.gebco.net/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | survey accuracy and vertical datum |
| forcing | flow/tide/wave series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | matching boundary/time/units |
| parameters | model configuration | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | turbulence, friction and module fixed |

- **Preparación que hay que resolver:** Use upstream mesh/case preparation; document boundary mapping and selected solver module.
- **Validación requerida:** Mesh quality, boundaries, datums, temporal alignment and reference-case diagnostics.
- **Faltante para un caso real:** Global bathymetry is not a harbor survey; field forcing and calibration may be required.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir solver ni inferir batimetría o condiciones de borde.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-deltares--hydromt"></a>

## Deltares/hydromt

- **Interfaz original:** API y CLI HydroMT.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| terrain | terrain raster/mesh | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | terrain versus surface and vertical datum checked |
| land | landcover/roughness | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar) | classes translated with documented coefficients |
| forcing | rainfall/inflow/boundary series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | event and units fixed |

- **Preparación que hay que resolver:** Prepare using native tools/HydroMT, record resampling, grid, boundary conditions and coefficients.
- **Validación requerida:** Vertical/horizontal CRS, resolution fitness, wet/dry references, timestep and mass balance.
- **Faltante para un caso real:** Coarse surface products and reanalysis do not automatically support street-scale calibrated flood predictions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentarlo como solver; los plugins tienen versiones y requisitos propios.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-deltares--hydromt_sfincs"></a>

## Deltares/hydromt_sfincs

- **Interfaz original:** Configuración HydroMT y API del plugin.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| terrain | terrain raster/mesh | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | terrain versus surface and vertical datum checked |
| land | landcover/roughness | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar) | classes translated with documented coefficients |
| forcing | rainfall/inflow/boundary series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | event and units fixed |

- **Preparación que hay que resolver:** Prepare using native tools/HydroMT, record resampling, grid, boundary conditions and coefficients.
- **Validación requerida:** Vertical/horizontal CRS, resolution fitness, wet/dry references, timestep and mass balance.
- **Faltante para un caso real:** Coarse surface products and reanalysis do not automatically support street-scale calibrated flood predictions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuirle ejecución ni calibración del solver SFINCS.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-deltares--hydromt_wflow"></a>

## Deltares/hydromt_wflow

- **Interfaz original:** HydroMT y configuración del plugin.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| catchment | basin/river/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology and routing model |
| land | terrain/soil/cover | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); [ESA WorldCover](https://esa-worldcover.org/en); Municipality, utility, transit agency or project owner (por configurar) | resolution and parameter conversion |
| forcing | rainfall/evaporation series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | variables, units and timestep |

- **Preparación que hay que resolver:** Use the selected hydrological model/plugin; record basin delineation, parameters and forcing conversion.
- **Validación requerida:** Basin topology, units, temporal completeness, water balance and calibration diagnostics.
- **Faltante para un caso real:** A hydrological runoff model does not automatically produce street inundation depths.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar el modelo hidrológico ni asumir que datos globales lo calibran.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-deltares--sfincs"></a>

## Deltares/SFINCS

- **Interfaz original:** Ejecutable y archivos de caso; preparación separada.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| terrain | terrain raster/mesh | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | terrain versus surface and vertical datum checked |
| land | landcover/roughness | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar) | classes translated with documented coefficients |
| forcing | rainfall/inflow/boundary series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | event and units fixed |

- **Preparación que hay que resolver:** Prepare using native tools/HydroMT, record resampling, grid, boundary conditions and coefficients.
- **Validación requerida:** Vertical/horizontal CRS, resolution fitness, wet/dry references, timestep and mass balance.
- **Faltante para un caso real:** Coarse surface products and reanalysis do not automatically support street-scale calibrated flood predictions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No inventar datos de terreno, lluvia o fronteras; validar distribución binaria.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-geoscienceaustralia--anuga_core"></a>

## GeoscienceAustralia/anuga_core

- **Interfaz original:** API Python ANUGA y extensiones compiladas.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| terrain | terrain raster/mesh | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | terrain versus surface and vertical datum checked |
| land | landcover/roughness | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar) | classes translated with documented coefficients |
| forcing | rainfall/inflow/boundary series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | event and units fixed |

- **Preparación que hay que resolver:** Prepare using native tools/HydroMT, record resampling, grid, boundary conditions and coefficients.
- **Validación requerida:** Vertical/horizontal CRS, resolution fitness, wet/dry references, timestep and mass balance.
- **Faltante para un caso real:** Coarse surface products and reanalysis do not automatically support street-scale calibrated flood predictions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir esquema numérico ni vender una malla como modelo calibrado.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-markuspic--swmm_api"></a>

## MarkusPic/swmm_api

- **Interfaz original:** API Python de archivos INP, reportes y salidas.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | base revision and physical bounds |

- **Preparación que hay que resolver:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validación requerida:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Faltante para un caso real:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar PySWMM ni prometer control temporal por editar un archivo.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-openstreams--wflow"></a>

## openstreams/wflow

- **Interfaz original:** Scripts y configuraciones propios; verificar versión vigente.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| catchment | basin/river/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology and routing model |
| land | terrain/soil/cover | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); [ESA WorldCover](https://esa-worldcover.org/en); Municipality, utility, transit agency or project owner (por configurar) | resolution and parameter conversion |
| forcing | rainfall/evaporation series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | variables, units and timestep |

- **Preparación que hay que resolver:** Use the selected hydrological model/plugin; record basin delineation, parameters and forcing conversion.
- **Validación requerida:** Basin topology, units, temporal completeness, water balance and calibration diagnostics.
- **Faltante para un caso real:** A hydrological runoff model does not automatically produce street inundation depths.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir este repositorio con todas las versiones actuales de wflow.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-openwateranalytics--epanet"></a>

## OpenWaterAnalytics/EPANET

- **Interfaz original:** Biblioteca C/toolkit y distribuciones originales.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | EPANET INP | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology, diameters, elevations, demands, pumps and controls |
| scenario | demand/pump/quality parameters | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units and time pattern explicit |

- **Preparación que hay que resolver:** Preserve native network and parameter sets, separate hypothetical interventions and measurement provenance.
- **Validación requerida:** Connectivity, hydraulic units, demand patterns, controls, solver status and mass/energy checks.
- **Faltante para un caso real:** Pipe inventory, demand and operating controls normally require the utility/project owner.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reescribir hidráulica; distinguir binding, motor y editor gráfico.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pyswmm--pyswmm"></a>

## pyswmm/pyswmm

- **Interfaz original:** API Python y motor asociado.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | base revision and physical bounds |

- **Preparación que hay que resolver:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validación requerida:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Faltante para un caso real:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar simulación ni elegirlo además de otro wrapper sin necesidad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-usepa--epanet2.2"></a>

## USEPA/EPANET2.2

- **Interfaz original:** Ejecutable/editor y archivos INP.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | EPANET INP | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology, diameters, elevations, demands, pumps and controls |
| scenario | demand/pump/quality parameters | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units and time pattern explicit |

- **Preparación que hay que resolver:** Preserve native network and parameter sets, separate hypothetical interventions and measurement provenance.
- **Validación requerida:** Connectivity, hydraulic units, demand patterns, controls, solver status and mass/energy checks.
- **Faltante para un caso real:** Pipe inventory, demand and operating controls normally require the utility/project owner.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No sumar otro motor hidráulico por confundir editor con toolkit.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-usepa--stormwater-management-model"></a>

## USEPA/Stormwater-Management-Model

- **Interfaz original:** Toolkit o ejecutable nativo.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | base revision and physical bounds |

- **Preparación que hay que resolver:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validación requerida:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Faltante para un caso real:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir un segundo solver; no duplicar la envoltura si ya cubre el caso.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-usepa--wntr"></a>

## USEPA/WNTR

- **Interfaz original:** API Python y conexión EPANET.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | EPANET INP | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology, diameters, elevations, demands, pumps and controls |
| scenario | demand/pump/quality parameters | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units and time pattern explicit |

- **Preparación que hay que resolver:** Preserve native network and parameter sets, separate hypothetical interventions and measurement provenance.
- **Validación requerida:** Connectivity, hydraulic units, demand patterns, controls, solver status and mass/energy checks.
- **Faltante para un caso real:** Pipe inventory, demand and operating controls normally require the utility/project owner.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir sus simuladores ni presentar fallas hipotéticas como observaciones.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-blender--blender"></a>

## blender/blender

- **Interfaz original:** API bpy en Blender y ejecución por proceso/plugin.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir editor; geometría visual no equivale a BIM ni simulación física.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-buildingsmart--bcf-xml"></a>

## buildingSMART/BCF-XML

- **Interfaz original:** Esquemas BCF y archivos de intercambio.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| issues | BCF package | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); [buildingSMART Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) | model revision and element references |
| model | IFC/reference | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | GUID mapping available |

- **Preparación que hay que resolver:** Validate schema and references and retain comment/issue authorship and revision.
- **Validación requerida:** Resolvable components, model version, geometry viewpoint units and permissions.
- **Faltante para un caso real:** Issue data and model access are project-provided.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir una especificación en motor ni duplicar gestión de incidencias existente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-buildingsmart--ids"></a>

## buildingSMART/IDS

- **Interfaz original:** XML y validadores compatibles por seleccionar.
- **Alcance de esta ficha:** dependency. Requirements file plus IFC and a selected validator; schema documents are not a standalone solver.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | IFC | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); [buildingSMART Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) | schema, GUIDs, units and georeferencing |
| requirements | IDS or project constraints | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | requirements identify exact model revision |

- **Preparación que hay que resolver:** Validate IFC, map only explicit properties, preserve GUIDs and express losses in any conversion.
- **Validación requerida:** Schema version, units, geometry, references, georeferencing and required fields.
- **Faltante para un caso real:** Public footprints do not provide building systems, materials or a valid IFC model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No afirmar cumplimiento normativo general por pasar un IDS.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-compas-dev--compas"></a>

## compas-dev/compas

- **Interfaz original:** API Python COMPAS.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No publicar toda la API ni atribuirle validación estructural universal.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-compas-dev--compas_fab"></a>

## compas-dev/compas_fab

- **Interfaz original:** API Python y backends de robótica.
- **Alcance de esta ficha:** candidate. Simulation-only planning requires robot/backend configuration; no hardware actuation admitted by this inventory.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No añadir operación de robots al alcance urbano por compartir geometría.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-dynamods--dynamo"></a>

## DynamoDS/Dynamo

- **Interfaz original:** Host de Dynamo y grafos; verificar ejecución automatizable.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir que todo nodo funciona fuera de su aplicación anfitriona.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-freecad--freecad"></a>

## FreeCAD/FreeCAD

- **Interfaz original:** API Python, FreeCADCmd y sesión gráfica.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir CAD; modelado libre y referencias topológicas requieren control.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ifcopenshell--ifcopenshell"></a>

## IfcOpenShell/IfcOpenShell

- **Interfaz original:** API Python/C++ y utilidades existentes.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | IFC | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); [buildingSMART Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) | schema, GUIDs, units and georeferencing |
| requirements | IDS or project constraints | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | requirements identify exact model revision |

- **Preparación que hay que resolver:** Validate IFC, map only explicit properties, preserve GUIDs and express losses in any conversion.
- **Validación requerida:** Schema version, units, geometry, references, georeferencing and required fields.
- **Faltante para un caso real:** Public footprints do not provide building systems, materials or a valid IFC model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reimplementar parser IFC ni inferir propiedades técnicas faltantes.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-openscad--openscad"></a>

## openscad/openscad

- **Interfaz original:** CLI y archivos de modelo.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No generar código irrestricto ni tratar sólidos como objetos BIM completos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pixaranimationstudios--openusd"></a>

## PixarAnimationStudios/OpenUSD

- **Interfaz original:** Bibliotecas y bindings USD.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir USD en modelo de autoridad urbana o inventar semántica IFC.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-specklesystems--speckle-server"></a>

## specklesystems/speckle-server

- **Interfaz original:** API de la instancia y autenticación correspondiente.
- **Alcance de esta ficha:** candidate. Use authorized project/model/version IDs and native object data, not a STAC contract; instance API binding is pending.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| instance | project/model/version API | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | scope, native object protocol and credentials |
| objects | native object graph/artifact references | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | IDs, units and version ancestry |

- **Preparación que hay que resolver:** Preserve the native object graph, authorize the project and record serialization/conversion losses.
- **Validación requerida:** Project scope, object IDs, versions, units, permissions and round trip.
- **Faltante para un caso real:** A catalog protocol cannot substitute the native Speckle object/project contract.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir colaboración; verificar API y conectores de la versión instalada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-specklesystems--specklepy"></a>

## specklesystems/specklepy

- **Interfaz original:** SDK Python.
- **Alcance de esta ficha:** dependency. Dependency of the Speckle connector; native project/object/version contract replaces generic catalog fields.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| instance | project/model/version API | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | scope, native object protocol and credentials |
| objects | native object graph/artifact references | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | IDs, units and version ancestry |

- **Preparación que hay que resolver:** Preserve the native object graph, authorize the project and record serialization/conversion losses.
- **Validación requerida:** Project scope, object IDs, versions, units, permissions and round trip.
- **Faltante para un caso real:** A catalog protocol cannot substitute the native Speckle object/project contract.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otra plataforma ni servidor MCP por cada SDK.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-apa-technology-division--urban-and-regional-planning-resources"></a>

## APA-Technology-Division/urban-and-regional-planning-resources

- **Interfaz original:** Documentos y enlaces del catálogo.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| references | urls | Original format/schema specifications (por configurar) | verify identity and date |

- **Preparación que hay que resolver:** Catalog only; no solver input or invented runtime.
- **Validación requerida:** Links, provenance and classification.
- **Faltante para un caso real:** Not an executable capability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No anunciar cada enlace como integración disponible.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-durbanitas--awesome-urban-planning"></a>

## durbanitas/awesome-urban-planning

- **Interfaz original:** Archivos documentales.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| references | urls | Original format/schema specifications (por configurar) | verify identity and date |

- **Preparación que hay que resolver:** Catalog only; no solver input or invented runtime.
- **Validación requerida:** Links, provenance and classification.
- **Faltante para un caso real:** Not an executable capability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No equiparar popularidad o inclusión en la lista con aptitud técnica.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ireliya--awesome-urban-planning-agents"></a>

## Ireliya/Awesome-Urban-Planning-Agents

- **Interfaz original:** Catálogo y enlaces a implementaciones.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| references | urls | Original format/schema specifications (por configurar) | verify identity and date |

- **Preparación que hay que resolver:** Catalog only; no solver input or invented runtime.
- **Validación requerida:** Links, provenance and classification.
- **Faltante para un caso real:** Not an executable capability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir un agente completo con una herramienta neutral para cualquier IA.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-sacridini--awesome-geospatial"></a>

## sacridini/Awesome-Geospatial

- **Interfaz original:** Documentos y enlaces.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| references | urls | Original format/schema specifications (por configurar) | verify identity and date |

- **Preparación que hay que resolver:** Catalog only; no solver input or invented runtime.
- **Validación requerida:** Links, provenance and classification.
- **Faltante para un caso real:** Not an executable capability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No prometer cobertura operativa de todos sus enlaces.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-kunifujiwara--voxcity"></a>

## kunifujiwara/VoxCity

- **Interfaz original:** API Python y proveedores de datos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (por configurar) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | no inferred physics without declaration |

- **Preparación que hay que resolver:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validación requerida:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Faltante para un caso real:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir estimaciones de geometría o vegetación en levantamiento observado.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ladybug-tools--uwg"></a>

## ladybug-tools/uwg

- **Interfaz original:** API Python y archivos meteorológicos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| series | weather/EPW | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); [NASA POWER](https://power.larc.nasa.gov/docs/services/api/); [ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | variable definition, interval and status |
| site | location and site parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | CRS, altitude and timezone |

- **Preparación que hay que resolver:** Translate formats explicitly; record timezone, resampling and observed/modelled/TMY distinction.
- **Validación requerida:** Coverage, variable units, missing values, calendar and station/grid representativeness.
- **Faltante para un caso real:** TMY and gridded reanalysis are not measurements of a chosen local event.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentarlo como CFD ni clima local validado sin parámetros adecuados.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-openfoam--openfoam-dev"></a>

## OpenFOAM/OpenFOAM-dev

- **Interfaz original:** Casos, diccionarios y ejecutables nativos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | watertight simulation geometry and mesh | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | domain, mesh quality and scale |
| conditions | boundary/initial conditions | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | velocity, turbulence, material and units |
| solver | case and numerical configuration | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | version and convergence criteria |

- **Preparación que hay que resolver:** Use native mesher/solver tools; separate geometry preparation from physical case validation.
- **Validación requerida:** Boundary completeness, mesh metrics, dimensions, timestep, residuals and conservation/reference fields.
- **Faltante para un caso real:** A display scene or OSM model does not provide a valid CFD mesh or calibrated conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No generar un CFD defendible solo a partir de edificios OSM.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-udales--u-dales"></a>

## uDALES/u-dales

- **Interfaz original:** Compilación y configuración del modelo.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| domain | mesh/domain/land inputs | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | nested grid and physics configuration |
| forcing | atmospheric initial/boundary data | [NCAR atmospheric forcing catalog](https://gdex.ucar.edu/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | full required variables and time |
| parameters | physics and model configuration | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | compiler/MPI/model compatibility |

- **Preparación que hay que resolver:** Keep upstream preprocessing and domain nesting; record forcing source and conversion chain.
- **Validación requerida:** Domain boundaries, vertical levels, forcing completeness, timestep and reference diagnostics.
- **Faltante para un caso real:** Surface ERA5-Land alone is not a full atmospheric initialization dataset.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir simulación de alta resolución con datos disponibles para cualquier ciudad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-umep-dev--solweig"></a>

## UMEP-dev/solweig

- **Interfaz original:** Entradas y ejecutor del proyecto; contrastar ruta UMEP.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (por configurar) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | no inferred physics without declaration |

- **Preparación que hay que resolver:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validación requerida:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Faltante para un caso real:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No mantener dos versiones de SOLWEIG por separado sin necesidad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-umep-dev--suews"></a>

## UMEP-dev/SUEWS

- **Interfaz original:** Configuración, forzamientos y wrapper admitido.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (por configurar) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | no inferred physics without declaration |

- **Preparación que hay que resolver:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validación requerida:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Faltante para un caso real:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No sustituir calibración, meteorología ni parámetros de superficie.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-umep-dev--umep"></a>

## UMEP-dev/UMEP

- **Interfaz original:** Plugin y algoritmos que exponga la versión instalada.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (por configurar) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | no inferred physics without declaration |

- **Preparación que hay que resolver:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validación requerida:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Faltante para un caso real:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir que todos los módulos corren sin escritorio.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-umep-dev--umep-processing"></a>

## UMEP-dev/UMEP-processing

- **Interfaz original:** Registro de algoritmos QGIS Processing.
- **Alcance de esta ficha:** candidate. Each Processing algorithm selects a subset of climate inputs; no universal UMEP input bundle is claimed.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (por configurar) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | no inferred physics without declaration |

- **Preparación que hay que resolver:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validación requerida:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Faltante para un caso real:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir un MCP climático paralelo si el conector QGIS ya sirve el algoritmo.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-usepa--cmaq"></a>

## USEPA/CMAQ

- **Interfaz original:** Compilación, casos y forzamientos del sistema.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| meteorology | model-ready meteorological fields | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | selected chemistry/model grid |
| emissions | speciated spatial/temporal inventory | [JRC EDGAR emissions](https://edgar.jrc.ec.europa.eu/); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | conversion and sector assumptions |
| chemistry | mechanism/boundaries | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | compatible version and units |

- **Preparación que hay que resolver:** Use upstream preprocessing, explicit speciation/temporalization and emission-grid mapping.
- **Validación requerida:** Species, units, grids, meteorological coverage and mass/chemistry diagnostics.
- **Faltante para un caso real:** Global emissions inventory is not automatically a street-level or model-ready local inventory.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No simular calidad de aire sin inventarios de emisiones y meteorología compatibles.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-wrf-model--wrf"></a>

## wrf-model/WRF

- **Interfaz original:** Ejecutables WRF y cadena de preprocesamiento correspondiente.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| domain | mesh/domain/land inputs | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | nested grid and physics configuration |
| forcing | atmospheric initial/boundary data | [NCAR atmospheric forcing catalog](https://gdex.ucar.edu/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | full required variables and time |
| parameters | physics and model configuration | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | compiler/MPI/model compatibility |

- **Preparación que hay que resolver:** Keep upstream preprocessing and domain nesting; record forcing source and conversion chain.
- **Validación requerida:** Domain boundaries, vertical levels, forcing completeness, timestep and reference diagnostics.
- **Faltante para un caso real:** Surface ERA5-Land alone is not a full atmospheric initialization dataset.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No prometer predicción urbana lista sin condiciones iniciales y configuración física.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-eclipse-ditto--ditto"></a>

## eclipse-ditto/ditto

- **Interfaz original:** API HTTP/WebSocket de una instancia Ditto.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No sustituir su política ni confundir twin IoT con modelo urbano geográfico.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-fiware--context.orion-ld"></a>

## FIWARE/context.Orion-LD

- **Interfaz original:** API NGSI-LD de una instancia.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No inventar un broker ni convertir automáticamente modelos incompatibles.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-fiware--tutorials.step-by-step"></a>

## FIWARE/tutorials.Step-by-Step

- **Interfaz original:** Documentos, ejemplos y recetas.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| references | urls | Original format/schema specifications (por configurar) | verify identity and date |

- **Preparación que hay que resolver:** Catalog only; no solver input or invented runtime.
- **Validación requerida:** Links, provenance and classification.
- **Faltante para un caso real:** Not an executable capability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No contar cada tutorial como producto integrado ni copiar secretos de ejemplo.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-fraunhoferiosb--frost-server"></a>

## FraunhoferIOSB/FROST-Server

- **Interfaz original:** API SensorThings de la instancia.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar almacenamiento ni perder relaciones Sensor/Datastream/Observation.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-scorpiobroker--scorpiobroker"></a>

## ScorpioBroker/ScorpioBroker

- **Interfaz original:** API de la instancia Scorpio.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No instalarlo junto con Orion-LD por defecto; evaluar capacidades requeridas.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-smart-data-models--data-models"></a>

## smart-data-models/data-models

- **Interfaz original:** Esquemas y contextos seleccionados.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| schema | IDS/BCF/NGSI-LD/openEO definitions | Original format/schema specifications (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | exact version and profile |
| instance | data/model being validated | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | references and IDs preserved |

- **Preparación que hay que resolver:** Use maintained validator and explicit profile, report unresolved references.
- **Validación requerida:** Schema version, reference resolution, units and semantic requirements where defined.
- **Faltante para un caso real:** Schema validity is not scientific validity or evidence that a backend implements every operation.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No tratar nombres de entidades iguales como equivalencia semántica garantizada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-telefonicaid--fiware-orion"></a>

## telefonicaid/fiware-orion

- **Interfaz original:** API NGSIv2.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No etiquetar NGSIv2 como NGSI-LD ni ocultar pérdida semántica.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-thingsboard--thingsboard"></a>

## thingsboard/thingsboard

- **Interfaz original:** REST/telemetría de la instalación; revisar edición.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No mezclar funciones de ediciones distintas ni eludir permisos de dispositivo.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-hpscil--open-space-cellular_automata"></a>

## HPSCIL/Open-Space-Cellular_Automata

- **Interfaz original:** Código/datos reales pendientes de identificar.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No vender una referencia académica como motor mantenible.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-johanlahti--urban-lu-model"></a>

## johanlahti/urban-lu-model

- **Interfaz original:** Scripts, configuración y datos del proyecto.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No inferir aptitud actual ni extrapolar parámetros de otra ciudad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-landinsightlab--muse"></a>

## LandInsightLab/MUSE

- **Interfaz original:** Interfaz y configuraciones Python por revisar.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir simulación de uso del suelo con resultado normativo o causal.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-udst--choicemodels"></a>

## UDST/choicemodels

- **Interfaz original:** API Python.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuir causalidad ni validez local por ajustar un modelo.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-udst--developer"></a>

## UDST/developer

- **Interfaz original:** API Python y tablas del modelo.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentar supuestos de factibilidad como valuación o permisos aprobados.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-udst--orca"></a>

## UDST/orca

- **Interfaz original:** API y registro de pasos Orca.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No desarrollar otro scheduler que replique los pasos internos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-udst--urbansim"></a>

## UDST/urbansim

- **Interfaz original:** API Python y configuración de modelos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear un modelo de ciudad sin población, parcelas, estimación y calibración.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-udst--urbansim_defaults"></a>

## UDST/urbansim_defaults

- **Interfaz original:** Paquetes/tablas del proyecto.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No instalar defaults como modelo válido de cualquier municipio.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-udst--urbansim_templates"></a>

## UDST/urbansim_templates

- **Interfaz original:** API/configuraciones de plantillas.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | choice/feasibility assumptions |

- **Preparación que hay que resolver:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validación requerida:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Faltante para un caso real:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otra herramienta por cada plantilla ni prometer interoperabilidad entre versiones.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cityscope--cs_cityio"></a>

## CityScope/CS_CityIO

- **Interfaz original:** API del servidor CityIO.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir que todas las tablas comparten esquema o que una propuesta es dato observado.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cityscope--cs_cityscopejs"></a>

## CityScope/CS_cityscopeJS

- **Interfaz original:** Componentes y API del cliente.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar CityIO ni añadir un visor obligatorio al producto MCP.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cityscope--cs_cityscopy"></a>

## CityScope/CS_CityScoPy

- **Interfaz original:** SDK/API Python.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No desplegar otro servidor solo por existir un cliente Python.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cityscope--cs_mobility_service"></a>

## CityScope/CS_Mobility_Service

- **Interfaz original:** Código y contratos de la versión elegida.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | zones and skims compatible |

- **Preparación que hay que resolver:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validación requerida:** Control totals, missingness, joins, weights and model diagnostics.
- **Faltante para un caso real:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No llamar servicio productivo a un notebook ni inventar demanda.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cityscope--cs_simulation_gama"></a>

## CityScope/CS_Simulation_GAMA

- **Interfaz original:** Modelos GAML y ruta de intercambio CityScope.
- **Alcance de esta ficha:** dependency. CityIO table mapping plus GAML model/population parameters are required; context entities alone cannot run the model.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | semantics and transforms explicit |

- **Preparación que hay que resolver:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validación requerida:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Faltante para un caso real:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuir resultados de ese modelo a toda ciudad o a cualquier versión GAMA.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-consuldemocracy--consuldemocracy"></a>

## consuldemocracy/consuldemocracy

- **Interfaz original:** APIs y extensiones admitidas por la instalación.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| process | authorized process/project reference | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | permissions and actual API capabilities |
| contribution | explicit contribution with provenance | Authorized files supplied for the case (por configurar); Municipality, utility, transit agency or project owner (por configurar) | authorship and intended submission |

- **Preparación que hay que resolver:** Use platform API; keep drafts separate from submissions and link to scenario only when authorized.
- **Validación requerida:** Process status, scope, identity, receipt and read-back.
- **Faltante para un caso real:** There is no universal public write endpoint or permission to speak/vote for participants.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No automatizar identidad, voto o decisiones ciudadanas ni reemplazar el proceso.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-decidim--decidim"></a>

## decidim/decidim

- **Interfaz original:** API disponible y extensiones Rails específicas.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| process | authorized process/project reference | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | permissions and actual API capabilities |
| contribution | explicit contribution with provenance | Authorized files supplied for the case (por configurar); Municipality, utility, transit agency or project owner (por configurar) | authorship and intended submission |

- **Preparación que hay que resolver:** Use platform API; keep drafts separate from submissions and link to scenario only when authorized.
- **Validación requerida:** Process status, scope, identity, receipt and read-back.
- **Faltante para un caso real:** There is no universal public write endpoint or permission to speak/vote for participants.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No inventar receptor ni pasar propuestas del agente por opiniones ciudadanas.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-umap-project--umap"></a>

## umap-project/umap

- **Interfaz original:** API/exportaciones de la instancia y GeoJSON.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| process | authorized process/project reference | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | permissions and actual API capabilities |
| contribution | explicit contribution with provenance | Authorized files supplied for the case (por configurar); Municipality, utility, transit agency or project owner (por configurar) | authorship and intended submission |

- **Preparación que hay que resolver:** Use platform API; keep drafts separate from submissions and link to scenario only when authorized.
- **Validación requerida:** Process status, scope, identity, receipt and read-back.
- **Faltante para un caso real:** There is no universal public write endpoint or permission to speak/vote for participants.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar editor ni asumir API de edición pública por tener exportación.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-martibosch--pylandstats"></a>

## martibosch/pylandstats

- **Interfaz original:** API Python.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| classes | categorical raster | [ESA WorldCover](https://esa-worldcover.org/en); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | class scheme, resolution and extent |
| parameters | metric definitions/coefficients | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood and ecological interpretation |

- **Preparación que hay que resolver:** Translate class schemes and grid definition explicitly; preserve metric definition.
- **Validación requerida:** Class codes, nodata, pixel area, neighborhood, extent and reference metrics.
- **Faltante para un caso real:** Landscape pattern does not automatically establish ecological function or observed biodiversity.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir métricas de patrón espacial en biodiversidad observada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-natcap--invest"></a>

## natcap/invest

- **Interfaz original:** API/modelos y paquetes de datos específicos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| land | landcover and environmental layers | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | required model layers |
| coefficients | biophysical tables/valuation assumptions | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | local applicability |
| forcing | model-specific climate/hydrology | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | explicit selected InVEST model |

- **Preparación que hay que resolver:** Select one upstream model, prepare its tables and layers and record assumptions.
- **Validación requerida:** Each model input specification, coverage, units and reference outputs.
- **Faltante para un caso real:** Coefficients, observations and local validation are not supplied by a generic global raster.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No generar servicios ecosistémicos sin coeficientes/datos locales ni duplicar modelos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-natcap--pygeoprocessing"></a>

## natcap/pygeoprocessing

- **Interfaz original:** API Python y dependencias GDAL.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar) | band meaning, nodata and resolution explicit |

- **Preparación que hay que resolver:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validación requerida:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Faltante para un caso real:** An available raster can be unsuitable for the intended analysis.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear un MCP separado por una biblioteca auxiliar.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-r-spatialecology--landscapemetrics"></a>

## r-spatialecology/landscapemetrics

- **Interfaz original:** API R.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| classes | categorical raster | [ESA WorldCover](https://esa-worldcover.org/en); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | class scheme, resolution and extent |
| parameters | metric definitions/coefficients | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood and ecological interpretation |

- **Preparación que hay que resolver:** Translate class schemes and grid definition explicitly; preserve metric definition.
- **Validación requerida:** Class codes, nodata, pixel area, neighborhood, extent and reference metrics.
- **Faltante para un caso real:** Landscape pattern does not automatically establish ecological function or observed biodiversity.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No exponer simultáneamente métricas homónimas de otra biblioteca como equivalentes.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-architecture-building-systems--cityenergyanalyst"></a>

## architecture-building-systems/CityEnergyAnalyst

- **Interfaz original:** Scripts/API CEA y estructura de escenario.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otro UBEM ni asumir edificios y usos completos en cualquier ciudad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-betalab-team--eureca"></a>

## BETALAB-team/EUReCA

- **Interfaz original:** API/ejecutor Python EUReCA.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No tratar aproximaciones de arquetipos como datos observados ni duplicar CEA sin caso.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-kth-urbant--mubes-ubem"></a>

## KTH-UrbanT/mubes-ubem

- **Interfaz original:** Ejecutor Python y EnergyPlus de la versión elegida.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No sumar otro frontend energético antes de demostrar diferencia frente a CEA/URBANopt.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ladybug-tools--dragonfly-core"></a>

## ladybug-tools/dragonfly-core

- **Interfaz original:** API Python y formatos nativos.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No vender conversión geométrica como simulación energética.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ladybug-tools--dragonfly-energy"></a>

## ladybug-tools/dragonfly-energy

- **Interfaz original:** API y CLI de Dragonfly Energy.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir traductor ni ocultar pérdida de detalle entre representaciones.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ladybug-tools--honeybee-core"></a>

## ladybug-tools/honeybee-core

- **Interfaz original:** API Python y HBJSON.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar esquema de edificios ni tratar toda geometría IFC como térmica.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ladybug-tools--honeybee-energy"></a>

## ladybug-tools/honeybee-energy

- **Interfaz original:** API/CLI y herramientas energéticas admitidas.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuir certificación o calibración por lograr una corrida.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ladybug-tools--honeybee-radiance"></a>

## ladybug-tools/honeybee-radiance

- **Interfaz original:** API/CLI de recetas y motor Radiance externo.
- **Alcance de esta ficha:** candidate. Lighting requires sensors/materials/sky recipe, not necessarily HVAC; bind a separate daylight case.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | Honeybee/Radiance scene | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | surfaces, optical materials and scene units |
| sky | sky/weather recipe | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | time, location and recipe |
| receivers | sensor grid and parameters | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | orientation, spacing and result units |

- **Preparación que hay que resolver:** Use native Radiance/Honeybee recipe and preserve sensor IDs and execution parameters.
- **Validación requerida:** Scene geometry, material definitions, sky, sensor orientation and known light result.
- **Faltante para un caso real:** A footprint or HVAC model is not a complete daylight scene.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reimplementar trazado ni reutilizar parámetros entre estudios sin validación.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ladybug-tools--ladybug"></a>

## ladybug-tools/ladybug

- **Interfaz original:** API Python y estructuras meteorológicas.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| series | weather/EPW | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); [NASA POWER](https://power.larc.nasa.gov/docs/services/api/); [ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | variable definition, interval and status |
| site | location and site parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | CRS, altitude and timezone |

- **Preparación que hay que resolver:** Translate formats explicitly; record timezone, resampling and observed/modelled/TMY distinction.
- **Validación requerida:** Coverage, variable units, missing values, calendar and station/grid representativeness.
- **Faltante para un caso real:** TMY and gridded reanalysis are not measurements of a chosen local event.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otra API meteorológica superpuesta ni inferir confort completo con una métrica.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-natlabrockies--comstock"></a>

## NatLabRockies/ComStock

- **Interfaz original:** Workflows, medidas y datos propios del proyecto.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No trasladar stock/arquetipos estadounidenses como representación de otra ciudad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-natlabrockies--energyplus"></a>

## NatLabRockies/EnergyPlus

- **Interfaz original:** Ejecutable y API oficial de EnergyPlus.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear simulador propio ni usar un IDF incompatible con su versión.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-natlabrockies--openstudio"></a>

## NatLabRockies/OpenStudio

- **Interfaz original:** CLI, bindings y medidas compatibles.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir SDK ni asumir compatibilidad entre cualquier OpenStudio y EnergyPlus.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-natlabrockies--openstudio-hpxml"></a>

## NatLabRockies/OpenStudio-HPXML

- **Interfaz original:** Medidas Ruby y ejecutor OpenStudio.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No rehacer conversor ni confundir cumplimiento XML con validez del edificio.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-natlabrockies--resstock"></a>

## NatLabRockies/resstock

- **Interfaz original:** Workflows y muestreo del proyecto.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No extrapolar stock estadounidense a cualquier municipio sin adaptación científica.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-rwth-ebc--teaser"></a>

## RWTH-EBC/TEASER

- **Interfaz original:** API Python y exportaciones Modelica.
- **Alcance de esta ficha:** candidate. Produces models (e.g. Modelica) requiring another admitted simulator; EnergyPlus formats are not assumed equivalent.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No afirmar que exportar Modelica ya ejecuta o valida el modelo.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-samuelduchesne--archetypal"></a>

## samuelduchesne/archetypal

- **Interfaz original:** API/CLI Python y dependencia EnergyPlus.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No mantener otro simulador; comprobar compatibilidad del paquete con EnergyPlus.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-samuelduchesne--geomeppy"></a>

## samuelduchesne/geomeppy

- **Interfaz original:** API Python sobre eppy.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir geometría sintética en envolvente térmica completa.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-santoshphilip--eppy"></a>

## santoshphilip/eppy

- **Interfaz original:** API Python y diccionario de versión.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reescribir lector IDF ni usar diccionario de otra versión.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ucl--simstock"></a>

## UCL/simstock

- **Interfaz original:** API Python y pipeline SimStock.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir que huellas urbanas bastan para deducir usos y construcciones.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-urbanopt--urbanopt-cli"></a>

## urbanopt/urbanopt-cli

- **Interfaz original:** CLI Ruby y estructura GeoJSON/workflows.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No ejecutar cualquier proyecto descargado ni duplicar CityEnergyAnalyst sin requisito.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-urbanopt--urbanopt-example-geojson-project"></a>

## urbanopt/urbanopt-example-geojson-project

- **Interfaz original:** Archivos GeoJSON, workflows y medidas de ejemplo.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No contar el ejemplo como otro motor o como escenario real de una ciudad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-urbanopt--urbanopt-reopt-gem"></a>

## urbanopt/urbanopt-reopt-gem

- **Interfaz original:** Gem Ruby y servicio/ejecutor REopt correspondiente.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | objective and solver stated |

- **Preparación que hay que resolver:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validación requerida:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Faltante para un caso real:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar REopt ni atribuir rentabilidad cierta a un escenario.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cloudcompare--cloudcompare"></a>

## CloudCompare/CloudCompare

- **Interfaz original:** CLI y herramientas de la aplicación.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| cloud | LAS/LAZ/PLY/point cloud | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | scale, origin, CRS and acquisition metadata |
| pipeline | native processing parameters | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | filters and tolerances explicit |

- **Preparación que hay que resolver:** Run native pipeline, subset without losing coordinate metadata and export artifact references.
- **Validación requerida:** Point count, CRS, precision, classification, transform and known-geometry checks.
- **Faltante para un caso real:** Local survey coverage and acquisition quality are project-specific.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir registro de nubes ni perder CRS/escalas globales.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-isl-org--open3d"></a>

## isl-org/Open3D

- **Interfaz original:** API Python/C++ de Open3D.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| cloud | LAS/LAZ/PLY/point cloud | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | scale, origin, CRS and acquisition metadata |
| pipeline | native processing parameters | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | filters and tolerances explicit |

- **Preparación que hay que resolver:** Run native pipeline, subset without losing coordinate metadata and export artifact references.
- **Validación requerida:** Point count, CRS, precision, classification, transform and known-geometry checks.
- **Faltante para un caso real:** Local survey coverage and acquisition quality are project-specific.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentar registro aproximado como levantamiento topográfico certificado.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pdal--pdal"></a>

## PDAL/PDAL

- **Interfaz original:** CLI y pipelines JSON PDAL.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| cloud | LAS/LAZ/PLY/point cloud | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | scale, origin, CRS and acquisition metadata |
| pipeline | native processing parameters | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | filters and tolerances explicit |

- **Preparación que hay que resolver:** Run native pipeline, subset without losing coordinate metadata and export artifact references.
- **Validación requerida:** Point count, CRS, precision, classification, transform and known-geometry checks.
- **Faltante para un caso real:** Local survey coverage and acquisition quality are project-specific.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reescribir formatos LAS/LAZ ni publicar filtros sin unidades y CRS.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pdal--python"></a>

## PDAL/python

- **Interfaz original:** API Python y biblioteca PDAL compatible.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| cloud | LAS/LAZ/PLY/point cloud | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | scale, origin, CRS and acquisition metadata |
| pipeline | native processing parameters | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | filters and tolerances explicit |

- **Preparación que hay que resolver:** Run native pipeline, subset without losing coordinate metadata and export artifact references.
- **Validación requerida:** Point count, CRS, precision, classification, transform and known-geometry checks.
- **Faltante para un caso real:** Local survey coverage and acquisition quality are project-specific.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No mantener dos instalaciones PDAL incompatibles ni otro servidor equivalente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-potree--potree"></a>

## potree/potree

- **Interfaz original:** API JavaScript y formato servido por el visor.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir que el visor convierte LAS ni duplicar un visor ya seleccionado.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-anandb--energyplus-mcp-java"></a>

## anandb/energyplus-mcp-java

- **Interfaz original:** Servidor y herramientas upstream.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir otro MCP EnergyPlus por preferencia de lenguaje.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-bonninr--freecad_mcp"></a>

## bonninr/freecad_mcp

- **Interfaz original:** main.py remite a blender_mcp.server; comprobar paquete y bridge efectivos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** El nombre del repositorio no acredita control FreeCAD; el namespace observado requiere investigación.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-contextform--freecad-mcp"></a>

## contextform/freecad-mcp

- **Interfaz original:** Servidor y material histórico del repositorio.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** La inspección encontró código en archive; eso no acredita un servidor vigente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ericmartinpe--energyplus-mcp-epjson"></a>

## ericmartinpe/EnergyPlus-MCP-epjson

- **Interfaz original:** Servidor Python y conversión IDF/epJSON existentes.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir inspección/edición ya expuestas ni adoptar todos los forks.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-gaopengbin--cesium-mcp"></a>

## gaopengbin/cesium-mcp

- **Interfaz original:** Paquetes TypeScript de servidor/contratos y conexión a visor.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reemplazar renderizador ni asumir un visor conectado por iniciar el servidor.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-idfkit--idfkit-mcp"></a>

## idfkit/idfkit-mcp

- **Interfaz original:** Entradas del paquete idfkit-mcp.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No sumar otro servidor energético sin diferencia funcional probada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-jagan-shanmugam--open-streetmap-mcp"></a>

## jagan-shanmugam/open-streetmap-mcp

- **Interfaz original:** Herramientas upstream y servicios externos que invocan.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | direction, topology and cost definition |

- **Preparación que hay que resolver:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validación requerida:** Connectivity, direction, intersection semantics, units and source coverage.
- **Faltante para un caso real:** Mapped roads do not imply capacity, reliable speed or traffic demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentarlo como servidor OSM autosuficiente ni inventar disponibilidad de proveedores.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-jjsantos01--qgis_mcp"></a>

## jjsantos01/qgis_mcp

- **Interfaz original:** Herramientas para proyectos, capas y operaciones de sesión.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No rehacer carga/edición existentes ni confundir conexión con validez de Processing.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-jordangunn--gdal-mcp"></a>

## JordanGunn/gdal-mcp

- **Interfaz original:** Servidor y módulos upstream.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir otro GDAL MCP sin contrastar catálogo, límites y salidas.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-klabum--swmm-mcp-pub"></a>

## kLabUM/SWMM-MCP-PUB

- **Interfaz original:** Herramientas list_models, duplicate_model, run_model y reportes identificadas.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | base revision and physical bounds |

- **Preparación que hay que resolver:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validación requerida:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Faltante para un caso real:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No proponer como nuevo un run_model ya implementado; revisar unidades de edición.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-lbnl-eta--energyplus-mcp"></a>

## LBNL-ETA/EnergyPlus-MCP

- **Interfaz original:** Servidor Python, configuración y receta de contenedor upstream.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuir como aporte propio cargar/validar/simular si ya está expuesto.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-mahdin75--gis-mcp"></a>

## mahdin75/gis-mcp

- **Interfaz original:** Servidor real y separación frente a agentes por localizar.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** Una prueba de herramientas en LangChain no demuestra el punto de arranque del servidor.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-msradam--osmnx-mcp"></a>

## msradam/osmnx-mcp

- **Interfaz original:** create_server y registro de grafos identificados.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | direction, topology and cost definition |

- **Preparación que hay que resolver:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validación requerida:** Connectivity, direction, intersection semantics, units and source coverage.
- **Faltante para un caso real:** Mapped roads do not imply capacity, reliable speed or traffic demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reinventar registro de grafos; un grafo activo global puede requerir revisar aislamiento.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-neka-nat--freecad-mcp"></a>

## neka-nat/freecad-mcp

- **Interfaz original:** Servidor Python y RPC del addon.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir otro sistema de jobs sin probar el existente; no publicar ejecución libre por defecto.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-nkarasiak--qgis-mcp"></a>

## nkarasiak/qgis-mcp

- **Interfaz original:** Servidor, plugin y resolución de instancias identificados.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No proponer descubrimiento multiinstancia como novedad si ya está implementado.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-osgeo--grass-mcp"></a>

## OSGeo/grass-mcp

- **Interfaz original:** README/licencia; no se localizaron archivos de implementación.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentarlo como MCP instalable ni contar una prueba aprobada inexistente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-piatkowski--qgis-mcp"></a>

## piatkowski/qgis-mcp

- **Interfaz original:** Herramientas de capa, reproyección, recorte, estadísticas y exportación identificadas.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir funciones ya expuestas; medir diferencias frente a otros QGIS MCP.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-profrino--bonsai-bim-skills"></a>

## ProfRino/bonsai-bim-skills

- **Interfaz original:** Instrucciones y funciones Python del proyecto.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| references | urls | Original format/schema specifications (por configurar) | verify identity and date |

- **Preparación que hay que resolver:** Catalog only; no solver input or invented runtime.
- **Validación requerida:** Links, provenance and classification.
- **Faltante para un caso real:** Not an executable capability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No anunciar skills como endpoint MCP ni copiar instrucciones como código de confianza.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-rainergaier--energyplus-mcp-server"></a>

## RainerGaier/energyplus-mcp-server

- **Interfaz original:** Servidor MCP y rutas HTTP identificadas.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | may be embedded in the building model |

- **Preparación que hay que resolver:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validación requerida:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Faltante para un caso real:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otra API de jobs o generación si sus rutas ya cubren la necesidad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-salog0d--urbanplannermcp"></a>

## salog0d/UrbanPlannerMCP

- **Interfaz original:** run_city_infra_model y run_population_inequalities_model identificadas.
- **Alcance de esta ficha:** candidate. Requires inspecting the actual model formulas/parameters; a general social profile is not its approved input schema.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No tratar UrbanPlanner como cobertura de todo urbanismo ni convertir estimaciones en hechos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-show2instruct--ifc-bonsai-mcp"></a>

## Show2Instruct/ifc-bonsai-mcp

- **Interfaz original:** Servidor, addon y servicio de embeddings separado.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | IFC | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); [buildingSMART Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) | schema, GUIDs, units and georeferencing |
| requirements | IDS or project constraints | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | requirements identify exact model revision |

- **Preparación que hay que resolver:** Validate IFC, map only explicit properties, preserve GUIDs and express losses in any conversion.
- **Validación requerida:** Schema version, units, geometry, references, georeferencing and required fields.
- **Faltante para un caso real:** Public footprints do not provide building systems, materials or a valid IFC model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir el stack completo en requisito de leer un IFC; revisar código ejecutable expuesto.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-sparkgeo--geo-mcp-servers"></a>

## sparkgeo/geo-mcp-servers

- **Interfaz original:** Subpaquetes y puntos de arranque por identificar individualmente.
- **Alcance de esta ficha:** candidate. First split monorepo into actual servers and data contracts; this is a catalog-level starting point only.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| catalog | STAC API/item collection | Configured service/API instance (por configurar); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | conformance, pagination and asset links |
| query | area/time/bands | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | explicit search limits |

- **Preparación que hay que resolver:** Discover capabilities, filter, preserve item/asset versions and resolve authorized assets.
- **Validación requerida:** Conformance, item IDs, geometry, datetime, asset availability and rights.
- **Faltante para un caso real:** A catalog entry does not prove the asset is downloadable or fit for a model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** Un healthcheck del repositorio no acredita todas sus herramientas.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-spkane--freecad-addon-robust-mcp-server"></a>

## spkane/freecad-addon-robust-mcp-server

- **Interfaz original:** MCPServer, registro de componentes y bridge de FreeCAD.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | bounds and intended result |

- **Preparación que hay que resolver:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validación requerida:** Native reopen, object identity, dimensions, recompute status and version.
- **Faltante para un caso real:** A geometric object is not a complete engineering/BIM model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reimplementar timeouts o bridge sin identificar falla; distinguir timeout de detener cálculo.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-xrds76354--sumo-mcp-server"></a>

## XRDS76354/SUMO-MCP-Server

- **Interfaz original:** manage_network, control_simulation y query_simulation_state identificadas.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | SUMO net.xml | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | netconvert and junction assumptions recorded |
| demand | SUMO routes/trips/OD | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | observed or synthetic status explicit |
| config | sumocfg | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | seed, time and vehicle types fixed |

- **Preparación que hay que resolver:** Convert network with SUMO tools, prepare demand separately, resolve relative file references and preserve assumptions.
- **Validación requerida:** Network-route consistency, edge IDs, units, time coverage, vehicle counts and configuration.
- **Faltante para un caso real:** OSM cannot supply calibrated OD demand or signal timings everywhere.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No vender sus comandos de optimización como mejora garantizada; revisar estado compartido.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-zhonghao1995--agentic-swmm-workflow"></a>

## Zhonghao1995/agentic-swmm-workflow

- **Interfaz original:** Servidores JavaScript identificados y orquestador del proyecto.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | base revision and physical bounds |

- **Preparación que hay que resolver:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validación requerida:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Faltante para un caso real:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir workflow agentic con motor hidráulico ni duplicar herramientas ya disponibles.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-3dcitydb--3dcitydb"></a>

## 3dcitydb/3dcitydb

- **Interfaz original:** Esquema SQL y herramientas de su versión.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar base 3D ni confundir v4/v5 y sus herramientas compatibles.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-3dcitydb--citydb-tool"></a>

## 3dcitydb/citydb-tool

- **Interfaz original:** CLI Java y conexión a esquema compatible.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No desarrollar importador CityGML propio ni lanzar migraciones como consulta ordinaria.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-citygml4j--citygml-tools"></a>

## citygml4j/citygml-tools

- **Interfaz original:** CLI Java del proyecto.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otra implementación de cada versión del formato.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-citygml4j--citygml4j"></a>

## citygml4j/citygml4j

- **Interfaz original:** API Java.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No mantener parser propio ni un servicio por cada biblioteca.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cityjson--cjio"></a>

## cityjson/cjio

- **Interfaz original:** API/CLI Python cjio.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir toda ciudad a GeoJSON perdiendo superficies y semántica.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-dtcc-platform--dtcc-core"></a>

## dtcc-platform/dtcc-core

- **Interfaz original:** API Python y extensiones del proyecto.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No añadir una representación urbana universal sin probar correspondencia.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-dtcc-platform--dtcc-sim"></a>

## dtcc-platform/dtcc-sim

- **Interfaz original:** Servicio/ejecutor y contratos de esa versión.
- **Alcance de esta ficha:** candidate. Model/service must be identified before this proposed CFD profile can be accepted as its interface.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | watertight simulation geometry and mesh | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | domain, mesh quality and scale |
| conditions | boundary/initial conditions | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | velocity, turbulence, material and units |
| solver | case and numerical configuration | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | version and convergence criteria |

- **Preparación que hay que resolver:** Use native mesher/solver tools; separate geometry preparation from physical case validation.
- **Validación requerida:** Boundary completeness, mesh metrics, dimensions, timestep, residuals and conservation/reference fields.
- **Faltante para un caso real:** A display scene or OSM model does not provide a valid CFD mesh or calibrated conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuir cobertura científica al nombre sim sin identificar modelos y datos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-dtcc-platform--dtcc-viewer"></a>

## dtcc-platform/dtcc-viewer

- **Interfaz original:** API y ejecutor del visor.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otro visor obligatorio ni confundir mostrar con validar simulación.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-project-plateau--plateau-builder"></a>

## Project-PLATEAU/PLATEAU-Builder

- **Interfaz original:** Aplicación Java y formatos de proyecto.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir editor ni prometer headless sin interfaz probada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-project-plateau--plateau-gis-converter"></a>

## Project-PLATEAU/PLATEAU-GIS-Converter

- **Interfaz original:** CLI y configuración Rust.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar conversión ni asumir que cualquier CityGML es perfil PLATEAU.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-reearth--reearth-flow"></a>

## reearth/reearth-flow

- **Interfaz original:** Ejecutor/API y grafos de acciones Re:Earth Flow.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir otro motor de grafos ni exponer todas las acciones como herramientas sin control.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-tudelft3d--3dcitydb-tools-for-qgis"></a>

## tudelft3d/3DCityDB-Tools-for-QGIS

- **Interfaz original:** Plugin/PyQGIS y esquema compatible.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | losses and consumer requirements explicit |

- **Preparación que hay que resolver:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validación requerida:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Faltante para un caso real:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar importadores ni montar otro servicio por ser un plugin.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-tudelft3d--3dfier"></a>

## tudelft3d/3dfier

- **Interfaz original:** Ejecutable C++ y configuración.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| cloud | LiDAR/point cloud or elevation source | Municipality, utility, transit agency or project owner (por configurar); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | accuracy, classification and vertical datum |
| footprints | building/terrain outlines | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | identity, geometry and coverage |
| parameters | reconstruction settings | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | desired LoD and tolerances |

- **Preparación que hay que resolver:** Align sources and use native reconstruction tools; label reconstructed versus observed attributes.
- **Validación requerida:** Alignment, point/classification quality, units, watertightness and comparison against control geometry.
- **Faltante para un caso real:** Incomplete heights/footprints and low-resolution elevation can prevent suitable reconstruction.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentar reconstrucción inferida como medición ni ocultar calidad de elevación.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-tudelft3d--city4cfd"></a>

## tudelft3d/City4CFD

- **Interfaz original:** CLI y configuración de caso.
- **Alcance de esta ficha:** candidate. Geometry preparation operation may omit solver conditions; simulation requires separate admitted CFD case.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | watertight simulation geometry and mesh | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | domain, mesh quality and scale |
| conditions | boundary/initial conditions | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | velocity, turbulence, material and units |
| solver | case and numerical configuration | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | version and convergence criteria |

- **Preparación que hay que resolver:** Use native mesher/solver tools; separate geometry preparation from physical case validation.
- **Validación requerida:** Boundary completeness, mesh metrics, dimensions, timestep, residuals and conservation/reference fields.
- **Faltante para un caso real:** A display scene or OSM model does not provide a valid CFD mesh or calibrated conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir geometría preparada con malla CFD validada o simulación ejecutada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-vcityteam--ud-viz"></a>

## VCityTeam/UD-Viz

- **Interfaz original:** API JavaScript/TypeScript.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir motor ni obligar todos los agentes a una UI concreta.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-benchmark-urbanism--cityseer-api"></a>

## benchmark-urbanism/cityseer-api

- **Interfaz original:** API Python con extensión Rust.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | direction, topology and cost definition |

- **Preparación que hay que resolver:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validación requerida:** Connectivity, direction, intersection semantics, units and source coverage.
- **Faltante para un caso real:** Mapped roads do not imply capacity, reliable speed or traffic demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir distancia de red o mezcla de usos en impacto causal.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-gboeing--osmnx"></a>

## gboeing/osmnx

- **Interfaz original:** API Python; comparar MCP OSMnx existente.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | direction, topology and cost definition |

- **Preparación que hay que resolver:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validación requerida:** Connectivity, direction, intersection semantics, units and source coverage.
- **Faltante para un caso real:** Mapped roads do not imply capacity, reliable speed or traffic demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No rehacer descarga/topología ni asumir OSM completo o apto para cada simulador.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pysal--esda"></a>

## pysal/esda

- **Interfaz original:** API Python.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | seed and inference assumptions |

- **Preparación que hay que resolver:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validación requerida:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Faltante para un caso real:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No interpretar autocorrelación como causalidad ni ocultar elección de vecindad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pysal--inequality"></a>

## pysal/inequality

- **Interfaz original:** API Python.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | seed and inference assumptions |

- **Preparación que hay que resolver:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validación requerida:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Faltante para un caso real:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir desigualdad agregada con desigualdad individual ni mezclar unidades.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pysal--libpysal"></a>

## pysal/libpysal

- **Interfaz original:** API Python de pesos/estructuras.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | seed and inference assumptions |

- **Preparación que hay que resolver:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validación requerida:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Faltante para un caso real:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No inventar vecindades ni perder alineación entre tabla y matriz de pesos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pysal--mgwr"></a>

## pysal/mgwr

- **Interfaz original:** API Python de ajuste y selección de parámetros.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | seed and inference assumptions |

- **Preparación que hay que resolver:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validación requerida:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Faltante para un caso real:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentar coeficientes locales como causalidad ni ignorar colinealidad/escala.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pysal--momepy"></a>

## pysal/momepy

- **Interfaz original:** API Python y datos geoespaciales nativos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | seed and inference assumptions |

- **Preparación que hay que resolver:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validación requerida:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Faltante para un caso real:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No rehacer indicadores ni tratar resultados homónimos de versiones distintas como iguales.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pysal--segregation"></a>

## pysal/segregation

- **Interfaz original:** API Python.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | seed and inference assumptions |

- **Preparación que hay que resolver:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validación requerida:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Faltante para un caso real:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No producir inferencias individuales ni comparar métricas con universos incompatibles.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pysal--spopt"></a>

## pysal/spopt

- **Interfaz original:** API Python y solvers configurados.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | seed and inference assumptions |

- **Preparación que hay que resolver:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validación requerida:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Faltante para un caso real:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No llamar óptima una solución factible ni inventar objetivos del proyecto.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pysal--spreg"></a>

## pysal/spreg

- **Interfaz original:** API Python.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | seed and inference assumptions |

- **Preparación que hay que resolver:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validación requerida:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Faltante para un caso real:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No automatizar selección causal ni ocultar supuestos del modelo espacial.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-spacegroupucl--depthmapx"></a>

## SpaceGroupUCL/depthmapX

- **Interfaz original:** CLI o aplicación; verificar automatización de la versión.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | direction, topology and cost definition |

- **Preparación que hay que resolver:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validación requerida:** Connectivity, direction, intersection semantics, units and source coverage.
- **Faltante para un caso real:** Mapped roads do not imply capacity, reliable speed or traffic demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No sumar centralidades homónimas sin explicar diferencia frente a cityseer/OSMnx.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-a-b-street--abstreet"></a>

## a-b-street/abstreet

- **Interfaz original:** Herramientas/formatos de A/B Street y ejecutores disponibles.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | SUMO net.xml | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | netconvert and junction assumptions recorded |
| demand | SUMO routes/trips/OD | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | observed or synthetic status explicit |
| config | sumocfg | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | seed, time and vehicle types fixed |

- **Preparación que hay que resolver:** Convert network with SUMO tools, prepare demand separately, resolve relative file references and preserve assumptions.
- **Validación requerida:** Network-route consistency, edge IDs, units, time coverage, vehicle counts and configuration.
- **Faltante para un caso real:** OSM cannot supply calibrated OD demand or signal timings everywhere.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No tratar un simulador interactivo como servicio estable por defecto.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-activitysim--activitysim"></a>

## ActivitySim/activitysim

- **Interfaz original:** CLI, configuraciones y tablas ActivitySim.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | zones and skims compatible |

- **Preparación que hay que resolver:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validación requerida:** Control totals, missingness, joins, weights and model diagnostics.
- **Faltante para un caso real:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No simular demanda creíble sin encuestas, población y estimación compatibles.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-activitysim--populationsim"></a>

## ActivitySim/populationsim

- **Interfaz original:** CLI Python y tablas de controles.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | zones and skims compatible |

- **Preparación que hay que resolver:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validación requerida:** Control totals, missingness, joins, weights and model diagnostics.
- **Faltante para un caso real:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentar población sintética como padrón de personas reales.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-aequilibrae--aequilibrae"></a>

## AequilibraE/aequilibrae

- **Interfaz original:** API Python y proyecto de datos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | transport project and zone network | Municipality, utility, transit agency or project owner (por configurar); [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | costs, direction, capacity and zone connectors |
| od | OD demand matrix | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | zone IDs, modes, period and units |
| parameters | assignment assumptions | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | algorithm, convergence and calibration scope |

- **Preparación que hay que resolver:** Use native network/matrix APIs; align zones and demand and retain congestion assumptions.
- **Validación requerida:** OD/network consistency, demand totals, flows, cost units and convergence.
- **Faltante para un caso real:** Mapped streets do not supply the OD matrix, capacities or observed congestion calibration.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No generar OD o calibración de red automáticamente a partir de calles.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-conveyal--analysis-backend"></a>

## conveyal/analysis-backend

- **Interfaz original:** API/arquitectura del backend y workers.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | coordinate order and travel profile explicit |

- **Preparación que hay que resolver:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validación requerida:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Faltante para un caso real:** Feeds may be missing, expired or not include realtime information.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir autorización multiusuario o despliegue listo por inspeccionar el repo.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-conveyal--r5"></a>

## conveyal/r5

- **Interfaz original:** Biblioteca Java y wrappers existentes.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | coordinate order and travel profile explicit |

- **Preparación que hay que resolver:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validación requerida:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Faltante para un caso real:** Feeds may be missing, expired or not include realtime information.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar r5r/r5py ni comparar resultados con fechas GTFS distintas.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-eclipse-sumo--sumo"></a>

## eclipse-sumo/sumo

- **Interfaz original:** TraCI, libsumo y CLI; comparar MCP SUMO existente.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | SUMO net.xml | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | netconvert and junction assumptions recorded |
| demand | SUMO routes/trips/OD | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | observed or synthetic status explicit |
| config | sumocfg | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | seed, time and vehicle types fixed |

- **Preparación que hay que resolver:** Convert network with SUMO tools, prepare demand separately, resolve relative file references and preserve assumptions.
- **Validación requerida:** Network-route consistency, edge IDs, units, time coverage, vehicle counts and configuration.
- **Faltante para un caso real:** OSM cannot supply calibrated OD demand or signal timings everywhere.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reimplementar control ni optimización existente; red sin demanda no basta.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-giscience--openrouteservice"></a>

## GIScience/openrouteservice

- **Interfaz original:** API HTTP y perfiles del servidor.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | direction, topology and cost definition |

- **Preparación que hay que resolver:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validación requerida:** Connectivity, direction, intersection semantics, units and source coverage.
- **Faltante para un caso real:** Mapped roads do not imply capacity, reliable speed or traffic demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No instalarlo junto con OSRM/Valhalla por defecto ni asumir servicios públicos ilimitados.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ipea--accessibility"></a>

## ipea/accessibility

- **Interfaz original:** API R.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| matrix | travel time matrix | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | time window, units and modes |
| opportunities | destinations and quantities | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | counts and taxonomy defined |
| population | aggregate weights | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (por configurar) | same aggregation and period |

- **Preparación que hay que resolver:** Align IDs and travel-time definition; select thresholds/impedance without silent defaults.
- **Validación requerida:** Matrix dimensions, reachable/unreachable coding, weights, time and denominators.
- **Faltante para un caso real:** Travel-time generation and opportunity quality remain separate dependencies.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir cálculo de indicador con generación de tiempos de viaje.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ipea--r5r"></a>

## ipea/r5r

- **Interfaz original:** API R y runtime Java.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | coordinate order and travel profile explicit |

- **Preparación que hay que resolver:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validación requerida:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Faltante para un caso real:** Feeds may be missing, expired or not include realtime information.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir otro cliente Java si el usuario trabaja en R; no duplicar r5py en el mismo perfil.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-matsim-org--matsim-libs"></a>

## matsim-org/matsim-libs

- **Interfaz original:** Configuraciones, modelos y ejecutor Java MATSim.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | zones and skims compatible |

- **Preparación que hay que resolver:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validación requerida:** Control totals, missingness, joins, weights and model diagnostics.
- **Faltante para un caso real:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No generar planes de actividad calibrados desde una red OSM solamente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-mobilitydata--gtfs-validator"></a>

## MobilityData/gtfs-validator

- **Interfaz original:** CLI/servicio y reportes del validador.
- **Alcance de esta ficha:** dependency. Only the GTFS feed is required for validation; street graph and trip query belong to routing cases, not this operation.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | coordinate order and travel profile explicit |

- **Preparación que hay que resolver:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validación requerida:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Faltante para un caso real:** Feeds may be missing, expired or not include realtime information.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No interpretar feed válido como servicio vigente o cobertura adecuada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-opentripplanner--opentripplanner"></a>

## opentripplanner/OpenTripPlanner

- **Interfaz original:** API de la versión instalada y construcción de grafo.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | coordinate order and travel profile explicit |

- **Preparación que hay que resolver:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validación requerida:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Faltante para un caso real:** Feeds may be missing, expired or not include realtime information.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No sustituir operador de transporte ni inventar datos en tiempo real.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-project-osrm--osrm-backend"></a>

## Project-OSRM/osrm-backend

- **Interfaz original:** HTTP y herramientas de preparación de datos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | direction, topology and cost definition |

- **Preparación que hay que resolver:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validación requerida:** Connectivity, direction, intersection semantics, units and source coverage.
- **Faltante para un caso real:** Mapped roads do not imply capacity, reliable speed or traffic demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir routing ni sumar todos los motores de rutas al perfil base.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-r5py--r5py"></a>

## r5py/r5py

- **Interfaz original:** API Python y JVM compatible.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | coordinate order and travel profile explicit |

- **Preparación que hay que resolver:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validación requerida:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Faltante para un caso real:** Feeds may be missing, expired or not include realtime information.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No publicar otro R5 MCP si la fachada del wrapper ya cubre el caso.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ropensci--stplanr"></a>

## ropensci/stplanr

- **Interfaz original:** API R y servicios que cada función utilice.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | transport project and zone network | Municipality, utility, transit agency or project owner (por configurar); [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | costs, direction, capacity and zone connectors |
| od | OD demand matrix | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | zone IDs, modes, period and units |
| parameters | assignment assumptions | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | algorithm, convergence and calibration scope |

- **Preparación que hay que resolver:** Use native network/matrix APIs; align zones and demand and retain congestion assumptions.
- **Validación requerida:** OD/network consistency, demand totals, flows, cost units and convergence.
- **Faltante para un caso real:** Mapped streets do not supply the OD matrix, capacities or observed congestion calibration.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir que toda función es local ni duplicar servicios de rutas externos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-udst--synthpop"></a>

## UDST/synthpop

- **Interfaz original:** API Python y tablas de controles.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | zones and skims compatible |

- **Preparación que hay que resolver:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validación requerida:** Control totals, missingness, joins, weights and model diagnostics.
- **Faltante para un caso real:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No elegirla además de PopulationSim por inercia; revisar mantenimiento y compatibilidad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-valhalla--valhalla"></a>

## valhalla/valhalla

- **Interfaz original:** API HTTP y herramientas de preparación.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | direction, topology and cost definition |

- **Preparación que hay que resolver:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validación requerida:** Connectivity, direction, intersection semantics, units and source coverage.
- **Faltante para un caso real:** Mapped roads do not imply capacity, reliable speed or traffic demand.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir coste/routing ni prometer restricciones no soportadas por el perfil.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-azavea--raster-vision"></a>

## azavea/raster-vision

- **Interfaz original:** Configuraciones y ejecutores Python.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | license and evaluation scope |

- **Preparación que hay que resolver:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validación requerida:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Faltante para un caso real:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No incorporar entrenamiento genérico ni considerar libre un peso por ser abierto el código.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-open-eo--openeo-processes"></a>

## Open-EO/openeo-processes

- **Interfaz original:** Esquemas y especificación de procesos.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| schema | IDS/BCF/NGSI-LD/openEO definitions | Original format/schema specifications (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | exact version and profile |
| instance | data/model being validated | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | references and IDs preserved |

- **Preparación que hay que resolver:** Use maintained validator and explicit profile, report unresolved references.
- **Validación requerida:** Schema version, reference resolution, units and semantic requirements where defined.
- **Faltante para un caso real:** Schema validity is not scientific validity or evidence that a backend implements every operation.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No anunciar definiciones JSON como motor ejecutable ni asumir cobertura total del backend.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-open-eo--openeo-python-client"></a>

## Open-EO/openeo-python-client

- **Interfaz original:** API Python y conexión al backend.
- **Alcance de esta ficha:** candidate. Requires backend capabilities and a process graph; reuse backend jobs/auth rather than inventing a local executor.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| backend | openEO backend capabilities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | auth, processes, formats and limits |
| graph | openEO process graph | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | supported processes and parameters |
| collection | backend collection and query window | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | bands, extent and period |

- **Preparación que hay que resolver:** Use native openEO client and backend jobs; validate graph against the configured backend.
- **Validación requerida:** Backend capabilities, graph validity, bands, quotas, job status and result assets.
- **Faltante para un caso real:** A process definition or STAC listing does not guarantee executable backend coverage.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir el backend ni otra cola si openEO ya da jobs; revisar cuotas y costes.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-opendatacube--datacube-core"></a>

## opendatacube/datacube-core

- **Interfaz original:** API/CLI Python y catálogo de productos.
- **Alcance de esta ficha:** candidate. Requires configured indexed products and measurement schemas; a STAC query alone is insufficient.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| products | indexed product definitions | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | measurement names, metadata schema and storage |
| query | cube selection | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | space, time, bands and grid |

- **Preparación que hay que resolver:** Use native Data Cube index/API; align measurements and preserve xarray/grid metadata.
- **Validación requerida:** Index health, product schema, storage links, units, nodata and coverage.
- **Faltante para un caso real:** Unindexed STAC assets do not automatically form a Data Cube product.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otro catálogo ni cargar conjuntos gigantes al contexto de un agente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-opengeos--geoai"></a>

## opengeos/geoai

- **Interfaz original:** API Python y componentes de agente/CLI del repositorio.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | license and evaluation scope |

- **Preparación que hay que resolver:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validación requerida:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Faltante para un caso real:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir un paquete amplio de IA en una sola herramienta irrestricta.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-opengeos--segment-geospatial"></a>

## opengeos/segment-geospatial

- **Interfaz original:** API Python y automatizaciones ya presentes.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | license and evaluation scope |

- **Preparación que hay que resolver:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validación requerida:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Faltante para un caso real:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No tratar segmentación como objeto urbano validado ni ignorar licencia de pesos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-orfeotoolbox--otb"></a>

## orfeotoolbox/OTB

- **Interfaz original:** CLI/aplicaciones y bindings disponibles.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | license and evaluation scope |

- **Preparación que hay que resolver:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validación requerida:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Faltante para un caso real:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No publicar todas las aplicaciones a ciegas ni confundir sus requisitos ráster.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-orfeotoolbox--pyotb"></a>

## orfeotoolbox/pyotb

- **Interfaz original:** Binding/API Python y OTB compatible.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | license and evaluation scope |

- **Preparación que hay que resolver:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validación requerida:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Faltante para un caso real:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No mantener dos OTB incompatibles ni otro servidor equivalente al CLI.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-sentinel-hub--sentinelhub-py"></a>

## sentinel-hub/sentinelhub-py

- **Interfaz original:** SDK y API del proveedor configurado.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | license and evaluation scope |

- **Preparación que hay que resolver:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validación requerida:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Faltante para un caso real:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** El SDK abierto no garantiza acceso gratuito ni derechos sobre todos los datos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-stac-utils--pystac"></a>

## stac-utils/pystac

- **Interfaz original:** API Python.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| catalog | STAC API/item collection | Configured service/API instance (por configurar); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | conformance, pagination and asset links |
| query | area/time/bands | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | explicit search limits |

- **Preparación que hay que resolver:** Discover capabilities, filter, preserve item/asset versions and resolve authorized assets.
- **Validación requerida:** Conformance, item IDs, geometry, datetime, asset availability and rights.
- **Faltante para un caso real:** A catalog entry does not prove the asset is downloadable or fit for a model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir un objeto STAC con un archivo ráster disponible.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-stac-utils--pystac-client"></a>

## stac-utils/pystac-client

- **Interfaz original:** API Python y capacidades del servidor.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| catalog | STAC API/item collection | Configured service/API instance (por configurar); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | conformance, pagination and asset links |
| query | area/time/bands | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | explicit search limits |

- **Preparación que hay que resolver:** Discover capabilities, filter, preserve item/asset versions and resolve authorized assets.
- **Validación requerida:** Conformance, item IDs, geometry, datetime, asset availability and rights.
- **Faltante para un caso real:** A catalog entry does not prove the asset is downloadable or fit for a model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir todas las extensiones STAC ni descargar automáticamente cada asset.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-stac-utils--stac-fastapi"></a>

## stac-utils/stac-fastapi

- **Interfaz original:** Servicio y backend de almacenamiento elegido.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| catalog | STAC API/item collection | Configured service/API instance (por configurar); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | conformance, pagination and asset links |
| query | area/time/bands | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | explicit search limits |

- **Preparación que hay que resolver:** Discover capabilities, filter, preserve item/asset versions and resolve authorized assets.
- **Validación requerida:** Conformance, item IDs, geometry, datetime, asset availability and rights.
- **Faltante para un caso real:** A catalog entry does not prove the asset is downloadable or fit for a model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No instalar un servidor STAC cuando solo necesitamos consultar uno.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-torchgeo--torchgeo"></a>

## torchgeo/torchgeo

- **Interfaz original:** API Python/PyTorch.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | license and evaluation scope |

- **Preparación que hay que resolver:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validación requerida:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Faltante para un caso real:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir un framework de investigación en predicciones urbanas validadas por defecto.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-crowddynamics--crowddynamics"></a>

## crowddynamics/crowddynamics

- **Interfaz original:** CLI/API Python y configuración.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No extrapolar comportamientos humanos ni asumir mantenimiento actual.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-mengecrowdsim--menge"></a>

## MengeCrowdSim/Menge

- **Interfaz original:** Ejecutable, configuración y plugins admitidos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No inventar comportamiento o calibración ni cargar plugins no revisados.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pedestriandynamics--jupedsim"></a>

## PedestrianDynamics/jupedsim

- **Interfaz original:** API Python y geometrías/modelos admitidos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir evacuación validada ni traducir geometría urbana sin verificar transitabilidad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-svenkreiss--socialforce"></a>

## svenkreiss/socialforce

- **Interfaz original:** API Python y ejemplos de simulación/ajuste.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentarlo como motor peatonal universal o evidencia de conducta real.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-dss-extensions--opendssdirect.py"></a>

## dss-extensions/OpenDSSDirect.py

- **Interfaz original:** API Python y motor nativo asociado.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | objective and solver stated |

- **Preparación que hay que resolver:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validación requerida:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Faltante para un caso real:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir compatibilidad entre variantes DSS ni inferir red física desde mapas.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-e2niee--pandapower"></a>

## e2nIEE/pandapower

- **Interfaz original:** API Python y solvers admitidos.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | objective and solver stated |

- **Preparación que hay que resolver:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validación requerida:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Faltante para un caso real:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No generar una red calibrada de datos incompletos ni ocultar falta de convergencia.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-natlabrockies--reopt_api"></a>

## NatLabRockies/REopt_API

- **Interfaz original:** Servicio/API y motor de optimización correspondiente.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | objective and solver stated |

- **Preparación que hay que resolver:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validación requerida:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Faltante para un caso real:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir servidor API con todo el solver ni prometer ahorro económico cierto.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-oemof--oemof-solph"></a>

## oemof/oemof-solph

- **Interfaz original:** API Python y solver configurado.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | objective and solver stated |

- **Preparación que hay que resolver:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validación requerida:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Faltante para un caso real:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuir óptimo sin verificar estado, brecha y restricciones.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-pypsa--pypsa"></a>

## PyPSA/PyPSA

- **Interfaz original:** API Python y backend de optimización admitido.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | objective and solver stated |

- **Preparación que hay que resolver:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validación requerida:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Faltante para un caso real:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No mezclar series o unidades ni presentar plan óptimo como decisión aprobada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-rwth-ebc--uesgraphs"></a>

## RWTH-EBC/uesgraphs

- **Interfaz original:** API Python y exportaciones del paquete.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (por configurar); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | objective and solver stated |

- **Preparación que hay que resolver:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validación requerida:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Faltante para un caso real:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir un grafo con dimensionamiento o simulación ya ejecutados.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-climada-project--climada_petals"></a>

## CLIMADA-project/climada_petals

- **Interfaz original:** API Python y módulos concretos.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| hazard | hazard/event model | Hazard data selected by the model owner (por configurar); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | probability/intensity and event set |
| exposure | assets/population/value | Municipality, utility, transit agency or project owner (por configurar); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | aggregation and valuation |
| vulnerability | functions/model configuration | Model author or qualified project team (por configurar); Hazard data selected by the model owner (por configurar); Original tool examples/tests (por configurar) | applicability and uncertainty |

- **Preparación que hay que resolver:** Match hazard/exposure definitions and preserve event/revision links.
- **Validación requerida:** Units, vulnerability domain, spatial/temporal alignment and reference impact.
- **Faltante para un caso real:** Geometry alone cannot determine losses or locally valid vulnerability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No instalar todos los peligros ni atribuir validación a la familia completa.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-climada-project--climada_python"></a>

## CLIMADA-project/climada_python

- **Interfaz original:** API Python y fuentes de datos del caso.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| hazard | hazard/event model | Hazard data selected by the model owner (por configurar); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | probability/intensity and event set |
| exposure | assets/population/value | Municipality, utility, transit agency or project owner (por configurar); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | aggregation and valuation |
| vulnerability | functions/model configuration | Model author or qualified project team (por configurar); Hazard data selected by the model owner (por configurar); Original tool examples/tests (por configurar) | applicability and uncertainty |

- **Preparación que hay que resolver:** Match hazard/exposure definitions and preserve event/revision links.
- **Validación requerida:** Units, vulnerability domain, spatial/temporal alignment and reference impact.
- **Faltante para un caso real:** Geometry alone cannot determine losses or locally valid vulnerability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No producir pérdidas reales desde geometría sola ni omitir incertidumbre/vulnerabilidad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-gem--oq-engine"></a>

## gem/oq-engine

- **Interfaz original:** CLI/API del engine y archivos de configuración.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| hazard | hazard/event model | Hazard data selected by the model owner (por configurar); Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | probability/intensity and event set |
| exposure | assets/population/value | Municipality, utility, transit agency or project owner (por configurar); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | aggregation and valuation |
| vulnerability | functions/model configuration | Model author or qualified project team (por configurar); Hazard data selected by the model owner (por configurar); Original tool examples/tests (por configurar) | applicability and uncertainty |

- **Preparación que hay que resolver:** Match hazard/exposure definitions and preserve event/revision links.
- **Validación requerida:** Units, vulnerability domain, spatial/temporal alignment and reference impact.
- **Faltante para un caso real:** Geometry alone cannot determine losses or locally valid vulnerability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir mapa de peligro con pérdida urbana ni elegir modelos sin justificación.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-universite-gustave-eiffel--noisemodelling"></a>

## Universite-Gustave-Eiffel/NoiseModelling

- **Interfaz original:** Scripts/CLI Java y datos de emisión/escena.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| sources | traffic/activity/emission sources | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | observed versus assumed flows/spectrum |
| scene | terrain/buildings/receivers | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | heights materials and coordinates |
| conditions | propagation/weather parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | time period and standard specified |

- **Preparación que hay que resolver:** Use native noise model and explicit emission preparation; retain receiver IDs.
- **Validación requerida:** Source units, frequency/period, geometry, receiver location and reference levels.
- **Faltante para un caso real:** A road centerline is not a measured noise source or calibrated acoustic model.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No deducir emisión acústica solo de calles ni etiquetar resultado como medición.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-duckdb--duckdb-spatial"></a>

## duckdb/duckdb-spatial

- **Interfaz original:** SQL y drivers de la extensión instalada.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir funciones espaciales ni dar SQL/lectura de archivos irrestrictos al agente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-geopandas--geopandas"></a>

## geopandas/geopandas

- **Interfaz original:** API Python GeoDataFrame.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otra base GIS ni duplicar cada función de GDAL/QGIS.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-geotools--geotools"></a>

## geotools/geotools

- **Interfaz original:** APIs Java y módulos requeridos.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No publicar otro servidor GIS equivalente por existir una biblioteca amplia.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-jblindsay--whitebox-tools"></a>

## jblindsay/whitebox-tools

- **Interfaz original:** CLI y catálogo de herramientas del binario admitido.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar) | band meaning, nodata and resolution explicit |

- **Preparación que hay que resolver:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validación requerida:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Faltante para un caso real:** An available raster can be unsuitable for the intended analysis.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir que todas las extensiones/binarios tienen iguales condiciones de distribución.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-locationtech--jts"></a>

## locationtech/jts

- **Interfaz original:** API Java JTS.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No añadir otro MCP de geometría además de GEOS/Shapely sin diferencia requerida.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-opengeos--whitebox-python"></a>

## opengeos/whitebox-python

- **Interfaz original:** API Python y binario Whitebox compatible.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar) | band meaning, nodata and resolution explicit |

- **Preparación que hay que resolver:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validación requerida:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Faltante para un caso real:** An available raster can be unsuitable for the intended analysis.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No contar wrapper y binario como dos motores independientes.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-osgeo--gdal"></a>

## OSGeo/gdal

- **Interfaz original:** CLI, API y bindings; comparar GDAL MCP existente.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No inventar transformaciones ni exponer todos los drivers/accesos externos sin límites.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-osgeo--grass"></a>

## OSGeo/grass

- **Interfaz original:** Sesión/mapset, CLI y API Python.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No depender del grass-mcp anunciado sin código ni mezclar mapsets entre proyectos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-osgeo--proj"></a>

## OSGeo/PROJ

- **Interfaz original:** Biblioteca/CLI y bindings ya usados por GIS.
- **Alcance de esta ficha:** dependency. An operation requires control coordinates, datum/epoch and grids when applicable; not an arbitrary feature collection.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No aceptar solo un EPSG como garantía de datum/época/transformación adecuada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-postgis--postgis"></a>

## postgis/postgis

- **Interfaz original:** SQL mediante API de aplicación y rol acotado.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| collection | database/API reference | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | authorized project and schema |

- **Preparación que hay que resolver:** Use typed queries and bounded artifacts; preserve IDs and revision.
- **Validación requerida:** Role/scope, CRS, geometry column, counts and query limits.
- **Faltante para un caso real:** An instance and authorized data are required.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No construir otra base espacial ni copiar bases de productos existentes.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-qgis--qgis"></a>

## qgis/QGIS

- **Interfaz original:** qgis_process/PyQGIS y plugin; comparar MCP QGIS existentes.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir GIS ni mezclar automatización headless con control de sesión gráfica.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-r-spatial--sf"></a>

## r-spatial/sf

- **Interfaz original:** API R y bibliotecas nativas de sf.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir igualdad entre motores o semántica esférica/planar.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-rasterio--rasterio"></a>

## rasterio/rasterio

- **Interfaz original:** API Python basada en GDAL.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar) | band meaning, nodata and resolution explicit |

- **Preparación que hay que resolver:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validación requerida:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Faltante para un caso real:** An available raster can be unsuitable for the intended analysis.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar GDAL ni cargar rásters completos al contexto del agente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-rspatial--terra"></a>

## rspatial/terra

- **Interfaz original:** API R y núcleo nativo.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar) | band meaning, nodata and resolution explicit |

- **Preparación que hay que resolver:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validación requerida:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Faltante para un caso real:** An available raster can be unsuitable for the intended analysis.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otro stack ráster general paralelo por uniformidad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-saga-gis--saga-gis"></a>

## saga-gis/saga-gis

- **Interfaz original:** CLI y bibliotecas de herramientas de la distribución.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (por configurar) | band meaning, nodata and resolution explicit |

- **Preparación que hay que resolver:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validación requerida:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Faltante para un caso real:** An available raster can be unsuitable for the intended analysis.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No fijar IDs de algoritmos sin versión ni reconstruir análisis de terreno existente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-shapely--shapely"></a>

## shapely/shapely

- **Interfaz original:** API Python Shapely.
- **Alcance de esta ficha:** dependency. Planar geometries and explicitly declared measurement units; no full CRS transformation service is supplied by Shapely.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar) | CRS and IDs explicit |

- **Preparación que hay que resolver:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validación requerida:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Faltante para un caso real:** Coverage and domain attributes are not guaranteed by a map.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuirle manejo CRS completo, geodesia o simulación urbana; no duplicar GEOS.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-ckan--ckan"></a>

## ckan/ckan

- **Interfaz original:** Action API y permisos de una instancia.
- **Alcance de esta ficha:** candidate. Dataset/resource catalog; CKAN Action API binding, not STAC conformance, must be mapped explicitly.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| instance | catalog API and scope | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | native API/version and permissions |
| query | resource metadata search | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | geography, date, format and limits |

- **Preparación que hay que resolver:** Use the native CKAN/GeoNetwork/GeoNode API; resolve resource links and access terms before ingestion.
- **Validación requerida:** API version, pagination, resource IDs, license, format and link availability.
- **Faltante para un caso real:** Metadata does not imply a usable downloadable dataset; no STAC conformance is assumed.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No duplicar catálogo ni considerar descargable cualquier recurso listado.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-geonetwork--core-geonetwork"></a>

## geonetwork/core-geonetwork

- **Interfaz original:** API de la versión instalada y estándares que publique.
- **Alcance de esta ficha:** candidate. Geographic metadata catalog; use version-specific API/standards, not assumed STAC compatibility.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| instance | catalog API and scope | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | native API/version and permissions |
| query | resource metadata search | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | geography, date, format and limits |

- **Preparación que hay que resolver:** Use the native CKAN/GeoNetwork/GeoNode API; resolve resource links and access terms before ingestion.
- **Validación requerida:** API version, pagination, resource IDs, license, format and link availability.
- **Faltante para un caso real:** Metadata does not imply a usable downloadable dataset; no STAC conformance is assumed.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No convertir metadatos en garantía de acceso, licencia o calidad del dataset.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-geonode--geonode"></a>

## GeoNode/geonode

- **Interfaz original:** API GeoNode y servicios asociados de la instalación.
- **Alcance de esta ficha:** candidate. Use GeoNode resource/project permissions and its native API; generic catalog profile does not assert STAC support.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| instance | catalog API and scope | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | native API/version and permissions |
| query | resource metadata search | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | geography, date, format and limits |

- **Preparación que hay que resolver:** Use the native CKAN/GeoNetwork/GeoNode API; resolve resource links and access terms before ingestion.
- **Validación requerida:** API version, pagination, resource IDs, license, format and link availability.
- **Faltante para un caso real:** Metadata does not imply a usable downloadable dataset; no STAC conformance is assumed.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir portal ni publicar capas sin respetar permisos/procedencia.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-geopython--pygeoapi"></a>

## geopython/pygeoapi

- **Interfaz original:** OGC API de colecciones/procesos de la instancia.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| instance | OGC service endpoint/capabilities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | version, collections, layers and processes |
| query | bounded layer/process parameters | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | CRS, extent, dimensions and authorization |

- **Preparación que hay que resolver:** Discover native capabilities and select only supported operations; separate querying from administration.
- **Validación requerida:** Advertised conformance, collection schema, CRS, filters, bounds and result links.
- **Faltante para un caso real:** A configured endpoint and actual provider data are required; process support cannot be inferred.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No crear otro adaptador por cada proceso OGC ni afirmar soporte de extensiones no configuradas.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-geoserver--geoserver"></a>

## geoserver/geoserver

- **Interfaz original:** WMS/WFS/OGC y REST administrativo según instalación.
- **Alcance de esta ficha:** candidate. Collections/maps via native OGC services; do not assume STAC, arbitrary process support or administrative access.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| instance | OGC service endpoint/capabilities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | version, collections, layers and processes |
| query | bounded layer/process parameters | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | CRS, extent, dimensions and authorization |

- **Preparación que hay que resolver:** Discover native capabilities and select only supported operations; separate querying from administration.
- **Validación requerida:** Advertised conformance, collection schema, CRS, filters, bounds and result links.
- **Faltante para un caso real:** A configured endpoint and actual provider data are required; process support cannot be inferred.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir map server ni usar credenciales administrativas para consultas del agente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-mapserver--mapserver"></a>

## MapServer/MapServer

- **Interfaz original:** Servicios OGC y configuración de mapfiles.
- **Alcance de esta ficha:** candidate. Native OGC/mapfile contract; STAC-like catalog fields are not a claim of STAC support.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| instance | OGC service endpoint/capabilities | Configured service/API instance (por configurar); Municipality, utility, transit agency or project owner (por configurar) | version, collections, layers and processes |
| query | bounded layer/process parameters | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | CRS, extent, dimensions and authorization |

- **Preparación que hay que resolver:** Discover native capabilities and select only supported operations; separate querying from administration.
- **Validación requerida:** Advertised conformance, collection schema, CRS, filters, bounds and result links.
- **Faltante para un caso real:** A configured endpoint and actual provider data are required; process support cannot be inferred.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No instalarlo además de GeoServer sin motivo ni reescribir renderizado.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-gama-platform--gama"></a>

## gama-platform/gama

- **Interfaz original:** Modelos GAML y ejecutor headless admitido.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No prometer un modelo social o urbano universal por tener un framework.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-mesa--mesa"></a>

## mesa/mesa

- **Interfaz original:** Clases y API del modelo definido por su autor.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** La novedad del modelo pertenece a quien lo define; Mesa no trae una ciudad calibrada.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-metadriverse--metaurban"></a>

## metadriverse/metaurban

- **Interfaz original:** API Python y motor/recursos del entorno.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir benchmark de agentes con predicción de movilidad real.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-netlogo--netlogo"></a>

## NetLogo/NetLogo

- **Interfaz original:** Ejecutor headless, modelos y BehaviorSpace según versión.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No tomar modelos educativos como modelos de política pública validados.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-tsinghua-fib-lab--agentsociety"></a>

## tsinghua-fib-lab/AgentSociety

- **Interfaz original:** APIs, modelos y proveedores de la versión elegida.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | declared scale and completeness |

- **Preparación que hay que resolver:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validación requerida:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Faltante para un caso real:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No equiparar conversación sintética con evidencia social ni disponibilidad libre de proveedores/datos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-tsinghua-fib-lab--citybench"></a>

## tsinghua-fib-lab/CityBench

- **Interfaz original:** Scripts, datasets y métricas de evaluación.
- **Alcance de esta ficha:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| references | urls | Original format/schema specifications (por configurar) | verify identity and date |

- **Preparación que hay que resolver:** Catalog only; no solver input or invented runtime.
- **Validación requerida:** Links, provenance and classification.
- **Faltante para un caso real:** Not an executable capability.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No presentarlo como motor de planificación ni confundir puntuación con utilidad real.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cesiumgs--3d-tiles-tools"></a>

## CesiumGS/3d-tiles-tools

- **Interfaz original:** CLI/API TypeScript y dependencias específicas.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No asumir que transforma cualquier modelo en tiles correctos ni duplicar conversores.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-cesiumgs--cesium"></a>

## CesiumGS/cesium

- **Interfaz original:** API JavaScript del visor; comparar MCP Cesium existente.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir globo/renderizador ni asumir credenciales de servicios asociados.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-itowns--itowns"></a>

## iTowns/itowns

- **Interfaz original:** API JavaScript y proveedores del visor.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No incluir todos los visores por defecto ni confundir captura con dato científico.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-keplergl--kepler.gl"></a>

## keplergl/kepler.gl

- **Interfaz original:** API del visor y src/mcp/src/server/index.ts recuperado.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** El catálogo anterior lo trataba solo como visor; no atribuirnos su MCP como novedad.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-maplibre--maplibre-gl-js"></a>

## maplibre/maplibre-gl-js

- **Interfaz original:** API JavaScript del mapa.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No atribuir análisis espacial al renderizador ni convertir todo dataset en GeoJSON del agente.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-terriajs--terriajs"></a>

## TerriaJS/terriajs

- **Interfaz original:** Modelos de catálogo y APIs de la aplicación.
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No reconstruir catálogo/visor ni asumir que todas sus fuentes tienen iguales permisos.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-visgl--deck.gl"></a>

## visgl/deck.gl

- **Interfaz original:** API JavaScript/TypeScript.
- **Alcance de esta ficha:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (por configurar); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (por configurar); Authorized files supplied for the case (por configurar) | target scene/session explicit |

- **Preparación que hay que resolver:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validación requerida:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Faltante para un caso real:** A renderable scene may omit analysis semantics or source accuracy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** No confundir visualización acelerada con análisis geográfico o almacenamiento.
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-palm"></a>

## external:palm

- **Interfaz original:** Version/API/CLI to be selected from upstream evidence
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (por configurar) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | no inferred physics without declaration |

- **Preparación que hay que resolver:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validación requerida:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Faltante para un caso real:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** Source, data and runtime admission are pending; documented commands are not execution evidence
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-telemac"></a>

## external:telemac

- **Interfaz original:** Version/API/CLI to be selected from upstream evidence
- **Alcance de esta ficha:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| mesh | bathymetry and computational mesh | [GEBCO bathymetry catalog](https://www.gebco.net/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | survey accuracy and vertical datum |
| forcing | flow/tide/wave series | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | matching boundary/time/units |
| parameters | model configuration | Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | turbulence, friction and module fixed |

- **Preparación que hay que resolver:** Use upstream mesh/case preparation; document boundary mapping and selected solver module.
- **Validación requerida:** Mesh quality, boundaries, datums, temporal alignment and reference-case diagnostics.
- **Faltante para un caso real:** Global bathymetry is not a harbor survey; field forcing and calibration may be required.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** Source, data and runtime admission are pending; documented commands are not execution evidence
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.

<a id="data-simstadt"></a>

## external:simstadt

- **Interfaz original:** Version/API/CLI to be selected from upstream evidence
- **Alcance de esta ficha:** candidate. Verify the current open release and workflow-specific inputs; legacy private-repository documentation is inconsistent with the current publisher notice.

| Entrada candidata | Formato/contrato | Posibles fuentes | Condición de admisión |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (por configurar); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (por configurar); Original tool examples/tests (por configurar) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (por configurar); Model author or qualified project team (por configurar); Original tool examples/tests (por configurar) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (por configurar); Original tool examples/tests (por configurar) | climate period and location |

- **Preparación que hay que resolver:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validación requerida:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Faltante para un caso real:** Global building data does not supply local building physics or occupancy.
- **Binding nativo:** pendiente de mapear cada entrada al archivo/API/argumento de la operación elegida; no se infiere de esta tabla.
- **Crítica propia del proyecto:** Source, data and runtime admission are pending; documented commands are not execution evidence
- **Siguiente contribución:** seleccionar una operación y un asset permitido, fijar versión/hash/licencia, documentar conversión y reproducir caso directo antes de probar MCP.
