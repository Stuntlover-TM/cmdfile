# Changelog for 1.2.2 Bugfix
- Fixed cmdfile giving error when directly calling without args

# Changelog for 1.2.1 Bugfix
- Fixed filename by default being "cmd" and not "cmdfile"

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

# Changelog for 1.1.1
- Rename buildfile to cmdfile

# Changelog for 1.1.0
- Add variables in cmdfiles and `add_var()` function

# Changelog for 1.0.0
- Add support for changing cmdfile filename for cmdfile CLI

# Changelog for 0.0.1
- Initial Release
