from django.contrib import admin
from poi_manager.models import PointOfInterest


# admin.py
from django.contrib import admin
from .models import PointOfInterest

class PointOfInterestAdmin(admin.ModelAdmin):
    list_display = ('poi_id', 'poi_name', 'poi_category')  
    list_filter = ('poi_category',) 
admin.site.register(PointOfInterest, PointOfInterestAdmin)
