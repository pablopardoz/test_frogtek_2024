import requests
import os
from datetime import datetime
from City import City
from typing import List


def read_cities_from_source(file_path: str) -> List:
    with open(file_path, 'r') as f:
        cities = f.read().splitlines()
    return cities


def write_cities_to_file(file_path: str, cities: List):
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

def get_city_data(city: City, api_key: str) -> City:
    params = {
        "q": f"{city.name},{city.country_iso2}",
        "limit": 5,
        "units": 'metric',
        "appid": api_key
    }
    response_dict = retrieve_api_data(params)
    print(response_dict)
    if response_dict.get('cod') == 200:
        city.lon = response_dict['coord']['lon']
        city.lat = response_dict['coord']['lat']
        city.temp_c = response_dict['main']['temp']
        city.wind_speed = response_dict['wind']['speed']
        city.valid_city = True
        return city
    else:
        city.valid_city = False
        return city

def get_sun_data(city: City, api_key: str) -> City:
    params = dict(lat=city.lat,
                  lon=city.lon,
                  units='metric',
                  appid=api_key)
    response_dict = retrieve_api_data(params)
    if response_dict.get('cod') == 200:
        city.sunset = datetime.fromtimestamp(response_dict['sys']['sunset'])
        city.sunrise = datetime.fromtimestamp(response_dict['sys']['sunrise'])
        city.valid_name = validate_city(city.name, response_dict['name'])
        print(city)
        return city
    else:
        return city


def validate_city(original_name: str, returned_name: str) -> bool:
    if original_name.lower() == returned_name.lower():
        return True
    else:
        return False