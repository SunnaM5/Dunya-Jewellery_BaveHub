import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY is required in environment variables")

DEBUG = os.environ.get("DEBUG", "0") == "1"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

# ---- Database (Supabase/Render Postgres) ----
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    # НЕ даём тихо уйти в localhost/SQLite — иначе потом "всё пропало"
    raise RuntimeError("DATABASE_URL is required (use Supabase/Render Postgres).")

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=True,   # Supabase обычно требует SSL
    )
}

# ---- Proxy/HTTPS (Render) ----
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# ---- Static/Media ----
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ---- CORS ----
CORS_ALLOW_CREDENTIALS = True

# Вариант 1 (строго и правильно): только перечисленные домены
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://dunya-jewellery.vercel.app",
    "https://dunyajewellery.netlify.app",
    "https://futureec1.github.io",
    "http://localhost:3000",
    "http://localhost:5173",
]

# Если хотите временно “чтобы точно работало” — включите True,
# НО тогда удалите список origins (он не нужен):
# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOWED_ORIGINS = []
