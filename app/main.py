from fastapi import FastAPI, APIRouter, Request
from .controller.address_controller import AddressController
from fastapi.openapi.utils import get_openapi
from app.extensions import logging

#intialize FastAPI
app = FastAPI()

# Middleware to log every request
@app.middleware("http")
async def log_request(request: Request, call_next):
    logging.info(f"Request: {request.method} {request.url.path}")
    response = await call_next(request)

    return response
# Initialize Controller for the routs
address_router = AddressController("/address")

# Add address router to FastAPI App
app.include_router(address_router)

# Customization of Swagger Details
def custom_openapi():
    return get_openapi(
        title="API Documentation For Address Book Application",
        version="1.0.0",
        description="Demonstration of my exisiting Python3 skills",
        routes=app.routes
    )


# Put custom swagger details to FastAPI app
app.openapi = custom_openapi

# Log every start of service
logging.info("Book Application Service running")
