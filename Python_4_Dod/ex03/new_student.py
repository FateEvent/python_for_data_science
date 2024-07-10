import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Representing a student in 42 school system"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Function called after call to __init__() under \
the hood"""

        self.login = self.name[0].lower() + self.surname[:7].lower()
        self.id = generate_id()
        print(self.__dict__)
