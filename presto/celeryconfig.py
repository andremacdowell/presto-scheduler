# encoding: utf-8
from __future__ import absolute_import

import os
from celery.schedules import crontab
from datetime import timedelta

## Environment variables load
ENV_BROKER_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
ENV_BROKER_PORT = os.getenv('RABBITMQ_PORT', 32782)
ENV_BROKER_USER = os.getenv('RABBITMQ_USER', 'guest')
ENV_BROKER_PASSWORD = os.getenv('RABBITMQ_PASSWORD', 'guest')
ENV_BROKER_VIRTUAL_HOST = os.getenv('RABBITMQ_VIRTUAL_HOST', '/')
ENV_BACKEND_HOST = os.getenv('REDIS_HOST', 'localhost')
ENV_BACKEND_PORT = os.getenv('REDIS_PORT', 32786)

## Broker settings
BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(
    ENV_BROKER_USER,
    ENV_BROKER_PASSWORD,
    ENV_BROKER_HOST,
    ENV_BROKER_PORT,
    ENV_BROKER_VIRTUAL_HOST
)

## Backend settings
CELERY_RESULT_BACKEND = 'redis://{}:{}'.format(
    ENV_BACKEND_HOST,
    ENV_BACKEND_PORT
)

## DateTime settings
CELERY_TIMEZONE = 'America/Sao_Paulo'
CELERY_ENABLE_UTC = True

# List of modules to import when celery starts.
CELERY_IMPORTS = ('presto.tasks', )

## Crontab settings
CELERYBEAT_SCHEDULE = {
    'task_1': {
        'task': 'test_name',
        'schedule': timedelta(seconds=3),
        'args': (2, 3)
    }
}
