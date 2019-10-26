import os
from wgu_course.settings.common import *

if os.environ.get('ENV') == 'production':
    from wgu_course.settings.production import *
else:
    from wgu_course.settings.development import *
