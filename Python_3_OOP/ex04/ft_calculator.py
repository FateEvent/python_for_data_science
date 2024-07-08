class calculator:
    """The Calculator class allows to perform elementary operations \
on a vector and operations between two vectors"""

    def __init__(self, slice):
        """The __init__() function initialises an instance of the \
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

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """The dotproduct() function computes the dot product \
between two vectors"""

        try:
            sum = 0
            for e1, e2 in zip(V1, V2):
                sum += e1 * e2
            print(f'Dot product is: { sum }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """The add_vec() function calculates the sum of two \
vectors"""

        try:
            res = [e1 + e2 for e1, e2 in zip(V1, V2)]
            print(f'Vector addition is: { res }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')

    @staticmethod
    def sub_vec(V1: list[float], V2: list[float]) -> None:
        """The sub_vec() function calculates the difference \
of two vectors"""

        try:
            res = [e1 - e2 for e1, e2 in zip(V1, V2)]
            print(f'Vector subtraction is: { res }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')
