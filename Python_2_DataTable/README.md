# Python - 2 - DataTable

### Table Manipulation

To [read a CSV](https://pythonbasics.org/read-csv-with-pandas) file as `pandas.DataFrame`, I need to use the Pandas function `read_csv()` or `read_table()`.

The difference between them is just the used delimiter. In fact, the same function is called by the source:

    read_csv() delimiter is a comma character
    read_table() is a delimiter of tab \t.

To obtain the shape of the DataFrame object we use the [`pandas.DataFrame.shape` attribute](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html).

