from .base_repository import BaseRepository
from ..model.address_model import Address

class AddressRepository(BaseRepository):
    """
    Address Repositry that handles the communication with the database

    Attributes:
        model(Base): SqlAlchemy model to help with ORM
    """
    def __init__(self, model) -> None:
        """Class initialization"""
        super().__init__()
        self.__model = model
  
    def create_address(self, address_data: Address) -> int:
        """
        Insert Address in the database

        Args:
            address_data(object): All address data to be added in the Database
        
        Returns:
            Address id(int): Address id for the new address
        """
        address = address_data
        self.session.add(address)
        self.session.commit() 
        self.session.refresh(address)
        self.session.flush()
        self.session.close()

        return address.address_id

    def get_all(self):
        """
        Select * in the database, Retrieves all in the database

        Returns:
            results(list): list of retrieve addresses
        """
        results = self.session.query(self.__model).all()

        return results
    
    def get_by_id(self, address_id):
        """
        Getter by specific ID

        Args:
            address id(int): Address id to be searched
        Returns:
            address(object): retrieved address by id
        """
        address = self.session.query(self.__model).filter_by(address_id=address_id).first()

        return address
    
    def get_by_ids(self, addresses):
        """
        Getter by muliple IDs

        Args:
            addresses(list): list of ids 
        Returns:
            results(list): list of retrieve addresses
        """
        addresses = self.session \
            .query(self.__model).filter(self.__model.address_id.in_(addresses)).all()

        return addresses

    def update_address(self, address_id, address_data: Address):
        """
        Updates Address in the database

        Args:
            address_id(int): address_id to be updated
            address_data(object): All address data to be added in the Database
        
        Returns:
            Address id(int): Address id for the updated address
        """
        current_address = self.get_by_id(address_id)
        current_address.input_address = address_data.input_address
        current_address.town = address_data.town
        current_address.city = address_data.city
        current_address.postal_code = address_data.postal_code
        current_address.longitude = address_data.longitude
        current_address.latitude = address_data.latitude

        self.session.commit() 
        self.session.refresh(current_address)
        self.session.close()

        return current_address.address_id 
    
    def delete_address(self, address_id):
        """
        Deletes Address in the database

        Args:
            address_id(int): address_id to be updated
        
        Returns:
            Address id(int): Address id for the deleted address
        """
        address = self.get_by_id(address_id)
        self.session.delete(address)
        self.session.commit()
        self.session.close()

        return address_id

    def get_saved_coordinates(self):
        """
        Getter for saved coordinates 

        Returns:
            results(list): list of coordinates with id
        """
        results = self.session.query(
            self.__model.address_id, self.__model.longitude, self.__model.latitude).all()

        return results
