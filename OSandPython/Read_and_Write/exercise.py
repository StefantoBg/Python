import os
import csv
Хората, подвластни на такава политическа система, поради постоянното ѝ настойничество, стават духовно осакатени и икономически обременени – защитават интереси, противни на собствената им природа.

духът деградира заради неправдата и се принизява до икономически цели.
Аналогично има социални реформатори и социални революционери, които са слепи за психологията и биха искали да формират социалния организъм по калъпа на някой икономически синдикат,
Такива агитатори нямат представа за слепотата си.
with open("coma.csv", 'w') as f:

    csvf = csv.reader(f)

    for row in csvf:
         one, two, three = row

         print(" Name: {},--> Phone: {}, Position: {}".format(pow[one], row[two], three))

# with open("first.txt", "a") as file:
#     file.write("2 This is my first time to save file with input from me! \n")
# file.close()

# READING CSV FILES
# import csv
#
# file = open("coma.csv")
# csv_r= csv.reader(file)
# n=0
# for row in csv_r:
#     name, phone, role = row   # rows are final after selecting columns for each csv
#     n+=1
#     print("{}. Name: {},--> Phone: {}, Position: {}".format(n, name, phone, role))
# file.close()

# Generating CSV files
# import csv
# hosts = [["sation.com", "156.432.34.54"], ["barsation.com", "136.32.224.254"], ["sansedsn.com", "153.442.44.11"]]
#
# with open("hosts.csv", "w") as host_csv:
#     writer = csv.writer(host_csv)
#     writer.writerows(hosts)
#     host_csv.close()
# file = open("hosts.csv")
# print(file.read())

# Reading  CSV files with Dictionaries   csv.DictReader()

import os
import csv

# Create a file with data in it
# def create_file(filename):
#     with open(filename, "w") as file:
#         file.write("name,color,type\n")
#         file.write("carnation,pink,annual\n")
#         file.write("daffodil,yellow,perennial\n")
#         file.write("iris,blue,perennial\n")
#         file.write("poinsettia,red,perennial\n")
#         file.write("sunflower,yellow,annual\n")
#         file.close()
#
#
# # Read the file contents and format the information about each row
# def contents_of_file(filename):
#     return_string = ""
#
#     # Call the function to create the file
#     create_file(filename)
#
#     # Open the file
#     with open(filename, "w") as csv_dict:
#         # Read the rows of the file into a dictionary
#         reader = csv.DictReader(csv_dict)
#
#         # Process each item of the dictionary
#         for row in reader:
#             return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
#
#     return return_string
#
#
# # Call the function
# print(contents_of_file("employees.csv"))
#
#


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
