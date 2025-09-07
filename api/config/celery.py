"""
celery config for thymius project.

Sets up the celery beat schedule for the application, which determines when to run periodic tasks for the application.

"""

import os

from celery import Celery

from config.settings import CELERY_ENABLED, TIME_ZONE

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")


# Load task modules from all registered Django apps.
app.autodiscover_tasks()
if CELERY_ENABLED:
    app.conf.beat_schedule = {}

# Use update for setting configuration values
app.conf.update(timezone=TIME_ZONE)
