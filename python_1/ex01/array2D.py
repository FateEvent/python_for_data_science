import numpy as np


def check_indexes(family: list, start: int, end: int):

    if start >= len(family) or end >= len(family):
        raise AssertionError("start or end index out of bounds")


def slice_me(family: list, start: int, end: int) -> list:
    """slice_me(family: list, start: int, end: int) -> list

The slice_me() function takes a list of element and returns
an slice of it from the value at the start index until the
value at the end index."""

    try:
        check_indexes(family, start, end)
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return

    return family[start:end]


def main():
    try:
        unit = np.array([])
        print(slice_me(unit, 0, 0))
    except Exception as error:
        print(f'{type(error).__name__}: {error}')

    return 0


if __name__ == "__main__":
    main()
