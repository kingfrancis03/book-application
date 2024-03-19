from .base_controller import BaseController
from ..helpers.geopy_helpers import GeoHelper


class AddressController(BaseController):
    geohelper: GeoHelper

    def __init__(self, prefix):
        super().__init__(prefix) 
        self.geohelper = GeoHelper()
        self.add_api_routes()

    def add_api_routes(self):
        self.add_api_route("/", self.get_addresses, methods=["GET"])
        self.add_api_route("/", self.post_address, methods=["POST"])

    async def get_addresses(self):
        return {"message": "Read all addresses"}
    
    async def post_address(self):
        return {"message": "Post Address"}
    
