from .base_response import BaseModel, BaseReponse


class DeletedAddressID(BaseModel):
    deleted_address_id: int

class DeleteAddress(BaseReponse):
    data: DeletedAddressID
