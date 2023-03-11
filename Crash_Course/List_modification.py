str1="WHere is my pants?"
str2="Zebra Monkey Lion Zia Mia Kia Pantera Orangutan"

list1 = str2.split()
chars = 0
for name in list1:
    chars = chars + len(name)

print("Total characters : {}, Average length: {} ".format(chars, chars/len(list1)))

for index , name in enumerate(list1):
    print(index+1," - ", name)

# for index , name in enumerate(list1,start=1):
#     print(index," - ", name)