from email.mime import base
from django.db import router
from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('point', views.PointViewSet, basename='Point')
router.register('pointConnection', views.PointConnectionViewSet, basename='PointConnection')
router.register('pointConnectionList', views.PointConnectionList, basename='PointConnectionList')

urlpatterns = [
    path('', include(router.urls)),
]