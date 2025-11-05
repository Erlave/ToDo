import sys
from pathlib import Path

APP_NAME = "ErlaveTodo"
APP_VERSION = "0.1.0"


if getattr(sys, "_MEIPASS", False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent


DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR /"todo.db" 

# اگه data وجود نداشت، بساز
DATA_DIR.mkdir(exist_ok=True)
