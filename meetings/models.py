from datetime import time
from django.db import models

# Create your models here.


class Meeting(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()
    time = models.TimeField(default=time(9))
    durationInHours = models.IntegerField(default=1)

    def __str__(self):
        return f'Meeting {self.title} at {self.date} {self.time}'