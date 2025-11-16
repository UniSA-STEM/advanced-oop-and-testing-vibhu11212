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
        self.__name = name
        self.__staff_id = staff_id

class Zookeeper(Staff):
    """
    Represents a Zookeeper, inheriting from Staff
    """
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id)
        self.__assigned_enclosures = [] # enclosure assigned to zookeper

class Veterinarian(Staff):
    """
    Represents a Veterinarian, inheriting from Staff
    """
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id)