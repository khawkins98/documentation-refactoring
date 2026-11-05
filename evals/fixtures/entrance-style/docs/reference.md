# Maplet reference

Maplet needs Python 3 and no additional packages. Run it from the checkout root:

```sh
python3 maplet.py --text hello
```

`--text` is required. The program writes that text to standard output, adds a
newline and exits. It does not write files or contact a server. The Python
standard library's argparse module handles arguments and help.
