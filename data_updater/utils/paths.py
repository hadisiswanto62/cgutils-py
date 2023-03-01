from django.conf import settings
from pathlib import Path

DATA_PATH = settings.DATA_DIR / "game_data"

GAME_DB_PATH = DATA_PATH / "game_db"
MANIFEST_PATH = GAME_DB_PATH / "manifest.db"
MASTERDB_PATH = GAME_DB_PATH / "master.db"

CARD_ICON_PATH = settings.BASE_DIR / "static" / "card_icon"


def get_card_icon_path(id: int) -> Path:
    return CARD_ICON_PATH / f"{id}.png"
