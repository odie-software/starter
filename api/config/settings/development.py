from .base import PG_HOST, PG_NAME, PG_PASSWORD, PG_PORT, PG_USER

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": PG_NAME,
        "USER": PG_USER,
        "PASSWORD": PG_PASSWORD,
        "HOST": PG_HOST,
        "PORT": PG_PORT,
    }
}
