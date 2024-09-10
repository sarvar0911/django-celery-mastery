import os
import time
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')
app = Celery('dcelery')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.task_routes = {'newapp.tasks.task1': {'queue': 'queue1'}, 'newapp.tasks.task2': {'queue': 'queue2'}}

app.conf.task_default_rate_limit = '1/m'

app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'separator': ':',
    'queue_order_strategy': 'priority',
}

app.autodiscover_tasks()