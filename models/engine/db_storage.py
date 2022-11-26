#!/usr/bin/python3
"""This module defines a class to manage data base storage for hbnb clone"""
import json
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(f"mysql+mysqldb://\
{getenv('HBNB_MYSQL_USER')}:\
{getenv('HBNB_MYSQL_PWD')}@{getenv('HBNB_MYSQL_HOST')}:3306/\
{getenv('HBNB_MYSQL_DB')}", pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':  # drop all tables
            MetaData.drop_all(self.__engine)

    def all(self, cls=None):

        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        classes = {
                    'State': State, 'User': User, 'Place': Place,
                    'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

        final_dictionary = {}
        if cls:
            for object in self.__session.query(classes[str(cls)]):
                key_auxiliar = str(cls) + '.' + object.id
                final_dictionary[key_auxiliar] = object.to_dict()
        else:
            for class_aux in classes.keys():
                for object in self.__session.query(classes[class_aux]).all():
                    key_auxiliar = str(class_aux) + '.' + object.id
                    final_dictionary[key_auxiliar] = object.to_dict()
        return final_dictionary
        # if cls:
        #     if type(cls) == str:
        #         cls = eval(cls)
        #     objs = self.__session.query(cls)
        # else:
        #     objs = self.__session.query(State).all()
        #     objs.extend(self.__session.query(City).all())
        #     objs.extend(self.__session.query(User).all())
        #     objs.extend(self.__session.query(Place).all())
        #     objs.extend(self.__session.query(Review).all())
        #     objs.extend(self.__session.query(Amenity).all())
        # return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """
            add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            commit all changes of the current database session
        """
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.base_model import Base

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        Base.metadata.create_all(self.__engine)

        Sess = scoped_session(sessionmaker(expire_on_commit=False,
                                           bind=self.__engine))
        self.__session = Sess()

    def delete(self, obj=None):
        """
            delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)
