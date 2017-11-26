# encoding: utf-8
from __future__ import absolute_import
from presto.celery import app

# Celery Tasks
@app.task(name='test_name')
def add(x, y):
    result = x + y
    print "Calculated a result of {}".format(result)
    return result
