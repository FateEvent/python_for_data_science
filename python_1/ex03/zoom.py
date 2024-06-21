from PIL import Image
import numpy as np
from load_image import ft_load


def main():
    try:
        pixel_arr = ft_load("../img/animal.jpeg").astype(np.uint8)
        img = Image.fromarray(pixel_arr, "RGB")
        img = img.crop((455, 110, 850, 490))
        img.show()

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()
    return 0


if __name__ == "__main__":
    main()
