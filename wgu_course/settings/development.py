import os
from wgu_course.settings.common import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6)*zrl$bo6r4o8)%9y58b$_jjk9mryk0n*aw^8wckhll1$m#oc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Django Sass
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR,'static', 'compiled-css')

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]