from pydantic import BaseModel


class Coordinates(BaseModel):
    latitude: float
    longitude: float

class FindAddressRequest(BaseModel):
    coordinates: Coordinates
    proximity: float
