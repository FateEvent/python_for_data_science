from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()


@callLimit(-7)
def e():
    print("e()")


@callLimit(1)
def e_plus_plus():
    print(f'e() and zero division: { 3 / 0 }!')


e()
e_plus_plus()
