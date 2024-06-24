from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        df = load("../material/life_expectancy_years.csv")

        df_france = df[df["country"] == "France"]
        life_expectancy = df_france.values[0][1:]
        print(life_expectancy)
        years = df.columns[1:]
        print(years)
        df_france.plot()

        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        # plt.show()

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()

    return 0


if __name__ == "__main__":
    main()
