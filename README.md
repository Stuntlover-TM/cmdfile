# cmdfile
cmdfile runs annoying commands automatically. [PyPI Page here](https://pypi.org/project/cmdfile/)

# Docs

## Installation

Run `python -m pip install cmdfile` in your terminal.

## Usage

You can use cmdfile as a command, or as a module.

Example for using as a command:
```
> python -m cmdfile build
Hello
```
You can specify cmdfile filename with the following: `python -m cmdfile tablename filename`

This will run the `hello` table of the cmdfile, note that the build file must be in the directory you're running the script from, example cmdfile:

```
(hello)
echo Hello
```

---

`python -m cmdfile check temp` is the equivalent of this:

```py
import cmdfile

cmdfile.run("check", filename="temp")
```

---

You can declare variables in the cmdfile using:
```
(table)
variable = some text

echo {_variable_}
```
`some text`

You can also declare variables like this:
```py
import cmdfile

cmdfile.add_var("variable", "some text")
cmdfile.run("table")
```

And then this will also output `some text`:
```
(table)
echo {_variable_}
```

---

# Changelog
## 1.1.0
- Add variables in cmdfiles and `add_var()` function
