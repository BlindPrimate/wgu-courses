import os
from wgu_course.settings.common import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Django Sass
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR,'static', 'compiled-css')

SASS_PROCESSOR_INCLUDE_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]