from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError, DatabaseError

from ..repository.address_repository import AddressRepository
from ..model.address_model import Address
from ..helpers.geopy_helpers import GeoHelper
from ..constants import error_messages, key_constants


class AddressService:
    """
    Address Service that contains all the logic in address management

    Attributes:
      repository(object): Repositry to be used in commincation in the database
      geohelper(object): Helper for the geolocation stuff

    """
    def __init__(self, model: Address = Depends(Address), repository: AddressRepository = Depends(AddressRepository)) -> None:
        """Class intialization"""
        self.repository = repository(model)
        self.geohelper = GeoHelper()

    def create_address(self, input_address):
        """Address creation

          Args:
            input_address(str): Inputted address
          Returns:
            address id(int): Address Id created
          """
        geo_location: any = self.geohelper.get_location(input_address)
        if geo_location is not None:
          address_data = self.__extract_address_details(input_address, geo_location)

          try:
            return self.repository.create_address(address_data)
          except IntegrityError:
              raise ValueError(error_messages.ADDRESS_SAVED)
          except DatabaseError as error:
              raise ValueError(error_messages.FAILED_SAVED.format(error))
          except Exception as error:
              raise ValueError(error_messages.INNER_ERROR.format(error))

        raise ValueError(error_messages.INVALID_ADDRESS)

    def __extract_address_details(self, input_address, geo_location):
        """Extraction from location's metadata

        Args:
            input_address(str): Inputted address
            geo_location(object): Locations metadata by geopy
        Returns:
            address (object): Address data ti be put ib teg database
        """
        town: str = geo_location.raw[key_constants.ADDRESS].get('quarter')
        city: str = geo_location.raw[key_constants.ADDRESS].get('city')
        postal_code: str = geo_location.raw[key_constants.ADDRESS].get('postcode')
        country: str = geo_location.raw[key_constants.ADDRESS].get('country')
        longitude: float = geo_location.longitude
        latitude: float = geo_location.latitude
        
        return Address(input_address, town, city, postal_code, country, latitude, longitude)

    def get_all_address(self):
        """Getter for all address
      
        Returns:
            addresses (list): retrieved addresses from the repository class
        """
        addresses = self.repository.get_all()

        return jsonable_encoder(addresses)
      
    def update_address(self, address_id, input_address):
        """Updates Address

        Args:
          address_id(int): address id to be updated
          input_address(str): Inputted address
        Returns:
          address id(int): Address Id updated
        """
        geo_location: any = self.geohelper.get_location(input_address)
        if geo_location is not None:
          address_data = self.__extract_address_details(input_address, geo_location)

          try:
            return self.repository.update_address(address_id, address_data)
          except IntegrityError:
              raise ValueError(error_messages.ADDRESS_EXIST)
          except DatabaseError as error:
              raise ValueError(error_messages.FAILED_SAVED.format(error))
          except AttributeError:
              raise AttributeError(error_messages.ADDRESS_DONT_EXIST)
          except Exception as error:
              raise ValueError(error_messages.INNER_ERROR.format(error))
        raise ValueError(error_messages.INVALID_ADDRESS)

    def delete_address(self, address_id):
        """Deletes Address

        Args:
          address_id(int): address id to be updated
        Returns:
          address id(int): Address Id deleted
        """
        address = self.repository.get_by_id(address_id)
        if address is not None:
          return self.repository.delete_address(address_id)

        raise ValueError(error_messages.ADDRESS_DONT_EXIST)

    def get_nearby_address(self, input_coordinates, proximity):
        """Retieves Nearby Addresses

          Args:
            input_coordinates(dict): coordinates of the base location
            proximity(int): the range where you will find what's nearby 
          Returns:
            Addresses(List):List of Address thats nearby the base location
          """
        saved_coordinates = self.__get_saved_coordinates()
        nearby_ids = []
        for coordinates in saved_coordinates:
          distance = self.geohelper.get_distance(coordinates[key_constants.COORDINATES], input_coordinates)
          if distance < proximity:
            nearby_ids.append(coordinates[key_constants.ADDRESS_ID])

        return jsonable_encoder(self.repository.get_by_ids(nearby_ids))

    def __get_saved_coordinates(self):
        """Retieves Saved coordinates

        coordinates(List):List of coordinates with id
        """
        rows = self.repository.get_saved_coordinates()
        address_list = []
        for address_id, longitude, latitude in rows:
          address_list.append({
            key_constants.ADDRESS_ID: address_id,
            key_constants.COORDINATES: {
              key_constants.LATITUDE: latitude,
              key_constants.LONGITUDE: longitude
            }
          })

        return address_list
