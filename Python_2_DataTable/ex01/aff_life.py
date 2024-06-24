from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        df = load("../material/life_expectancy_years.csv")

        df.plot(x="France Life Expectancy Projections")

    except Exception as error:
        print(f'{type(error).__name__}: {error}')
        print()

    return 0


if __name__ == "__main__":
    main()
