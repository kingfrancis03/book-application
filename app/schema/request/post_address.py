from pydantic import BaseModel


class Address(BaseModel):
    input_address: str
