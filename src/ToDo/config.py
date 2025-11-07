import sys
from pathlib import Path

APP_NAME = "ErlaveToDo"
APP_VERSION = "0.1.0"

# مسیر نصب (فقط برای حالت exe)
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

# مسیر امن برای دیتابیس (در AppData کاربر)
APP_DIR = Path.home() / "AppData" / "Local" / APP_NAME
DATA_DIR = APP_DIR / "data"
DB_PATH = DATA_DIR / "todo.db"

# ساخت پوشه‌ها در صورت نیاز
DATA_DIR.mkdir(parents=True, exist_ok=True)
