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

        str_name = str(self.name).lower()
        if str_name:
            str_name = str_name[0]
        self.login = str_name + str(self.surname)[:7].lower()
        self.id = generate_id()
