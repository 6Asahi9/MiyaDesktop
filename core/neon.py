from core.path import SETTINGS_JSON
import json
DEFAULT_NEON_ENABLED = True
DEFAULT_NEON_COLOR = "#00ffff"

def load_neon_settings():
    if not SETTINGS_JSON.exists():
        return DEFAULT_NEON_ENABLED, DEFAULT_NEON_COLOR
    with open(SETTINGS_JSON, "r") as f:
        data = json.load(f)
    enabled = data.get("neon_enabled", DEFAULT_NEON_ENABLED)
    color = data.get("neon_color", DEFAULT_NEON_COLOR)
    return enabled, color

def save_neon_settings(enabled: bool = None, color: str = None):
    data = {}
    if SETTINGS_JSON.exists():
        with open(SETTINGS_JSON, "r") as f:
            data = json.load(f)
    if enabled is not None:
        data["neon_enabled"] = enabled
    if color is not None:
        data["neon_color"] = color
    with open(SETTINGS_JSON, "w") as f:
        json.dump(data, f, indent=2)
