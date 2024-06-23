from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def main():
    try:
        pixel_arr = ft_load("../img/animal.jpeg").astype(np.uint8)
        img = Image.fromarray(pixel_arr, "RGB").crop((455, 110, 850, 490))
        img = img.convert("L")
        img = ImageOps.mirror(img)
        print(np.asarray(img))
        img = img.rotate(90)
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
