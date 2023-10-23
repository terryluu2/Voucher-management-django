from django.db import models


class Country(models.Model):
    country_code = models.CharField(max_length=8)
