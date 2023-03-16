import os
import subprocess

variables = {"shell": ""}

def _load(filename="cmdfile"):
    global variables

    with open(filename, "r") as cmdfile:
        contents = cmdfile.read().splitlines()
        get_output = False
        commands = {}
        requirements = {}

        for line in contents:
            line = line.strip().split("#")[0]
            if line.startswith("#"):
                continue

            if line.strip() == "":
                continue

            if line.startswith("["):
                reqs = line.replace("[", "").replace("]", "").split(" ")
                tablename = reqs[0]
                del reqs[0]
                commands[tablename] = []
                continue


            try:
                var = line.split(" = ")
                key = var[0]
                value = var[1]

                if value.startswith('output("') and value.rstrip().endswith('")'):
                    get_output = True
                    output = value.split('output("')[1].split('")')[0]
                    value = subprocess.check_output(variables["shell"] + f" {output}", shell=True, text=True)

                if not get_output:
                    value = value.split('"')[1].split('"')[0]


                variables[key] = value
                is_variable = True
            except:
                is_variable = False


            try:
                requirements[tablename] = reqs
                commands[tablename].append(line) if not is_variable else None
            except UnboundLocalError:
                continue
    
    return commands, variables, requirements


def _run(table, tables, variables, shell):
    for key, value in variables.items():
        if value.endswith("}}") and value.startswith("{{"):
            variables[key] = variables[value.replace("{{", "").replace("}}", "")]

    for cmd in tables[table]:
        if "{{" and "}}" in cmd:
            varcmd = variables[cmd.split("{{")[1].split("}}")[0]]
            rest = cmd.split("}}")[1]
            cmd = cmd.split("{{")[0] + varcmd + rest

        os.system(shell + f" {cmd}")


def run(table="main", filename="cmdfile"):
    tables, variables, requirements = _load(filename=filename)
    shell = variables["shell"]

    for req in requirements[table]:
        _run(req, tables, variables, shell)

    _run(table, tables, variables, shell)


def add_var(key, value):
    global variables
    variables[key] = value
