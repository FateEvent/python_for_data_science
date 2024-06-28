# Generate a Distribution Archive

I followed the official [pyPI](https://packaging.python.org/en/latest/tutorials/packaging-projects) documentation tutorial to package a library for Python.

After having installed the latest version of pyPI (preferably in a virtual environment):
```
python3 -m pip install --upgrade build
```

run this command from the same directory where pyproject.toml is located:
```
python3 -m build
```

Two files should have been generated in the `dist` directory:
```
dist/
├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
└── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
```

The `tar.gz` file is a source distribution whereas the `.whl` file is a built distribution.
A [source distribution](https://packaging.python.org/en/latest/glossary/#term-Source-Distribution-or-sdist) is a distribution format (usually generated using python -m build --sdist) providing metadata and the essential source files needed for installing by a tool like pip, or for generating a Built Distribution. It contains the [source files](https://www.geeksforgeeks.org/source-distribution-and-built-distribution-in-python) of module/script (.py files or .c/.cpp for binary modules), data files, etc. The result is an archive that can then be used to recompile everything on any platform like Linux, Windows, and Mac.
A [built distribution](https://packaging.python.org/en/latest/glossary/#term-Built-Distribution), on the contrary, is a distribution format containing files and metadata that only need to be moved to the correct location on the target system to be installed. It includes [files](https://www.geeksforgeeks.org/source-distribution-and-built-distribution-in-python) such as .pyc (Python bytecode), .so/.dll/.dylib for binary modules, data files… but no setup.py. The result is an archive that is specific to a platform (for example linux-x86_64) and to a version of Python that can be installed and then used directly by extracting it into the root of your filesystem.

We can then [install the library](https://stackoverflow.com/a/27909082) by typing:

```
pip3 install dist/ft_package-0.0.1-py3-none-any.whl
```