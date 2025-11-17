'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from abc import ABC, abstractmethod

class Staff(ABC):
    """
    Abstract Class for all staff members
    """
    def __init__(self, name, staff_id):
        self.name = name
        self.__staff_id = staff_id

    def get_name(self):
        return self.__name

    def get_staff_id(self):
        return self.__staff_id

    def set_name(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name is required.")
        self.__name = name

    name = property(get_name, set_name)
    staff_id = property(get_staff_id)

class Zookeeper(Staff):
    """
    Represents a Zookeeper, inheriting from Staff
    """
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id)
        self.__assigned_enclosures = [] # enclosure assigned to zookeper

    def get_assigned_enclosures(self):
        return self.__assigned_enclosures

    assigned_enclosures = property(get_assigned_enclosures)

class Veterinarian(Staff):
    """
    Represents a Veterinarian, inheriting from Staff
    """
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id)