from django.db import models


class PointOfInterest(models.Model):
    poi_id = models.CharField(max_length=100, default='')  
    poi_name = models.CharField(max_length=100)
    poi_latitude = models.FloatField()
    poi_longitude = models.FloatField()
    poi_category = models.CharField(max_length=100)
    poi_ratings = models.CharField(max_length=255)

    def __str__(self):
        return self.poi_name


