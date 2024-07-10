from in_out import outer
from in_out import square
from in_out import pow

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())

a_third_one = outer(2, pow)
print(a_third_one())
print(a_third_one())
print(a_third_one())


def cube(x: int | float) -> int | float:
    """Returns the cube of x"""
    return (x * x * x)


again_another_counter = outer(4, cube)
print(again_another_counter())
print(again_another_counter())
print(again_another_counter())