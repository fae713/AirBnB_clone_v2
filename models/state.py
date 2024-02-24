#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.city import City
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


BaseModel = declarative_base()

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="states",
                          cascade="all, delete, delete-orphan")

    if getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """ returns list of City instances related to state """
            from models import storage
            the_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    the_cities.append(city)
            return the_cities
