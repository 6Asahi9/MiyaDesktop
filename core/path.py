import sys
from pathlib import Path


def get_base_path():
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parents[1]


BASE_PATH = get_base_path()

CONFIG_PATH = BASE_PATH / "config"
ASSETS_PATH = BASE_PATH / "assets"
MIYA = ASSETS_PATH / "placeholder_miya.gif"

SETTINGS_JSON = CONFIG_PATH / "settings.json"
