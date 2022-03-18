from .base import *  # noqa pylint: disable=unused-wildcard-import,wildcard-import

SECRET_KEY = 'be3c137458090abd0c5d5e4af7e9f01c5d'

DEBUG = True

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_ROOT = BASE_DIR / 'static'
