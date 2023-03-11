# with open("first.txt", "a") as file:
#     file.write("2 This is my first time to save file with input from me! \n")
# file.close()
import csv

file = open("coma.csv")
csv_r= csv.reader(file)
n=0
for row in csv_r:
    name, phone, role = row
    n+=1
    print("{}. Name: {},--> Phone: {}, Position: {}".format(n, name, phone, role))


# print("\n\n {}".format(lines))


# 1. create script
#
# import os
# import datetime
#
#
# def file_date(filename):
#     # Create the file in the current directory
#     file = open("newfile.txt", "w")
#     file.write("Hello Bruther")
#     file.close()
#
#     timestamp = os.path.getmtime("newfile.txt")
#     # Convert the timestamp into a readable format, then into a string
#     conv = datetime.datetime.fromtimestamp(timestamp).isoformat()
#     # Return just the date portion
#     # Hint: how many characters are in “yyyy-mm-dd”?
#     return ("{}".format(conv[:10]))
#
#
# print(file_date("newfile.txt"))
# # Should be today's date in the format of yyyy-mm-dd