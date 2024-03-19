from fastapi import FastAPI, APIRouter
from .controller.address_controller import AddressController
from fastapi.openapi.utils import get_openapi
from app import extensions

app = FastAPI()

address_router = AddressController("/address")

app.include_router(address_router)
def custom_openapi():
    return get_openapi(
        title="API Documentation For Address Book Application",
        version="1.0.0",
        description="Demonstration of my exisiting Python3 skills",
        routes=app.routes
    )

app.openapi = custom_openapi