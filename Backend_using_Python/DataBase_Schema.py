
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class Attribute(Base):
    __tablename__ = 'attributes'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Variant(Base):
    __tablename__ = 'variants'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    attribute_id = Column(Integer, ForeignKey('attributes.id'))
    value = Column(String)

