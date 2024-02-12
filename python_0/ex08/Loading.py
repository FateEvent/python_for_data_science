def ft_tqdm(lst: range) -> None:
    """
    The `tqdm` function is what's called a generator function, a function
    that acts as an iterable since it returns a generator object that is
    iterable, i.e. can be used as an Iterator.

    The yield keyword pauses the execution of the function instead of
    just stopping it.
    """

    for i in lst:
        width = round(i / len(lst) * 100)
        if i % 20 == 0:
            print('{0:3d}% |'.format(width), end='')
            print('{}'.format("#" * width + " " * (100 - width)), end='')
            print(f'| {i}/{len(lst)}', end='\r', flush=True)

        yield i

    print('{0:3d}% |'.format(width), end='')
    print('{}'.format("#" * width + " " * (100 - width)), end='')
    print(f'| {i + 1}/{len(lst)}')
