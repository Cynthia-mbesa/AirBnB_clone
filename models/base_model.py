#!/usr/bin/python3
"""this module creates a class BaseModel"""

import models
from models import storage
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Base class for all models in the application"""

    def __init__(self, *args, **kwargs):
        """initializes a new instance of the BaseModel.

        Args:
        *args: variable length argument list
        **kwargs: arbitrary keyword arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at' and type(self.created_at) is str:
                    value = datetime.strptime(value, time)
                if key == 'updated_at' and type(self.updated_at) is str:
                    value = datetime.strptime(value, time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates current datetime and saves to storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary representation of BaseModel instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].strftime(time)
        new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """returns string rep of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)
