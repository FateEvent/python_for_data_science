import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """The load() function loads a CSV file, prints the dimensions \
of the data set on the terminal and returns it."""

    try:
        if not os.path.isfile(path):
            raise AssertionError("invalid path")
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return

    try:
        df = pd.read_csv(path)

        print(f'Loading dataset of dimensions { df.shape }')
        return df
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        return


def main():
    try:
        print(load("../material/population_total.csv"))
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()

    try:
        print(load("../nonexisting.csv"))
    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()
    return 0


if __name__ == "__main__":
    main()
