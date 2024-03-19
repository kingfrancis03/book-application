from functools import partial
from geopy.geocoders import Nominatim

from geopy.distance import geodesic
from geopy.point import Point

# # Coordinates of the two points (latitude, longitude)
# point1 = Point(40.7128, -74.0060)  # New York City
# point2 = Point(34.0522, -118.2437)  # Los Angeles

# # Calculate the distance between the two points using the WGS-84 ellipsoid (default)

# distance = geodesic(point1, point2).kilometers



class GeoHelper:
  def __init__(self) -> None:
    self.geolocator = Nominatim(user_agent="my_email@myserver.com")
    print(self.geolocator.geocode("SM Cabanatuan").raw)
    self.test_distance()

  def get_location(self, input_location: str) -> str:
    return self.geolocator.geocode(input_location)
  
  def test_distance(self):
    point1 = Point(15.300888, 120.948554)  # New York City
    point2 = Point(15.4878088, 120.96789870028536)
    distance = geodesic(point1, point2).kilometers

    print("Distance between New York City and Los Angeles:", distance, "kilometers")


  

