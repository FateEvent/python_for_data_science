def ft_mean(args: any) -> float:
    """ft_mean() computes the median of an array of numbers."""
    sum = 0.0
    for entry in args:
        sum += float(entry)

    return round(sum / len(args), 2)


def ft_median(args: any) -> float:
    """ft_median() computes the median of an array of numbers."""

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

    return mitm


def ft_quartiles(args: any) -> list[float]:
    """ft_quartiles() computes the first and third quartiles \
of an array of numbers."""
    median = ft_median(args)
    q1 = [entry for entry in sorted(args) if entry <= median]
    q3 = [entry for entry in sorted(args) if entry >= median]
    arr = [ft_median(q1), ft_median(q3)]
    return arr


def ft_variance(args: any) -> float:
    """ft_variance() computes the variance of an array \
of numbers."""
    mean = ft_mean(args)
    squared_dev = [pow(entry - mean, 2) for entry in sorted(args)]
    return ft_mean(squared_dev)


def ft_std(args: any) -> float:
    """ft_std() computes the standard deviation of an \
array of numbers."""

    var = ft_variance(args)
    return pow(var, 0.5)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """The program takes as parameters a quantity of unknown numbers \
and a series of commands and make the mean, median, quartile (25% and \
75%), standard deviation and variance according to the commands."""

    try:
        if len(args) <= 0 or len(args) <= 0:
            raise ValueError("ERROR")

        for k in kwargs:
            if kwargs[k] != "mean" and kwargs[k] != "median" \
                and kwargs[k] != "quartile" and kwargs[k] != "std" \
                    and kwargs[k] != "var":
                raise ValueError("ERROR")

            if kwargs[k] == "mean":
                mean = ft_mean(args)
                print(f'mean: { mean }')

            if kwargs[k] == "median":
                mitm = ft_median(args)
                print(f'median: { mitm }')

            if kwargs[k] == "quartile":
                quartiles = ft_quartiles(args)
                print(f'quartiles: { quartiles }')

            if kwargs[k] == "std":
                std = ft_std(args)
                print(f'std: { std }')

            if kwargs[k] == "var":
                var = ft_variance(args)
                print(f'var: { var }')

    except Exception as error:
        print(f'{error}')
