from fastapi import APIRouter


class BaseController(APIRouter):
    """
    Base controller for all controler.
        - extends FastApi's APIRouter
    """
    def __init__(self, prefix):
        """
        Class initializer
        
        Args:
          prefix(str): prefix for routs
          tags(str): For enpoint title in swagger
        """
        super().__init__(prefix=prefix, tags=[prefix.title()[1:]])
