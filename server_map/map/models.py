from django.db import models
from django.utils import timezone
# Create your models here.
class MapRequests(models.Model):
    ip = models.GenericIPAddressField()
    location = models.CharField(max_length=300)
    date_time_connection = models.DateTimeField(default=timezone.now)
