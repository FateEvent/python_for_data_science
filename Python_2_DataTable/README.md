# Python - 2 - DataTable

### Table Manipulation

To [read a CSV](https://pythonbasics.org/read-csv-with-pandas) file as `pandas.DataFrame`, I need to use the Pandas function `read_csv()` or `read_table()`.

The difference between them is just the used delimiter. In fact, the same function is called by the source:

    read_csv() delimiter is a comma character
    read_table() is a delimiter of tab \t.

To obtain the shape of the DataFrame object we use the [`pandas.DataFrame.shape` attribute](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html).

To obtain a [subset of data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html) I filter the dataset by country with the `==` operator:

```python
    df = load("../material/life_expectancy_years.csv")

    df_france = df[df["country"] == "France"]
```
And then I use the `.plot` method to create a visual chart with `matplotlib.pyplot`:

```
    life_expectancy = df_france.values[0][1:]
    years = df.columns[1:]
    years = pd.to_numeric(years)

    plt.plot(years, life_expectancy)
```
The axis labels are then set with `plt.xlabel()` and `plt.ylabel()` functions, and `plt.xticks()` is used to set the interval of 40 between the year values:

```
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("France Life Expectancy Projections")

    custom_ticks = list(range(1800, 2100, 40))
    plt.xticks(custom_ticks)
```

