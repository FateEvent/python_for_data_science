# Python 0

### Exercise 08: Loading

The `tqdm` function is what's called a [generator](https://www.geeksforgeeks.org/generators-in-python) function, a function that acts as an iterable since it returns a generator object that is iterable, i.e. can be used as an Iterator.
Instead of the `return` statement, a generator function uses the [`yield`](https://www.geeksforgeeks.org/python-yield-keyword) keyword. Similar to a `return` statement that terminates the execution of the function, the `yield` statement only pauses the execution of the function.

To create a progress bar, I took inspiration from [Build your own Command Line with ANSI escape codes](http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#ascii-progress-bar) from Haoyi's Programming Blog.
To format my output, I used the [`.format()`](https://docs.python.org/3.10/tutorial/inputoutput.html) method of the `string` object and put [`end=\r`](https://stackoverflow.com/questions/4897359/output-to-the-same-line-overwriting-previous-output) in my print statements to always print on the same line.

###### To go further:

I would have highly appreciated to have access to the [`get_terminal_size()`](https://www.geeksforgeeks.org/python-os-get_terminal_size-method) method to be able to calculate the width of my progress bar based on the width of the terminal.
