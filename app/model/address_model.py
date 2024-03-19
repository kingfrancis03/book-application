class Address:
  def __init__(self, town, city, postal_code,\
                country, latitude=None, longitude=None):
    self.town = town
    self.city = city
    self.postal_code = postal_code
    self.country = country
    self.latitude = latitude
    self.longitude = longitude
