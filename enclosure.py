'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
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

    enclosure_id = property(get_enclosure_id)
    size = property(get_size)
    environmental_type = property(get_environmental_type)
    is_clean = property(get_is_clean, set_is_clean)
    animals_housed = property(get_animals_housed)
    allowed_species = property(get_allowed_species)