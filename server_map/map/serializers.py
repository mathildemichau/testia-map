from .models import MapRequests
from rest_framework import serializers

class MapRequestsSerialiser(serializers.ModelSerializer):
    class Meta: 
        model = MapRequests
        fields = "__all__"
