# JSON Transformer
# Ingests, modifies, and serializes JSON configuration files.

import json

RAW_CONFIG_JSON = """{
    "app_name": "MetricsService",
    "version": "1.0.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "metrics_db"
    },
    "features": ["logging", "rate_limiting"]
}"""

def update_config(json_str: str, new_features: list[str]) -> str:
    data = json.loads(json_str)
    # Add new features without duplicates
    current_features = set(data.get("features", []))
    current_features.update(new_features)
    data["features"] = sorted(current_features)
    data["version"] = "1.1.0"
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    updated = update_config(RAW_CONFIG_JSON, ["caching", "metrics_exporter"])
    print("Updated JSON Configuration:")
    print(updated)
