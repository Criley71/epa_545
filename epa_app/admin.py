from django.contrib import admin
from .models import siteData, SiteAqiData

@admin.register(siteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'state', 'county', 'pollutant', 'value', 'units', 'date')

@admin.register(SiteAqiData)
class SiteAqiDataAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'state', 'county', 'pollutant', 'value', 'units', 'date')
