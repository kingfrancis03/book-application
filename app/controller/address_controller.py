from fastapi import Path, HTTPException
from .base_controller import BaseController
from ..repository.address_repository import AddressRepository
from ..service.address_service import AddressService
from ..schema.response import GetAllAddress, InputAddress, DeleteAddress
from ..schema.request import Address
from ..model.address_model import Address as AddressModel
from ..model.response_model import Response
from ..constants import httpmethod, key_constants, success_messages


class AddressController(BaseController):
    """
    Adress controller handles routes related to address management.
        - extends Base Controller
    Attribute:
        service(object): service that has address management

    """
    def __init__(self, prefix):
        """
        Class initializer
        
        Args:
            prefix(str): to be pass on super
        
        """
        super().__init__(prefix) 
        self.service = AddressService(AddressModel, AddressRepository)
        self.add_api_routes()

    def add_api_routes(self):
        """
        Initialize Routes for this Route '/address'
        
        """
        self.add_api_route("/", self.get_addresses, methods=[httpmethod.GET], response_model=GetAllAddress)
        self.add_api_route("/", self.post_address, methods=[httpmethod.POST], response_model=InputAddress)
        self.add_api_route("/{address_id}", self.put_address, methods=[httpmethod.PUT], response_model=InputAddress)
        self.add_api_route("/{address_id}", self.delete_address, methods=[httpmethod.DEL], response_model=DeleteAddress)
        self.add_api_route("/address-nearby",
                           self.find_nearby_addresses, methods=[httpmethod.GET], response_model=GetAllAddress)

    async def get_addresses(self):
        """Get All Addresses

        Returns:
            Data(List):List of Address
        """
        data = self.service.get_all_address()

        return Response(success_messages.SUCCESS, success_messages.RETRIEVED, data)
    
    def post_address(self, address: Address):
        """Add an Address

        Args: 
            address(string): The input address to be added
        Returns:
            Address Id(int):Generated ID of the new Address
        """
        try:
            address_id = {key_constants.ADDRESS_ID:self.service.create_address(address.input_address)}

            return Response(success_messages.SUCCESS, success_messages.SAVED, address_id)
        except ValueError as error:
            error_message = error.args[0]
            detail = {key_constants.MESSAGE: error_message}

            raise HTTPException(status_code=400, detail=detail)

    def put_address(self, address_id: int = Path(..., description="The ID of the address to be updated"),
                    address: Address = {}):
        """Update an Address
        
        Args:
            Address Id(int):Id of the deleted Address
        Returns:
            Address Id(int):Id of the updated Address
        """
        try:
            address_id = {key_constants.ADDRESS_ID:self.service.update_address(address_id, address.input_address)}

            return Response(success_messages.SUCCESS, success_messages.UPDATED, address_id)
        except (ValueError, AttributeError) as error:
            error_message = error.args[0]
            detail = {key_constants.MESSAGE: error_message}
            status_code = 400 if isinstance(error, ValueError) else 404

            raise HTTPException(status_code=status_code, detail=detail)
    
    def delete_address(self, address_id: int = Path(..., description="The ID of the address to delete")):
        """Delete an Address

        Args:
            Address Id(int):Id of the deleted Address

        Returns:
            Address Id(int):Id of the deleted Address
        """
        try:        
            address_id = {key_constants.DELETED_ID:self.service.delete_address(address_id)}

            return Response(success_messages.SUCCESS, success_messages.DELETED, address_id)
        except ValueError as error:
            error_message = error.args[0]
            detail = {key_constants.MESSAGE: error_message}

            raise HTTPException(status_code=404, detail=detail)
    
    
    def find_nearby_addresses(self, latitude: float, longitude: float, proximity: float):
        """Find Nearby Address

        Args:
            latitude(float):latitude of the origin place
            latitude(float):longitude of the origin place
            proximity(float):the range where you will find what's nearby

        Returns:
            Data(List):List of Address thats nearby the base location
        """
        coordinates = {
            key_constants.LATITUDE: latitude,
            key_constants.LONGITUDE: longitude
        }

        return Response(success_messages.SUCCESS,
                        success_messages.RETRIEVED_NEARBY,
                        self.service.get_nearby_address(coordinates, proximity))
