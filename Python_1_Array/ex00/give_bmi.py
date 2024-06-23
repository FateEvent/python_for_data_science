import numpy as np


def check_type(lst: list[int | float]):
    """check_type(lst: list[int | float])

The check_type() function takes a list of integers or floats in input
and checks whether the elements are of the proper type (i.e. int or
float)."""

    for el in lst:
        if not isinstance(el, float) and not isinstance(el, int):
            raise AssertionError("not every list element is a float or an int")


def check_errors(lst1: list[int | float], lst2: list[int | float]):
    """check_errors(lst1: list[int | float], lst2: list[int | float])

The check_errors() function takes 2 lists of integers or floats
in input and checks whether the two lists have the same size and if 
they contain the proper element type (i.e. int or float)."""

    if len(lst1) != len(lst2):
        raise AssertionError("the lists have not the same size")
    check_type(lst1)
    check_type(lst2)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]

The give_bmi() function takes 2 lists of integers or floats
in input and returns a list of BMI values."""

    try:
        check_errors(height, weight)
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return

    return [w / np.power(h, 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit(bmi: list[int | float], limit: int) -> list[bool]

The apply_limit() function takes a list of integers or floats in input
and a limit and returns False if each element is inferiour or equal to
the limit, and True otherwise."""

    try:
        check_type(bmi)
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return

    return [False if el <= limit else True for el in bmi]


def main():

    print(apply_limit([5, 7, 87, "ff", 45, 33], 33))

    try:
        check_type([5, 7, 87, "ff", 45, 33])
    except Exception as error:
        print(f'{type(error).__name__}: {error}')

    return 0


if __name__ == "__main__":
    main()
