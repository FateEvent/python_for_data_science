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
##### Plot Multiple Lines

To [plot multiple lines](https://stackoverflow.com/a/40071258) I used the I didn't use the `.subplot()` method:

```python
    fig, ax = plt.subplots()

    ax.plot(years, france_pop, label="France")
    ax.plot(years, chosen_pop, label=chosen_country)
```

To [modify a column](https://stackoverflow.com/a/12605055) of the dataframe a create the function `convert()` and used it in a list comprehension structure:

```python
    def convert(value: str) -> float:

        if value.endswith('M'):
            return float(value[:-1]) * 1e6
        elif value.endswith('k'):
            return float(value[:-1]) * 1e3
        else:
            return float(value)

    <SNIP>

    france_pop = df_france.values[0][1:]
    france_pop = [convert(entry) for entry in france_pop]
```

And to display the modified Y axis I create a function `millions_formatter()` and used the [`FuncFormatter()` method](https://stackoverflow.com/a/40511626) from `matplotlib.ticker`:

```python
    def millions_formatter(x, pos):
        return f'{x / 1e6:.1f}M'

    <SNIP>

    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
```

And finally I set the [legend location](https://stackoverflow.com/questions/59791884/set-the-legend-location-of-a-pandas-plot) to the bottom right corner of the chart with the `.legend()` method:

```python
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    ax.legend(loc='lower right')
```

Another type of plot if [the scattered plot](https://matplotlib.org/stable/plot_types/index.html).

To realise a scattered plot, we use the `.scatter()` method instead of the `.plot()` method.
As this one, `scatter()` may take as parameters the x and y axes data.

To define the scale of the x axis I made use of the [`xscale()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html) of `matplotlib.pyplot`, with the [logarithmic option](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html).
