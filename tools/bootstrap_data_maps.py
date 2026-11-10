"""Explicit mapping of researched tools to proposed first-case data profiles."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    "none": "APA-Technology-Division/urban-and-regional-planning-resources durbanitas/awesome-urban-planning Ireliya/Awesome-Urban-Planning-Agents sacridini/Awesome-Geospatial FIWARE/tutorials.Step-by-Step ProfRino/bonsai-bim-skills tsinghua-fib-lab/CityBench",
    "vector": "duckdb/duckdb-spatial geopandas/geopandas geotools/geotools locationtech/jts OSGeo/gdal OSGeo/grass OSGeo/PROJ qgis/QGIS r-spatial/sf shapely/shapely JordanGunn/gdal-mcp jjsantos01/qgis_mcp mahdin75/gis-mcp nkarasiak/qgis-mcp piatkowski/qgis-mcp OSGeo/grass-mcp",
    "raster": "rasterio/rasterio rspatial/terra saga-gis/saga-gis jblindsay/whitebox-tools opengeos/whitebox-python natcap/pygeoprocessing",
    "spatial-db": "postgis/postgis",
    "roads": "benchmark-urbanism/cityseer-api gboeing/osmnx msradam/osmnx-mcp jagan-shanmugam/open-streetmap-mcp SpaceGroupUCL/depthmapX Project-OSRM/osrm-backend GIScience/openrouteservice valhalla/valhalla",
    "sumo": "eclipse-sumo/sumo XRDS76354/SUMO-MCP-Server a-b-street/abstreet",
    "transit": "opentripplanner/OpenTripPlanner conveyal/r5 conveyal/analysis-backend r5py/r5py ipea/r5r MobilityData/gtfs-validator",
    "demand": "ActivitySim/activitysim ActivitySim/populationsim AequilibraE/aequilibrae matsim-org/matsim-libs ropensci/stplanr UDST/synthpop CityScope/CS_Mobility_Service",
    "accessibility": "ipea/accessibility",
    "swmm": "USEPA/Stormwater-Management-Model pyswmm/pyswmm MarkusPic/swmm_api kLabUM/SWMM-MCP-PUB Zhonghao1995/agentic-swmm-workflow",
    "epanet": "OpenWaterAnalytics/EPANET USEPA/EPANET2.2 USEPA/WNTR",
    "flood": "Deltares/hydromt Deltares/hydromt_sfincs Deltares/hydromt_wflow Deltares/SFINCS GeoscienceAustralia/anuga_core openstreams/wflow",
    "coastal": "Deltares/Delft3D external:telemac",
    "bim": "IfcOpenShell/IfcOpenShell buildingSMART/IDS Show2Instruct/ifc-bonsai-mcp",
    "bcf": "buildingSMART/BCF-XML",
    "cad": "FreeCAD/FreeCAD blender/blender compas-dev/compas compas-dev/compas_fab DynamoDS/Dynamo openscad/openscad bonninr/freecad_mcp contextform/freecad-mcp neka-nat/freecad-mcp spkane/freecad-addon-robust-mcp-server",
    "scene": "PixarAnimationStudios/OpenUSD potree/potree CesiumGS/3d-tiles-tools CesiumGS/cesium gaopengbin/cesium-mcp iTowns/itowns maplibre/maplibre-gl-js keplergl/kepler.gl TerriaJS/terriajs visgl/deck.gl VCityTeam/UD-Viz dtcc-platform/dtcc-viewer",
    "city-model": "3dcitydb/3dcitydb 3dcitydb/citydb-tool citygml4j/citygml-tools citygml4j/citygml4j cityjson/cjio dtcc-platform/dtcc-core Project-PLATEAU/PLATEAU-Builder Project-PLATEAU/PLATEAU-GIS-Converter reearth/reearth-flow tudelft3d/3DCityDB-Tools-for-QGIS",
    "reconstruction": "tudelft3d/3dfier",
    "cfd": "OpenFOAM/OpenFOAM-dev tudelft3d/City4CFD dtcc-platform/dtcc-sim",
    "energy": "NatLabRockies/EnergyPlus NatLabRockies/OpenStudio NatLabRockies/OpenStudio-HPXML ladybug-tools/honeybee-core ladybug-tools/honeybee-energy ladybug-tools/dragonfly-energy samuelduchesne/archetypal samuelduchesne/geomeppy santoshphilip/eppy RWTH-EBC/TEASER anandb/energyplus-mcp-java ericmartinpe/EnergyPlus-MCP-epjson idfkit/idfkit-mcp LBNL-ETA/EnergyPlus-MCP RainerGaier/energyplus-mcp-server",
    "urban-energy": "architecture-building-systems/CityEnergyAnalyst BETALAB-team/EUReCA KTH-UrbanT/mubes-ubem ladybug-tools/dragonfly-core NatLabRockies/ComStock NatLabRockies/resstock UCL/simstock urbanopt/urbanopt-cli urbanopt/urbanopt-example-geojson-project external:simstadt",
    "weather": "ladybug-tools/ladybug ladybug-tools/uwg",
    "microclimate": "kunifujiwara/VoxCity UMEP-dev/solweig UMEP-dev/SUEWS UMEP-dev/UMEP UMEP-dev/UMEP-processing external:palm",
    "atmosphere": "wrf-model/WRF uDALES/u-dales",
    "air-quality": "USEPA/CMAQ",
    "lidar": "CloudCompare/CloudCompare isl-org/Open3D PDAL/PDAL PDAL/python",
    "landscape": "martibosch/pylandstats r-spatialecology/landscapemetrics",
    "ecosystem": "natcap/invest",
    "statistics": "pysal/esda pysal/inequality pysal/libpysal pysal/mgwr pysal/momepy pysal/segregation pysal/spopt pysal/spreg",
    "land-use": "HPSCIL/Open-Space-Cellular_Automata johanlahti/urban-lu-model LandInsightLab/MUSE UDST/choicemodels UDST/developer UDST/orca UDST/urbansim UDST/urbansim_defaults UDST/urbansim_templates",
    "participation": "consuldemocracy/consuldemocracy decidim/decidim umap-project/umap",
    "context": "eclipse-ditto/ditto FIWARE/context.Orion-LD FraunhoferIOSB/FROST-Server ScorpioBroker/ScorpioBroker telefonicaid/fiware-orion thingsboard/thingsboard CityScope/CS_CityIO CityScope/CS_cityscopeJS CityScope/CS_CityScoPy CityScope/CS_Simulation_GAMA",
    "electrical": "dss-extensions/OpenDSSDirect.py e2nIEE/pandapower NatLabRockies/REopt_API oemof/oemof-solph PyPSA/PyPSA RWTH-EBC/uesgraphs urbanopt/urbanopt-reopt-gem",
    "risk": "CLIMADA-project/climada_petals CLIMADA-project/climada_python gem/oq-engine",
    "noise": "Universite-Gustave-Eiffel/NoiseModelling",
    "imagery": "azavea/raster-vision opengeos/geoai opengeos/segment-geospatial orfeotoolbox/OTB orfeotoolbox/pyotb sentinel-hub/sentinelhub-py torchgeo/torchgeo",
    "stac": "Open-EO/openeo-python-client opendatacube/datacube-core stac-utils/pystac stac-utils/pystac-client stac-utils/stac-fastapi ckan/ckan geonetwork/core-geonetwork GeoNode/geonode geopython/pygeoapi geoserver/geoserver MapServer/MapServer sparkgeo/geo-mcp-servers specklesystems/speckle-server specklesystems/specklepy",
    "social": "gama-platform/gama mesa/mesa metadriverse/metaurban NetLogo/NetLogo tsinghua-fib-lab/AgentSociety crowddynamics/crowddynamics MengeCrowdSim/Menge PedestrianDynamics/jupedsim svenkreiss/socialforce salog0d/UrbanPlannerMCP",
    "schemas": "smart-data-models/data-models Open-EO/openeo-processes",
}
# Each note identifies an important tool-specific qualification to the shared profile.
NOTES = {
    "MobilityData/gtfs-validator": "Only the GTFS feed is required for validation; street graph and trip query belong to routing cases, not this operation.",
    "specklesystems/speckle-server": "Use authorized project/model/version IDs and native object data, not a STAC contract; instance API binding is pending.",
    "specklesystems/specklepy": "Dependency of the Speckle connector; native project/object/version contract replaces generic catalog fields.",
    "ckan/ckan": "Dataset/resource catalog; CKAN Action API binding, not STAC conformance, must be mapped explicitly.",
    "geonetwork/core-geonetwork": "Geographic metadata catalog; use version-specific API/standards, not assumed STAC compatibility.",
    "GeoNode/geonode": "Use GeoNode resource/project permissions and its native API; generic catalog profile does not assert STAC support.",
    "geoserver/geoserver": "Collections/maps via native OGC services; do not assume STAC, arbitrary process support or administrative access.",
    "MapServer/MapServer": "Native OGC/mapfile contract; STAC-like catalog fields are not a claim of STAC support.",
    "sparkgeo/geo-mcp-servers": "First split monorepo into actual servers and data contracts; this is a catalog-level starting point only.",
    "opendatacube/datacube-core": "Requires configured indexed products and measurement schemas; a STAC query alone is insufficient.",
    "Open-EO/openeo-python-client": "Requires backend capabilities and a process graph; reuse backend jobs/auth rather than inventing a local executor.",
    "tudelft3d/City4CFD": "Geometry preparation operation may omit solver conditions; simulation requires separate admitted CFD case.",
    "dtcc-platform/dtcc-sim": "Model/service must be identified before this proposed CFD profile can be accepted as its interface.",
    "UMEP-dev/UMEP-processing": "Each Processing algorithm selects a subset of climate inputs; no universal UMEP input bundle is claimed.",
    "ladybug-tools/honeybee-radiance": "Lighting requires sensors/materials/sky recipe, not necessarily HVAC; bind a separate daylight case.",
    "RWTH-EBC/TEASER": "Produces models (e.g. Modelica) requiring another admitted simulator; EnergyPlus formats are not assumed equivalent.",
    "CityScope/CS_Simulation_GAMA": "CityIO table mapping plus GAML model/population parameters are required; context entities alone cannot run the model.",
    "salog0d/UrbanPlannerMCP": "Requires inspecting the actual model formulas/parameters; a general social profile is not its approved input schema.",
    "shapely/shapely": "Planar geometries and explicitly declared measurement units; no full CRS transformation service is supplied by Shapely.",
    "OSGeo/PROJ": "An operation requires control coordinates, datum/epoch and grids when applicable; not an arbitrary feature collection.",
    "buildingSMART/IDS": "Requirements file plus IFC and a selected validator; schema documents are not a standalone solver.",
    "compas-dev/compas_fab": "Simulation-only planning requires robot/backend configuration; no hardware actuation admitted by this inventory.",
    "external:simstadt": "Verify the current open release and workflow-specific inputs; legacy private-repository documentation is inconsistent with the current publisher notice.",
}
GROUPS["daylight"] = "ladybug-tools/honeybee-radiance"
MOVES = {
    "resource-catalog": "ckan/ckan geonetwork/core-geonetwork GeoNode/geonode",
    "ogc-service": "geopython/pygeoapi geoserver/geoserver MapServer/MapServer",
    "object-service": "specklesystems/speckle-server specklesystems/specklepy",
    "eo-process": "Open-EO/openeo-python-client",
    "data-cube": "opendatacube/datacube-core",
    "hydrology": "Deltares/hydromt_wflow openstreams/wflow",
    "traffic-assignment": "AequilibraE/aequilibrae ropensci/stplanr",
}
for destination, repositories in MOVES.items():
    moved = set(repositories.split())
    for profile in list(GROUPS):
        GROUPS[profile] = " ".join(repo for repo in GROUPS[profile].split() if repo not in moved)
    GROUPS[destination] = repositories


def main():
    target = ROOT / "planning/tool-data-map.tsv"
    seen = set()
    with target.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter="|", lineterminator="\n")
        writer.writerow(["repository", "profile", "note"])
        for profile, repositories in GROUPS.items():
            for repo in repositories.split():
                if repo in seen:
                    raise ValueError(f"Duplicate assignment {repo}")
                seen.add(repo)
                note = NOTES.get(repo, "Proposed representative-case requirements only; operation-specific native bindings and admissible source assets still require review.")
                writer.writerow([repo, profile, note])
    print(f"Authored {len(seen)} tool/profile assignments")


if __name__ == "__main__":
    main()
