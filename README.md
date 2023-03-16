# cmdfile
cmdfile runs annoying commands automatically.

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

(By default, if you simply run `python -m cmdfile`, it will run the `main` table of the `cmdfile` file)

This will run the `hello` table of the cmdfile, note that the cmdfile must be in the directory you're running the script from, example cmdfile:

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

### Variables

You can declare variables in the cmdfile using:
```
# You can declare variables outside of tables
# some_variable = "I'm not in any table!"

(table)
variable = "some text"

echo {{variable}}
```
`some text`

You can also declare variables through code like this:
```py
import cmdfile

cmdfile.add_var("variable", "some text")
cmdfile.run("table")
```

And then this will also output `some text`:
```
(table)
echo {{variable}}
```

---

### Changing the shell

You can change what shell to use by changing the `shell` variable:
```
shell = "powershell.exe -c"

[main]
echo 'Hello' # Executes "powershell.exe -c echo 'Hello'"
```

---

### Requirements

Requirements are tables that run before the main table, example:
```
[main] a_requirement another_requirement
# This will call a_requirement, another_requirement and main, respectively


[a_requirement]
# ...

[another_requirement]
# ...
```

---

# Changelog for 1.2.0
- Added "requirements", this calls other tables before running the current table, example:

```
[main] a_requirement another_requirement
# This will call a_requirement, another_requirement and main, respectively


[a_requirement]
# ...

[another_requirement]
# ...
```

- You can now select the shell to use to run commands like this:
```
shell = "powershell.exe -c"

[main]
echo 'Hello' # Executes "powershell.exe -c echo 'Hello'"
```

- Changed variable usage from `{_varname_}` to `{{varname}}`
