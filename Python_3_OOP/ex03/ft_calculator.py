class calculator:
    """The Calculator class allows to perform elementary
operations on a vector"""

    def __init__(self, slice):
        """The __init__() function initialises an instance of the
calculator class"""
        self.slice = slice

    def __add__(self, scalar) -> None:
        """The add() function allows us to overload the + operator"""

        print([el + scalar for el in self.slice])

    def __mul__(self, scalar) -> None:
        """The mul() function allows us to overload the * operator"""

        print([el * scalar for el in self.slice])

    def __sub__(self, scalar) -> None:
        """The sub() function allows us to overload the - operator"""

        print([el - scalar for el in self.slice])

    def __truediv__(self, scalar) -> None:
        """The truediv() function allows us to overload the / operator"""

        try:
            if scalar == 0:
                raise ZeroDivisionError("Division by zero is undefined")
            print([el / scalar for el in self.slice])
        except Exception as error:
            print(f'{type(error).__name__}: {error}')
