# Tool data requirements and admitted scopes

**Status: proposed requirements, not general operational availability.** Each tool has a profile. These describe a first representative case; every operation needs its own native binding and may use a different subset. Dependencies inherit the parent capability's inputs. GTFS is not mandatory for geometric validation, nor HVAC inputs for a daylight calculation. Historical research descriptions retain their original language.

Candidate sources are not automatically downloaded, licensed or suitable assets. Operator sources require a specific project and authorization. 3 entry/entries have case-scoped admission; the rest retain `ready_to_run=false`. Admission does not cover every upstream function. See [the master test record](../../MASTER_TEST_RECORD.md) for executed evidence.

| Tool | Proposed profile | Status |
|---|---|---|
| [Deltares/Delft3D](#data-deltares--delft3d) | `coastal` | candidate; binding pending |
| [Deltares/hydromt](#data-deltares--hydromt) | `flood` | dependency; binding pending |
| [Deltares/hydromt_sfincs](#data-deltares--hydromt_sfincs) | `flood` | dependency; binding pending |
| [Deltares/hydromt_wflow](#data-deltares--hydromt_wflow) | `hydrology` | dependency; binding pending |
| [Deltares/SFINCS](#data-deltares--sfincs) | `flood` | candidate; binding pending |
| [GeoscienceAustralia/anuga_core](#data-geoscienceaustralia--anuga_core) | `flood` | candidate; binding pending |
| [MarkusPic/swmm_api](#data-markuspic--swmm_api) | `swmm` | dependency; binding pending |
| [openstreams/wflow](#data-openstreams--wflow) | `hydrology` | candidate; binding pending |
| [OpenWaterAnalytics/EPANET](#data-openwateranalytics--epanet) | `epanet` | candidate; binding pending |
| [pyswmm/pyswmm](#data-pyswmm--pyswmm) | `swmm` | candidate; binding pending |
| [USEPA/EPANET2.2](#data-usepa--epanet2.2) | `epanet` | candidate; binding pending |
| [USEPA/Stormwater-Management-Model](#data-usepa--stormwater-management-model) | `swmm` | candidate; binding pending |
| [USEPA/WNTR](#data-usepa--wntr) | `epanet` | candidate; binding pending |
| [blender/blender](#data-blender--blender) | `cad` | candidate; binding pending |
| [buildingSMART/BCF-XML](#data-buildingsmart--bcf-xml) | `bcf` | dependency; binding pending |
| [buildingSMART/IDS](#data-buildingsmart--ids) | `bim` | dependency; binding pending |
| [compas-dev/compas](#data-compas-dev--compas) | `cad` | candidate; binding pending |
| [compas-dev/compas_fab](#data-compas-dev--compas_fab) | `cad` | candidate; binding pending |
| [DynamoDS/Dynamo](#data-dynamods--dynamo) | `cad` | candidate; binding pending |
| [FreeCAD/FreeCAD](#data-freecad--freecad) | `cad` | candidate; binding pending |
| [IfcOpenShell/IfcOpenShell](#data-ifcopenshell--ifcopenshell) | `bim` | candidate; binding pending |
| [openscad/openscad](#data-openscad--openscad) | `cad` | candidate; binding pending |
| [PixarAnimationStudios/OpenUSD](#data-pixaranimationstudios--openusd) | `scene` | dependency; binding pending |
| [specklesystems/speckle-server](#data-specklesystems--speckle-server) | `object-service` | candidate; binding pending |
| [specklesystems/specklepy](#data-specklesystems--specklepy) | `object-service` | dependency; binding pending |
| [APA-Technology-Division/urban-and-regional-planning-resources](#data-apa-technology-division--urban-and-regional-planning-resources) | `none` | reference; binding pending |
| [durbanitas/awesome-urban-planning](#data-durbanitas--awesome-urban-planning) | `none` | reference; binding pending |
| [Ireliya/Awesome-Urban-Planning-Agents](#data-ireliya--awesome-urban-planning-agents) | `none` | reference; binding pending |
| [sacridini/Awesome-Geospatial](#data-sacridini--awesome-geospatial) | `none` | reference; binding pending |
| [kunifujiwara/VoxCity](#data-kunifujiwara--voxcity) | `microclimate` | candidate; binding pending |
| [ladybug-tools/uwg](#data-ladybug-tools--uwg) | `weather` | candidate; binding pending |
| [OpenFOAM/OpenFOAM-dev](#data-openfoam--openfoam-dev) | `cfd` | candidate; binding pending |
| [uDALES/u-dales](#data-udales--u-dales) | `atmosphere` | candidate; binding pending |
| [UMEP-dev/solweig](#data-umep-dev--solweig) | `microclimate` | candidate; binding pending |
| [UMEP-dev/SUEWS](#data-umep-dev--suews) | `microclimate` | candidate; binding pending |
| [UMEP-dev/UMEP](#data-umep-dev--umep) | `microclimate` | dependency; binding pending |
| [UMEP-dev/UMEP-processing](#data-umep-dev--umep-processing) | `microclimate` | candidate; binding pending |
| [USEPA/CMAQ](#data-usepa--cmaq) | `air-quality` | candidate; binding pending |
| [wrf-model/WRF](#data-wrf-model--wrf) | `atmosphere` | candidate; binding pending |
| [eclipse-ditto/ditto](#data-eclipse-ditto--ditto) | `context` | candidate; binding pending |
| [FIWARE/context.Orion-LD](#data-fiware--context.orion-ld) | `context` | candidate; binding pending |
| [FIWARE/tutorials.Step-by-Step](#data-fiware--tutorials.step-by-step) | `none` | reference; binding pending |
| [FraunhoferIOSB/FROST-Server](#data-fraunhoferiosb--frost-server) | `context` | candidate; binding pending |
| [ScorpioBroker/ScorpioBroker](#data-scorpiobroker--scorpiobroker) | `context` | candidate; binding pending |
| [smart-data-models/data-models](#data-smart-data-models--data-models) | `schemas` | dependency; binding pending |
| [telefonicaid/fiware-orion](#data-telefonicaid--fiware-orion) | `context` | candidate; binding pending |
| [thingsboard/thingsboard](#data-thingsboard--thingsboard) | `context` | candidate; binding pending |
| [HPSCIL/Open-Space-Cellular_Automata](#data-hpscil--open-space-cellular_automata) | `land-use` | candidate; binding pending |
| [johanlahti/urban-lu-model](#data-johanlahti--urban-lu-model) | `land-use` | candidate; binding pending |
| [LandInsightLab/MUSE](#data-landinsightlab--muse) | `land-use` | candidate; binding pending |
| [UDST/choicemodels](#data-udst--choicemodels) | `land-use` | dependency; binding pending |
| [UDST/developer](#data-udst--developer) | `land-use` | dependency; binding pending |
| [UDST/orca](#data-udst--orca) | `land-use` | dependency; binding pending |
| [UDST/urbansim](#data-udst--urbansim) | `land-use` | candidate; binding pending |
| [UDST/urbansim_defaults](#data-udst--urbansim_defaults) | `land-use` | dependency; binding pending |
| [UDST/urbansim_templates](#data-udst--urbansim_templates) | `land-use` | dependency; binding pending |
| [CityScope/CS_CityIO](#data-cityscope--cs_cityio) | `context` | candidate; binding pending |
| [CityScope/CS_cityscopeJS](#data-cityscope--cs_cityscopejs) | `context` | dependency; binding pending |
| [CityScope/CS_CityScoPy](#data-cityscope--cs_cityscopy) | `context` | dependency; binding pending |
| [CityScope/CS_Mobility_Service](#data-cityscope--cs_mobility_service) | `demand` | candidate; binding pending |
| [CityScope/CS_Simulation_GAMA](#data-cityscope--cs_simulation_gama) | `context` | dependency; binding pending |
| [consuldemocracy/consuldemocracy](#data-consuldemocracy--consuldemocracy) | `participation` | candidate; binding pending |
| [decidim/decidim](#data-decidim--decidim) | `participation` | candidate; binding pending |
| [umap-project/umap](#data-umap-project--umap) | `participation` | candidate; binding pending |
| [martibosch/pylandstats](#data-martibosch--pylandstats) | `landscape` | candidate; binding pending |
| [natcap/invest](#data-natcap--invest) | `ecosystem` | candidate; binding pending |
| [natcap/pygeoprocessing](#data-natcap--pygeoprocessing) | `raster` | dependency; binding pending |
| [r-spatialecology/landscapemetrics](#data-r-spatialecology--landscapemetrics) | `landscape` | candidate; binding pending |
| [architecture-building-systems/CityEnergyAnalyst](#data-architecture-building-systems--cityenergyanalyst) | `urban-energy` | candidate; binding pending |
| [BETALAB-team/EUReCA](#data-betalab-team--eureca) | `urban-energy` | candidate; binding pending |
| [KTH-UrbanT/mubes-ubem](#data-kth-urbant--mubes-ubem) | `urban-energy` | candidate; binding pending |
| [ladybug-tools/dragonfly-core](#data-ladybug-tools--dragonfly-core) | `urban-energy` | dependency; binding pending |
| [ladybug-tools/dragonfly-energy](#data-ladybug-tools--dragonfly-energy) | `energy` | candidate; binding pending |
| [ladybug-tools/honeybee-core](#data-ladybug-tools--honeybee-core) | `energy` | dependency; binding pending |
| [ladybug-tools/honeybee-energy](#data-ladybug-tools--honeybee-energy) | `energy` | candidate; binding pending |
| [ladybug-tools/honeybee-radiance](#data-ladybug-tools--honeybee-radiance) | `daylight` | candidate; binding pending |
| [ladybug-tools/ladybug](#data-ladybug-tools--ladybug) | `weather` | dependency; binding pending |
| [NatLabRockies/ComStock](#data-natlabrockies--comstock) | `urban-energy` | candidate; binding pending |
| [NatLabRockies/EnergyPlus](#data-natlabrockies--energyplus) | `energy` | candidate; binding pending |
| [NatLabRockies/OpenStudio](#data-natlabrockies--openstudio) | `energy` | dependency; binding pending |
| [NatLabRockies/OpenStudio-HPXML](#data-natlabrockies--openstudio-hpxml) | `energy` | dependency; binding pending |
| [NatLabRockies/resstock](#data-natlabrockies--resstock) | `urban-energy` | candidate; binding pending |
| [RWTH-EBC/TEASER](#data-rwth-ebc--teaser) | `energy` | candidate; binding pending |
| [samuelduchesne/archetypal](#data-samuelduchesne--archetypal) | `energy` | dependency; binding pending |
| [samuelduchesne/geomeppy](#data-samuelduchesne--geomeppy) | `energy` | dependency; binding pending |
| [santoshphilip/eppy](#data-santoshphilip--eppy) | `energy` | dependency; binding pending |
| [UCL/simstock](#data-ucl--simstock) | `urban-energy` | candidate; binding pending |
| [urbanopt/urbanopt-cli](#data-urbanopt--urbanopt-cli) | `urban-energy` | candidate; binding pending |
| [urbanopt/urbanopt-example-geojson-project](#data-urbanopt--urbanopt-example-geojson-project) | `urban-energy` | reference; binding pending |
| [urbanopt/urbanopt-reopt-gem](#data-urbanopt--urbanopt-reopt-gem) | `electrical` | dependency; binding pending |
| [CloudCompare/CloudCompare](#data-cloudcompare--cloudcompare) | `lidar` | candidate; binding pending |
| [isl-org/Open3D](#data-isl-org--open3d) | `lidar` | candidate; binding pending |
| [PDAL/PDAL](#data-pdal--pdal) | `lidar` | candidate; binding pending |
| [PDAL/python](#data-pdal--python) | `lidar` | dependency; binding pending |
| [potree/potree](#data-potree--potree) | `scene` | candidate; binding pending |
| [anandb/energyplus-mcp-java](#data-anandb--energyplus-mcp-java) | `energy` | candidate; binding pending |
| [bonninr/freecad_mcp](#data-bonninr--freecad_mcp) | `cad` | candidate; binding pending |
| [contextform/freecad-mcp](#data-contextform--freecad-mcp) | `cad` | candidate; binding pending |
| [ericmartinpe/EnergyPlus-MCP-epjson](#data-ericmartinpe--energyplus-mcp-epjson) | `energy` | candidate; binding pending |
| [gaopengbin/cesium-mcp](#data-gaopengbin--cesium-mcp) | `scene` | candidate; binding pending |
| [idfkit/idfkit-mcp](#data-idfkit--idfkit-mcp) | `energy` | candidate; binding pending |
| [jagan-shanmugam/open-streetmap-mcp](#data-jagan-shanmugam--open-streetmap-mcp) | `roads` | candidate; binding pending |
| [jjsantos01/qgis_mcp](#data-jjsantos01--qgis_mcp) | `vector` | candidate; binding pending |
| [JordanGunn/gdal-mcp](#data-jordangunn--gdal-mcp) | `vector` | candidate; case-scoped admission |
| [kLabUM/SWMM-MCP-PUB](#data-klabum--swmm-mcp-pub) | `swmm` | candidate; binding pending |
| [LBNL-ETA/EnergyPlus-MCP](#data-lbnl-eta--energyplus-mcp) | `energy` | candidate; binding pending |
| [mahdin75/gis-mcp](#data-mahdin75--gis-mcp) | `vector` | candidate; binding pending |
| [msradam/osmnx-mcp](#data-msradam--osmnx-mcp) | `roads` | candidate; binding pending |
| [neka-nat/freecad-mcp](#data-neka-nat--freecad-mcp) | `cad` | candidate; binding pending |
| [nkarasiak/qgis-mcp](#data-nkarasiak--qgis-mcp) | `vector` | candidate; binding pending |
| [OSGeo/grass-mcp](#data-osgeo--grass-mcp) | `vector` | reference; binding pending |
| [piatkowski/qgis-mcp](#data-piatkowski--qgis-mcp) | `vector` | candidate; binding pending |
| [ProfRino/bonsai-bim-skills](#data-profrino--bonsai-bim-skills) | `none` | reference; binding pending |
| [RainerGaier/energyplus-mcp-server](#data-rainergaier--energyplus-mcp-server) | `energy` | candidate; binding pending |
| [salog0d/UrbanPlannerMCP](#data-salog0d--urbanplannermcp) | `social` | candidate; binding pending |
| [Show2Instruct/ifc-bonsai-mcp](#data-show2instruct--ifc-bonsai-mcp) | `bim` | candidate; binding pending |
| [sparkgeo/geo-mcp-servers](#data-sparkgeo--geo-mcp-servers) | `stac` | candidate; binding pending |
| [spkane/freecad-addon-robust-mcp-server](#data-spkane--freecad-addon-robust-mcp-server) | `cad` | candidate; binding pending |
| [XRDS76354/SUMO-MCP-Server](#data-xrds76354--sumo-mcp-server) | `sumo` | candidate; binding pending |
| [Zhonghao1995/agentic-swmm-workflow](#data-zhonghao1995--agentic-swmm-workflow) | `swmm` | candidate; binding pending |
| [3dcitydb/3dcitydb](#data-3dcitydb--3dcitydb) | `city-model` | candidate; binding pending |
| [3dcitydb/citydb-tool](#data-3dcitydb--citydb-tool) | `city-model` | dependency; binding pending |
| [citygml4j/citygml-tools](#data-citygml4j--citygml-tools) | `city-model` | candidate; binding pending |
| [citygml4j/citygml4j](#data-citygml4j--citygml4j) | `city-model` | dependency; binding pending |
| [cityjson/cjio](#data-cityjson--cjio) | `city-model` | candidate; binding pending |
| [dtcc-platform/dtcc-core](#data-dtcc-platform--dtcc-core) | `city-model` | dependency; binding pending |
| [dtcc-platform/dtcc-sim](#data-dtcc-platform--dtcc-sim) | `cfd` | candidate; binding pending |
| [dtcc-platform/dtcc-viewer](#data-dtcc-platform--dtcc-viewer) | `scene` | candidate; binding pending |
| [Project-PLATEAU/PLATEAU-Builder](#data-project-plateau--plateau-builder) | `city-model` | candidate; binding pending |
| [Project-PLATEAU/PLATEAU-GIS-Converter](#data-project-plateau--plateau-gis-converter) | `city-model` | candidate; binding pending |
| [reearth/reearth-flow](#data-reearth--reearth-flow) | `city-model` | candidate; binding pending |
| [tudelft3d/3DCityDB-Tools-for-QGIS](#data-tudelft3d--3dcitydb-tools-for-qgis) | `city-model` | dependency; binding pending |
| [tudelft3d/3dfier](#data-tudelft3d--3dfier) | `reconstruction` | candidate; binding pending |
| [tudelft3d/City4CFD](#data-tudelft3d--city4cfd) | `cfd` | candidate; binding pending |
| [VCityTeam/UD-Viz](#data-vcityteam--ud-viz) | `scene` | candidate; binding pending |
| [benchmark-urbanism/cityseer-api](#data-benchmark-urbanism--cityseer-api) | `roads` | candidate; binding pending |
| [gboeing/osmnx](#data-gboeing--osmnx) | `roads` | candidate; case-scoped admission |
| [pysal/esda](#data-pysal--esda) | `statistics` | candidate; binding pending |
| [pysal/inequality](#data-pysal--inequality) | `statistics` | candidate; binding pending |
| [pysal/libpysal](#data-pysal--libpysal) | `statistics` | dependency; binding pending |
| [pysal/mgwr](#data-pysal--mgwr) | `statistics` | candidate; binding pending |
| [pysal/momepy](#data-pysal--momepy) | `statistics` | candidate; binding pending |
| [pysal/segregation](#data-pysal--segregation) | `statistics` | candidate; binding pending |
| [pysal/spopt](#data-pysal--spopt) | `statistics` | candidate; binding pending |
| [pysal/spreg](#data-pysal--spreg) | `statistics` | candidate; binding pending |
| [SpaceGroupUCL/depthmapX](#data-spacegroupucl--depthmapx) | `roads` | candidate; binding pending |
| [a-b-street/abstreet](#data-a-b-street--abstreet) | `sumo` | candidate; binding pending |
| [ActivitySim/activitysim](#data-activitysim--activitysim) | `demand` | candidate; binding pending |
| [ActivitySim/populationsim](#data-activitysim--populationsim) | `demand` | dependency; binding pending |
| [AequilibraE/aequilibrae](#data-aequilibrae--aequilibrae) | `traffic-assignment` | candidate; binding pending |
| [conveyal/analysis-backend](#data-conveyal--analysis-backend) | `transit` | candidate; binding pending |
| [conveyal/r5](#data-conveyal--r5) | `transit` | dependency; binding pending |
| [eclipse-sumo/sumo](#data-eclipse-sumo--sumo) | `sumo` | candidate; binding pending |
| [GIScience/openrouteservice](#data-giscience--openrouteservice) | `roads` | candidate; binding pending |
| [ipea/accessibility](#data-ipea--accessibility) | `accessibility` | candidate; binding pending |
| [ipea/r5r](#data-ipea--r5r) | `transit` | candidate; binding pending |
| [matsim-org/matsim-libs](#data-matsim-org--matsim-libs) | `demand` | candidate; binding pending |
| [MobilityData/gtfs-validator](#data-mobilitydata--gtfs-validator) | `transit` | dependency; binding pending |
| [opentripplanner/OpenTripPlanner](#data-opentripplanner--opentripplanner) | `transit` | candidate; binding pending |
| [Project-OSRM/osrm-backend](#data-project-osrm--osrm-backend) | `roads` | candidate; binding pending |
| [r5py/r5py](#data-r5py--r5py) | `transit` | candidate; binding pending |
| [ropensci/stplanr](#data-ropensci--stplanr) | `traffic-assignment` | candidate; binding pending |
| [UDST/synthpop](#data-udst--synthpop) | `demand` | candidate; binding pending |
| [valhalla/valhalla](#data-valhalla--valhalla) | `roads` | candidate; binding pending |
| [azavea/raster-vision](#data-azavea--raster-vision) | `imagery` | candidate; binding pending |
| [Open-EO/openeo-processes](#data-open-eo--openeo-processes) | `schemas` | dependency; binding pending |
| [Open-EO/openeo-python-client](#data-open-eo--openeo-python-client) | `eo-process` | candidate; binding pending |
| [opendatacube/datacube-core](#data-opendatacube--datacube-core) | `data-cube` | candidate; binding pending |
| [opengeos/geoai](#data-opengeos--geoai) | `imagery` | candidate; binding pending |
| [opengeos/segment-geospatial](#data-opengeos--segment-geospatial) | `imagery` | candidate; binding pending |
| [orfeotoolbox/OTB](#data-orfeotoolbox--otb) | `imagery` | candidate; binding pending |
| [orfeotoolbox/pyotb](#data-orfeotoolbox--pyotb) | `imagery` | dependency; binding pending |
| [sentinel-hub/sentinelhub-py](#data-sentinel-hub--sentinelhub-py) | `imagery` | candidate; binding pending |
| [stac-utils/pystac](#data-stac-utils--pystac) | `stac` | dependency; binding pending |
| [stac-utils/pystac-client](#data-stac-utils--pystac-client) | `stac` | candidate; binding pending |
| [stac-utils/stac-fastapi](#data-stac-utils--stac-fastapi) | `stac` | candidate; binding pending |
| [torchgeo/torchgeo](#data-torchgeo--torchgeo) | `imagery` | candidate; binding pending |
| [crowddynamics/crowddynamics](#data-crowddynamics--crowddynamics) | `social` | candidate; binding pending |
| [MengeCrowdSim/Menge](#data-mengecrowdsim--menge) | `social` | candidate; binding pending |
| [PedestrianDynamics/jupedsim](#data-pedestriandynamics--jupedsim) | `social` | candidate; binding pending |
| [svenkreiss/socialforce](#data-svenkreiss--socialforce) | `social` | candidate; binding pending |
| [dss-extensions/OpenDSSDirect.py](#data-dss-extensions--opendssdirect.py) | `electrical` | candidate; binding pending |
| [e2nIEE/pandapower](#data-e2niee--pandapower) | `electrical` | candidate; binding pending |
| [NatLabRockies/REopt_API](#data-natlabrockies--reopt_api) | `electrical` | candidate; binding pending |
| [oemof/oemof-solph](#data-oemof--oemof-solph) | `electrical` | candidate; binding pending |
| [PyPSA/PyPSA](#data-pypsa--pypsa) | `electrical` | candidate; binding pending |
| [RWTH-EBC/uesgraphs](#data-rwth-ebc--uesgraphs) | `electrical` | dependency; binding pending |
| [CLIMADA-project/climada_petals](#data-climada-project--climada_petals) | `risk` | dependency; binding pending |
| [CLIMADA-project/climada_python](#data-climada-project--climada_python) | `risk` | candidate; binding pending |
| [gem/oq-engine](#data-gem--oq-engine) | `risk` | candidate; binding pending |
| [Universite-Gustave-Eiffel/NoiseModelling](#data-universite-gustave-eiffel--noisemodelling) | `noise` | candidate; binding pending |
| [duckdb/duckdb-spatial](#data-duckdb--duckdb-spatial) | `vector` | candidate; binding pending |
| [geopandas/geopandas](#data-geopandas--geopandas) | `vector` | candidate; binding pending |
| [geotools/geotools](#data-geotools--geotools) | `vector` | dependency; binding pending |
| [jblindsay/whitebox-tools](#data-jblindsay--whitebox-tools) | `raster` | candidate; binding pending |
| [locationtech/jts](#data-locationtech--jts) | `vector` | dependency; binding pending |
| [opengeos/whitebox-python](#data-opengeos--whitebox-python) | `raster` | dependency; binding pending |
| [OSGeo/gdal](#data-osgeo--gdal) | `vector` | candidate; binding pending |
| [OSGeo/grass](#data-osgeo--grass) | `vector` | candidate; binding pending |
| [OSGeo/PROJ](#data-osgeo--proj) | `vector` | dependency; binding pending |
| [postgis/postgis](#data-postgis--postgis) | `spatial-db` | candidate; binding pending |
| [qgis/QGIS](#data-qgis--qgis) | `vector` | candidate; binding pending |
| [r-spatial/sf](#data-r-spatial--sf) | `vector` | candidate; binding pending |
| [rasterio/rasterio](#data-rasterio--rasterio) | `raster` | candidate; case-scoped admission |
| [rspatial/terra](#data-rspatial--terra) | `raster` | candidate; binding pending |
| [saga-gis/saga-gis](#data-saga-gis--saga-gis) | `raster` | candidate; binding pending |
| [shapely/shapely](#data-shapely--shapely) | `vector` | dependency; binding pending |
| [ckan/ckan](#data-ckan--ckan) | `resource-catalog` | candidate; binding pending |
| [geonetwork/core-geonetwork](#data-geonetwork--core-geonetwork) | `resource-catalog` | candidate; binding pending |
| [GeoNode/geonode](#data-geonode--geonode) | `resource-catalog` | candidate; binding pending |
| [geopython/pygeoapi](#data-geopython--pygeoapi) | `ogc-service` | candidate; binding pending |
| [geoserver/geoserver](#data-geoserver--geoserver) | `ogc-service` | candidate; binding pending |
| [MapServer/MapServer](#data-mapserver--mapserver) | `ogc-service` | candidate; binding pending |
| [gama-platform/gama](#data-gama-platform--gama) | `social` | candidate; binding pending |
| [mesa/mesa](#data-mesa--mesa) | `social` | candidate; binding pending |
| [metadriverse/metaurban](#data-metadriverse--metaurban) | `social` | candidate; binding pending |
| [NetLogo/NetLogo](#data-netlogo--netlogo) | `social` | candidate; binding pending |
| [tsinghua-fib-lab/AgentSociety](#data-tsinghua-fib-lab--agentsociety) | `social` | candidate; binding pending |
| [tsinghua-fib-lab/CityBench](#data-tsinghua-fib-lab--citybench) | `none` | reference; binding pending |
| [CesiumGS/3d-tiles-tools](#data-cesiumgs--3d-tiles-tools) | `scene` | candidate; binding pending |
| [CesiumGS/cesium](#data-cesiumgs--cesium) | `scene` | candidate; binding pending |
| [iTowns/itowns](#data-itowns--itowns) | `scene` | candidate; binding pending |
| [keplergl/kepler.gl](#data-keplergl--kepler.gl) | `scene` | candidate; binding pending |
| [maplibre/maplibre-gl-js](#data-maplibre--maplibre-gl-js) | `scene` | candidate; binding pending |
| [TerriaJS/terriajs](#data-terriajs--terriajs) | `scene` | candidate; binding pending |
| [visgl/deck.gl](#data-visgl--deck.gl) | `scene` | dependency; binding pending |
| [external:palm](#data-palm) | `microclimate` | candidate; binding pending |
| [external:telemac](#data-telemac) | `coastal` | candidate; binding pending |
| [external:simstadt](#data-simstadt) | `urban-energy` | candidate; binding pending |

<a id="data-deltares--delft3d"></a>

## Deltares/Delft3D

- **Original interface:** Archivos de caso y ejecutables originales.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| mesh | bathymetry and computational mesh | [GEBCO bathymetry catalog](https://www.gebco.net/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | survey accuracy and vertical datum |
| forcing | flow/tide/wave series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | matching boundary/time/units |
| parameters | model configuration | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | turbulence, friction and module fixed |

- **Preparation required:** Use upstream mesh/case preparation; document boundary mapping and selected solver module.
- **Validation required:** Mesh quality, boundaries, datums, temporal alignment and reference-case diagnostics.
- **Real-city blocker:** Global bathymetry is not a harbor survey; field forcing and calibration may be required.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir solver ni inferir batimetría o condiciones de borde.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-deltares--hydromt"></a>

## Deltares/hydromt

- **Original interface:** API y CLI HydroMT.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| terrain | terrain raster/mesh | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | terrain versus surface and vertical datum checked |
| land | landcover/roughness | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required) | classes translated with documented coefficients |
| forcing | rainfall/inflow/boundary series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | event and units fixed |

- **Preparation required:** Prepare using native tools/HydroMT, record resampling, grid, boundary conditions and coefficients.
- **Validation required:** Vertical/horizontal CRS, resolution fitness, wet/dry references, timestep and mass balance.
- **Real-city blocker:** Coarse surface products and reanalysis do not automatically support street-scale calibrated flood predictions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentarlo como solver; los plugins tienen versiones y requisitos propios.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-deltares--hydromt_sfincs"></a>

## Deltares/hydromt_sfincs

- **Original interface:** Configuración HydroMT y API del plugin.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| terrain | terrain raster/mesh | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | terrain versus surface and vertical datum checked |
| land | landcover/roughness | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required) | classes translated with documented coefficients |
| forcing | rainfall/inflow/boundary series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | event and units fixed |

- **Preparation required:** Prepare using native tools/HydroMT, record resampling, grid, boundary conditions and coefficients.
- **Validation required:** Vertical/horizontal CRS, resolution fitness, wet/dry references, timestep and mass balance.
- **Real-city blocker:** Coarse surface products and reanalysis do not automatically support street-scale calibrated flood predictions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuirle ejecución ni calibración del solver SFINCS.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-deltares--hydromt_wflow"></a>

## Deltares/hydromt_wflow

- **Original interface:** HydroMT y configuración del plugin.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| catchment | basin/river/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology and routing model |
| land | terrain/soil/cover | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); [ESA WorldCover](https://esa-worldcover.org/en); Municipality, utility, transit agency or project owner (configuration required) | resolution and parameter conversion |
| forcing | rainfall/evaporation series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | variables, units and timestep |

- **Preparation required:** Use the selected hydrological model/plugin; record basin delineation, parameters and forcing conversion.
- **Validation required:** Basin topology, units, temporal completeness, water balance and calibration diagnostics.
- **Real-city blocker:** A hydrological runoff model does not automatically produce street inundation depths.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar el modelo hidrológico ni asumir que datos globales lo calibran.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-deltares--sfincs"></a>

## Deltares/SFINCS

- **Original interface:** Ejecutable y archivos de caso; preparación separada.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| terrain | terrain raster/mesh | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | terrain versus surface and vertical datum checked |
| land | landcover/roughness | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required) | classes translated with documented coefficients |
| forcing | rainfall/inflow/boundary series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | event and units fixed |

- **Preparation required:** Prepare using native tools/HydroMT, record resampling, grid, boundary conditions and coefficients.
- **Validation required:** Vertical/horizontal CRS, resolution fitness, wet/dry references, timestep and mass balance.
- **Real-city blocker:** Coarse surface products and reanalysis do not automatically support street-scale calibrated flood predictions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No inventar datos de terreno, lluvia o fronteras; validar distribución binaria.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-geoscienceaustralia--anuga_core"></a>

## GeoscienceAustralia/anuga_core

- **Original interface:** API Python ANUGA y extensiones compiladas.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| terrain | terrain raster/mesh | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | terrain versus surface and vertical datum checked |
| land | landcover/roughness | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required) | classes translated with documented coefficients |
| forcing | rainfall/inflow/boundary series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | event and units fixed |

- **Preparation required:** Prepare using native tools/HydroMT, record resampling, grid, boundary conditions and coefficients.
- **Validation required:** Vertical/horizontal CRS, resolution fitness, wet/dry references, timestep and mass balance.
- **Real-city blocker:** Coarse surface products and reanalysis do not automatically support street-scale calibrated flood predictions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir esquema numérico ni vender una malla como modelo calibrado.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-markuspic--swmm_api"></a>

## MarkusPic/swmm_api

- **Original interface:** API Python de archivos INP, reportes y salidas.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | base revision and physical bounds |

- **Preparation required:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validation required:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Real-city blocker:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar PySWMM ni prometer control temporal por editar un archivo.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-openstreams--wflow"></a>

## openstreams/wflow

- **Original interface:** Scripts y configuraciones propios; verificar versión vigente.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| catchment | basin/river/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology and routing model |
| land | terrain/soil/cover | [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); [ESA WorldCover](https://esa-worldcover.org/en); Municipality, utility, transit agency or project owner (configuration required) | resolution and parameter conversion |
| forcing | rainfall/evaporation series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | variables, units and timestep |

- **Preparation required:** Use the selected hydrological model/plugin; record basin delineation, parameters and forcing conversion.
- **Validation required:** Basin topology, units, temporal completeness, water balance and calibration diagnostics.
- **Real-city blocker:** A hydrological runoff model does not automatically produce street inundation depths.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir este repositorio con todas las versiones actuales de wflow.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-openwateranalytics--epanet"></a>

## OpenWaterAnalytics/EPANET

- **Original interface:** Biblioteca C/toolkit y distribuciones originales.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | EPANET INP | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology, diameters, elevations, demands, pumps and controls |
| scenario | demand/pump/quality parameters | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units and time pattern explicit |

- **Preparation required:** Preserve native network and parameter sets, separate hypothetical interventions and measurement provenance.
- **Validation required:** Connectivity, hydraulic units, demand patterns, controls, solver status and mass/energy checks.
- **Real-city blocker:** Pipe inventory, demand and operating controls normally require the utility/project owner.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reescribir hidráulica; distinguir binding, motor y editor gráfico.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pyswmm--pyswmm"></a>

## pyswmm/pyswmm

- **Original interface:** API Python y motor asociado.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | base revision and physical bounds |

- **Preparation required:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validation required:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Real-city blocker:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar simulación ni elegirlo además de otro wrapper sin necesidad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-usepa--epanet2.2"></a>

## USEPA/EPANET2.2

- **Original interface:** Ejecutable/editor y archivos INP.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | EPANET INP | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology, diameters, elevations, demands, pumps and controls |
| scenario | demand/pump/quality parameters | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units and time pattern explicit |

- **Preparation required:** Preserve native network and parameter sets, separate hypothetical interventions and measurement provenance.
- **Validation required:** Connectivity, hydraulic units, demand patterns, controls, solver status and mass/energy checks.
- **Real-city blocker:** Pipe inventory, demand and operating controls normally require the utility/project owner.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No sumar otro motor hidráulico por confundir editor con toolkit.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-usepa--stormwater-management-model"></a>

## USEPA/Stormwater-Management-Model

- **Original interface:** Toolkit o ejecutable nativo.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | base revision and physical bounds |

- **Preparation required:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validation required:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Real-city blocker:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No construir un segundo solver; no duplicar la envoltura si ya cubre el caso.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-usepa--wntr"></a>

## USEPA/WNTR

- **Original interface:** API Python y conexión EPANET.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | EPANET INP | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology, diameters, elevations, demands, pumps and controls |
| scenario | demand/pump/quality parameters | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units and time pattern explicit |

- **Preparation required:** Preserve native network and parameter sets, separate hypothetical interventions and measurement provenance.
- **Validation required:** Connectivity, hydraulic units, demand patterns, controls, solver status and mass/energy checks.
- **Real-city blocker:** Pipe inventory, demand and operating controls normally require the utility/project owner.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir sus simuladores ni presentar fallas hipotéticas como observaciones.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-blender--blender"></a>

## blender/blender

- **Original interface:** API bpy en Blender y ejecución por proceso/plugin.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir editor; geometría visual no equivale a BIM ni simulación física.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-buildingsmart--bcf-xml"></a>

## buildingSMART/BCF-XML

- **Original interface:** Esquemas BCF y archivos de intercambio.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| issues | BCF package | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); [buildingSMART Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) | model revision and element references |
| model | IFC/reference | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | GUID mapping available |

- **Preparation required:** Validate schema and references and retain comment/issue authorship and revision.
- **Validation required:** Resolvable components, model version, geometry viewpoint units and permissions.
- **Real-city blocker:** Issue data and model access are project-provided.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir una especificación en motor ni duplicar gestión de incidencias existente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-buildingsmart--ids"></a>

## buildingSMART/IDS

- **Original interface:** XML y validadores compatibles por seleccionar.
- **Profile scope:** dependency. Requirements file plus IFC and a selected validator; schema documents are not a standalone solver.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | IFC | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); [buildingSMART Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) | schema, GUIDs, units and georeferencing |
| requirements | IDS or project constraints | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | requirements identify exact model revision |

- **Preparation required:** Validate IFC, map only explicit properties, preserve GUIDs and express losses in any conversion.
- **Validation required:** Schema version, units, geometry, references, georeferencing and required fields.
- **Real-city blocker:** Public footprints do not provide building systems, materials or a valid IFC model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No afirmar cumplimiento normativo general por pasar un IDS.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-compas-dev--compas"></a>

## compas-dev/compas

- **Original interface:** API Python COMPAS.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No publicar toda la API ni atribuirle validación estructural universal.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-compas-dev--compas_fab"></a>

## compas-dev/compas_fab

- **Original interface:** API Python y backends de robótica.
- **Profile scope:** candidate. Simulation-only planning requires robot/backend configuration; no hardware actuation admitted by this inventory.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No añadir operación de robots al alcance urbano por compartir geometría.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-dynamods--dynamo"></a>

## DynamoDS/Dynamo

- **Original interface:** Host de Dynamo y grafos; verificar ejecución automatizable.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir que todo nodo funciona fuera de su aplicación anfitriona.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-freecad--freecad"></a>

## FreeCAD/FreeCAD

- **Original interface:** API Python, FreeCADCmd y sesión gráfica.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir CAD; modelado libre y referencias topológicas requieren control.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ifcopenshell--ifcopenshell"></a>

## IfcOpenShell/IfcOpenShell

- **Original interface:** API Python/C++ y utilidades existentes.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | IFC | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); [buildingSMART Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) | schema, GUIDs, units and georeferencing |
| requirements | IDS or project constraints | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | requirements identify exact model revision |

- **Preparation required:** Validate IFC, map only explicit properties, preserve GUIDs and express losses in any conversion.
- **Validation required:** Schema version, units, geometry, references, georeferencing and required fields.
- **Real-city blocker:** Public footprints do not provide building systems, materials or a valid IFC model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reimplementar parser IFC ni inferir propiedades técnicas faltantes.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-openscad--openscad"></a>

## openscad/openscad

- **Original interface:** CLI y archivos de modelo.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No generar código irrestricto ni tratar sólidos como objetos BIM completos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pixaranimationstudios--openusd"></a>

## PixarAnimationStudios/OpenUSD

- **Original interface:** Bibliotecas y bindings USD.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir USD en modelo de autoridad urbana o inventar semántica IFC.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-specklesystems--speckle-server"></a>

## specklesystems/speckle-server

- **Original interface:** API de la instancia y autenticación correspondiente.
- **Profile scope:** candidate. Use authorized project/model/version IDs and native object data, not a STAC contract; instance API binding is pending.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| instance | project/model/version API | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | scope, native object protocol and credentials |
| objects | native object graph/artifact references | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | IDs, units and version ancestry |

- **Preparation required:** Preserve the native object graph, authorize the project and record serialization/conversion losses.
- **Validation required:** Project scope, object IDs, versions, units, permissions and round trip.
- **Real-city blocker:** A catalog protocol cannot substitute the native Speckle object/project contract.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir colaboración; verificar API y conectores de la versión instalada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-specklesystems--specklepy"></a>

## specklesystems/specklepy

- **Original interface:** SDK Python.
- **Profile scope:** dependency. Dependency of the Speckle connector; native project/object/version contract replaces generic catalog fields.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| instance | project/model/version API | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | scope, native object protocol and credentials |
| objects | native object graph/artifact references | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | IDs, units and version ancestry |

- **Preparation required:** Preserve the native object graph, authorize the project and record serialization/conversion losses.
- **Validation required:** Project scope, object IDs, versions, units, permissions and round trip.
- **Real-city blocker:** A catalog protocol cannot substitute the native Speckle object/project contract.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otra plataforma ni servidor MCP por cada SDK.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-apa-technology-division--urban-and-regional-planning-resources"></a>

## APA-Technology-Division/urban-and-regional-planning-resources

- **Original interface:** Documentos y enlaces del catálogo.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| references | urls | Original format/schema specifications (configuration required) | verify identity and date |

- **Preparation required:** Catalog only; no solver input or invented runtime.
- **Validation required:** Links, provenance and classification.
- **Real-city blocker:** Not an executable capability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No anunciar cada enlace como integración disponible.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-durbanitas--awesome-urban-planning"></a>

## durbanitas/awesome-urban-planning

- **Original interface:** Archivos documentales.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| references | urls | Original format/schema specifications (configuration required) | verify identity and date |

- **Preparation required:** Catalog only; no solver input or invented runtime.
- **Validation required:** Links, provenance and classification.
- **Real-city blocker:** Not an executable capability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No equiparar popularidad o inclusión en la lista con aptitud técnica.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ireliya--awesome-urban-planning-agents"></a>

## Ireliya/Awesome-Urban-Planning-Agents

- **Original interface:** Catálogo y enlaces a implementaciones.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| references | urls | Original format/schema specifications (configuration required) | verify identity and date |

- **Preparation required:** Catalog only; no solver input or invented runtime.
- **Validation required:** Links, provenance and classification.
- **Real-city blocker:** Not an executable capability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir un agente completo con una herramienta neutral para cualquier IA.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-sacridini--awesome-geospatial"></a>

## sacridini/Awesome-Geospatial

- **Original interface:** Documentos y enlaces.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| references | urls | Original format/schema specifications (configuration required) | verify identity and date |

- **Preparation required:** Catalog only; no solver input or invented runtime.
- **Validation required:** Links, provenance and classification.
- **Real-city blocker:** Not an executable capability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No prometer cobertura operativa de todos sus enlaces.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-kunifujiwara--voxcity"></a>

## kunifujiwara/VoxCity

- **Original interface:** API Python y proveedores de datos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (configuration required) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | no inferred physics without declaration |

- **Preparation required:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validation required:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Real-city blocker:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir estimaciones de geometría o vegetación en levantamiento observado.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ladybug-tools--uwg"></a>

## ladybug-tools/uwg

- **Original interface:** API Python y archivos meteorológicos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| series | weather/EPW | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); [NASA POWER](https://power.larc.nasa.gov/docs/services/api/); [ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | variable definition, interval and status |
| site | location and site parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | CRS, altitude and timezone |

- **Preparation required:** Translate formats explicitly; record timezone, resampling and observed/modelled/TMY distinction.
- **Validation required:** Coverage, variable units, missing values, calendar and station/grid representativeness.
- **Real-city blocker:** TMY and gridded reanalysis are not measurements of a chosen local event.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentarlo como CFD ni clima local validado sin parámetros adecuados.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-openfoam--openfoam-dev"></a>

## OpenFOAM/OpenFOAM-dev

- **Original interface:** Casos, diccionarios y ejecutables nativos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | watertight simulation geometry and mesh | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | domain, mesh quality and scale |
| conditions | boundary/initial conditions | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | velocity, turbulence, material and units |
| solver | case and numerical configuration | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | version and convergence criteria |

- **Preparation required:** Use native mesher/solver tools; separate geometry preparation from physical case validation.
- **Validation required:** Boundary completeness, mesh metrics, dimensions, timestep, residuals and conservation/reference fields.
- **Real-city blocker:** A display scene or OSM model does not provide a valid CFD mesh or calibrated conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No generar un CFD defendible solo a partir de edificios OSM.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-udales--u-dales"></a>

## uDALES/u-dales

- **Original interface:** Compilación y configuración del modelo.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| domain | mesh/domain/land inputs | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | nested grid and physics configuration |
| forcing | atmospheric initial/boundary data | [NCAR atmospheric forcing catalog](https://gdex.ucar.edu/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | full required variables and time |
| parameters | physics and model configuration | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | compiler/MPI/model compatibility |

- **Preparation required:** Keep upstream preprocessing and domain nesting; record forcing source and conversion chain.
- **Validation required:** Domain boundaries, vertical levels, forcing completeness, timestep and reference diagnostics.
- **Real-city blocker:** Surface ERA5-Land alone is not a full atmospheric initialization dataset.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir simulación de alta resolución con datos disponibles para cualquier ciudad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-umep-dev--solweig"></a>

## UMEP-dev/solweig

- **Original interface:** Entradas y ejecutor del proyecto; contrastar ruta UMEP.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (configuration required) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | no inferred physics without declaration |

- **Preparation required:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validation required:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Real-city blocker:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No mantener dos versiones de SOLWEIG por separado sin necesidad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-umep-dev--suews"></a>

## UMEP-dev/SUEWS

- **Original interface:** Configuración, forzamientos y wrapper admitido.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (configuration required) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | no inferred physics without declaration |

- **Preparation required:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validation required:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Real-city blocker:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No sustituir calibración, meteorología ni parámetros de superficie.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-umep-dev--umep"></a>

## UMEP-dev/UMEP

- **Original interface:** Plugin y algoritmos que exponga la versión instalada.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (configuration required) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | no inferred physics without declaration |

- **Preparation required:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validation required:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Real-city blocker:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir que todos los módulos corren sin escritorio.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-umep-dev--umep-processing"></a>

## UMEP-dev/UMEP-processing

- **Original interface:** Registro de algoritmos QGIS Processing.
- **Profile scope:** candidate. Each Processing algorithm selects a subset of climate inputs; no universal UMEP input bundle is claimed.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (configuration required) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | no inferred physics without declaration |

- **Preparation required:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validation required:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Real-city blocker:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No construir un MCP climático paralelo si el conector QGIS ya sirve el algoritmo.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-usepa--cmaq"></a>

## USEPA/CMAQ

- **Original interface:** Compilación, casos y forzamientos del sistema.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| meteorology | model-ready meteorological fields | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | selected chemistry/model grid |
| emissions | speciated spatial/temporal inventory | [JRC EDGAR emissions](https://edgar.jrc.ec.europa.eu/); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | conversion and sector assumptions |
| chemistry | mechanism/boundaries | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | compatible version and units |

- **Preparation required:** Use upstream preprocessing, explicit speciation/temporalization and emission-grid mapping.
- **Validation required:** Species, units, grids, meteorological coverage and mass/chemistry diagnostics.
- **Real-city blocker:** Global emissions inventory is not automatically a street-level or model-ready local inventory.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No simular calidad de aire sin inventarios de emisiones y meteorología compatibles.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-wrf-model--wrf"></a>

## wrf-model/WRF

- **Original interface:** Ejecutables WRF y cadena de preprocesamiento correspondiente.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| domain | mesh/domain/land inputs | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | nested grid and physics configuration |
| forcing | atmospheric initial/boundary data | [NCAR atmospheric forcing catalog](https://gdex.ucar.edu/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | full required variables and time |
| parameters | physics and model configuration | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | compiler/MPI/model compatibility |

- **Preparation required:** Keep upstream preprocessing and domain nesting; record forcing source and conversion chain.
- **Validation required:** Domain boundaries, vertical levels, forcing completeness, timestep and reference diagnostics.
- **Real-city blocker:** Surface ERA5-Land alone is not a full atmospheric initialization dataset.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No prometer predicción urbana lista sin condiciones iniciales y configuración física.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-eclipse-ditto--ditto"></a>

## eclipse-ditto/ditto

- **Original interface:** API HTTP/WebSocket de una instancia Ditto.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No sustituir su política ni confundir twin IoT con modelo urbano geográfico.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-fiware--context.orion-ld"></a>

## FIWARE/context.Orion-LD

- **Original interface:** API NGSI-LD de una instancia.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No inventar un broker ni convertir automáticamente modelos incompatibles.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-fiware--tutorials.step-by-step"></a>

## FIWARE/tutorials.Step-by-Step

- **Original interface:** Documentos, ejemplos y recetas.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| references | urls | Original format/schema specifications (configuration required) | verify identity and date |

- **Preparation required:** Catalog only; no solver input or invented runtime.
- **Validation required:** Links, provenance and classification.
- **Real-city blocker:** Not an executable capability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No contar cada tutorial como producto integrado ni copiar secretos de ejemplo.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-fraunhoferiosb--frost-server"></a>

## FraunhoferIOSB/FROST-Server

- **Original interface:** API SensorThings de la instancia.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar almacenamiento ni perder relaciones Sensor/Datastream/Observation.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-scorpiobroker--scorpiobroker"></a>

## ScorpioBroker/ScorpioBroker

- **Original interface:** API de la instancia Scorpio.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No instalarlo junto con Orion-LD por defecto; evaluar capacidades requeridas.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-smart-data-models--data-models"></a>

## smart-data-models/data-models

- **Original interface:** Esquemas y contextos seleccionados.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| schema | IDS/BCF/NGSI-LD/openEO definitions | Original format/schema specifications (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | exact version and profile |
| instance | data/model being validated | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | references and IDs preserved |

- **Preparation required:** Use maintained validator and explicit profile, report unresolved references.
- **Validation required:** Schema version, reference resolution, units and semantic requirements where defined.
- **Real-city blocker:** Schema validity is not scientific validity or evidence that a backend implements every operation.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No tratar nombres de entidades iguales como equivalencia semántica garantizada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-telefonicaid--fiware-orion"></a>

## telefonicaid/fiware-orion

- **Original interface:** API NGSIv2.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No etiquetar NGSIv2 como NGSI-LD ni ocultar pérdida semántica.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-thingsboard--thingsboard"></a>

## thingsboard/thingsboard

- **Original interface:** REST/telemetría de la instalación; revisar edición.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No mezclar funciones de ediciones distintas ni eludir permisos de dispositivo.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-hpscil--open-space-cellular_automata"></a>

## HPSCIL/Open-Space-Cellular_Automata

- **Original interface:** Código/datos reales pendientes de identificar.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No vender una referencia académica como motor mantenible.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-johanlahti--urban-lu-model"></a>

## johanlahti/urban-lu-model

- **Original interface:** Scripts, configuración y datos del proyecto.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No inferir aptitud actual ni extrapolar parámetros de otra ciudad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-landinsightlab--muse"></a>

## LandInsightLab/MUSE

- **Original interface:** Interfaz y configuraciones Python por revisar.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir simulación de uso del suelo con resultado normativo o causal.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-udst--choicemodels"></a>

## UDST/choicemodels

- **Original interface:** API Python.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuir causalidad ni validez local por ajustar un modelo.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-udst--developer"></a>

## UDST/developer

- **Original interface:** API Python y tablas del modelo.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentar supuestos de factibilidad como valuación o permisos aprobados.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-udst--orca"></a>

## UDST/orca

- **Original interface:** API y registro de pasos Orca.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No desarrollar otro scheduler que replique los pasos internos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-udst--urbansim"></a>

## UDST/urbansim

- **Original interface:** API Python y configuración de modelos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear un modelo de ciudad sin población, parcelas, estimación y calibración.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-udst--urbansim_defaults"></a>

## UDST/urbansim_defaults

- **Original interface:** Paquetes/tablas del proyecto.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No instalar defaults como modelo válido de cualquier municipio.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-udst--urbansim_templates"></a>

## UDST/urbansim_templates

- **Original interface:** API/configuraciones de plantillas.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| zones | parcels/buildings/zones | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | geography and legal vintage |
| population | population/jobs/market tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | compatible years and IDs |
| parameters | calibrated model/constraints | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | choice/feasibility assumptions |

- **Preparation required:** Prepare native model tables/configuration and distinguish observed stock from scenario assumptions.
- **Validation required:** Control totals, joins, IDs, calibration data, constraints and reference forecast.
- **Real-city blocker:** Parcel attributes, market data and local coefficients cannot be inferred from map geometry alone.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otra herramienta por cada plantilla ni prometer interoperabilidad entre versiones.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cityscope--cs_cityio"></a>

## CityScope/CS_CityIO

- **Original interface:** API del servidor CityIO.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir que todas las tablas comparten esquema o que una propuesta es dato observado.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cityscope--cs_cityscopejs"></a>

## CityScope/CS_cityscopeJS

- **Original interface:** Componentes y API del cliente.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar CityIO ni añadir un visor obligatorio al producto MCP.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cityscope--cs_cityscopy"></a>

## CityScope/CS_CityScoPy

- **Original interface:** SDK/API Python.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No desplegar otro servidor solo por existir un cliente Python.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cityscope--cs_mobility_service"></a>

## CityScope/CS_Mobility_Service

- **Original interface:** Código y contratos de la versión elegida.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | zones and skims compatible |

- **Preparation required:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validation required:** Control totals, missingness, joins, weights and model diagnostics.
- **Real-city blocker:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No llamar servicio productivo a un notebook ni inventar demanda.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cityscope--cs_simulation_gama"></a>

## CityScope/CS_Simulation_GAMA

- **Original interface:** Modelos GAML y ruta de intercambio CityScope.
- **Profile scope:** dependency. CityIO table mapping plus GAML model/population parameters are required; context entities alone cannot run the model.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| entities | JSON-LD/SensorThings/twin entities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | protocol/version and project |
| observations | telemetry/events | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | units, time and quality |
| mapping | vocabulary/IDs | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | semantics and transforms explicit |

- **Preparation required:** Query native API and translate only declared models; preserve timestamp/relationship semantics.
- **Validation required:** Schema/context, IDs, scope, units, pagination and temporal ordering.
- **Real-city blocker:** An endpoint, credentials and domain mapping may be required; protocols are not automatically equivalent.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuir resultados de ese modelo a toda ciudad o a cualquier versión GAMA.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-consuldemocracy--consuldemocracy"></a>

## consuldemocracy/consuldemocracy

- **Original interface:** APIs y extensiones admitidas por la instalación.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| process | authorized process/project reference | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | permissions and actual API capabilities |
| contribution | explicit contribution with provenance | Authorized files supplied for the case (configuration required); Municipality, utility, transit agency or project owner (configuration required) | authorship and intended submission |

- **Preparation required:** Use platform API; keep drafts separate from submissions and link to scenario only when authorized.
- **Validation required:** Process status, scope, identity, receipt and read-back.
- **Real-city blocker:** There is no universal public write endpoint or permission to speak/vote for participants.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No automatizar identidad, voto o decisiones ciudadanas ni reemplazar el proceso.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-decidim--decidim"></a>

## decidim/decidim

- **Original interface:** API disponible y extensiones Rails específicas.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| process | authorized process/project reference | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | permissions and actual API capabilities |
| contribution | explicit contribution with provenance | Authorized files supplied for the case (configuration required); Municipality, utility, transit agency or project owner (configuration required) | authorship and intended submission |

- **Preparation required:** Use platform API; keep drafts separate from submissions and link to scenario only when authorized.
- **Validation required:** Process status, scope, identity, receipt and read-back.
- **Real-city blocker:** There is no universal public write endpoint or permission to speak/vote for participants.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No inventar receptor ni pasar propuestas del agente por opiniones ciudadanas.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-umap-project--umap"></a>

## umap-project/umap

- **Original interface:** API/exportaciones de la instancia y GeoJSON.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| process | authorized process/project reference | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | permissions and actual API capabilities |
| contribution | explicit contribution with provenance | Authorized files supplied for the case (configuration required); Municipality, utility, transit agency or project owner (configuration required) | authorship and intended submission |

- **Preparation required:** Use platform API; keep drafts separate from submissions and link to scenario only when authorized.
- **Validation required:** Process status, scope, identity, receipt and read-back.
- **Real-city blocker:** There is no universal public write endpoint or permission to speak/vote for participants.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar editor ni asumir API de edición pública por tener exportación.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-martibosch--pylandstats"></a>

## martibosch/pylandstats

- **Original interface:** API Python.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| classes | categorical raster | [ESA WorldCover](https://esa-worldcover.org/en); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | class scheme, resolution and extent |
| parameters | metric definitions/coefficients | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood and ecological interpretation |

- **Preparation required:** Translate class schemes and grid definition explicitly; preserve metric definition.
- **Validation required:** Class codes, nodata, pixel area, neighborhood, extent and reference metrics.
- **Real-city blocker:** Landscape pattern does not automatically establish ecological function or observed biodiversity.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir métricas de patrón espacial en biodiversidad observada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-natcap--invest"></a>

## natcap/invest

- **Original interface:** API/modelos y paquetes de datos específicos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| land | landcover and environmental layers | [ESA WorldCover](https://esa-worldcover.org/en); [ISRIC SoilGrids](https://isric.org/explore/soilgrids); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | required model layers |
| coefficients | biophysical tables/valuation assumptions | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | local applicability |
| forcing | model-specific climate/hydrology | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | explicit selected InVEST model |

- **Preparation required:** Select one upstream model, prepare its tables and layers and record assumptions.
- **Validation required:** Each model input specification, coverage, units and reference outputs.
- **Real-city blocker:** Coefficients, observations and local validation are not supplied by a generic global raster.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No generar servicios ecosistémicos sin coeficientes/datos locales ni duplicar modelos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-natcap--pygeoprocessing"></a>

## natcap/pygeoprocessing

- **Original interface:** API Python y dependencias GDAL.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required) | band meaning, nodata and resolution explicit |

- **Preparation required:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validation required:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Real-city blocker:** An available raster can be unsuitable for the intended analysis.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear un MCP separado por una biblioteca auxiliar.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-r-spatialecology--landscapemetrics"></a>

## r-spatialecology/landscapemetrics

- **Original interface:** API R.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| classes | categorical raster | [ESA WorldCover](https://esa-worldcover.org/en); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | class scheme, resolution and extent |
| parameters | metric definitions/coefficients | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood and ecological interpretation |

- **Preparation required:** Translate class schemes and grid definition explicitly; preserve metric definition.
- **Validation required:** Class codes, nodata, pixel area, neighborhood, extent and reference metrics.
- **Real-city blocker:** Landscape pattern does not automatically establish ecological function or observed biodiversity.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No exponer simultáneamente métricas homónimas de otra biblioteca como equivalentes.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-architecture-building-systems--cityenergyanalyst"></a>

## architecture-building-systems/CityEnergyAnalyst

- **Original interface:** Scripts/API CEA y estructura de escenario.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otro UBEM ni asumir edificios y usos completos en cualquier ciudad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-betalab-team--eureca"></a>

## BETALAB-team/EUReCA

- **Original interface:** API/ejecutor Python EUReCA.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No tratar aproximaciones de arquetipos como datos observados ni duplicar CEA sin caso.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-kth-urbant--mubes-ubem"></a>

## KTH-UrbanT/mubes-ubem

- **Original interface:** Ejecutor Python y EnergyPlus de la versión elegida.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No sumar otro frontend energético antes de demostrar diferencia frente a CEA/URBANopt.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ladybug-tools--dragonfly-core"></a>

## ladybug-tools/dragonfly-core

- **Original interface:** API Python y formatos nativos.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No vender conversión geométrica como simulación energética.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ladybug-tools--dragonfly-energy"></a>

## ladybug-tools/dragonfly-energy

- **Original interface:** API y CLI de Dragonfly Energy.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir traductor ni ocultar pérdida de detalle entre representaciones.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ladybug-tools--honeybee-core"></a>

## ladybug-tools/honeybee-core

- **Original interface:** API Python y HBJSON.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar esquema de edificios ni tratar toda geometría IFC como térmica.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ladybug-tools--honeybee-energy"></a>

## ladybug-tools/honeybee-energy

- **Original interface:** API/CLI y herramientas energéticas admitidas.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuir certificación o calibración por lograr una corrida.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ladybug-tools--honeybee-radiance"></a>

## ladybug-tools/honeybee-radiance

- **Original interface:** API/CLI de recetas y motor Radiance externo.
- **Profile scope:** candidate. Lighting requires sensors/materials/sky recipe, not necessarily HVAC; bind a separate daylight case.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | Honeybee/Radiance scene | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | surfaces, optical materials and scene units |
| sky | sky/weather recipe | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | time, location and recipe |
| receivers | sensor grid and parameters | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | orientation, spacing and result units |

- **Preparation required:** Use native Radiance/Honeybee recipe and preserve sensor IDs and execution parameters.
- **Validation required:** Scene geometry, material definitions, sky, sensor orientation and known light result.
- **Real-city blocker:** A footprint or HVAC model is not a complete daylight scene.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reimplementar trazado ni reutilizar parámetros entre estudios sin validación.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ladybug-tools--ladybug"></a>

## ladybug-tools/ladybug

- **Original interface:** API Python y estructuras meteorológicas.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| series | weather/EPW | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); [NASA POWER](https://power.larc.nasa.gov/docs/services/api/); [ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=overview); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | variable definition, interval and status |
| site | location and site parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | CRS, altitude and timezone |

- **Preparation required:** Translate formats explicitly; record timezone, resampling and observed/modelled/TMY distinction.
- **Validation required:** Coverage, variable units, missing values, calendar and station/grid representativeness.
- **Real-city blocker:** TMY and gridded reanalysis are not measurements of a chosen local event.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otra API meteorológica superpuesta ni inferir confort completo con una métrica.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-natlabrockies--comstock"></a>

## NatLabRockies/ComStock

- **Original interface:** Workflows, medidas y datos propios del proyecto.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No trasladar stock/arquetipos estadounidenses como representación de otra ciudad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-natlabrockies--energyplus"></a>

## NatLabRockies/EnergyPlus

- **Original interface:** Ejecutable y API oficial de EnergyPlus.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear simulador propio ni usar un IDF incompatible con su versión.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-natlabrockies--openstudio"></a>

## NatLabRockies/OpenStudio

- **Original interface:** CLI, bindings y medidas compatibles.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir SDK ni asumir compatibilidad entre cualquier OpenStudio y EnergyPlus.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-natlabrockies--openstudio-hpxml"></a>

## NatLabRockies/OpenStudio-HPXML

- **Original interface:** Medidas Ruby y ejecutor OpenStudio.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No rehacer conversor ni confundir cumplimiento XML con validez del edificio.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-natlabrockies--resstock"></a>

## NatLabRockies/resstock

- **Original interface:** Workflows y muestreo del proyecto.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No extrapolar stock estadounidense a cualquier municipio sin adaptación científica.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-rwth-ebc--teaser"></a>

## RWTH-EBC/TEASER

- **Original interface:** API Python y exportaciones Modelica.
- **Profile scope:** candidate. Produces models (e.g. Modelica) requiring another admitted simulator; EnergyPlus formats are not assumed equivalent.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No afirmar que exportar Modelica ya ejecuta o valida el modelo.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-samuelduchesne--archetypal"></a>

## samuelduchesne/archetypal

- **Original interface:** API/CLI Python y dependencia EnergyPlus.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No mantener otro simulador; comprobar compatibilidad del paquete con EnergyPlus.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-samuelduchesne--geomeppy"></a>

## samuelduchesne/geomeppy

- **Original interface:** API Python sobre eppy.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir geometría sintética en envolvente térmica completa.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-santoshphilip--eppy"></a>

## santoshphilip/eppy

- **Original interface:** API Python y diccionario de versión.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reescribir lector IDF ni usar diccionario de otra versión.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ucl--simstock"></a>

## UCL/simstock

- **Original interface:** API Python y pipeline SimStock.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir que huellas urbanas bastan para deducir usos y construcciones.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-urbanopt--urbanopt-cli"></a>

## urbanopt/urbanopt-cli

- **Original interface:** CLI Ruby y estructura GeoJSON/workflows.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No ejecutar cualquier proyecto descargado ni duplicar CityEnergyAnalyst sin requisito.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-urbanopt--urbanopt-example-geojson-project"></a>

## urbanopt/urbanopt-example-geojson-project

- **Original interface:** Archivos GeoJSON, workflows y medidas de ejemplo.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No contar el ejemplo como otro motor o como escenario real de una ciudad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-urbanopt--urbanopt-reopt-gem"></a>

## urbanopt/urbanopt-reopt-gem

- **Original interface:** Gem Ruby y servicio/ejecutor REopt correspondiente.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | objective and solver stated |

- **Preparation required:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validation required:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Real-city blocker:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar REopt ni atribuir rentabilidad cierta a un escenario.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cloudcompare--cloudcompare"></a>

## CloudCompare/CloudCompare

- **Original interface:** CLI y herramientas de la aplicación.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| cloud | LAS/LAZ/PLY/point cloud | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | scale, origin, CRS and acquisition metadata |
| pipeline | native processing parameters | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | filters and tolerances explicit |

- **Preparation required:** Run native pipeline, subset without losing coordinate metadata and export artifact references.
- **Validation required:** Point count, CRS, precision, classification, transform and known-geometry checks.
- **Real-city blocker:** Local survey coverage and acquisition quality are project-specific.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir registro de nubes ni perder CRS/escalas globales.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-isl-org--open3d"></a>

## isl-org/Open3D

- **Original interface:** API Python/C++ de Open3D.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| cloud | LAS/LAZ/PLY/point cloud | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | scale, origin, CRS and acquisition metadata |
| pipeline | native processing parameters | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | filters and tolerances explicit |

- **Preparation required:** Run native pipeline, subset without losing coordinate metadata and export artifact references.
- **Validation required:** Point count, CRS, precision, classification, transform and known-geometry checks.
- **Real-city blocker:** Local survey coverage and acquisition quality are project-specific.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentar registro aproximado como levantamiento topográfico certificado.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pdal--pdal"></a>

## PDAL/PDAL

- **Original interface:** CLI y pipelines JSON PDAL.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| cloud | LAS/LAZ/PLY/point cloud | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | scale, origin, CRS and acquisition metadata |
| pipeline | native processing parameters | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | filters and tolerances explicit |

- **Preparation required:** Run native pipeline, subset without losing coordinate metadata and export artifact references.
- **Validation required:** Point count, CRS, precision, classification, transform and known-geometry checks.
- **Real-city blocker:** Local survey coverage and acquisition quality are project-specific.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reescribir formatos LAS/LAZ ni publicar filtros sin unidades y CRS.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pdal--python"></a>

## PDAL/python

- **Original interface:** API Python y biblioteca PDAL compatible.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| cloud | LAS/LAZ/PLY/point cloud | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | scale, origin, CRS and acquisition metadata |
| pipeline | native processing parameters | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | filters and tolerances explicit |

- **Preparation required:** Run native pipeline, subset without losing coordinate metadata and export artifact references.
- **Validation required:** Point count, CRS, precision, classification, transform and known-geometry checks.
- **Real-city blocker:** Local survey coverage and acquisition quality are project-specific.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No mantener dos instalaciones PDAL incompatibles ni otro servidor equivalente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-potree--potree"></a>

## potree/potree

- **Original interface:** API JavaScript y formato servido por el visor.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir que el visor convierte LAS ni duplicar un visor ya seleccionado.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-anandb--energyplus-mcp-java"></a>

## anandb/energyplus-mcp-java

- **Original interface:** Servidor y herramientas upstream.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No construir otro MCP EnergyPlus por preferencia de lenguaje.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-bonninr--freecad_mcp"></a>

## bonninr/freecad_mcp

- **Original interface:** main.py remite a blender_mcp.server; comprobar paquete y bridge efectivos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** El nombre del repositorio no acredita control FreeCAD; el namespace observado requiere investigación.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-contextform--freecad-mcp"></a>

## contextform/freecad-mcp

- **Original interface:** Servidor y material histórico del repositorio.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** La inspección encontró código en archive; eso no acredita un servidor vigente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ericmartinpe--energyplus-mcp-epjson"></a>

## ericmartinpe/EnergyPlus-MCP-epjson

- **Original interface:** Servidor Python y conversión IDF/epJSON existentes.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir inspección/edición ya expuestas ni adoptar todos los forks.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-gaopengbin--cesium-mcp"></a>

## gaopengbin/cesium-mcp

- **Original interface:** Paquetes TypeScript de servidor/contratos y conexión a visor.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reemplazar renderizador ni asumir un visor conectado por iniciar el servidor.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-idfkit--idfkit-mcp"></a>

## idfkit/idfkit-mcp

- **Original interface:** Entradas del paquete idfkit-mcp.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No sumar otro servidor energético sin diferencia funcional probada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-jagan-shanmugam--open-streetmap-mcp"></a>

## jagan-shanmugam/open-streetmap-mcp

- **Original interface:** Herramientas upstream y servicios externos que invocan.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [INEGI Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | direction topology and cost definition with source supporting declared travel mode |

- **Preparation required:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validation required:** Connectivity, direction, intersection semantics, units and source coverage.
- **Real-city blocker:** Mapped roads do not imply capacity, reliable speed, pedestrian completeness or traffic demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentarlo como servidor OSM autosuficiente ni inventar disponibilidad de proveedores.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-jjsantos01--qgis_mcp"></a>

## jjsantos01/qgis_mcp

- **Original interface:** Herramientas para proyectos, capas y operaciones de sesión.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No rehacer carga/edición existentes ni confundir conexión con validez de Processing.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-jordangunn--gdal-mcp"></a>

## JordanGunn/gdal-mcp

- **Original interface:** Servidor y módulos upstream.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.
- **Scoped executable case:** [helsinki-service-inventory](../../cases/helsinki-service-inventory/README.md); operations: harvest_municipal_sources, inventory_by_district, municipal_status, prepare_municipal_data, raster_convert, raster_info, raster_query, raster_reproject, raster_stats, read_case_artifact, service_catalog, store_justification, vector_buffer, vector_clip, vector_convert, vector_info, vector_query, vector_reproject, vector_simplify. The generic profile below remains a proposal for other operations.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** verified only for the linked case and operations; the generic profile does not admit additional operations.
- **Project critique:** No construir otro GDAL MCP sin contrastar catálogo, límites y salidas.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-klabum--swmm-mcp-pub"></a>

## kLabUM/SWMM-MCP-PUB

- **Original interface:** Herramientas list_models, duplicate_model, run_model y reportes identificadas.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | base revision and physical bounds |

- **Preparation required:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validation required:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Real-city blocker:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No proponer como nuevo un run_model ya implementado; revisar unidades de edición.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-lbnl-eta--energyplus-mcp"></a>

## LBNL-ETA/EnergyPlus-MCP

- **Original interface:** Servidor Python, configuración y receta de contenedor upstream.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuir como aporte propio cargar/validar/simular si ya está expuesto.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-mahdin75--gis-mcp"></a>

## mahdin75/gis-mcp

- **Original interface:** Servidor real y separación frente a agentes por localizar.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** Una prueba de herramientas en LangChain no demuestra el punto de arranque del servidor.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-msradam--osmnx-mcp"></a>

## msradam/osmnx-mcp

- **Original interface:** FastMCP create_server/mount with process-global named graph registry; Python OSMnx/NetworkX.
- **Profile scope:** candidate. Source/runtime audit recorded in cases/two-city-walking/upstream-audit.md; this third-party MCP is not admitted or redistributed.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [INEGI Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | direction topology and cost definition with source supporting declared travel mode |

- **Preparation required:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validation required:** Connectivity, direction, intersection semantics, units and source coverage.
- **Real-city blocker:** Mapped roads do not imply capacity, reliable speed, pedestrian completeness or traffic demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No declared license at inspected revision; route totals assume key 0, bbox order differs from current OSMnx, metric preconditions/portable plotting and municipal data contracts are missing.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-neka-nat--freecad-mcp"></a>

## neka-nat/freecad-mcp

- **Original interface:** Servidor Python y RPC del addon.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No construir otro sistema de jobs sin probar el existente; no publicar ejecución libre por defecto.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-nkarasiak--qgis-mcp"></a>

## nkarasiak/qgis-mcp

- **Original interface:** Servidor, plugin y resolución de instancias identificados.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No proponer descubrimiento multiinstancia como novedad si ya está implementado.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-osgeo--grass-mcp"></a>

## OSGeo/grass-mcp

- **Original interface:** README/licencia; no se localizaron archivos de implementación.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentarlo como MCP instalable ni contar una prueba aprobada inexistente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-piatkowski--qgis-mcp"></a>

## piatkowski/qgis-mcp

- **Original interface:** Herramientas de capa, reproyección, recorte, estadísticas y exportación identificadas.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir funciones ya expuestas; medir diferencias frente a otros QGIS MCP.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-profrino--bonsai-bim-skills"></a>

## ProfRino/bonsai-bim-skills

- **Original interface:** Instrucciones y funciones Python del proyecto.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| references | urls | Original format/schema specifications (configuration required) | verify identity and date |

- **Preparation required:** Catalog only; no solver input or invented runtime.
- **Validation required:** Links, provenance and classification.
- **Real-city blocker:** Not an executable capability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No anunciar skills como endpoint MCP ni copiar instrucciones como código de confianza.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-rainergaier--energyplus-mcp-server"></a>

## RainerGaier/energyplus-mcp-server

- **Original interface:** Servidor MCP y rutas HTTP identificadas.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| building_model | IDF/epJSON/HBJSON/HPXML | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | engine-compatible physical model |
| weather | EPW/weather reference | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | location, period, timezone and units |
| physics | materials systems occupancy schedules | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | may be embedded in the building model |

- **Preparation required:** Use native translator and version transition only where supported; preserve schedules and simulation settings.
- **Validation required:** Model schema/version, closed zones, units, weather coverage, HVAC/schedules and native error reports.
- **Real-city blocker:** Footprints and EPW alone cannot determine a complete or calibrated energy model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otra API de jobs o generación si sus rutas ya cubren la necesidad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-salog0d--urbanplannermcp"></a>

## salog0d/UrbanPlannerMCP

- **Original interface:** run_city_infra_model y run_population_inequalities_model identificadas.
- **Profile scope:** candidate. Requires inspecting the actual model formulas/parameters; a general social profile is not its approved input schema.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No tratar UrbanPlanner como cobertura de todo urbanismo ni convertir estimaciones en hechos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-show2instruct--ifc-bonsai-mcp"></a>

## Show2Instruct/ifc-bonsai-mcp

- **Original interface:** Servidor, addon y servicio de embeddings separado.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | IFC | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); [buildingSMART Sample-Test-Files](https://github.com/buildingSMART/Sample-Test-Files) | schema, GUIDs, units and georeferencing |
| requirements | IDS or project constraints | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | requirements identify exact model revision |

- **Preparation required:** Validate IFC, map only explicit properties, preserve GUIDs and express losses in any conversion.
- **Validation required:** Schema version, units, geometry, references, georeferencing and required fields.
- **Real-city blocker:** Public footprints do not provide building systems, materials or a valid IFC model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir el stack completo en requisito de leer un IFC; revisar código ejecutable expuesto.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-sparkgeo--geo-mcp-servers"></a>

## sparkgeo/geo-mcp-servers

- **Original interface:** Subpaquetes y puntos de arranque por identificar individualmente.
- **Profile scope:** candidate. First split monorepo into actual servers and data contracts; this is a catalog-level starting point only.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| catalog | STAC API/item collection | Configured service/API instance (configuration required); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | conformance, pagination and asset links |
| query | area/time/bands | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | explicit search limits |

- **Preparation required:** Discover capabilities, filter, preserve item/asset versions and resolve authorized assets.
- **Validation required:** Conformance, item IDs, geometry, datetime, asset availability and rights.
- **Real-city blocker:** A catalog entry does not prove the asset is downloadable or fit for a model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** Un healthcheck del repositorio no acredita todas sus herramientas.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-spkane--freecad-addon-robust-mcp-server"></a>

## spkane/freecad-addon-robust-mcp-server

- **Original interface:** MCPServer, registro de componentes y bridge de FreeCAD.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| document | native CAD/project template | Authorized files supplied for the case (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and parametric dependencies |
| parameters | admitted typed changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | bounds and intended result |

- **Preparation required:** Open a separate document/session, apply native operations and preserve recompute/save semantics.
- **Validation required:** Native reopen, object identity, dimensions, recompute status and version.
- **Real-city blocker:** A geometric object is not a complete engineering/BIM model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reimplementar timeouts o bridge sin identificar falla; distinguir timeout de detener cálculo.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-xrds76354--sumo-mcp-server"></a>

## XRDS76354/SUMO-MCP-Server

- **Original interface:** manage_network, control_simulation y query_simulation_state identificadas.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | SUMO net.xml | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | netconvert and junction assumptions recorded |
| demand | SUMO routes/trips/OD | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | observed or synthetic status explicit |
| config | sumocfg | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | seed, time and vehicle types fixed |

- **Preparation required:** Convert network with SUMO tools, prepare demand separately, resolve relative file references and preserve assumptions.
- **Validation required:** Network-route consistency, edge IDs, units, time coverage, vehicle counts and configuration.
- **Real-city blocker:** OSM cannot supply calibrated OD demand or signal timings everywhere.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No vender sus comandos de optimización como mejora garantizada; revisar estado compartido.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-zhonghao1995--agentic-swmm-workflow"></a>

## Zhonghao1995/agentic-swmm-workflow

- **Original interface:** Servidores JavaScript identificados y orquestador del proyecto.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | SWMM INP | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | nodes, conduits, invert levels, sections, roughness and catchments |
| rainfall | series or embedded INP series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units, timestep and event explicit |
| scenario | parameter changes | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | base revision and physical bounds |

- **Preparation required:** Parse/validate INP, check referenced series, use copies for alternatives and preserve declared units.
- **Validation required:** Topology, conduit/node references, catchment coverage, rainfall interval, continuity and native diagnostics.
- **Real-city blocker:** Street maps and global DEM do not provide a hydraulic drainage model or design rainfall.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir workflow agentic con motor hidráulico ni duplicar herramientas ya disponibles.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-3dcitydb--3dcitydb"></a>

## 3dcitydb/3dcitydb

- **Original interface:** Esquema SQL y herramientas de su versión.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar base 3D ni confundir v4/v5 y sus herramientas compatibles.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-3dcitydb--citydb-tool"></a>

## 3dcitydb/citydb-tool

- **Original interface:** CLI Java y conexión a esquema compatible.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No desarrollar importador CityGML propio ni lanzar migraciones como consulta ordinaria.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-citygml4j--citygml-tools"></a>

## citygml4j/citygml-tools

- **Original interface:** CLI Java del proyecto.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otra implementación de cada versión del formato.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-citygml4j--citygml4j"></a>

## citygml4j/citygml4j

- **Original interface:** API Java.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No mantener parser propio ni un servicio por cada biblioteca.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cityjson--cjio"></a>

## cityjson/cjio

- **Original interface:** API/CLI Python cjio.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir toda ciudad a GeoJSON perdiendo superficies y semántica.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-dtcc-platform--dtcc-core"></a>

## dtcc-platform/dtcc-core

- **Original interface:** API Python y extensiones del proyecto.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No añadir una representación urbana universal sin probar correspondencia.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-dtcc-platform--dtcc-sim"></a>

## dtcc-platform/dtcc-sim

- **Original interface:** Servicio/ejecutor y contratos de esa versión.
- **Profile scope:** candidate. Model/service must be identified before this proposed CFD profile can be accepted as its interface.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | watertight simulation geometry and mesh | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | domain, mesh quality and scale |
| conditions | boundary/initial conditions | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | velocity, turbulence, material and units |
| solver | case and numerical configuration | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | version and convergence criteria |

- **Preparation required:** Use native mesher/solver tools; separate geometry preparation from physical case validation.
- **Validation required:** Boundary completeness, mesh metrics, dimensions, timestep, residuals and conservation/reference fields.
- **Real-city blocker:** A display scene or OSM model does not provide a valid CFD mesh or calibrated conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuir cobertura científica al nombre sim sin identificar modelos y datos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-dtcc-platform--dtcc-viewer"></a>

## dtcc-platform/dtcc-viewer

- **Original interface:** API y ejecutor del visor.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otro visor obligatorio ni confundir mostrar con validar simulación.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-project-plateau--plateau-builder"></a>

## Project-PLATEAU/PLATEAU-Builder

- **Original interface:** Aplicación Java y formatos de proyecto.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir editor ni prometer headless sin interfaz probada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-project-plateau--plateau-gis-converter"></a>

## Project-PLATEAU/PLATEAU-GIS-Converter

- **Original interface:** CLI y configuración Rust.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar conversión ni asumir que cualquier CityGML es perfil PLATEAU.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-reearth--reearth-flow"></a>

## reearth/reearth-flow

- **Original interface:** Ejecutor/API y grafos de acciones Re:Earth Flow.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No construir otro motor de grafos ni exponer todas las acciones como herramientas sin control.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-tudelft3d--3dcitydb-tools-for-qgis"></a>

## tudelft3d/3DCityDB-Tools-for-QGIS

- **Original interface:** Plugin/PyQGIS y esquema compatible.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | CityGML/CityJSON/3D city database | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | schema, CRS, vertical units, IDs and LoD |
| mapping | format/profile selection | Original format/schema specifications (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | losses and consumer requirements explicit |

- **Preparation required:** Use original importer/exporter, retain semantic surfaces and identifiers, record conversion losses.
- **Validation required:** Schema, coordinates, topology, LoD, IDs, relationships and native validation.
- **Real-city blocker:** Open footprints do not constitute a complete CityGML/CityJSON model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar importadores ni montar otro servicio por ser un plugin.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-tudelft3d--3dfier"></a>

## tudelft3d/3dfier

- **Original interface:** Ejecutable C++ y configuración.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| cloud | LiDAR/point cloud or elevation source | Municipality, utility, transit agency or project owner (configuration required); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | accuracy, classification and vertical datum |
| footprints | building/terrain outlines | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | identity, geometry and coverage |
| parameters | reconstruction settings | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | desired LoD and tolerances |

- **Preparation required:** Align sources and use native reconstruction tools; label reconstructed versus observed attributes.
- **Validation required:** Alignment, point/classification quality, units, watertightness and comparison against control geometry.
- **Real-city blocker:** Incomplete heights/footprints and low-resolution elevation can prevent suitable reconstruction.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentar reconstrucción inferida como medición ni ocultar calidad de elevación.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-tudelft3d--city4cfd"></a>

## tudelft3d/City4CFD

- **Original interface:** CLI y configuración de caso.
- **Profile scope:** candidate. Geometry preparation operation may omit solver conditions; simulation requires separate admitted CFD case.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | watertight simulation geometry and mesh | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | domain, mesh quality and scale |
| conditions | boundary/initial conditions | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | velocity, turbulence, material and units |
| solver | case and numerical configuration | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | version and convergence criteria |

- **Preparation required:** Use native mesher/solver tools; separate geometry preparation from physical case validation.
- **Validation required:** Boundary completeness, mesh metrics, dimensions, timestep, residuals and conservation/reference fields.
- **Real-city blocker:** A display scene or OSM model does not provide a valid CFD mesh or calibrated conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir geometría preparada con malla CFD validada o simulación ejecutada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-vcityteam--ud-viz"></a>

## VCityTeam/UD-Viz

- **Original interface:** API JavaScript/TypeScript.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir motor ni obligar todos los agentes a una UI concreta.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-benchmark-urbanism--cityseer-api"></a>

## benchmark-urbanism/cityseer-api

- **Original interface:** API Python con extensión Rust.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [INEGI Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | direction topology and cost definition with source supporting declared travel mode |

- **Preparation required:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validation required:** Connectivity, direction, intersection semantics, units and source coverage.
- **Real-city blocker:** Mapped roads do not imply capacity, reliable speed, pedestrian completeness or traffic demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir distancia de red o mezcla de usos en impacto causal.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-gboeing--osmnx"></a>

## gboeing/osmnx

- **Original interface:** Public Python API; admitted walking runtime pins OSMnx 2.1.1, NetworkX 3.7 and FastMCP 3.4.2.
- **Profile scope:** candidate. Helsinki/Amsterdam central walking cases have scoped execution evidence. The generic roads profile remains a proposal for other operations.
- **Scoped executable case:** [amsterdam-walking](../../cases/amsterdam-walking/README.md); operations: harvest_walking_data, walking_accessibility, walking_compare, walking_edge, walking_export_graph, walking_feature_catalog, walking_graph_info, walking_isochrone, walking_network_stats, walking_node, walking_read_artifact, walking_render_map, walking_route, walking_snap, walking_status. The generic profile below remains a proposal for other operations.
- **Scoped executable case:** [helsinki-walking](../../cases/helsinki-walking/README.md); operations: harvest_walking_data, walking_accessibility, walking_compare, walking_edge, walking_export_graph, walking_feature_catalog, walking_graph_info, walking_isochrone, walking_network_stats, walking_node, walking_read_artifact, walking_render_map, walking_route, walking_snap, walking_status. The generic profile below remains a proposal for other operations.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [INEGI Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | direction topology and cost definition with source supporting declared travel mode |

- **Preparation required:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validation required:** Connectivity, direction, intersection semantics, units and source coverage.
- **Real-city blocker:** Mapped roads do not imply capacity, reliable speed, pedestrian completeness or traffic demand.
- **Native binding:** verified only for the linked case and operations; the generic profile does not admit additional operations.
- **Project critique:** OSM completeness and public library admission are unverified; bidirectional walk graph omits important barriers/directional rules. No wheelchair, population, calibrated-time or entire-city claim.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pysal--esda"></a>

## pysal/esda

- **Original interface:** API Python.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | seed and inference assumptions |

- **Preparation required:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validation required:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Real-city blocker:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No interpretar autocorrelación como causalidad ni ocultar elección de vecindad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pysal--inequality"></a>

## pysal/inequality

- **Original interface:** API Python.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | seed and inference assumptions |

- **Preparation required:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validation required:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Real-city blocker:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir desigualdad agregada con desigualdad individual ni mezclar unidades.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pysal--libpysal"></a>

## pysal/libpysal

- **Original interface:** API Python de pesos/estructuras.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | seed and inference assumptions |

- **Preparation required:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validation required:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Real-city blocker:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No inventar vecindades ni perder alineación entre tabla y matriz de pesos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pysal--mgwr"></a>

## pysal/mgwr

- **Original interface:** API Python de ajuste y selección de parámetros.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | seed and inference assumptions |

- **Preparation required:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validation required:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Real-city blocker:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentar coeficientes locales como causalidad ni ignorar colinealidad/escala.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pysal--momepy"></a>

## pysal/momepy

- **Original interface:** API Python y datos geoespaciales nativos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | seed and inference assumptions |

- **Preparation required:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validation required:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Real-city blocker:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No rehacer indicadores ni tratar resultados homónimos de versiones distintas como iguales.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pysal--segregation"></a>

## pysal/segregation

- **Original interface:** API Python.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | seed and inference assumptions |

- **Preparation required:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validation required:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Real-city blocker:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No producir inferencias individuales ni comparar métricas con universos incompatibles.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pysal--spopt"></a>

## pysal/spopt

- **Original interface:** API Python y solvers configurados.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | seed and inference assumptions |

- **Preparation required:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validation required:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Real-city blocker:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No llamar óptima una solución factible ni inventar objetivos del proyecto.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pysal--spreg"></a>

## pysal/spreg

- **Original interface:** API Python.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| observations | spatial tables/geometries | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | year, aggregation and variable meaning |
| weights | spatial weights/IDs | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | neighborhood/normalization explicit |
| parameters | model specification | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | seed and inference assumptions |

- **Preparation required:** Join by stable IDs, preserve aggregation and specify estimation/permutation settings.
- **Validation required:** Denominators, missingness, ID order, weights, units and diagnostics.
- **Real-city blocker:** Aggregate/modelled grids do not establish individual behavior or causal effects.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No automatizar selección causal ni ocultar supuestos del modelo espacial.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-spacegroupucl--depthmapx"></a>

## SpaceGroupUCL/depthmapX

- **Original interface:** CLI o aplicación; verificar automatización de la versión.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [INEGI Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | direction topology and cost definition with source supporting declared travel mode |

- **Preparation required:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validation required:** Connectivity, direction, intersection semantics, units and source coverage.
- **Real-city blocker:** Mapped roads do not imply capacity, reliable speed, pedestrian completeness or traffic demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No sumar centralidades homónimas sin explicar diferencia frente a cityseer/OSMnx.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-a-b-street--abstreet"></a>

## a-b-street/abstreet

- **Original interface:** Herramientas/formatos de A/B Street y ejecutores disponibles.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | SUMO net.xml | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | netconvert and junction assumptions recorded |
| demand | SUMO routes/trips/OD | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | observed or synthetic status explicit |
| config | sumocfg | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | seed, time and vehicle types fixed |

- **Preparation required:** Convert network with SUMO tools, prepare demand separately, resolve relative file references and preserve assumptions.
- **Validation required:** Network-route consistency, edge IDs, units, time coverage, vehicle counts and configuration.
- **Real-city blocker:** OSM cannot supply calibrated OD demand or signal timings everywhere.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No tratar un simulador interactivo como servicio estable por defecto.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-activitysim--activitysim"></a>

## ActivitySim/activitysim

- **Original interface:** CLI, configuraciones y tablas ActivitySim.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | zones and skims compatible |

- **Preparation required:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validation required:** Control totals, missingness, joins, weights and model diagnostics.
- **Real-city blocker:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No simular demanda creíble sin encuestas, población y estimación compatibles.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-activitysim--populationsim"></a>

## ActivitySim/populationsim

- **Original interface:** CLI Python y tablas de controles.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | zones and skims compatible |

- **Preparation required:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validation required:** Control totals, missingness, joins, weights and model diagnostics.
- **Real-city blocker:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentar población sintética como padrón de personas reales.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-aequilibrae--aequilibrae"></a>

## AequilibraE/aequilibrae

- **Original interface:** API Python y proyecto de datos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | transport project and zone network | Municipality, utility, transit agency or project owner (configuration required); [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | costs, direction, capacity and zone connectors |
| od | OD demand matrix | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | zone IDs, modes, period and units |
| parameters | assignment assumptions | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | algorithm, convergence and calibration scope |

- **Preparation required:** Use native network/matrix APIs; align zones and demand and retain congestion assumptions.
- **Validation required:** OD/network consistency, demand totals, flows, cost units and convergence.
- **Real-city blocker:** Mapped streets do not supply the OD matrix, capacities or observed congestion calibration.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No generar OD o calibración de red automáticamente a partir de calles.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-conveyal--analysis-backend"></a>

## conveyal/analysis-backend

- **Original interface:** API/arquitectura del backend y workers.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | coordinate order and travel profile explicit |

- **Preparation required:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validation required:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Real-city blocker:** Feeds may be missing, expired or not include realtime information.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir autorización multiusuario o despliegue listo por inspeccionar el repo.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-conveyal--r5"></a>

## conveyal/r5

- **Original interface:** Biblioteca Java y wrappers existentes.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | coordinate order and travel profile explicit |

- **Preparation required:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validation required:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Real-city blocker:** Feeds may be missing, expired or not include realtime information.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar r5r/r5py ni comparar resultados con fechas GTFS distintas.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-eclipse-sumo--sumo"></a>

## eclipse-sumo/sumo

- **Original interface:** TraCI, libsumo y CLI; comparar MCP SUMO existente.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | SUMO net.xml | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | netconvert and junction assumptions recorded |
| demand | SUMO routes/trips/OD | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | observed or synthetic status explicit |
| config | sumocfg | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | seed, time and vehicle types fixed |

- **Preparation required:** Convert network with SUMO tools, prepare demand separately, resolve relative file references and preserve assumptions.
- **Validation required:** Network-route consistency, edge IDs, units, time coverage, vehicle counts and configuration.
- **Real-city blocker:** OSM cannot supply calibrated OD demand or signal timings everywhere.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reimplementar control ni optimización existente; red sin demanda no basta.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-giscience--openrouteservice"></a>

## GIScience/openrouteservice

- **Original interface:** API HTTP y perfiles del servidor.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [INEGI Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | direction topology and cost definition with source supporting declared travel mode |

- **Preparation required:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validation required:** Connectivity, direction, intersection semantics, units and source coverage.
- **Real-city blocker:** Mapped roads do not imply capacity, reliable speed, pedestrian completeness or traffic demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No instalarlo junto con OSRM/Valhalla por defecto ni asumir servicios públicos ilimitados.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ipea--accessibility"></a>

## ipea/accessibility

- **Original interface:** API R.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| matrix | travel time matrix | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | time window, units and modes |
| opportunities | destinations and quantities | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | counts and taxonomy defined |
| population | aggregate weights | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Municipality, utility, transit agency or project owner (configuration required) | same aggregation and period |

- **Preparation required:** Align IDs and travel-time definition; select thresholds/impedance without silent defaults.
- **Validation required:** Matrix dimensions, reachable/unreachable coding, weights, time and denominators.
- **Real-city blocker:** Travel-time generation and opportunity quality remain separate dependencies.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir cálculo de indicador con generación de tiempos de viaje.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ipea--r5r"></a>

## ipea/r5r

- **Original interface:** API R y runtime Java.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | coordinate order and travel profile explicit |

- **Preparation required:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validation required:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Real-city blocker:** Feeds may be missing, expired or not include realtime information.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No construir otro cliente Java si el usuario trabaja en R; no duplicar r5py en el mismo perfil.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-matsim-org--matsim-libs"></a>

## matsim-org/matsim-libs

- **Original interface:** Configuraciones, modelos y ejecutor Java MATSim.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | zones and skims compatible |

- **Preparation required:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validation required:** Control totals, missingness, joins, weights and model diagnostics.
- **Real-city blocker:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No generar planes de actividad calibrados desde una red OSM solamente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-mobilitydata--gtfs-validator"></a>

## MobilityData/gtfs-validator

- **Original interface:** CLI/servicio y reportes del validador.
- **Profile scope:** dependency. Only the GTFS feed is required for validation; street graph and trip query belong to routing cases, not this operation.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | coordinate order and travel profile explicit |

- **Preparation required:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validation required:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Real-city blocker:** Feeds may be missing, expired or not include realtime information.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No interpretar feed válido como servicio vigente o cobertura adecuada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-opentripplanner--opentripplanner"></a>

## opentripplanner/OpenTripPlanner

- **Original interface:** API de la versión instalada y construcción de grafo.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | coordinate order and travel profile explicit |

- **Preparation required:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validation required:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Real-city blocker:** Feeds may be missing, expired or not include realtime information.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No sustituir operador de transporte ni inventar datos en tiempo real.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-project-osrm--osrm-backend"></a>

## Project-OSRM/osrm-backend

- **Original interface:** HTTP y herramientas de preparación de datos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [INEGI Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | direction topology and cost definition with source supporting declared travel mode |

- **Preparation required:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validation required:** Connectivity, direction, intersection semantics, units and source coverage.
- **Real-city blocker:** Mapped roads do not imply capacity, reliable speed, pedestrian completeness or traffic demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No construir routing ni sumar todos los motores de rutas al perfil base.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-r5py--r5py"></a>

## r5py/r5py

- **Original interface:** API Python y JVM compatible.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| streets | OSM/PBF | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | routing coverage known |
| feed | GTFS zip | [Mobility Database and original transit publishers](https://mobilitydatabase.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | publisher rights, service dates and timezone |
| query | origin destination and time | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | coordinate order and travel profile explicit |

- **Preparation required:** Validate feed, align graph/feed versions, build native graph and retain query date/timezone.
- **Validation required:** GTFS validation, service calendar, stop/street linkage, CRS and transfer assumptions.
- **Real-city blocker:** Feeds may be missing, expired or not include realtime information.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No publicar otro R5 MCP si la fachada del wrapper ya cubre el caso.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ropensci--stplanr"></a>

## ropensci/stplanr

- **Original interface:** API R y servicios que cada función utilice.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | transport project and zone network | Municipality, utility, transit agency or project owner (configuration required); [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | costs, direction, capacity and zone connectors |
| od | OD demand matrix | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | zone IDs, modes, period and units |
| parameters | assignment assumptions | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | algorithm, convergence and calibration scope |

- **Preparation required:** Use native network/matrix APIs; align zones and demand and retain congestion assumptions.
- **Validation required:** OD/network consistency, demand totals, flows, cost units and convergence.
- **Real-city blocker:** Mapped streets do not supply the OD matrix, capacities or observed congestion calibration.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir que toda función es local ni duplicar servicios de rutas externos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-udst--synthpop"></a>

## UDST/synthpop

- **Original interface:** API Python y tablas de controles.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| population | aggregate/microdata tables | [INEGI census](https://www.inegi.org.mx/programas/ccpv/2020/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | authorized aggregation and weights |
| controls | zone totals and model parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | compatible geography and year |
| network | network/zone model | Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | zones and skims compatible |

- **Preparation required:** Align zone IDs/years and units; use upstream synthesis/choice model with declared seed and assumptions.
- **Validation required:** Control totals, missingness, joins, weights and model diagnostics.
- **Real-city blocker:** Population grids alone do not supply surveys, choice coefficients or OD demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No elegirla además de PopulationSim por inercia; revisar mantenimiento y compatibilidad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-valhalla--valhalla"></a>

## valhalla/valhalla

- **Original interface:** API HTTP y herramientas de preparación.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| road_graph | OSM/PBF/graph tables | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [INEGI Red Nacional de Caminos](https://www.inegi.org.mx/programas/rnc/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | direction topology and cost definition with source supporting declared travel mode |

- **Preparation required:** Build graph with native tool, preserve graph/source version, project and specify routing profile.
- **Validation required:** Connectivity, direction, intersection semantics, units and source coverage.
- **Real-city blocker:** Mapped roads do not imply capacity, reliable speed, pedestrian completeness or traffic demand.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir coste/routing ni prometer restricciones no soportadas por el perfil.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-azavea--raster-vision"></a>

## azavea/raster-vision

- **Original interface:** Configuraciones y ejecutores Python.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | license and evaluation scope |

- **Preparation required:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validation required:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Real-city blocker:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No incorporar entrenamiento genérico ni considerar libre un peso por ser abierto el código.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-open-eo--openeo-processes"></a>

## Open-EO/openeo-processes

- **Original interface:** Esquemas y especificación de procesos.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| schema | IDS/BCF/NGSI-LD/openEO definitions | Original format/schema specifications (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | exact version and profile |
| instance | data/model being validated | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | references and IDs preserved |

- **Preparation required:** Use maintained validator and explicit profile, report unresolved references.
- **Validation required:** Schema version, reference resolution, units and semantic requirements where defined.
- **Real-city blocker:** Schema validity is not scientific validity or evidence that a backend implements every operation.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No anunciar definiciones JSON como motor ejecutable ni asumir cobertura total del backend.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-open-eo--openeo-python-client"></a>

## Open-EO/openeo-python-client

- **Original interface:** API Python y conexión al backend.
- **Profile scope:** candidate. Requires backend capabilities and a process graph; reuse backend jobs/auth rather than inventing a local executor.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| backend | openEO backend capabilities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | auth, processes, formats and limits |
| graph | openEO process graph | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | supported processes and parameters |
| collection | backend collection and query window | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | bands, extent and period |

- **Preparation required:** Use native openEO client and backend jobs; validate graph against the configured backend.
- **Validation required:** Backend capabilities, graph validity, bands, quotas, job status and result assets.
- **Real-city blocker:** A process definition or STAC listing does not guarantee executable backend coverage.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir el backend ni otra cola si openEO ya da jobs; revisar cuotas y costes.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-opendatacube--datacube-core"></a>

## opendatacube/datacube-core

- **Original interface:** API/CLI Python y catálogo de productos.
- **Profile scope:** candidate. Requires configured indexed products and measurement schemas; a STAC query alone is insufficient.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| products | indexed product definitions | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | measurement names, metadata schema and storage |
| query | cube selection | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | space, time, bands and grid |

- **Preparation required:** Use native Data Cube index/API; align measurements and preserve xarray/grid metadata.
- **Validation required:** Index health, product schema, storage links, units, nodata and coverage.
- **Real-city blocker:** Unindexed STAC assets do not automatically form a Data Cube product.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otro catálogo ni cargar conjuntos gigantes al contexto de un agente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-opengeos--geoai"></a>

## opengeos/geoai

- **Original interface:** API Python y componentes de agente/CLI del repositorio.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | license and evaluation scope |

- **Preparation required:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validation required:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Real-city blocker:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir un paquete amplio de IA en una sola herramienta irrestricta.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-opengeos--segment-geospatial"></a>

## opengeos/segment-geospatial

- **Original interface:** API Python y automatizaciones ya presentes.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | license and evaluation scope |

- **Preparation required:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validation required:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Real-city blocker:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No tratar segmentación como objeto urbano validado ni ignorar licencia de pesos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-orfeotoolbox--otb"></a>

## orfeotoolbox/OTB

- **Original interface:** CLI/aplicaciones y bindings disponibles.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | license and evaluation scope |

- **Preparation required:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validation required:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Real-city blocker:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No publicar todas las aplicaciones a ciegas ni confundir sus requisitos ráster.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-orfeotoolbox--pyotb"></a>

## orfeotoolbox/pyotb

- **Original interface:** Binding/API Python y OTB compatible.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | license and evaluation scope |

- **Preparation required:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validation required:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Real-city blocker:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No mantener dos OTB incompatibles ni otro servidor equivalente al CLI.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-sentinel-hub--sentinelhub-py"></a>

## sentinel-hub/sentinelhub-py

- **Original interface:** SDK y API del proveedor configurado.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | license and evaluation scope |

- **Preparation required:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validation required:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Real-city blocker:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** El SDK abierto no garantiza acceso gratuito ni derechos sobre todos los datos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-stac-utils--pystac"></a>

## stac-utils/pystac

- **Original interface:** API Python.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| catalog | STAC API/item collection | Configured service/API instance (configuration required); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | conformance, pagination and asset links |
| query | area/time/bands | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | explicit search limits |

- **Preparation required:** Discover capabilities, filter, preserve item/asset versions and resolve authorized assets.
- **Validation required:** Conformance, item IDs, geometry, datetime, asset availability and rights.
- **Real-city blocker:** A catalog entry does not prove the asset is downloadable or fit for a model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir un objeto STAC con un archivo ráster disponible.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-stac-utils--pystac-client"></a>

## stac-utils/pystac-client

- **Original interface:** API Python y capacidades del servidor.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| catalog | STAC API/item collection | Configured service/API instance (configuration required); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | conformance, pagination and asset links |
| query | area/time/bands | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | explicit search limits |

- **Preparation required:** Discover capabilities, filter, preserve item/asset versions and resolve authorized assets.
- **Validation required:** Conformance, item IDs, geometry, datetime, asset availability and rights.
- **Real-city blocker:** A catalog entry does not prove the asset is downloadable or fit for a model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir todas las extensiones STAC ni descargar automáticamente cada asset.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-stac-utils--stac-fastapi"></a>

## stac-utils/stac-fastapi

- **Original interface:** Servicio y backend de almacenamiento elegido.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| catalog | STAC API/item collection | Configured service/API instance (configuration required); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | conformance, pagination and asset links |
| query | area/time/bands | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | explicit search limits |

- **Preparation required:** Discover capabilities, filter, preserve item/asset versions and resolve authorized assets.
- **Validation required:** Conformance, item IDs, geometry, datetime, asset availability and rights.
- **Real-city blocker:** A catalog entry does not prove the asset is downloadable or fit for a model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No instalar un servidor STAC cuando solo necesitamos consultar uno.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-torchgeo--torchgeo"></a>

## torchgeo/torchgeo

- **Original interface:** API Python/PyTorch.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| imagery | STAC/raster products | [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | bands, level, acquisition and cloud mask |
| model | weights/labels/pipeline | Dataset and weight publishers for selected model (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | license and evaluation scope |

- **Preparation required:** Subset, normalize and georeference through the selected model pipeline; isolate GPU dependencies.
- **Validation required:** Band order, scale, nodata/clouds, CRS, weights, split leakage and spatial output.
- **Real-city blocker:** Available imagery is not ground truth; weights/data may have separate rights or access conditions.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir un framework de investigación en predicciones urbanas validadas por defecto.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-crowddynamics--crowddynamics"></a>

## crowddynamics/crowddynamics

- **Original interface:** CLI/API Python y configuración.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No extrapolar comportamientos humanos ni asumir mantenimiento actual.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-mengecrowdsim--menge"></a>

## MengeCrowdSim/Menge

- **Original interface:** Ejecutable, configuración y plugins admitidos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No inventar comportamiento o calibración ni cargar plugins no revisados.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pedestriandynamics--jupedsim"></a>

## PedestrianDynamics/jupedsim

- **Original interface:** API Python y geometrías/modelos admitidos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir evacuación validada ni traducir geometría urbana sin verificar transitabilidad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-svenkreiss--socialforce"></a>

## svenkreiss/socialforce

- **Original interface:** API Python y ejemplos de simulación/ajuste.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentarlo como motor peatonal universal o evidencia de conducta real.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-dss-extensions--opendssdirect.py"></a>

## dss-extensions/OpenDSSDirect.py

- **Original interface:** API Python y motor nativo asociado.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | objective and solver stated |

- **Preparation required:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validation required:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Real-city blocker:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir compatibilidad entre variantes DSS ni inferir red física desde mapas.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-e2niee--pandapower"></a>

## e2nIEE/pandapower

- **Original interface:** API Python y solvers admitidos.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | objective and solver stated |

- **Preparation required:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validation required:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Real-city blocker:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No generar una red calibrada de datos incompletos ni ocultar falta de convergencia.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-natlabrockies--reopt_api"></a>

## NatLabRockies/REopt_API

- **Original interface:** Servicio/API y motor de optimización correspondiente.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | objective and solver stated |

- **Preparation required:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validation required:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Real-city blocker:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir servidor API con todo el solver ni prometer ahorro económico cierto.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-oemof--oemof-solph"></a>

## oemof/oemof-solph

- **Original interface:** API Python y solver configurado.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | objective and solver stated |

- **Preparation required:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validation required:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Real-city blocker:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuir óptimo sin verificar estado, brecha y restricciones.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-pypsa--pypsa"></a>

## PyPSA/PyPSA

- **Original interface:** API Python y backend de optimización admitido.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | objective and solver stated |

- **Preparation required:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validation required:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Real-city blocker:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No mezclar series o unidades ni presentar plan óptimo como decisión aprobada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-rwth-ebc--uesgraphs"></a>

## RWTH-EBC/uesgraphs

- **Original interface:** API Python y exportaciones del paquete.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| network | circuit/grid model | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | topology impedance voltage bases and controls |
| series | loads/generation | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | units and temporal alignment |
| parameters | constraints/costs | Model author or qualified project team (configuration required); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | objective and solver stated |

- **Preparation required:** Use native circuit/network model and solver; keep base and intervention separate.
- **Validation required:** Units, connectivity, balance, convergence, feasible constraints and reference solution.
- **Real-city blocker:** Mapped lines or buildings do not provide a calibrated electrical model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir un grafo con dimensionamiento o simulación ya ejecutados.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-climada-project--climada_petals"></a>

## CLIMADA-project/climada_petals

- **Original interface:** API Python y módulos concretos.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| hazard | hazard/event model | Hazard data selected by the model owner (configuration required); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | probability/intensity and event set |
| exposure | assets/population/value | Municipality, utility, transit agency or project owner (configuration required); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | aggregation and valuation |
| vulnerability | functions/model configuration | Model author or qualified project team (configuration required); Hazard data selected by the model owner (configuration required); Original tool examples/tests (configuration required) | applicability and uncertainty |

- **Preparation required:** Match hazard/exposure definitions and preserve event/revision links.
- **Validation required:** Units, vulnerability domain, spatial/temporal alignment and reference impact.
- **Real-city blocker:** Geometry alone cannot determine losses or locally valid vulnerability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No instalar todos los peligros ni atribuir validación a la familia completa.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-climada-project--climada_python"></a>

## CLIMADA-project/climada_python

- **Original interface:** API Python y fuentes de datos del caso.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| hazard | hazard/event model | Hazard data selected by the model owner (configuration required); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | probability/intensity and event set |
| exposure | assets/population/value | Municipality, utility, transit agency or project owner (configuration required); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | aggregation and valuation |
| vulnerability | functions/model configuration | Model author or qualified project team (configuration required); Hazard data selected by the model owner (configuration required); Original tool examples/tests (configuration required) | applicability and uncertainty |

- **Preparation required:** Match hazard/exposure definitions and preserve event/revision links.
- **Validation required:** Units, vulnerability domain, spatial/temporal alignment and reference impact.
- **Real-city blocker:** Geometry alone cannot determine losses or locally valid vulnerability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No producir pérdidas reales desde geometría sola ni omitir incertidumbre/vulnerabilidad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-gem--oq-engine"></a>

## gem/oq-engine

- **Original interface:** CLI/API del engine y archivos de configuración.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| hazard | hazard/event model | Hazard data selected by the model owner (configuration required); Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | probability/intensity and event set |
| exposure | assets/population/value | Municipality, utility, transit agency or project owner (configuration required); [Global Human Settlement Layer](https://human-settlement.emergency.copernicus.eu/datasets.php); [WorldPop](https://www.worldpop.org/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | aggregation and valuation |
| vulnerability | functions/model configuration | Model author or qualified project team (configuration required); Hazard data selected by the model owner (configuration required); Original tool examples/tests (configuration required) | applicability and uncertainty |

- **Preparation required:** Match hazard/exposure definitions and preserve event/revision links.
- **Validation required:** Units, vulnerability domain, spatial/temporal alignment and reference impact.
- **Real-city blocker:** Geometry alone cannot determine losses or locally valid vulnerability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir mapa de peligro con pérdida urbana ni elegir modelos sin justificación.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-universite-gustave-eiffel--noisemodelling"></a>

## Universite-Gustave-Eiffel/NoiseModelling

- **Original interface:** Scripts/CLI Java y datos de emisión/escena.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| sources | traffic/activity/emission sources | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | observed versus assumed flows/spectrum |
| scene | terrain/buildings/receivers | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | heights materials and coordinates |
| conditions | propagation/weather parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | time period and standard specified |

- **Preparation required:** Use native noise model and explicit emission preparation; retain receiver IDs.
- **Validation required:** Source units, frequency/period, geometry, receiver location and reference levels.
- **Real-city blocker:** A road centerline is not a measured noise source or calibrated acoustic model.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No deducir emisión acústica solo de calles ni etiquetar resultado como medición.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-duckdb--duckdb-spatial"></a>

## duckdb/duckdb-spatial

- **Original interface:** SQL y drivers de la extensión instalada.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir funciones espaciales ni dar SQL/lectura de archivos irrestrictos al agente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-geopandas--geopandas"></a>

## geopandas/geopandas

- **Original interface:** API Python GeoDataFrame.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otra base GIS ni duplicar cada función de GDAL/QGIS.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-geotools--geotools"></a>

## geotools/geotools

- **Original interface:** APIs Java y módulos requeridos.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No publicar otro servidor GIS equivalente por existir una biblioteca amplia.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-jblindsay--whitebox-tools"></a>

## jblindsay/whitebox-tools

- **Original interface:** CLI y catálogo de herramientas del binario admitido.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required) | band meaning, nodata and resolution explicit |

- **Preparation required:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validation required:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Real-city blocker:** An available raster can be unsuitable for the intended analysis.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir que todas las extensiones/binarios tienen iguales condiciones de distribución.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-locationtech--jts"></a>

## locationtech/jts

- **Original interface:** API Java JTS.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No añadir otro MCP de geometría además de GEOS/Shapely sin diferencia requerida.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-opengeos--whitebox-python"></a>

## opengeos/whitebox-python

- **Original interface:** API Python y binario Whitebox compatible.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required) | band meaning, nodata and resolution explicit |

- **Preparation required:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validation required:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Real-city blocker:** An available raster can be unsuitable for the intended analysis.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No contar wrapper y binario como dos motores independientes.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-osgeo--gdal"></a>

## OSGeo/gdal

- **Original interface:** CLI, API y bindings; comparar GDAL MCP existente.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No inventar transformaciones ni exponer todos los drivers/accesos externos sin límites.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-osgeo--grass"></a>

## OSGeo/grass

- **Original interface:** Sesión/mapset, CLI y API Python.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No depender del grass-mcp anunciado sin código ni mezclar mapsets entre proyectos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-osgeo--proj"></a>

## OSGeo/PROJ

- **Original interface:** Biblioteca/CLI y bindings ya usados por GIS.
- **Profile scope:** dependency. An operation requires control coordinates, datum/epoch and grids when applicable; not an arbitrary feature collection.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No aceptar solo un EPSG como garantía de datum/época/transformación adecuada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-postgis--postgis"></a>

## postgis/postgis

- **Original interface:** SQL mediante API de aplicación y rol acotado.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| collection | database/API reference | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | authorized project and schema |

- **Preparation required:** Use typed queries and bounded artifacts; preserve IDs and revision.
- **Validation required:** Role/scope, CRS, geometry column, counts and query limits.
- **Real-city blocker:** An instance and authorized data are required.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No construir otra base espacial ni copiar bases de productos existentes.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-qgis--qgis"></a>

## qgis/QGIS

- **Original interface:** qgis_process/PyQGIS y plugin; comparar MCP QGIS existentes.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir GIS ni mezclar automatización headless con control de sesión gráfica.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-r-spatial--sf"></a>

## r-spatial/sf

- **Original interface:** API R y bibliotecas nativas de sf.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir igualdad entre motores o semántica esférica/planar.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-rasterio--rasterio"></a>

## rasterio/rasterio

- **Original interface:** API Python basada en GDAL.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.
- **Scoped executable case:** [amsterdam-vegetation](../../cases/amsterdam-vegetation/README.md); operations: store_justification, raster_convert, raster_info, raster_query, raster_reproject, raster_stats, vector_buffer, vector_clip, vector_convert, vector_info, vector_query, vector_reproject, vector_simplify, vegetation_status, harvest_vegetation_data, prepare_vegetation_data, vegetation_class_catalog, analyze_vegetation, vegetation_compare, read_vegetation_artifact, render_vegetation_map. The generic profile below remains a proposal for other operations.
- **Scoped executable case:** [helsinki-vegetation](../../cases/helsinki-vegetation/README.md); operations: store_justification, raster_convert, raster_info, raster_query, raster_reproject, raster_stats, vector_buffer, vector_clip, vector_convert, vector_info, vector_query, vector_reproject, vector_simplify, vegetation_status, harvest_vegetation_data, prepare_vegetation_data, vegetation_class_catalog, analyze_vegetation, vegetation_compare, read_vegetation_artifact, render_vegetation_map. The generic profile below remains a proposal for other operations.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required) | band meaning, nodata and resolution explicit |

- **Preparation required:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validation required:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Real-city blocker:** An available raster can be unsuitable for the intended analysis.
- **Native binding:** verified only for the linked case and operations; the generic profile does not admit additional operations.
- **Project critique:** No duplicar GDAL ni cargar rásters completos al contexto del agente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-rspatial--terra"></a>

## rspatial/terra

- **Original interface:** API R y núcleo nativo.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required) | band meaning, nodata and resolution explicit |

- **Preparation required:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validation required:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Real-city blocker:** An available raster can be unsuitable for the intended analysis.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otro stack ráster general paralelo por uniformidad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-saga-gis--saga-gis"></a>

## saga-gis/saga-gis

- **Original interface:** CLI y bibliotecas de herramientas de la distribución.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| raster | GeoTIFF/COG | [Copernicus DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); [ESA WorldCover](https://esa-worldcover.org/en); [Copernicus Data Space STAC](https://documentation.dataspace.copernicus.eu/APIs/STAC.html); [USGS Landsat data access](https://www.usgs.gov/landsat-missions/landsat-data-access); Authorized files supplied for the case (configuration required) | band meaning, nodata and resolution explicit |

- **Preparation required:** Subset/window, harmonize grids only through recorded resampling; preserve original metadata.
- **Validation required:** CRS, affine transform, bands, nodata, coverage, units and resolution.
- **Real-city blocker:** An available raster can be unsuitable for the intended analysis.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No fijar IDs de algoritmos sin versión ni reconstruir análisis de terreno existente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-shapely--shapely"></a>

## shapely/shapely

- **Original interface:** API Python Shapely.
- **Profile scope:** dependency. Planar geometries and explicitly declared measurement units; no full CRS transformation service is supplied by Shapely.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| features | GeoPackage/GeoParquet/GeoJSON | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI Marco Geoestadistico](https://www.inegi.org.mx/temas/mg/); [INEGI DENUE](https://www.inegi.org.mx/servicios/api_denue.html); Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required) | CRS and IDs explicit with source edition and category coverage reviewed |

- **Preparation required:** Select area, preserve source IDs, project only with declared operation, map fields and retain provenance.
- **Validation required:** Geometry validity, dimensions, IDs, bounds, CRS/units and required attributes.
- **Real-city blocker:** Coverage and domain attributes are not guaranteed by a map.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuirle manejo CRS completo, geodesia o simulación urbana; no duplicar GEOS.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-ckan--ckan"></a>

## ckan/ckan

- **Original interface:** Action API y permisos de una instancia.
- **Profile scope:** candidate. Dataset/resource catalog; CKAN Action API binding, not STAC conformance, must be mapped explicitly.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| instance | catalog API and scope | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | native API/version and permissions |
| query | resource metadata search | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | geography, date, format and limits |

- **Preparation required:** Use the native CKAN/GeoNetwork/GeoNode API; resolve resource links and access terms before ingestion.
- **Validation required:** API version, pagination, resource IDs, license, format and link availability.
- **Real-city blocker:** Metadata does not imply a usable downloadable dataset; no STAC conformance is assumed.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No duplicar catálogo ni considerar descargable cualquier recurso listado.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-geonetwork--core-geonetwork"></a>

## geonetwork/core-geonetwork

- **Original interface:** API de la versión instalada y estándares que publique.
- **Profile scope:** candidate. Geographic metadata catalog; use version-specific API/standards, not assumed STAC compatibility.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| instance | catalog API and scope | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | native API/version and permissions |
| query | resource metadata search | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | geography, date, format and limits |

- **Preparation required:** Use the native CKAN/GeoNetwork/GeoNode API; resolve resource links and access terms before ingestion.
- **Validation required:** API version, pagination, resource IDs, license, format and link availability.
- **Real-city blocker:** Metadata does not imply a usable downloadable dataset; no STAC conformance is assumed.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No convertir metadatos en garantía de acceso, licencia o calidad del dataset.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-geonode--geonode"></a>

## GeoNode/geonode

- **Original interface:** API GeoNode y servicios asociados de la instalación.
- **Profile scope:** candidate. Use GeoNode resource/project permissions and its native API; generic catalog profile does not assert STAC support.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| instance | catalog API and scope | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | native API/version and permissions |
| query | resource metadata search | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | geography, date, format and limits |

- **Preparation required:** Use the native CKAN/GeoNetwork/GeoNode API; resolve resource links and access terms before ingestion.
- **Validation required:** API version, pagination, resource IDs, license, format and link availability.
- **Real-city blocker:** Metadata does not imply a usable downloadable dataset; no STAC conformance is assumed.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir portal ni publicar capas sin respetar permisos/procedencia.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-geopython--pygeoapi"></a>

## geopython/pygeoapi

- **Original interface:** OGC API de colecciones/procesos de la instancia.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| instance | OGC service endpoint/capabilities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | version, collections, layers and processes |
| query | bounded layer/process parameters | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | CRS, extent, dimensions and authorization |

- **Preparation required:** Discover native capabilities and select only supported operations; separate querying from administration.
- **Validation required:** Advertised conformance, collection schema, CRS, filters, bounds and result links.
- **Real-city blocker:** A configured endpoint and actual provider data are required; process support cannot be inferred.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No crear otro adaptador por cada proceso OGC ni afirmar soporte de extensiones no configuradas.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-geoserver--geoserver"></a>

## geoserver/geoserver

- **Original interface:** WMS/WFS/OGC y REST administrativo según instalación.
- **Profile scope:** candidate. Collections/maps via native OGC services; do not assume STAC, arbitrary process support or administrative access.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| instance | OGC service endpoint/capabilities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | version, collections, layers and processes |
| query | bounded layer/process parameters | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | CRS, extent, dimensions and authorization |

- **Preparation required:** Discover native capabilities and select only supported operations; separate querying from administration.
- **Validation required:** Advertised conformance, collection schema, CRS, filters, bounds and result links.
- **Real-city blocker:** A configured endpoint and actual provider data are required; process support cannot be inferred.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir map server ni usar credenciales administrativas para consultas del agente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-mapserver--mapserver"></a>

## MapServer/MapServer

- **Original interface:** Servicios OGC y configuración de mapfiles.
- **Profile scope:** candidate. Native OGC/mapfile contract; STAC-like catalog fields are not a claim of STAC support.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| instance | OGC service endpoint/capabilities | Configured service/API instance (configuration required); Municipality, utility, transit agency or project owner (configuration required) | version, collections, layers and processes |
| query | bounded layer/process parameters | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | CRS, extent, dimensions and authorization |

- **Preparation required:** Discover native capabilities and select only supported operations; separate querying from administration.
- **Validation required:** Advertised conformance, collection schema, CRS, filters, bounds and result links.
- **Real-city blocker:** A configured endpoint and actual provider data are required; process support cannot be inferred.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No instalarlo además de GeoServer sin motivo ni reescribir renderizado.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-gama-platform--gama"></a>

## gama-platform/gama

- **Original interface:** Modelos GAML y ejecutor headless admitido.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No prometer un modelo social o urbano universal por tener un framework.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-mesa--mesa"></a>

## mesa/mesa

- **Original interface:** Clases y API del modelo definido por su autor.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** La novedad del modelo pertenece a quien lo define; Mesa no trae una ciudad calibrada.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-metadriverse--metaurban"></a>

## metadriverse/metaurban

- **Original interface:** API Python y motor/recursos del entorno.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir benchmark de agentes con predicción de movilidad real.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-netlogo--netlogo"></a>

## NetLogo/NetLogo

- **Original interface:** Ejecutor headless, modelos y BehaviorSpace según versión.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No tomar modelos educativos como modelos de política pública validados.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-tsinghua-fib-lab--agentsociety"></a>

## tsinghua-fib-lab/AgentSociety

- **Original interface:** APIs, modelos y proveedores de la versión elegida.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| model | GAML/NetLogo/Python scenario | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | rules, seed, stop conditions and model version |
| population | agents/activity/control tables | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | synthetic status and calibration |
| environment | network/space/context | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | declared scale and completeness |

- **Preparation required:** Keep original model/rules, set reproducible seed and retain assumptions as scenario data.
- **Validation required:** Agent counts, constraints, seed, stop condition and reference trajectory/statistics.
- **Real-city blocker:** A framework does not supply validated human behavior; LLM agents may also require external providers and budget.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No equiparar conversación sintética con evidencia social ni disponibilidad libre de proveedores/datos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-tsinghua-fib-lab--citybench"></a>

## tsinghua-fib-lab/CityBench

- **Original interface:** Scripts, datasets y métricas de evaluación.
- **Profile scope:** reference. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| references | urls | Original format/schema specifications (configuration required) | verify identity and date |

- **Preparation required:** Catalog only; no solver input or invented runtime.
- **Validation required:** Links, provenance and classification.
- **Real-city blocker:** Not an executable capability.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No presentarlo como motor de planificación ni confundir puntuación con utilidad real.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cesiumgs--3d-tiles-tools"></a>

## CesiumGS/3d-tiles-tools

- **Original interface:** CLI/API TypeScript y dependencias específicas.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No asumir que transforma cualquier modelo en tiles correctos ni duplicar conversores.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-cesiumgs--cesium"></a>

## CesiumGS/cesium

- **Original interface:** API JavaScript del visor; comparar MCP Cesium existente.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir globo/renderizador ni asumir credenciales de servicios asociados.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-itowns--itowns"></a>

## iTowns/itowns

- **Original interface:** API JavaScript y proveedores del visor.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No incluir todos los visores por defecto ni confundir captura con dato científico.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-keplergl--kepler.gl"></a>

## keplergl/kepler.gl

- **Original interface:** API del visor y src/mcp/src/server/index.ts recuperado.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** El catálogo anterior lo trataba solo como visor; no atribuirnos su MCP como novedad.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-maplibre--maplibre-gl-js"></a>

## maplibre/maplibre-gl-js

- **Original interface:** API JavaScript del mapa.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No atribuir análisis espacial al renderizador ni convertir todo dataset en GeoJSON del agente.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-terriajs--terriajs"></a>

## TerriaJS/terriajs

- **Original interface:** Modelos de catálogo y APIs de la aplicación.
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No reconstruir catálogo/visor ni asumir que todas sus fuentes tienen iguales permisos.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-visgl--deck.gl"></a>

## visgl/deck.gl

- **Original interface:** API JavaScript/TypeScript.
- **Profile scope:** dependency. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| scene | USD/3D/tiles/artifact refs | Municipality, utility, transit agency or project owner (configuration required); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | units, coordinates and source IDs |
| interaction | camera/selection request | Model author or qualified project team (configuration required); Authorized files supplied for the case (configuration required) | target scene/session explicit |

- **Preparation required:** Load through native viewer/converter; map display IDs back to source artifacts.
- **Validation required:** Scene bounds, CRS/transforms, units, selection identity and visual state.
- **Real-city blocker:** A renderable scene may omit analysis semantics or source accuracy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** No confundir visualización acelerada con análisis geográfico o almacenamiento.
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-palm"></a>

## external:palm

- **Original interface:** Version/API/CLI to be selected from upstream evidence
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| geometry | terrain buildings vegetation rasters/mesh | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); [INEGI elevation products](https://www.inegi.org.mx/app/geo2/elevacionesmex/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | spatial scale and heights checked |
| forcing | meteorological series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Original tool examples/tests (configuration required) | model-specific variables/timestep |
| surface | material and surface parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | no inferred physics without declaration |

- **Preparation required:** Prepare with native climate tools; harmonize geometry/forcing at an explicitly accepted resolution.
- **Validation required:** Heights, roughness/materials, shading, temporal completeness, CRS and model-specific balances.
- **Real-city blocker:** Heights, vegetation and local forcing may be unavailable; coarse global layers do not remove those requirements.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** Source, data and runtime admission are pending; documented commands are not execution evidence
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-telemac"></a>

## external:telemac

- **Original interface:** Version/API/CLI to be selected from upstream evidence
- **Profile scope:** candidate. Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| mesh | bathymetry and computational mesh | [GEBCO bathymetry catalog](https://www.gebco.net/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | survey accuracy and vertical datum |
| forcing | flow/tide/wave series | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | matching boundary/time/units |
| parameters | model configuration | Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | turbulence, friction and module fixed |

- **Preparation required:** Use upstream mesh/case preparation; document boundary mapping and selected solver module.
- **Validation required:** Mesh quality, boundaries, datums, temporal alignment and reference-case diagnostics.
- **Real-city blocker:** Global bathymetry is not a harbor survey; field forcing and calibration may be required.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** Source, data and runtime admission are pending; documented commands are not execution evidence
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.

<a id="data-simstadt"></a>

## external:simstadt

- **Original interface:** Version/API/CLI to be selected from upstream evidence
- **Profile scope:** candidate. Verify the current open release and workflow-specific inputs; legacy private-repository documentation is inconsistent with the current publisher notice.

| Candidate input | Format/contract | Candidate sources | Admission condition |
|---|---|---|---|
| buildings | geometries plus use/age/area | Municipality, utility, transit agency or project owner (configuration required); [Overture Maps](https://docs.overturemaps.org/getting-data/); Authorized files supplied for the case (configuration required); Original tool examples/tests (configuration required) | unknown attributes stay unknown |
| archetypes | physical/usage parameters | Municipality, utility, transit agency or project owner (configuration required); Model author or qualified project team (configuration required); Original tool examples/tests (configuration required) | regional validity and uncertainty |
| weather | EPW/series | [Climate.OneBuilding weather files](https://climate.onebuilding.org/); Municipality, utility, transit agency or project owner (configuration required); Original tool examples/tests (configuration required) | climate period and location |

- **Preparation required:** Use the selected UBEM generator; document archetype assignment and geometry-to-building mapping.
- **Validation required:** IDs, building completeness, archetype assumptions, weather, units and aggregation.
- **Real-city blocker:** Global building data does not supply local building physics or occupancy.
- **Native binding:** each input still needs mapping to the selected operation's file/API/argument; this table does not establish that mapping.
- **Project critique:** Source, data and runtime admission are pending; documented commands are not execution evidence
- **Next contribution:** select an operation and permitted asset, pin version/hash/license, document conversion and reproduce the native case before MCP testing.
