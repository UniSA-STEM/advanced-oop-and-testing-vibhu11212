'''
File: animal.py
Description: A brief description of this Python module.
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base Class for all animals
    """
    def __init__(self, name, species, age,
                 dietary_needs , environment):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__dietary_needs = dietary_needs
        self.__required_environment = environment
        self.__health_records = []  # To store health record

class Mammal(Animal):
    """
    Represents a mammal, inheriting from Animal class
    """
    def __init__(self, name, species, age,
                 dietary_needs, environment):
        super().__init__(name, species, age, dietary_needs, environment)


class Bird(Animal):
    """
    Represents a bird, inheriting from Animal class
    """
    def __init__(self, name, species, age,
                 dietary_needs, environment):
        super().__init__(name, species, age, dietary_needs, environment)


class Reptile(Animal):
    """
    Represents a reptile, inheriting from Animal class
    """
    def __init__(self, name, species, age,
                 dietary_needs, environment):
        super().__init__(name, species, age, dietary_needs, environment)
