from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from datetime import datetime

from ..extensions import Base


class Address(Base):
    """
    Address Model that extend with Base to become sqlAlchemy model
    """
    __tablename__ = 't_address'

    address_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    input_address = Column(String)
    town = Column(String)
    city =  Column(String)
    postal_code =  Column(Integer)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.now())
    updated_at = Column(TIMESTAMP(timezone=True), default=datetime.now(), onupdate=datetime.now())

    __table_args__ = (
        UniqueConstraint('latitude', 'longitude', name='uq_latitude_longitude'),
    )

    def __init__(self, input_address, town, city, postal_code,\
                country, latitude=None, longitude=None):
        self.input_address = input_address
        self.town = town
        self.city = city
        self.postal_code = postal_code
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
