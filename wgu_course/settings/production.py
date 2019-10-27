import os
import dj_database_url
from wgu_course.settings.common import DATABASES


DEBUG = False



db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
