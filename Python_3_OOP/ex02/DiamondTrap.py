from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the king Joffrey Baratheon."""

    def __init__(self, first_name):
        """The __init__() method initialises an instantation \
of an instance of the king Joffrey Baratheon class"""

        super().__init__(first_name)

    # The @property decorator allows us to treat get_eyes as the attribute eyes
    # @property
    # def get_eyes(self):
    #     """A getter for the eyes attribute"""
    #     return self.eyes

    # @property
    # def get_hair(self):
    #     """A getter for the hair attribute"""
    #     return self.hair

    def get_eyes(self):
        """A getter for the eyes attribute"""
        return self.eyes

    def get_hair(self):
        """A getter for the hair attribute"""
        return self.hair

    def set_eyes(self, eye_colour):
        """A setter for the eyes attribute"""
        self.eyes = eye_colour

    def set_hair(self, hair_colour):
        """A setter for the hair attribute"""
        self.hair = hair_colour
