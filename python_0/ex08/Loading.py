def ft_tqdm(lst: range) -> None:

    for i in lst:
        if i % 20 == 0 or i == len(lst) - 1:
            print(f'{round(i / len(lst) * 100)} %')
        yield i
