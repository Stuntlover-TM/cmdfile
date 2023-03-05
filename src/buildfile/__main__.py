import buildfile
import sys

try:
    buildfile.run(sys.argv[1], filename=sys.argv[2])
except:
    buildfile.run(sys.argv[1])
