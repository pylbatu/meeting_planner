from django.db import models

# Create your models here.


class Meeting(models.Model):
    title = models.CharField(max_length=40)
    date = models.DateField()