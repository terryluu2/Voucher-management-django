from django.contrib import admin
from store.models import Country, City, Restaurant, Store

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Restaurant)
admin.site.register(Store)
