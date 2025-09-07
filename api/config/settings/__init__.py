import os

from .auth import *
from .base import *
from .celery import *

context = os.environ.get("DEPLOYMENT_CONTEXT")
if context == "PROD":
    from .production import *
elif context == "DEV":
    from .development import *
else:
    from .local import *
