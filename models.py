from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    sku = Column(String, unique=True)
    image_url = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
