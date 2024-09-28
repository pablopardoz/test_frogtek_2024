from dataclasses import dataclass
from datetime import datetime
@dataclass
class City:
    name: str
    country_iso2: str
    temp_c: float = 0.0
    wind_speed: float = 0
    lon: float = 0
    lat:float = 0
    sunrise: datetime = None
    sunset: datetime = None
    valid: bool = False


    def __repr__(self):
        return f"{self.name}," \
            f"{self.temp_c}," \
            f"{self.wind_speed}," \
            f"{self.lon}," \
            f" {self.lat}, " \
            f"{self.sunrise.strftime('%H:%M:%S') if self.sunrise else '0'}," \
            f" {self.sunset.strftime('%H:%M:%S') if self.sunset else '0'}"
