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
    if "city" in value and ("schools" in value or "paths" in value):
        return value
    for key in ["structured_content", "structuredContent", "result"]:
        if value.get(key) is not None:
            return decode(value[key])
    for block in value.get("content", []):
        if block.get("type") == "text":
            return decode(block["text"])
    raise ValueError("Selected response has no public walking diagnostic payload")
