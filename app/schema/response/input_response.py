from .base_response import BaseModel, BaseReponse


class NewAddressID(BaseModel):
    address_id: int

class InputAddress(BaseReponse):
    data: NewAddressID
