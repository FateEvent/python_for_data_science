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

In python it is possible to [return a function](https://www.geeksforgeeks.org/returning-a-function-from-a-function-python).
What's also asked in the exercise, it is to have a variable inside the `outer()` function storing and updating the original value every time the `inner()` function is called.