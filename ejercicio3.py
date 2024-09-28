"""
EJERCICIO 3

Escribe un script que tome como entrada un fichero con una lista de ciudades españolas (por ejemplo: "Huesca, Frogtek, Jaca, Guadalajara")
, una por línea. Por cada una de las ciudades el script hará dos queries a la API de OpenWeather
 (https://openweathermap.org, puedes usar la key 2b2c54bd4f822b146e23fc28a5e1c1e6) y guardará en el fichero original los datos que pedimos, separados por una coma (,):

Petición 1) Usando el nombre de la ciudad, consulta y guarda la temperatura,
la velocidad del viento y sus coordenadas geográficas (longitud y latitud).

Petición 2) Usando las coordenadas del punto anterior, consulta y guarda la hora del amanecer y anochecer
y valida que el nombre de la ciudad devuelto por la petición usando coordenadas
devuelve el mismo nombre de la ciudad del listado.

Si en el punto 1), hay algún tipo de error, se rellenarán los valores con 0 y no se hará la petición 2).

Por ejemplo, si el listado inicial fuera de dos ciudades de nombre EXISTE y NOEXISTE, el fichero final quedaría así:
EXISTE,23.21,2.54,-0.7499,40.560,06:45:12,21:45:12
NOEXISTE,0,0,0,0
"""

import sys
from dotenv import load_dotenv
import os
from datetime import datetime
from City import City
from utils import write_cities_to_file, read_cities_from_source, get_city_data, get_sun_data

load_dotenv()
api_key = os.getenv("OWM_API_KEY")
base_url = os.getenv("OWM_BASE_URL")

DICT_CONFIG = dict(
    api_url= base_url + f"data/2.5/weather",
    country_iso2='ES'
)

cities_to_write=list()

def process_cities(file_path):
    cities = read_cities_from_source(file_path)
    for city_to_retrieve in cities:
        print(f"City found: {city_to_retrieve}...")
        city = City(name=city_to_retrieve,
                    country_iso2=DICT_CONFIG['country_iso2'])
        city_weather_data=get_city_data(city, api_key)
        if city_weather_data:
            city_sun_data = get_sun_data(city_weather_data, api_key)
            cities_to_write.append(city_sun_data)
        else:
            print("Error en la ciudad", city)
            cities_to_write.append(city)

    write_cities_to_file(file_path, cities_to_write)


if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Error")
    else:
        print(sys.argv)
        file_path = sys.argv[1]
        process_cities(file_path)