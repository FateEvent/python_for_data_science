def ft_statistics(*args: any, **kwargs: any) -> None:

    try:
        for k in kwargs:
            if kwargs[k] == "mean":
                sum = 0.0
                for entry in args:
                    sum += float(entry)

                print(f'mean: { sum / len(args) }')

            if kwargs[k] == "median":
                sort = sorted(args)
                len(sort)
                print(sort)
                for index, entry in enumerate(sort):
                    sum += float(entry)

                print(f'median: { sum / 2 }')

            if kwargs[k] != "mean" and kwargs[k] != "median" \
                and kwargs[k] != "quartile" and kwargs[k] != "std" \
                    and kwargs[k] != "var":
                raise AssertionError("ERROR")
    except Exception as error:
        print(f'{error}')
