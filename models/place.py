#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, INTEGER, FLOAT, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'place_amenity'
    metadata = Base.metadata
    place_id = Column(String(60), ForeignKey('places.id'), primary_key=True, nullable=False)
    amenity_id = Column(String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(INTEGER, default=0, nullable=False)
    number_bathrooms = Column(INTEGER, default=0, nullable=False)
    max_guest = Column(INTEGER, default=0, nullable=False)
    price_by_night = Column(INTEGER, default=0, nullable=False)
    latitude = Column(FLOAT, nullable=True)
    longitude = Column(FLOAT, nullable=True)
    if getenv('HBNB_TYPE_STORAGE') == 'db' or\
        getenv('HBNB_TYPE_STORAGE') == 'test':
        amenities = relationship("Amenity", secondary='place_amenity', viewonly=False, backref='places')
    else:
        pass
