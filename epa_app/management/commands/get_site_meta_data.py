import pandas as pd
from django.core.management.base import BaseCommand
from epa_app.models import siteData, SiteAqiData, SiteMetaData
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

PROJECT_ROOT = os.path.abspath(os.path.join(__file__, '../../../../'))
CSV_PATH = os.path.join(PROJECT_ROOT, 'data', 'april-2022-near-road-site-list_public.csv')
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))
EPA_API_EMAIL = os.getenv("EPA_API_EMAIL")
EPA_API_KEY = os.getenv("EPA_API_KEY")
POLLUTE_CODES = {'42101' : 'Carbon Monoxide (CO)', '42401' : 'Sulfer Dioxide (SO2)', '42602' : 'Nitrogen Dioxide (NO2)', '88101' : 'PM2.5'}
START_DATE_COLUMNS = {'NO2     Start Date', 'CO     Start Date', 'Continuous PM2.5 Start Date'}
site_df = pd.read_csv(CSV_PATH)

class Command(BaseCommand):
  help = "Pull EPA site meta data"
  def handle(self, *args, **options):
    for _, row in site_df.iterrows():
      no2_date_ = None
      co_date_ = None
      pm_date_ = None
      site_id_ = row['AQS ID']
      state_ = row['State']
      city_ = row['City']
      county_ = row['County']
      latitude_ = row['Latitude']
      longitude_ = row['Longitude']
      if pd.isna(row['NO2     Start Date']):
        no2_date_ = None
      else:
        no2_date_ = datetime.strptime(row['NO2     Start Date'].strip(), "%m/%d/%Y").date()
      if pd.isna(row['CO     Start Date']):
        co_date_ = None
      else:
        co_date_ = datetime.strptime(row['CO     Start Date'].strip(), "%m/%d/%Y").date()
      if pd.isna(row['Continuous PM2.5 Start Date']):
        pm_date_ = None
      else:
        pm_date_ = datetime.strptime(row['Continuous PM2.5 Start Date'].strip(), "%m/%d/%Y").date()
      SiteMetaData.objects.create(
        site_id = site_id_,
        state = state_,
        city = city_,
        county = county_,
        latitude = latitude_,
        longitude = longitude_,
        no2_start_date = no2_date_,
        co_start_date = co_date_,
        pm_start_date = pm_date_        
      )

      
        