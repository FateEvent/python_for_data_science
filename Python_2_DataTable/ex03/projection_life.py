import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from ft_package import load


def main():
    """The program calls the load() function, loads the file
income_per_person_gdppercapita_ppp_inflation_adjusted.csv, and
displays the projection of life expectancy in relation to the
gross national product of the year of your choice for each country.
"""

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1:
            print('Please, choose a second country to compare France with.')
            chosen_year = sys.stdin.readline().strip()
        else:
            chosen_year = sys.argv[1].strip()

        prefix = "../material/"
        path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"

        df_income = load(prefix + path)
        df_life = load("../material/life_expectancy_years.csv")

        life_expectancy = df_life.columns[1:].astype(int).values

        print(life_expectancy)
        print(life_expectancy)

        # ax.plot(years, france_pop, label="France")

        # ax.set_xlabel("Gross Domestic Product")
        # ax.set_ylabel("Life Expectancy")

        # year_ticks = list(range(1800, 2051, 40))
        # plt.xticks(year_ticks)
        # plt.xlim(right=2050)

        # ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

        # pop_ticks = list(range(0, 70000000, 20000000))
        # plt.yticks(pop_ticks)
        # plt.ylim(top=70000000)

        # plt.title("Population Projections")

        # plt.show()

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()

    return 0


if __name__ == "__main__":
    main()
