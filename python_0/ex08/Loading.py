def ft_tqdm(lst: range) -> None:

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
