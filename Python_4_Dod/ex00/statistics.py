def ft_statistics(*args: any, **kwargs: any) -> None:

    try:
        print(args)
        for k in kwargs:
            if kwargs[k] != "mean" and kwargs[k] != "median" \
                    and kwargs[k] != "quartile":
                raise AssertionError("ERROR")
    except Exception as error:
        print(f'{error}')
