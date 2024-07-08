class calculator:
    """The Calculator class allows to perform operations between \
two vectors"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """The dotproduct() function computes the dot product \
between two vectors"""

        try:
            sum = 0
            for e1, e2 in zip(V1, V2):
                sum += e1 * e2
            print(f'Dot product is: { sum }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """The add_vec() function calculates the sum of two \
vectors"""

        try:
            res = [e1 + e2 for e1, e2 in zip(V1, V2)]
            print(f'Vector addition is: { res }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')

    @staticmethod
    def sub_vec(V1: list[float], V2: list[float]) -> None:
        """The sub_vec() function calculates the difference \
of two vectors"""

        try:
            res = [e1 - e2 for e1, e2 in zip(V1, V2)]
            print(f'Vector subtraction is: { res }')
        except Exception as error:
            print(f'{type(error).__name__}: {error}')
