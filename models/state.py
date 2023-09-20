#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models 
from models.city import City



class State(BaseModel,Base):
    """ State class """
    if models.storage_engine == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False) 
        cities = relationship('City', backref='state')
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """init the state class"""
        super().__init__(*args, **kwargs)

if models.storage_engine != "db":
    @property
    def cities(self):
        st_cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                st_cities.append(city)
        return st_cities
            