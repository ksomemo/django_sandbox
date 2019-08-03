import json
from datetime import datetime, timedelta
from django_celery_beat.models import (
    PeriodicTask, IntervalSchedule, CrontabSchedule
)

# from django_celery_beat.models import PeriodicTasks
# PeriodicTask.objects.all().update(last_run_at=None)

def run():
    # interval
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=10,
        period=IntervalSchedule.SECONDS
    )
    
    interval_task, created = PeriodicTask.objects.get_or_create(
        interval=schedule,                  # we created this above.
        name='Importing contacts',          # simply describes this periodic task.
        task='example_celery.tasks.import_contacts',  # name of task.
        args=json.dumps(['arg1', 'arg2']),
        kwargs=json.dumps({
           'be_careful': True,
        }),
        expires=datetime.now() + timedelta(days=30)
    ) 
    
    # cron
    schedule, _ = CrontabSchedule.objects.get_or_create(
        minute='3',
        hour='*',
        day_of_week='*',
        day_of_month='*',
        month_of_year='*',
    )
    
    cron_task, created = PeriodicTask.objects.get_or_create(
        crontab=schedule,
        name='Importing contacts cron',
        task='example_celery.tasks.import_contacts2'
    )
    
    interval_task.save()
    cron_task.save()
    