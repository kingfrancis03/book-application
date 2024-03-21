from .base_response import BaseModel, BaseReponse
from .get_all_address import Address
from typing import List

class SingleAddress(BaseReponse):
    data: Address
