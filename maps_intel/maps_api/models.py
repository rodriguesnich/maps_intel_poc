from django.db import models

# Create your models here.
class Point(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return self.name

class PointConnection(models.Model):
    pointFrom = models.ForeignKey(Point, related_name='pointFrom', on_delete=models.CASCADE)
    pointTo = models.ForeignKey(Point, related_name='pointTo', on_delete=models.CASCADE)

    @property
    def coords(self):
        point = [{'lat':self.pointFrom.latitude, 'lng':self.pointFrom.longitude}, {'lat':self.pointTo.latitude, 'lng':self.pointTo.longitude}]
        return point