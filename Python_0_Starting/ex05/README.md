`append_cr.c` is a C program that may be used to test the `building.py` script with carriage returns.

To test, you need to compile it and run the executable with, as argument, the filename you want to append the carriage return to:
```
./a.out <FILENAME>
```

If the file does not exist, the program will create it.

You can then copy the file content as argument for `building.py` on the command line or in the provided prompt.