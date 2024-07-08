class calculator:
    """The Calculator class allows to perform operations between \
two vectors"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:

        try:
            sum = 0
            for e1, e2 in zip(V1, V2):
                sum += e1 * e2
            print(f'Dot product is: { sum }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:

        try:
            res = [e1 + e2 for e1, e2 in zip(V1, V2)]
            print(f'Vector addition is: { res }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')

    @staticmethod
    def sub_vec(V1: list[float], V2: list[float]) -> None:

        try:
            res = [e1 - e2 for e1, e2 in zip(V1, V2)]
            print(f'Vector subtraction is: { res }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')
