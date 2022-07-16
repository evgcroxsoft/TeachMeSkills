from datetime import timedelta
                                                                                                                                                                                                                                                                                                                            from celery.schedules import crontab

broker_url = 'redis://redis:6379/0'
result_backend = 'redis://redis:6379/0'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Amsterdam'
beat_schedule = crontab(minute="1"),
enable_utc = True

task_routes = {
    'task_celery.add': 'low-priority',
}