from dataclasses import field
from rest_framework import serializers
from maps_api.models import Point, PointConnection

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'

class PointConnectionSerializer(serializers.ModelSerializer):
    coords = serializers.ReadOnlyField()
    class Meta:
        model = PointConnection
        fields = ['id', 'coords']

class PointConnectionListSerializer(serializers.ModelSerializer):
    coords = serializers.ReadOnlyField()
    class Meta:
        model = PointConnection
        fields = ['id', 'coords']
