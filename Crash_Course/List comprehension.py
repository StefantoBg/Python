multiples=[x*7 for x in range(1,11)]
# print(multiples)

lang= "Python Pearl Ruby C#".split()

lengths =[len(lans) for lans in lang]
length = "".join(str([x for x in lengths]))
print(length[::-1])
