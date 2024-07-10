def square(x: int | float) -> int | float:
    """square() squares a number"""

    return x**2


def pow(x: int | float) -> int | float:
    """pow() computes the exponentiation of a \
number raised to the power of itself"""

    return x**x


def outer(x: int | float, function) -> object:
    """ The outer() function takes as argument a number \
and a function, it returns an object that when called \
returns the result of the arguments calculation."""

    count = 0

    def inner() -> float:
        """Per me si va nella città dolente,
        per me si va nell'etterno dolore,
        per me si va tra la perduta gente."""

        nonlocal count

        count += 1
        i = count
        res = x
        while i > 0:
            res = function(res)
            i -= 1
        return res

    return inner
