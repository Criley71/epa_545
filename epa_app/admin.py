from django.contrib import admin
from .models import siteData, SiteAqiData, SiteMetaData

@admin.register(siteData)
class SiteDataAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'state', 'county', 'pollutant', 'value', 'units', 'date')

@admin.register(SiteAqiData)
class SiteAqiDataAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'state', 'county', 'pollutant', 'value', 'units', 'date')
    
@admin.register(SiteMetaData)
class SiteMetaDataAdmin(admin.ModelAdmin):
    list_display = ('site_id', 'state', 'city', 'county', 'no2_start_date', 'co_start_date', 'pm_start_date')
