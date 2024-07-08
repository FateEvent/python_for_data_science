import sys
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """The program calls the load() function, loads the file \
income_per_person_gdppercapita_ppp_inflation_adjusted.csv, and \
displays the projection of life expectancy in relation to the \
gross national product of the year of your choice for each country."""

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) == 1:
            print('Please, choose a year.')
            chosen_year = sys.stdin.readline().strip()
        else:
            chosen_year = sys.argv[1].strip()

        prefix = "../material/"
        path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"

        df_income = load(prefix + path)
        df_life = load("../material/life_expectancy_years.csv")

        df_income = df_income[chosen_year]
        df_life = df_life[chosen_year]

        if df_income.empty:
            raise ValueError(f'The year { chosen_year } is not present in \
the dataset.')
        if df_life.empty:
            raise ValueError(f'The year { chosen_year } is not present in \
the dataset.')

        print(df_income)
        print(df_life)

        plt.scatter(df_income, df_life)

        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")

        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

        plt.show()

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()

    return 0


if __name__ == "__main__":
    main()
