import re

x = None
links=[]
f = open("../spider.txt", "r+b")
line = f.read()
f.close()
string = "http://themes.googleusercontent.com/fonts/opensans/v6/k3k[6453]702ZOKiLJc3WVjuplzBa1RVmPjeKy21_GQJaLl"
# print(str(line))
x = str(line)
# match = string.replace("[^\w+]]", "")
match = re.search(r"[a-z]{,5}", string)
#     hatch.append(rem)
# teh = ",".join(match)
# raw = re.search("\.com\/", string)
# print(match.groups())
# def checkname(name):
#     result = re.search("^(\w*), (\w+)$", name)
#     if result is None:
#         return "Not correct"
#     return "{} {}".format(result[1], result[0 ])
def checkpId(name):
    result = re.search(r"\[(\d+)\]", name)
    if result is None:
        return "Not found PID"
    else:
        return result
# print(checkname("Siro, mashiq"))
print(checkpId(string))
def extract_pid(log_line):
    regex = r"(\d+)]\: ([A-Z]+)"
    result = re.sub(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result.group(1), result.group(2))

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
