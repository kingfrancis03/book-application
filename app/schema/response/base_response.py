from pydantic import BaseModel


class BaseReponse(BaseModel):
  status: str
  message: str