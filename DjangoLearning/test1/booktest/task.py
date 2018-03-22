import time
from celery import task

@task
def task():
    print("HELLO")
    time.sleep(5)
    print("WORLD")