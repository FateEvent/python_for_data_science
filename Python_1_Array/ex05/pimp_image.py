from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def ft_invert(array: np.array) -> np.array:
    """The ft_invert() function inverts the color of the image \
received."""

    arr = 255 - array
    img = Image.fromarray(arr, "RGB")
    print(arr)
    img.show()

    return arr


def ft_red(array: np.array) -> np.array:
    """The ft_red() function converts the image to redscale."""

    red = array.copy()
    red[:, :, (1, 2)] = 0

    img = Image.fromarray(red, "RGB")
    print(red)
    img.show()

    return red


def ft_green(array: np.array) -> np.array:
    """The ft_green() function converts the image to greenscale."""

    green = array.copy()
    green[:, :, (0, 2)] = 0

    img = Image.fromarray(green, "RGB")
    print(green)
    img.show()

    return green


def ft_blue(array: np.array) -> np.array:
    """The ft_blue() function converts the image to bluescale."""

    blue = array.copy()
    blue[:, :, (0, 1)] = 0

    img = Image.fromarray(blue, "RGB")
    print(blue)
    img.show()

    return blue


def ft_grey(array: np.array) -> np.array:
    """The ft_grey() function converts the image to grayscale."""

    arr = np.mean(array, axis=2).astype(np.uint8)
    img = Image.fromarray(arr, "L")
    print(arr)
    img.show()

    return arr


def main():
    try:
        pixel_arr = ft_load("../img/animal.jpeg").astype(np.uint8)
        piggy = ft_invert(pixel_arr)

        img = Image.fromarray(piggy, "RGB").crop((455, 110, 850, 490))
        img = img.convert("L")
        print(np.asarray(img))
        img = img.rotate(180)
        print(f'New shape after Transpose: { np.shape(img) }')
        print(np.array(img))
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        plt.show()

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()
    return 0


if __name__ == "__main__":
    main()
