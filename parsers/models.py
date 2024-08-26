from django.db import models
from datetime import datetime

class Parser(models.Model):
    name = models.CharField(max_length=255)
    script_path = models.FileField(help_text="Path to parser script")
    schedule_interval = models.CharField(max_length=50, help_text="Launch interval, e.g., 'daily', 'hourly'")
    last_run = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
