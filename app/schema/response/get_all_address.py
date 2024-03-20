from .base_response import BaseModel, BaseReponse
from typing import List


class Address(BaseModel):
    input_address: str
    address_id: int
    latitude: float
    longitude: float

class GetAllAddress(BaseReponse):
    data: List[Address]
