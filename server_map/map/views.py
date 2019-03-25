from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import MapRequests
from .serializers import MapRequestsSerialiser

class MapRequestViewSet(ModelViewSet):
    queryset = MapRequests.objects.all()
    serializer_class = MapRequestsSerialiser