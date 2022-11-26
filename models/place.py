#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, INTEGER, FLOAT, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


# asocitaion table
association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
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
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db' or\
        getenv('HBNB_TYPE_STORAGE') == 'test':
        amenities = relationship("Amenity", secondary='place_amenity', viewonly=False)
        reviews = relationship("Review", backref="places", cascade="delete")

    else:
        @property
        def amenities(self):
            """ list of amenities"""
            list_auxiliar = []
            from models.__init__ import storage
            from models.amenity import Amenity
            for amenity in storage.all(Amenity):
                if amenity.id in self.amenity_ids:
                    list_auxiliar.append(amenity)
            return list_auxiliar
        
        @amenities.setter
        def amenities(self, value):
            from models.amenity import Amenity
            if type(value) == Amenity:
                self.amenity_ids(value.id)
        
        @property
        def reviews(self):
            """ list of reviews """
            list_auxiliar = []
            from models.__init__ import storage
            from models.review import Review
            for review in storage.all(Review):
                if self.id == review.place_id:
                    list_auxiliar.append(review)
            return list_auxiliar
