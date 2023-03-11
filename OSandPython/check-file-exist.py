import os
import sys

filename = sys.argv[1]   # second value command line

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created")
else:
    print("Error, the file {} already exist".format(filename))
    print("System exitcode", os.system("echo %ERRORLEVEL%"))
    sys.exit(1)


