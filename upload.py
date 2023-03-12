import src.buildfile as buildfile

buildfile.add_var("TOKEN", "token_here")
buildfile.run("upload", filename="upload")
