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
        self.name = name
        self.__species = species
        self.age = age
        self.__dietary_needs = dietary_needs
        self.__required_environment = environment
        self.__health_records = []  # To store health record

    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_dietary_needs(self):
        return self.__dietary_needs

    def get_required_environment(self):
        return self.__required_environment

    def get_health_records(self):
        return self.__health_records

    def set_name(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a string")
        self.__name = name

    def set_age(self, age):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must not be negative")
        self.__age = age

    def set_dietary_needs(self, dietary_needs):
        self.__dietary_needs = dietary_needs

    name = property(get_name, set_name)
    species = property(get_species)
    age = property(get_age, set_age)
    dietary_needs = property(get_dietary_needs, set_dietary_needs)
    required_environment = property(get_required_environment)
    health_records = property(get_health_records)

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
