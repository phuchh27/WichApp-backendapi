from .base import *
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default="0kgdgseTbtbKFKlE1H_FQaExJf8tX2_8U_QhSzgk6rFEOtm08nY",
    )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
]