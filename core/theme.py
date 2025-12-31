import json
from core.path import SETTINGS_JSON

def load_theme() -> bool:
    if SETTINGS_JSON.exists():
        try:
            data = json.loads(SETTINGS_JSON.read_text(encoding="utf-8"))
            return data.get("is_light_theme", False)
        except Exception:
            return False
    return False


def save_theme(is_light: bool):
    data = {}

    if SETTINGS_JSON.exists():
        try:
            data = json.loads(SETTINGS_JSON.read_text(encoding="utf-8"))
        except Exception:
            data = {}

    data["is_light_theme"] = is_light
    SETTINGS_JSON.parent.mkdir(parents=True, exist_ok=True)
    SETTINGS_JSON.write_text(json.dumps(data, indent=4), encoding="utf-8")


def toggle_theme(is_light: bool) -> dict:
    save_theme(is_light)

    if is_light:
        return {
            "bg": "#f2f2f2",
            "text": "#000000",
            "subtext": "#444444"
        }

    return {
        "bg": "#1a1a1a",
        "text": "#ffffff",
        "subtext": "#888888"
    }
