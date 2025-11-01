# How To Run EPA Data Fetcher

1. aquire an EPA API key by entering your email in this link: https://aqs.epa.gov/data/api/signup?email=myemail@example.com, you will recieve an email with your API key

2. make a python virtual environment, activate it, and install requirements
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Make a postgres sql table locally or using a remote host provider. Note the database name, username and password.

4. make a .env file with the following info (*I have my .env in the discord so use that*):

```
DATABASE_URL="postgresql://[username]:[password]@localhost:[Postgres Port (default 5432)]/[DB Name]"   
#the database url can also point towards your remote db   
EPA_API_EMAIL= yourApiEmail@email.com  
EPA_API_KEY= API KEY   
#Django settings   
DEBUG=True   
SECRET_KEY=super-secret-key
```

5. set up django. In the root run
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

6. Open http://127.0.0.1:8000/admin and log in with the superuser credentials

7. To get site meta data in root run:

`python manage.py get_site_meta_data`

8. To get all site data run (note this will take roughly 18 hours if using a local sql table, remote providers add rate limits on top of the EPA rate limit):

`python manage.py get_epa_data`


# REST API USAGE

### Meta Data
| URL                        | Method    | Description               |
| -------------------------- | --------- | ------------------------- |
| `/sitemetadata/`           | GET       | List all sites            |
| `/sitemetadata/`           | POST      | Create a new site         |
| `/sitemetadata/<site_id>/` | GET       | Get metadata for one site |
| `/sitemetadata/<site_id>/` | PUT/PATCH | Update site metadata      |
| `/sitemetadata/<site_id>/` | DELETE    | Delete site metadata      |

### Site
 | URL                                      | Method    | Description                   | Query Params                                           |
| ---------------------------------------- | --------- | ----------------------------- | ------------------------------------------------------ |
| `/sitemetadata/<site_id>/data/`          | GET       | List all AQI data for a site  | `start_date`, `end_date`, `pollutant`                  |
| `/sitemetadata/<site_id>/data/`          | POST      | Create AQI data for that site | `site_id`, `date`, `pollutant`, `value`, `units`, etc. |
| `/sitemetadata/<site_id>/data/<aqi_id>/` | GET       | Get one AQI data entry        | -                                                      |
| `/sitemetadata/<site_id>/data/<aqi_id>/` | PUT/PATCH | Update one AQI data entry     | -                                                      |
| `/sitemetadata/<site_id>/data/<aqi_id>/` | DELETE    | Delete one AQI data entry     | -                                                      |

example for site 13-089-0003, start date 2023-01-01, and end date 2023-06-30:


`GET /sitemetadata/13-089-0003/data/?start_date=2023-01-01&end_date=2023-06-30`

