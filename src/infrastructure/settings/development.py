from pathlib import Path
from src.infrastructure.settings.base import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fusion_auth",
        "USER": "fusion_auth_user",
        "PASSWORD": "fusion_auth_password",
        "HOST": "auth-postgres-srv",
        "PORT": "5432",
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'Auth',  # Replace with the desired database name
#         'USER': 'sahlcyprus',
#         'PASSWORD': 'uFvba7V0WneL',
#         'HOST': 'ep-autumn-haze-176756.us-east-2.aws.neon.tech',
#         'PORT': '5432',
#     }
# }
