# Python - 4 - DAD

### Exercise 00

To [access each value](https://stackoverflow.com/a/26660785) of the array of key-value pairs `kwargs`, I can loop through the `dict`ionary with the keys as follows:

```python
    for k in kwargs:
        print(k, kwargs[k])
```

The star (`*`) is a sort of wrap for variadic arguments that bundles up the arguments that cannot be counted before the script is interpreted.
That's why you don't need the star anymore to pass the "bundle" as a parameter to another function once it has been "unbundled" in the primary function:

```Python
def ft_mean(args: any) -> None:
<SNIP>

def ft_statistics(*args: any, **kwargs: any) -> None:
<SNIP>
    if kwargs[k] == "mean":
        ft_mean(args)
<SNIP>
```

To [calculate the __median__](https://www.mathsisfun.com/median.html) of a series of numbers, you have to find either the number which is in the middle of the sorted series if the series contains an odd number of elements or the __mean__ of the two numbers located in the middle if the series has an even number of entries.

To [compute the first and third quartiles](https://en.wikipedia.org/wiki/Quartile) I implemented the __Turkey's hinges__ method, meaning I used the __median__ to divide the ordered data set into two halves and calculated the __median__ of each one of them.

[__Variance__](https://en.wikipedia.org/wiki/Variance) is the __expected value__ of the squared deviation from the __mean__ of a random variable. In fact, the [__standard deviation__](https://en.wikipedia.org/wiki/Standard_deviation) is obtained as the square root of the __variance__. __Variance__ is a measure of dispersion, meaning it is a measure of how far a set of numbers is spread out from their average value.

If we say that, in our case, the __expected value__ is given by the arithmetic __mean__, to obtain the __variance__ we calculate the deviations of each data point from the mean and square the result of each, before taking the mean of the squared deviations. To obtain the __standard deviation__ we then take the root square of the __variance__.

### Exercise 01

In the exercise it is asked to return an __inner function__ updating a variable contained in the __outer function__ every time it is called.

To do that, we have to increase the `count` variable every time the function is called, and this may be done in the __inner function__ thanks to the [`nonlocal` keyword](https://realpython.com/inner-functions-what-are-they-good-for/#modifying-the-closure-state) that allows us to access a variable stored in the __outer function__.

Without the `nonlocal` keyword, the only way to access it from the the __inner function__ is in the `return` statement.

### Exercise 02

This exercise introduces the concept of [wrappers](https://realpython.com/primer-on-python-decorators/#returning-values-from-decorated-functions) and asks us to create a wrapper limiting the number of possible calls to a functions.

When the number of calls gets over the limit, we are asked to print a message with the name and the location in memory of the function.
To do this, I used respectively the `__name__` attribute to obtain the function name and the `id()` function to get its memory location in decimal numbers (converted to hexadecimal with the `hex()` function) as follows:

```python
    print(f'Error: <function { function.__name__ } \
at { hex(id(function)) }> \
called too many times')
```
### Exercise 03

This exercise introduces [__data classes__](https://realpython.com/python-data-classes), a kind of class that simplifies the creation and management of the class.

In __data classes__, indicated by the use of the decorator `@dataclass`, the initialisation syntax is simplified in comparison to normal classes in Python, the `__init__` function being called under the hood.

The [`__post_init__` function](https://docs.python.org/3/library/dataclasses.html#post-init-processing), which is called after the `__init__` function, is used to [add attributes to a data class object after the initialization](https://stackoverflow.com/a/68440028). In addition, it allows the use of the `self` keyword allowing access to the constructor parameters. However, the `__repr__` attribute won't display the added attributes added in this way.

This is the trickiest part. And that's where the `field()` method becomes useful.

The [`field()`](https://docs.python.org/3/library/dataclasses.html#dataclasses.field) method is used, among other things, to initialise attributes with a default value.
For this, we will need the `default` keyword (or the `default_factory` keyword if we want to use a function to initialise ourr values):

```python
@dataclass
class Student:
    <SNIP>
    active: bool = field(default=True)
```
Another useful keyword is `init`. It allows developers to make initialisation impossible to users:

```python
@dataclass
class Student:
    <SNIP>
    login: str = field(init=False)
```
