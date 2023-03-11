import buildfile

buildfile.add_var("python_code", "print('Hello')")
buildfile.run("test", filename="test")