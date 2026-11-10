"""Decode selected public-case MCP results without exporting private host state."""
import json


def decode(value):
    if isinstance(value, str):
        # Hermes adds an untrusted-tool-result wrapper around the JSON body.
        start = value.find("{")
        if start < 0:
            raise ValueError("No JSON object in selected MCP result")
        value, _ = json.JSONDecoder().raw_decode(value[start:])
    if not isinstance(value, dict):
        raise ValueError("Selected MCP result is not an object")
    if "city" in value and any(key in value for key in ["schools", "paths", "zones", "low_vegetation_zone_ids", "newly_below_threshold_zone_ids"]):
        return value
    if value.get("name") in {"summary.json", "zone_metrics.csv", "class_counts.csv", "zones.geojson", "report.md", "map.png"} and "sha256" in value and "bytes" in value:
        return value
    for key in ["structured_content", "structuredContent", "result"]:
        if value.get(key) is not None:
            return decode(value[key])
    for block in value.get("content", []):
        if block.get("type") == "text":
            return decode(block["text"])
    raise ValueError("Selected response has no public case diagnostic payload")
