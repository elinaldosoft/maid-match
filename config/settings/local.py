from config.settings.base import * # noqa

DEBUG = True

SECRET_KEY = 'django-insecure-!fa6@lzyg(l0+5$2yapxvt-lf&d0f6%9e-)l*mby%3+mw*u8o@'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_ROOT = BASE_DIR / 'static'