def square(x: int | float) -> int | float:
    """square() computes the square root of a number"""

    return x**2


def pow(x: int | float) -> int | float:
    """pow() computes the exponentiation of a \
number raised to the power of 2"""

    return x**x


def outer(x: int | float, function) -> object:
    """ The outer() function takes as argument a number \
and a function, it returns an object that when called \
returns the result of the arguments calculation."""
    count = x

    def inner() -> float:
        """Per me si va nella città dolente,
        per me si va nell'etterno dolore,
        per me si va tra la perduta gente."""

        return function(count)

    return inner
