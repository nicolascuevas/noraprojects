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
    CELERY_REDIS_SCHEDULER_URL = 'redis://redis:6379/0',
    CELERYBEAT_SCHEDULE={
        'import_slack_users': {
            'task': 'employeeApp.tasks.import_slack_users',
            'schedule': crontab(minute=00, hour=5, day_of_week='mon,tue,wed,thu,fri,sat,sun')
        },
        'reminder_slack_users': {
            'task': 'employeeApp.tasks.import_slack_users',
            'schedule': crontab(minute=00, hour=8, day_of_week='mon,tue,wed,thu,fri,sat,sun')
        }
    }

)




app.conf.timezone = 'UTC'

CELERY_TIMEZONE = 'UTC'

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))