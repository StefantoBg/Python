'''file = open("spider.txt")
print("step 1 :")
print(file.readline())

print("step 2 :")
print(file.read())
file.close()'''
with open("spider.txt") as file:
    for line in file:
        print(line.upper())
print("\n\n\n Second \n\n\n")
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())