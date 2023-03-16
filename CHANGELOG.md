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

# Changelog for 1.1.1
- Rename buildfile to cmdfile

# Changelog for 1.1.0
- Add variables in cmdfiles and `add_var()` function

# Changelog for 1.0.0
- Add support for changing cmdfile filename for cmdfile CLI

# Changelog for 0.0.1
- Initial Release
