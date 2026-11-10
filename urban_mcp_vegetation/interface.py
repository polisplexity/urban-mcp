"""Bounded transport projection; full observations remain in paged artifacts."""
MAX_PAGE_CHARACTERS = 12000


def public_summary(full):
    summary = {key: value for key, value in full.items() if key != "zones"}
    summary["zone_details"] = {"complete_zone_count": full["zone_count"], "artifacts": ["summary.json", "zone_metrics.csv", "class_counts.csv"], "read_tool": "read_vegetation_artifact", "max_page_characters": MAX_PAGE_CHARACTERS, "instruction": "Read every page until next_offset is null. Full per-zone records are not duplicated in the primary tool response."}
    return summary
