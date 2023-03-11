# buildfile
Buildfile runs annoying tasks automatically. [PyPI Page here](https://pypi.org/project/buildfile/)

# Docs

## Installation

Run `python -m pip install buildfile` in your terminal.

## Usage

You can use buildfile as a command, or as a module.

Example for using as a command:
```
> python -m buildfile build
Hello
```
You can specify buildfile filename with the following: `python -m buildfile tablename filename`

This will run the `build` table of the build file, note that the build file must be in the directory you're running the script from, example build file:

```
(build)
echo Hello
```

---

`python -m buildfile build temp` is the equivalent of this:

```py
import buildfile

buildfile.run("build", filename="temp")
```

---

You can declare variables in the buildfile using:
```
(table)
variable = some text

echo {_variable_}
```
`some text`

You can also declare variables like this:
```py
import buildfile

buildfile.add_var("variable", "some text")
buildfile.run("table")
```

And then this will also output `some text`:
```
(table)
echo {_variable_}
```

---

# Changelog
## 1.1.0
- Add variables in buildfiles and `add_var()` function
