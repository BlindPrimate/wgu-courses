import os
import dj_database_url
from wgu_course.settings.common import DATABASES

SECRET_KEY=os.environ('COURSE_SELECTOR_SECRET')

DEBUG = False

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
