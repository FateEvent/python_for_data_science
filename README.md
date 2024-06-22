# python_for_data_science

Python for Data Science is a series of modules to learn Python for data science.

For module 2, I use the [Pillow](https://realpython.com/image-processing-with-the-python-pillow-library) library to load and manipulate images, and the [numpy](https://numpy.org/doc/stable/reference) library to manipulate tables.

To return an an array of RGB pixels, in the `ft_load()` function, I use `np.asarray()`, so that I can reconstruct the image from it in the zoom.py program by making use of the [`Image.fromarray()` function](https://stackoverflow.com/questions/62739851/convert-rgb-arrays-to-pil-image).

I then use the method [`.convert("L")`](https://stackoverflow.com/questions/3823752/display-image-as-grayscale) to convert the image to grayscale and show it with the [matplotLib](https://matplotlib.org/stable) method [.imshow()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html).

To rotate the image there are [various options](https://stackoverflow.com/questions/31401812/matplotlib-rotate-image-file-by-x-degrees) available, among which the [`.rotate()`](https://note.nkmk.me/en/python-pillow-flip-mirror) method from the ImageOps module of the Pillow library.

To [invert the colours](https://stackoverflow.com/questions/47382482/inverting-pixels-of-an-rgb-image-in-python) of an image (i.e. obtaining its negative), I subtract the array of pixels from 255 (and not the opposite).

For an explanation of the RGB colours, see this interesting and complete article on [geraldbakker.nl](https://www.geraldbakker.nl/psnumbers/rgb-explained.html).

