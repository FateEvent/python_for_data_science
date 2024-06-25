import sys
import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1:
            print('Please, choose a country.')
            chosen_country = sys.stdin.read()
        else:
            chosen_country = sys.argv[1]
        chosen_country = chosen_country.rstrip()

        df = load("../material/life_expectancy_years.csv")

        df_france = df[df["country"] == chosen_country]
        life_expectancy = df_france.values[0][1:]
        years = df.columns[1:]
        years = pd.to_numeric(years)

        plt.plot(years, life_expectancy)

        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.title("France Life Expectancy Projections")

        custom_ticks = list(range(1800, 2100, 40))
        plt.xticks(custom_ticks)

        plt.show()

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()

    return 0


if __name__ == "__main__":
    main()
