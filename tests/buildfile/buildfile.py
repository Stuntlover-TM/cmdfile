import os

def _load(filename="build"):
    with open(filename, "r") as buildfile:
        contents = buildfile.read().splitlines()
        commands = {}

        for line in contents:
            line = line.strip()

            if line.startswith("(") and line.endswith(")"):
                callname = line.replace("(", "").replace(")", "")
                commands[callname] = []
                continue
            try:
                commands[callname].append(line)
            except UnboundLocalError:
                raise UnboundLocalError("No table to run")
    
    return commands

def run(table, filename="build"):
    tables = _load(filename=filename)
    
    for cmd in tables[table]:
        os.system(cmd)