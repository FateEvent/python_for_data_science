from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """The __init__() method initialises an instantation \
of an instance of the Baratheon family character class"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hair = 'dark'

    def die(self):
        """The die() method set is_alive to False"""
        self.is_alive = False

    def __str__(self):
        """The __str__ method returns a string representation \
of the class instance."""
        ret = f'Vector: ("{self.family_name}", '
        return ret + f'"{self.eyes}", "{self.hair}")'

    def __repr__(self):
        """The __repr__ method returns the string representation \
of the object."""
        ret = f'Vector: ("{self.family_name}", '
        return ret + f'"{self.eyes}", "{self.hair}")'


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """The __init__() method initialises an instantation \
of an instance of the Lannister family character class"""
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hair = 'light'

    def die(self):
        """The die() method set is_alive to False"""
        self.is_alive = False

    def __str__(self):
        """The __str__ method returns a string representation \
of the class instance."""
        ret = f'Vector: ("{self.family_name}", '
        return ret + f'"{self.eyes}", "{self.hair}")'

    def __repr__(self):
        """The __repr__ method returns the string representation \
of the object."""
        ret = f'Vector: ("{self.family_name}", '
        return ret + f'"{self.eyes}", "{self.hair}")'

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        """The create_lannister() method allows to create \
characters in a chain"""
        return Lannister(first_name, is_alive)
