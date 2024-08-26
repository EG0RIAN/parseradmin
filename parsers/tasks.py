# parsers/tasks.py
import subprocess
from celery import shared_task, Celery
from celery.schedules import crontab
from datetime import datetime
from .models import Parser
from django.utils import timezone

@shared_task
def run_parser(parser_id):
    parser = Parser.objects.get(id=parser_id)
    if parser.is_active:
        # Run the script
        subprocess.call(['python', parser.script_path.path])
        # Update last run time
        parser.last_run = timezone.now()
        parser.save()

@shared_task
def schedule_parsers():
    parsers = Parser.objects.filter(is_active=True)
    for parser in parsers:
        schedule_interval = parser.schedule_interval.lower()

        # Map schedule_interval to appropriate scheduling
        if schedule_interval == 'hourly':
            run_parser.apply_async(args=[parser.id], countdown=3600)
        elif schedule_interval == 'daily':
            run_parser.apply_async(args=[parser.id], countdown=86400)
        elif schedule_interval == 'weekly':
            run_parser.apply_async(args=[parser.id], countdown=604800)
