from celery import Celery

# Configuration
module_name = 'tasks'
broker_uri = 'pyamqp://guest@localhost//'

app = Celery(module_name, broker=broker_uri)

@app.task
def add(x, y):
    return x + y
