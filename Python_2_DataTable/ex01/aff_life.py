import sys
import matplotlib.pyplot as plt

from load_csv import load


def main():
    """The program calls the load() function, loads the file \
life_expectancy_years.csv, and displays the country information of \
the country of your choice.
"""

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1:
            print('Please, choose a country.')
            chosen_country = sys.stdin.readline().strip()
        else:
            chosen_country = sys.argv[1].strip()

        df = load("../material/life_expectancy_years.csv")

        df_chosen_country = df[df["country"] == chosen_country]

        if df_chosen_country.empty:
            raise ValueError(f'Data for {chosen_country} is not available \
in the dataset')

        life_expectancy = df_chosen_country.values[0][1:]
        years = df.columns[1:].astype(int)

        plt.plot(years, life_expectancy)

        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.title(f'{ chosen_country } Life Expectancy Projections')

        custom_ticks = list(range(1800, 2100, 40))
        plt.xticks(custom_ticks)

        plt.show()

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()

    return 0


if __name__ == "__main__":
    main()
