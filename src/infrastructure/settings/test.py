from pathlib import Path
from src.infrastructure.settings.base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "auth_database",
        "USER": "auth_user",
        "PASSWORD": "auth_password",
        "HOST": "postgres_auth",
        "PORT": "5432",
    }
}
