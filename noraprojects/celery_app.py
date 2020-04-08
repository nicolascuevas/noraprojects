from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'noraprojects.settings')

app = Celery('celery_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.update(
    BROKER_URL='redis://localhost:6379/0',
)

CELERYBEAT_SCHEDULE = {
    # Executes every Monday morning at 7:30 A.M
    'add-every-monday-morning': {
        'task': 'employeeApp.tasks.reminder_slack_users',
        'schedule': timedelta(seconds=30),
        'args': (16, 16),
    },
}

CELERY_TIMEZONE = 'UTC'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))