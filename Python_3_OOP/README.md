# Python - 3 - OOP

### Classes and Inheritance

I followed [this interesting article](https://www.pythontutorial.net/python-oop/python-abstract-class) on [pythonturotial.net](https://www.pythontutorial.net/python-oop) to learn about Python abstract classes.

There you may find explanations and examples of use of a lot of OOP principles and concepts related in general and applied to the Python programming language.

### `__str__()` and `__repr__()`

The [`__str__()`](https://www.pythontutorial.net/python-oop/python-__str__) method allows to create a string representation of an instance of a class, while the [`__repr__()`](https://www.pythontutorial.net/python-oop/python-__repr__) is tipically used to return a string that can be executed and yields the same value as the object. 

Conventionally, the two methods are attributed different purposes: the `__repr__()` method should return a detailed description for a programmer who needs to maintain and debug the code, whereas the `__str__()` method should return a simpler description with information for the user of the program.

### The `@classmethod` decorator

Among the [available class decorators](https://diveintopython.org/learn/classes/class-decorator) we find the `@classmethod` decorator, which is used to define a method that is bound to the class and not the instance of the class. It takes a `cls` parameter instead of `self`.

### Properties

To understand how to create getters and setters I followed the leads of [this article](https://www.pythontutorial.net/python-oop/python-property-decorator). It's important to pay attention to add underscore (`_`) to the attribute in order to distinguish it from the getter and setter methods, otherwise the function will recursively call itself.

```python
	def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self._is_alive = is_alive

	@property
    def is_alive(self):
        return self._is_alive
```
### Multiple Inheritance, and the Diamond Problem

In Python the [diamond problem](https://www.datacamp.com/tutorial/super-multiple-inheritance-diamond-problem) is automatically managed.

When a class derived from two or more classes that derive from a common ancestor is instantiated, every parent class `__init__()` method is called once, but the program doesn't wait for the others to stop before starting a new one.

Attributes with a same name will be overwritten.

To reiterate, the diamond problem can get complicated fast and lead to unexpected results. That's why Python avoids complicated designs.

### Operator Overloading

To [overload an operator](https://www.geeksforgeeks.org/operator-overloading-in-python)