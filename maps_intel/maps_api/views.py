from rest_framework import viewsets, generics
from maps_api.models import Point, PointConnection
from . import serializer
#from django.http import JsonResponse

class PointViewSet(viewsets.ModelViewSet):
    """Access Point Informations"""
    queryset = Point.objects.all()
    serializer_class = serializer.PointSerializer

class PointConnectionViewSet(viewsets.ModelViewSet):
    queryset = PointConnection.objects.all()
    serializer_class = serializer.PointConnectionSerializer

class PointConnectionList(viewsets.ModelViewSet):
    queryset = PointConnection.objects.all()
    serializer_class = serializer.PointConnectionListSerializer