from datetime import time
from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=40)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Meeting(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()
    time = models.TimeField(default=time(9))
    duration_in_hours = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'Meeting {self.title} at {self.date} {self.time}'
