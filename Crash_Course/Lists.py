str = "I am the new programer!"
c= str.rstrip("!")
list = c.split(" ")
e ="!" in list

new_str = "".join(c)
print("IS there any special charachters in list?" , e)
print(str , "  is ", type(str))
print(list , " - without \"!\"", "  is ", type(list))
print(new_str, "  is ", type(new_str))

