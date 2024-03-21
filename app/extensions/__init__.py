import logging

from .sqlalchemy import Base, SessionLocal, engine
from ..model.address_model import Address # import for runthrough
from ..utils import log_config

# creates database when not exist using engine
Base.metadata.create_all(bind=engine)

# declare session to be used in imports
session = SessionLocal()
