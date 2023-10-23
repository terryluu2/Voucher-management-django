from django.db import models
from store.models.city import City
from store.models.restaurant import Restaurant


class Store(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
