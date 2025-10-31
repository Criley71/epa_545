from django.db import models
# Create your models here.

class siteData(models.Model):
  site_id = models.CharField(max_length=15)
  state = models.CharField(max_length=50, default="unknown")
  county = models.CharField(max_length=100, default="unknown")
  pollutant = models.CharField(max_length=70)
  value = models.FloatField()
  units = models.CharField(max_length=100, default="unknown")
  date = models.DateField()
  
  def __str__(self):
    return f"{self.county}, {self.state}: {self.site_id} - {self.pollutant}"

class SiteAqiData(models.Model):
  site_id = models.CharField(max_length=15)
  state = models.CharField(max_length=50, default="unknown")
  county = models.CharField(max_length=100, default="unknown")
  pollutant = models.CharField(max_length=70)
  value = models.FloatField()
  units = models.CharField(max_length=100, default="unknown")
  date = models.DateField()
  
  class Meta:
    db_table = 'site_aqi_data'
    verbose_name = 'Site AQI Data'
    verbose_name_plural = 'Site AQI Data'
  
  def __str__(self):
    return f" {self.state}, {self.county} : {self.site_id} - {self.date}: {self.pollutant}"

class SiteMetaData(models.Model):
  site_id = models.CharField(max_length=15)
  state = models.CharField(max_length=50, default="unknown")
  city = models.CharField(max_length=100, default="unknown")
  county = models.CharField(max_length=100, default="unknown")
  latitude = models.FloatField()
  longitude = models.FloatField()
  no2_start_date = models.DateField(null=True, blank=True)
  co_start_date = models.DateField(null=True, blank=True)
  pm_start_date = models.DateField(null=True, blank=True)
  
  class Meta:
    db_table = 'site_meta_data'
    verbose_name = 'Site Meta Data'
    verbose_name_plural = 'Site Meta Data'
    
  def __str__(self):
    return f" {self.state}, {self.county} : {self.site_id}"

