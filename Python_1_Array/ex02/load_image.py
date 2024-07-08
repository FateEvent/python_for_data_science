import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """The ft_load() function loads an image, prints its format \
and its pixels content in RGB format."""

    try:
        if not os.path.isfile(path):
            raise AssertionError("invalid path")
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return

    try:
        with Image.open(path) as img:
            img.load()

        print(f'The shape of the image is: { np.shape(img) }')
        return np.asarray(img)
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return


def main():
    try:
        print(ft_load("../img/animal.jpeg"))
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()
    return 0


if __name__ == "__main__":
    main()
