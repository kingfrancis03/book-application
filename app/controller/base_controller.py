from fastapi import APIRouter

class BaseController(APIRouter):
  def __init__(self, prefix):
    super().__init__(prefix=prefix, tags=[prefix.title()[1:]])

