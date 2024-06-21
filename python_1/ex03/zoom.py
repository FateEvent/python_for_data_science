from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from load_image import ft_load


def main():
    try:
        pixel_arr = ft_load("../img/animal.jpeg").astype(np.uint8)
        print(pixel_arr)
        img = Image.fromarray(pixel_arr, "RGB")
        img = img.crop((455, 110, 850, 490)).convert("L")
        # img.show()
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        plt.show()
        print(f'New shape after slicing: { np.shape(img) } \
              or { np.size(img) }')
        print(np.asarray(img))

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()
    return 0


if __name__ == "__main__":
    main()
