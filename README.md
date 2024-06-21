# python_for_data_science

Python for Data Science is a series of modules to learn Python

For module 2, I use the [Pillow](https://realpython.com/image-processing-with-the-python-pillow-library) library to load and manipulate images, and the [numpy](https://numpy.org/doc/stable/reference) library to manipulate tables.

To return an an array of RGB pixels, in the `ft_load()` function, I use `np.asarray()`, so that I can reconstruct the image from it in the zoom.py program by making use of the [`Image.fromarray()` function](https://stackoverflow.com/questions/62739851/convert-rgb-arrays-to-pil-image).