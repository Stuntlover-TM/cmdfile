import os

variables = {}

def _load(filename="build"):
    global variables

    with open(filename, "r") as buildfile:
        contents = buildfile.read().splitlines()
        commands = {}

        for line in contents:
            line = line.strip().split("#")[0]
            if line.startswith("#"):
                continue

            if line.startswith("(") and line.endswith(")"):
                callname = line.replace("(", "").replace(")", "")
                commands[callname] = []
                continue

            try:
                var = line.split(" = ")
                key = var[0]
                value = var[1]
                variables[key] = value
                is_variable = True
            except:
                is_variable = False

            try:
                commands[callname].append(line) if not is_variable else None
            except UnboundLocalError:
                raise UnboundLocalError("No table to run")
    
    return commands, variables

def run(table, filename="build"):
    tables, variables = _load(filename=filename)
    
    for cmd in tables[table]:
        if "{_" and "_}" in cmd:
            varcmd = variables[cmd.split("{_")[1].split("_}")[0]]
            rest = cmd.split("_}")[1]
            cmd = cmd.split("{_")[0] + varcmd + rest
        os.system(cmd)


def add_var(key, value):
    global variables
    variables[key] = value
