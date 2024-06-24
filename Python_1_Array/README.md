# Python - 1 - Array

### Image Manipulation

For module 2, I use the [Pillow](https://realpython.com/image-processing-with-the-python-pillow-library) library to load and manipulate images, and the [numpy](https://numpy.org/doc/stable/reference) library to manipulate tables.

To return an an array of RGB pixels, in the `ft_load()` function, I use `np.asarray()`, so that I can reconstruct the image from it in the zoom.py program by making use of the [`Image.fromarray()` function](https://stackoverflow.com/questions/62739851/convert-rgb-arrays-to-pil-image).

The [`.shape()`](https://note.nkmk.me/en/python-numpy-image-processing) method displays the dimensions and the number of colours, or channels (3 if the image is in the RGB format, for example).

`np.astype(np.uint8)` converts the floating-point mean values to unsigned 8-bit integers, which is a common format for image data.

I then use the method [`.convert("L")`](https://www.delftstack.com/fr/howto/python/convert-image-to-grayscale-python/#convertir-une-image-en-niveaux-de-gris-en-python-en-utilisant-la-m%C3%A9thode-imageconvert-de-la-biblioth%C3%A8que-pillow) to convert the image to [grayscale](https://stackoverflow.com/questions/3823752/display-image-as-grayscale) and show it with the matplotLib method [`.imshow()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html).

To rotate the image there are [various options](https://stackoverflow.com/questions/31401812/matplotlib-rotate-image-file-by-x-degrees) available, among which the [`.rotate()`](https://note.nkmk.me/en/python-pillow-flip-mirror) method from the ImageOps module of the Pillow library.

### The [RGB Colour Model](https://en.wikipedia.org/wiki/RGB_color_model)

To [invert the colours](https://stackoverflow.com/questions/47382482/inverting-pixels-of-an-rgb-image-in-python) of an image (i.e. obtaining its negative), I subtract the array of pixels from 255 (and not the opposite):

```python
def ft_invert(array: np.array) -> np.array:

    arr = 255 - array
    img = Image.fromarray(arr, "RGB")
```

For an explanation of the RGB colours, see this interesting and complete article on [geraldbakker.nl](https://www.geraldbakker.nl/psnumbers/rgb-explained.html).

To convert an image to grayscale by only using division I used the [`np.mean()`](https://mmuratarat.github.io/2020-05-13/rgb_to_grayscale_formulas#average-method) function to [__average the channels__](https://www.kdnuggets.com/2019/12/convert-rgb-image-grayscale.html).

In order to [generate single-colour images](https://note.nkmk.me/en/python-numpy-image-processing) for each RGB format primary colour, I set the other colour values to 0:

```python
def ft_red(array: np.array) -> np.array:

    red = array.copy()
    red[:, :, (1, 2)] = 0

    img = Image.fromarray(red, "RGB")
```
