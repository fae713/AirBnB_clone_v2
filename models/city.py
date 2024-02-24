#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="all, delete, delete-orphan")

    else:
        state_id = ""
        name = ""

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def places(self):
            """
            getter for places
            :return: list of places in that city
            """
            all_places = models.storage.all("Place")

            result = []

            for obj in all_places.values():
                if str(obj.city_id) == str(self.id):
                    result.append(obj)

            return result
