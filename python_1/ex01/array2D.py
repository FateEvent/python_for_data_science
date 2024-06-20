import numpy as np


def check_type(family: list):
    """check_type(family: list)

The check_type() function takes a list in input and checks whether
its type is list."""

    if not isinstance(family, list):
        raise AssertionError("list isn't a list")


def check_indexes(length: int, start: int, end: int):
    """check_indexes(length: int, start: int, end: int)

The check_indexes() function takes the list lenght and the start
end end indexes and check whether at least one of the indexes
is out of bounds."""

    if start >= length or end >= length:
        raise AssertionError("start or end index out of bounds")
    
    if start == end:
        raise AssertionError("start and end indexes are equal")

    if start >= 0 and end >= 0 and start > end:
        raise AssertionError("start is greater than end")

    if start < 0 and end < 0 and start > end:
        raise AssertionError("start is greater than end")

    if start < 0 and np.abs(start) > length:
        raise AssertionError("start index out of bounds")

    if end < 0 and np.abs(end) > length:
        raise AssertionError("end index out of bounds")


def slice_me(family: list, start: int, end: int) -> list:
    """slice_me(family: list, start: int, end: int) -> list

The slice_me() function takes a list of element and returns
its array slice from the value at the start index until the
value at the end index."""

    try:
        check_type(family)
        check_indexes(len(family), start, end)
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()
        return

    old_shape = np.shape(family)
    sliced = family[start:end]
    new_shape = np.shape(sliced)
    print(f'My shape is : {old_shape}')
    print(f'My new shape is : {new_shape}')
    print()
    return sliced


def main():
    try:
        unit = np.array([])
        print(slice_me(unit, 0, 0))
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()
    return 0


if __name__ == "__main__":
    main()
