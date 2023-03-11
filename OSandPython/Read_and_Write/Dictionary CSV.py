possible Creds[]<[]/[]a[]>[]<[]d[]i[]v[] []c[]l[]a[]s[]s[]=[]"[]c[]o[]n[]t[]a[]i[]n[]e[]r[]"[]>[][[]][]<[]/[]d[]i[]v[]>[]<[]/[]d[]i[]v[]>[]
possible Creds[]<[]/[]a[]>[]<[]d[]i[]v[] []c[]l[]a[]s[]s[]=[]"[]c[]o[]n[]t[]a[]i[]n[]e[]r[]"[]>[][[]][]<[]/[]d[]i[]v[]>[]<[]/[]d[]i[]v[]>[]

read_employees("employees.csv")

#  DictRead CSV files:
# with open("employees.csv") as team:
#     reader = csv.DictReader(team, delimeter="*" )
#
#     for row in reader:
#         print(row)
#         # print("{} {}".format(row["name"], row["ver"],row[""], row["num"]))
#
#  with open("employees.csv") as team:
#      reader = csv.DictReader(team, fieldnames=["name", "version", "ver", "num"])
#      for row in reader:
#          print(row)
#         # print("{} {}".format(row["name"], row["ver"]))

# DictWriter CSV file:
# users = [{'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},
#          {'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},{'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},
#          {'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},
#          {'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},{'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},
#          {'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},
#          {'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},{'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},
#          {'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},
#          {'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},{'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'},
#          {'name': 'Mailer', 'version': ' 3.4', 'ver': ' updated', 'num': ' 445'}]
#
# keys = ["name", "version", "ver", "num"]
# with open("newDictCsv.csv", "w") as team:
#     writer = csv.DictWriter(team, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(users)
# f = open("newDictCsv.csv")
# print(f.read())
# f.close()