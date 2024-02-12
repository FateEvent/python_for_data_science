def ft_tqdm(lst: range) -> None:

    for i in lst:
        if i % 20 == 0:
            print(f'{round(i / len(lst) * 100)} %  Progress bar  {i}/{len(lst)}', end='\r')
        yield i
        if i == len(lst) - 1:
            print(f'{round(i / len(lst) * 100)} %  Progress bar  {i + 1}/{len(lst)}', end='\r')
