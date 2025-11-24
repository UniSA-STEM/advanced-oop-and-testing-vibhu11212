'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    """
    Represents an enclosure and the animals in it
    """

    def __init__(self, enclosure_id, size, environmental_type):
        self.__enclosure_id = enclosure_id
        self.__size = size # sq meter
        self.__environmental_type = environmental_type
        self.is_clean = True
        self.__animals_housing = []
        self.__allowed_species = None

    def get_enclosure_id(self):
        return self.__enclosure_id

    def get_size(self):
        return self.__size

    def get_environmental_type(self):
        return self.__environmental_type

    def get_is_clean(self):
        return self.__is_clean

    def get_animals_housed(self):
        return self.__animals_housed

    def get_allowed_species(self):
        return self.__allowed_species

    def set_is_clean(self, is_clean):
        if not isinstance(is_clean, bool):
            raise TypeError("It must be a boolean (True/False).")
        self.__is_clean = is_clean

    def set_size(self, size):
        if not isinstance(size, float):
            raise TypeError("Size must be a float")
        self.__size = size

    def set_environmental_type(self, environmental_type):
        if not isinstance(environmental_type, str):
            raise TypeError("Environmental type must be a string")
        self.__environmental_type = environmental_type

    enclosure_id = property(get_enclosure_id)
    size = property(get_size, set_size)
    environmental_type = property(get_environmental_type, set_environmental_type)
    is_clean = property(get_is_clean, set_is_clean)
    animals_housed = property(get_animals_housed)
    allowed_species = property(get_allowed_species)

    def clean(self):
        """Sets the enclosure's clean status to True."""
        self.is_clean = True

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Must be an Animal object")

        if animal.is_sick():
            raise Exception(f"Cannot add {animal.name}: Animal is sick")

        if animal.required_environment != self.environmental_type:
            raise Exception(
                f"Environment doesnt match Required:"
                f" {animal.required_environment}")

        if self.allowed_species is None:
            self.__allowed_specie = animal.specie
        elif animal.specie != self.allowed_species:
            raise Exception(
                f"Species doesnt match Enclosure restricted to:{self.allowed_species}")
        self.__animals_housing.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals_housed:
            self.__animals_housing.remove(animal)
            if not self.animals_housed:
                self.__allowed_specie = None
        else:
            raise ValueError("Animal not found in this enclosure")