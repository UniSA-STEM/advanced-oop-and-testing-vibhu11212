'''
File: animal.py
Description: A brief description of this Python module.
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from health_record import HealthRecord

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base Class for all animals
    """
    def __init__(self, name, specie, age,
                 dietary_need , environment):
        self.name = name
        self.specie = specie
        self.age = age
        self.dietary_need = dietary_need
        self.required_environment = environment
        self.__health_records = []

    def get_name(self):
        return self.__name

    def get_specie(self):
        return self.__specie

    def get_age(self):
        return self.__age

    def get_dietary_need(self):
        return self.__dietary_need

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

    def set_dietary_need(self, dietary_need):
        if not isinstance(dietary_need, str):
            raise TypeError("Dietary needs must be a string")
        self.__dietary_need = dietary_need

    def set_specie(self, specie):
        if not isinstance(specie, str):
            raise TypeError("Species must be a string")
        self.__specie = specie

    def set_required_environment(self, environment):
        if not isinstance(environment, str):
            raise TypeError("Environment must be a string")
        self.__required_environment = environment

    name = property(get_name, set_name)
    specie = property(get_specie, set_specie)
    age = property(get_age, set_age)
    dietary_need = property(get_dietary_need, set_dietary_need)
    required_environment = property(get_required_environment,
                                    set_required_environment)
    health_records = property(get_health_records)

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        return f"{self.name} is eating {self.dietary_need}"

    def sleep(self):
        return f"{self.name} is sleeping"

    def add_health_record(self, record):
        if not isinstance(record, HealthRecord):
            raise TypeError("Must be a HealthRecord object")
        self.__health_records.append(record)

    def is_sick(self):
        for record in self.__health_records:
            if record.is_active:
                return True
        return False

class Mammal(Animal):
    """
    Represents a mammal, inheriting from Animal class
    """
    def __init__(self, name, specie, age,
                 dietary_need, environment):
        super().__init__(name, specie, age, dietary_need, environment)

    def make_sound(self):
        return "Roaring"


class Bird(Animal):
    """
    Represents a bird, inheriting from Animal class
    """
    def __init__(self, name, specie, age,
                 dietary_need, environment):
        super().__init__(name, specie, age, dietary_need, environment)

    def make_sound(self):
        return "Chirping"


class Reptile(Animal):
    """
    Represents a reptile, inheriting from Animal class
    """
    def __init__(self, name, specie, age,
                 dietary_need, environment):
        super().__init__(name, specie, age, dietary_need, environment)

    def make_sound(self):
        return "Hiss"