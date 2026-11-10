# Helsinki: school-to-library walking experiment

45 of 48 mapped school objects in the central study disk have an accepted modeled library route within 1200 m. 2 are unreachable on this snapshot and 0 fail the snap rule. This denominator is not residents or pupils.

- Central 2 km study disks, not complete municipal territories. The extra 2 km graph buffer reduces boundary effects for the 1200 m threshold; longer nearest routes can be censored.
- OSM mapped amenity=school and amenity=library objects, not an authoritative complete facility register. Multiple objects can represent one campus; no silent deduplication.
- Polygon representative points and nearest graph nodes are proxies, not verified entrances. Snap connectors are straight distances, not verified paths; reject distances over 150 m.
- General pedestrian network only. OSMnx walk mode is bidirectional; directional foot rules, barriers, opening hours, crossings, stairs, slope, winter conditions and wheelchair access are not fully modeled.
- 1200 m is an explicit planning scenario. Minutes use an assumed constant 4.8 km/h including snap connectors; no measured speeds, delay or calibration.
- Denominator is mapped school objects in the core, never population, pupils, residents, service capacity or service quality.
- A link closure is a hypothetical robustness scenario on the harvested graph, not a report of actual works or a forecast.

© OpenStreetMap contributors; https://www.openstreetmap.org/copyright. Data: ODbL-1.0.
