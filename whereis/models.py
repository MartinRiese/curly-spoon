from django.db import models


class Location(models.Model):
    user_name = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    lat_lon = models.CharField(max_length=200, default="51.01454,11.04377")
    created = models.DateTimeField(auto_now_add=True, blank=True)
