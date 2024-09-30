import unittest
from ejercicio1 import convert_number, process_string
from ejercicio2 import remove_zeros
from utils import read_cities_from_source, get_city_data, get_sun_data
from City import City
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OWM_API_KEY")
base_url = os.getenv("OWM_BASE_URL")


class TestsEjercicio1(unittest.TestCase):
    def test_convert_number_string(self):
        self.assertEqual(convert_number("Frogtek"),0 )

    def test_convert_number_string_int(self):
        self.assertEqual(convert_number("1"),1 )

    def test_convert_number_string_float(self):
        self.assertEqual(convert_number("1.3"),1.3 )

    def test_convert_number_string_float_comma(self):
        self.assertEqual(convert_number("1,3"),1.3 )

    def test_convert_number_comma(self):
        self.assertEqual(convert_number(','),0 )

    def test_convert_number_point(self):
        self.assertEqual(convert_number('.'),0 )

    def test_convert_number_point(self):
        self.assertEqual(process_string('Frogtek se fundó en 2010, y ahora tiene 40 empleados y hay 20,1. ayer 23.1'),2093.2 )

class TestsEjercicio2(unittest.TestCase):
    def test_remove_zeros_ip(self):
        self.assertEqual(remove_zeros('253.100.50.25'), '253.100.50.25')
        self.assertEqual(remove_zeros('253.0.50.25'), '253.0.50.25')
        self.assertEqual(remove_zeros('0253.00100.50.25'), '253.100.50.25')
        self.assertEqual(remove_zeros('0253.100.0.0'), '253.100.0.0')
        self.assertEqual(remove_zeros('192.168.1'), '192.168.1')
        self.assertEqual(remove_zeros(''), '')

class TestsEjercicio3(unittest.TestCase):
    def test_read_cities_from_source_list(self):
        file_path = 'data/cities.txt'
        result = read_cities_from_source(file_path)
        self.assertIsInstance(result, list)

    def test_query_api(self):
        city = City(name='Alicante', country_iso2='ES')
        r = get_city_data(city=city, api_key=api_key)
        self.assertIsInstance(r, City)
        self.assertIsNotNone(city.lon )
        self.assertIsNotNone(city.lat)
        self.assertIsNotNone(city.temp_c)

    def test_query_api_sun(self):
        city = City(name='Alicante', country_iso2='ES', lon=-0.4815 , lat=38.3452)
        r = get_sun_data(city=city, api_key=api_key)
        self.assertIsInstance(r, City)
        self.assertIsNotNone(city.sunrise )
        self.assertIsNotNone(city.sunset )




if __name__ == '__main__':
    unittest.main()
