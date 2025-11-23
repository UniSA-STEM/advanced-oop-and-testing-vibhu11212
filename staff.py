'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
from health_record import HealthRecord
from abc import ABC, abstractmethod
from enclosure import Enclosure

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

    @abstractmethod
    def duty(self):
        pass

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

    def assign_enclosure(self, enclosure):
        if isinstance(enclosure, Enclosure):
            self.__assigned_enclosures.append(enclosure)

    def duty(self):
        for enclosure in self.assigned_enclosures:
            enclosure.clean()
            print(f"{self.name} cleaned {enclosure.enclosure_id}")

    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}")
        animal.eat()

    def clean_enclosure(self, enclosure):
        print(f"{self.name} is cleaning {enclosure.enclosure_id}")
        enclosure.clean()

class Veterinarian(Staff):
    """
    Represents a Veterinarian, inheriting from Staff
    """
    def __init__(self, name, staff_id):
        super().__init__(name, staff_id)

    def duty(self):
        print(f"{self.name} is ready for health checks")

    def health_check(self, animal):
        print(f"Checking {animal.name}")
        if animal.is_sick():
            print(f"{animal.name} is sick")
        else:
            print(f"{animal.name} is healthy")

    def create_health_record(self, animal, issue, severity, treatment_plan):
        record = HealthRecord(issue, severity, treatment_plan)
        animal.add_health_record(record)
        return record