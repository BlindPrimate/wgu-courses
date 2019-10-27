import os
import dj_database_url
from wgu_course.settings.common import DATABASES


DEBUG = False

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


ALLOWWED_HOSTS = [
    '.herokuapp.com',
    'localhost',
    '127.0.0.1',
]


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
