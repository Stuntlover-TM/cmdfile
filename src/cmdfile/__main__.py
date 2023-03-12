import cmdfile
import sys

try:
    cmdfile.run(sys.argv[1], filename=sys.argv[2])
except:
    cmdfile.run(sys.argv[1])