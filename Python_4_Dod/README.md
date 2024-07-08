# Python - 4 - DAD

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

To [calculate the median](https://www.mathsisfun.com/median.html) of a series of numbers, you have to find either the number which is in the middle of the sorted series if the series is odd or the mean of the two numbers located in the middle if the series is even.

To [compute the quartile](https://en.wikipedia.org/wiki/Quartile)