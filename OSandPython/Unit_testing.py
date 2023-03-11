import re
import sys

def rearange(name):
    result = re.search(r"^([\w.]*), ([\w .]*)$", name)
    if result is None:
        return name
    elif "." in result[2]:
        return "{} {}".format(result[2], result[1])
    return "{}, {}".format(result[2], result[1])


#!/usr/bin/env python3
import sys
import subprocess

f = open(sys.argv[1],"r")

for line in f.readlines():
  old_name=line.strip()
  new_name = old_name.replace("jane", "jdoe")
  subprocess.run(["mv", old_name, new_name])
f.close()
