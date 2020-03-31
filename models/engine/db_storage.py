#!/usr/bin/python3
"""New storage engine Class: DBStorage """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity

classes = {"State": State, "City": City, "User": User,
           "Place": Place, "Review": Review, "Amenity": Amenity}


class DBStorage():
    """
    Database Engine for AirBnB project
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Init
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        """
        current_dict = {}
        for Class in classes:
            if cls is Class or cls is classes[Class] or cls is None:
                objs = self.__session.query(classes[Class]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    current_dict[key] = obj
        return (current_dict)

    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()
