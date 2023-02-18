from celery import Celery
import os
from celery.schedules import crontab

from django.conf import settings  # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_app_collection.settings")
app = Celery('my_django_app_collection')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'staking_status_app.tasks.check_and_save_status',
        'schedule': crontab( minute=1),
        #'args': (2,)
    }
}


# configure Celery
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
