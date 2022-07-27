
from application import celery, crontab

@celery.task()
@crontab.job(minute="1")
def anl(a,b):
    return a+b

anl.delay(5,7)

