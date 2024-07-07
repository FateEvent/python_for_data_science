from abc import ABC, abstractmethod


class Character(ABC):
    """The abstract Character class allows to instantiate \
a character"""

    def __init__(self, first_name, is_alive=True):
        """The __init__() method initialises an instantation \
of a character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """The die() method set is_alive to False"""
        self.is_alive = False


class Stark(Character):
    """The Start class is derived from the Character \
class"""

    def die(self):
        """The die() method set is_alive to False"""
        self.is_alive = False
