import requests
import os
from datetime import datetime

def read_cities_from_source(file_path):
    with open(file_path, 'r') as f:
        cities = f.read().splitlines()
    return cities


def write_cities_to_file(file_path, cities):
    with open(file_path, 'w') as f:
        for city in cities:
            #if city.valid:
            f.write(repr(city) + '\n')


def retrieve_api_data(params):
    url = os.getenv("OWM_BASE_URL")+f"data/2.5/weather"
    response = requests.get(url, params=params)
    datos = response.json()
    try:
        response = datos
    except Exception as e:
        print(e)
        return {}
    return response

def get_city_data(city, api_key):
    params = {
        "q": f"{city.name},{city.country_iso2}",
        "limit": 5,
        "units": 'metric',
        "appid": api_key
    }
    response_dict = retrieve_api_data(params)
    if response_dict.get('cod') == 200:
        city.lon = response_dict['coord']['lon']
        city.lat = response_dict['coord']['lat']
        city.temp_c = response_dict['main']['temp']
        city.wind_speed = response_dict['wind']['speed']
        return city
    else:
        return None

def get_sun_data(city, api_key):
    params = dict(lat=city.lat,
                  lon=city.lon,
                  units='metric',
                  appid=api_key)
    response_dict = retrieve_api_data(params)
    if response_dict.get('cod') == 200:
        city.sunset = datetime.fromtimestamp(response_dict['sys']['sunset'])
        city.sunrise = datetime.fromtimestamp(response_dict['sys']['sunrise'])
        city.valid = validate_city(city.name, response_dict['name'])
        print(city)
        return city
    else:
        return None


def validate_city(original_name: str, returned_name: str) -> bool:
    if original_name.lower() == returned_name.lower():
        return True
    else:
        return False