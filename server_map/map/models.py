from django.db import models

# Create your models here.
class MapRequests(models.Model):
    ip = models.GenericIPAddressField()
    location = models.CharField(max_length=300)
    date_time_connection = models.DateTimeField(auto_now_add=True)
