def ft_tqdm(lst: range, home_made: bool = False) -> None:
    """
    ft_tqdm(lst: range, home_made: bool = False) --> None

    The `tqdm` function is what's called a generator function, a function
    that acts as an iterable since it returns a generator object that is
    iterable, i.e. can be used as an Iterator.

    The yield keyword pauses the execution of the function instead of
    just stopping it.

    PS By setting the home_made variable at True, the character used for
    the progress bar will be '#' instead of '█'.
    """

    if home_made:
        c = '#'
    else:
        c = '█'
    for i in lst:
        width = round(i / len(lst) * 100)
        if i % 20 == 0:
            print('{0:3d}% |'.format(width), end='')
            print('{}'.format(c * width + ' ' * (100 - width)), end='')
            print(f'| {i}/{len(lst)}', end='\r', flush=True)

        yield i

    print('{0:3d}% |'.format(width), end='')
    print('{}'.format(c * width + ' ' * (100 - width)), end='')
    print(f'| {i + 1}/{len(lst)}')
