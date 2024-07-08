import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from load_csv import load


def millions_formatter(x, pos):
    """The millions_formatter() function creates a million formatting \
for the y axis ticks."""

    return f'{x / 1e6:.1f}M'


def convert(value: str) -> float:
    """The convert() function convert to float the dataframe values."""

    if value.endswith('M'):
        return float(value[:-1]) * 1e6
    elif value.endswith('k'):
        return float(value[:-1]) * 1e3
    else:
        return float(value)


def main():
    """The program calls the load() function, loads the file \
population_total.csv, and displays the country information of your \
campus and that of the campus of your choice.
"""

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1:
            print('Please, choose a second country to compare France with.')
            chosen_country = sys.stdin.readline().strip()
        else:
            chosen_country = sys.argv[1].strip()

        df = load("../material/population_total.csv")

        df_france = df[df["country"] == "France"]
        df_chosen_country = df[df["country"] == chosen_country]

        if df_france.empty:
            raise ValueError("Data for France is not available in the dataset")
        if df_chosen_country.empty:
            raise ValueError(f"Data for {chosen_country} is not available \
                             in the dataset")

        france_pop = df_france.values[0][1:]
        france_pop = [convert(entry) for entry in france_pop]

        chosen_pop = df_chosen_country.values[0][1:]
        chosen_pop = [convert(entry) for entry in chosen_pop]

        years = df.columns[1:].astype(int).values

        fig, ax = plt.subplots()

        ax.plot(years, france_pop, label="France")
        ax.plot(years, chosen_pop, label=chosen_country)

        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.legend(loc='lower right')

        year_ticks = list(range(1800, 2051, 40))
        plt.xticks(year_ticks)
        plt.xlim(right=2050)

        ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

        pop_ticks = list(range(0, 70000000, 20000000))
        plt.yticks(pop_ticks)
        plt.ylim(top=70000000)

        plt.title("Population Projections")

        plt.show()

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()

    return 0


if __name__ == "__main__":
    main()
