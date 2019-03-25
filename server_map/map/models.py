from django.db import models

# Create your models here.
class MapRequests(models.Model):
    ip = models.CharField(max_length=50)
    laocation = models.CharField(max_length=200)
    date_time_connection = models.DateTimeField('date time of the request')
