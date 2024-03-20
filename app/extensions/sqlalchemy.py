from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker as SessionMaker
from sqlalchemy.ext.declarative import declarative_base

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./assets/db_address.db"

# Define Base
Base = declarative_base()

# Create Database Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = SessionMaker(autocommit=False, autoflush=True, bind=engine)
