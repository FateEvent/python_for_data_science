import numpy as np


def check_type(lst: list[int | float]):

    for el in lst:
        if not isinstance(el, float) and not isinstance(el, int):
            raise AssertionError("not every list element is a float or an int")


def check_errors(lst1: list[int | float], lst2: list[int | float]):

    if len(lst1) != len(lst2):
        raise AssertionError("the lists have not the same size")
    check_type(lst1)
    check_type(lst2)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:

    check_errors(height, weight)
    return [w / np.power(h, 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    check_type(bmi)
    return [True if el <= limit else False for el in bmi]


def main():
    try:
        print(apply_limit([5, 7, 87, "ff", 45, 33], 33))
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        exit()

    return 0


if __name__ == "__main__":
    main()
