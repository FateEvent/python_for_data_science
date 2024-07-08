# Python - 4 - DAD

To [access each value](https://stackoverflow.com/a/26660785) of the array of key-value pairs `kwargs`, I can loop through the `dict`ionary with the keys as follows:

```python
	for k in kwargs:
        print(k, kwargs[k])
```