def ft_statistics(*args: any, **kwargs: any) -> None:
    """The program takes as parameters a quantity of unknown numbers \
and a series of commands and make the mean, median, quartile (25% and \
75%), standard deviation and variance according to the commands."""

    try:
        for k in kwargs:
            if kwargs[k] == "mean":
                sum = 0.0
                for entry in args:
                    sum += float(entry)

                print(f'mean: { round(sum / len(args), 2) }')

            if kwargs[k] == "median":
                sort = sorted(args)
                length = len(sort)
                mitm: int = 0
                index: int = int(length / 2)
                if length % 2 == 0:
                    index = index - 1
                    mitm = sort[index] + sort[index + 1]
                    mitm = round(mitm / 2, 2)
                else:
                    mitm = round(sort[index], 2)

                print(f'median: { mitm }')

            if kwargs[k] != "mean" and kwargs[k] != "median" \
                and kwargs[k] != "quartile" and kwargs[k] != "std" \
                    and kwargs[k] != "var":
                raise AssertionError("ERROR")
    except Exception as error:
        print(f'{error}')
