from django.conf import settings
from pathlib import Path

# ROOT_PATH = Path(__file__).parent
ROOT_PATH: Path = settings.BASE_DIR
DATA_PATH = ROOT_PATH / "game_data"

GAME_DB_PATH = DATA_PATH / "game_db"
MANIFEST_PATH = GAME_DB_PATH / "manifest.db"
MASTERDB_PATH = GAME_DB_PATH / "master.db"
