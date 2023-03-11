# with open("first.txt", "a") as file:
#     file.write("2 This is my first time to save file with input from me! \n")
# file.close()
#
# file = open("first.txt")
# lines= file.readlines()
# file.close()
# print(lines)

# print("\n\n {}".format(lines))


# 1. create script
import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename , "w") as f:
    f.write(comments)
    f.close()
    import os
    filesize =os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

#2. Create directory and file in it

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
      os.mkdir(directory)
      print(directory)
  # Create the new file inside of the new directory
  os.chdir(directory)
  with open(filename, "w") as file:
        file.write("Hello")
        file.close()
     #   os.chdir("..")
  # Return the list of files in the new directory
  return os.listdir(os.getcwd()) # or os.listdir(directory) - but have to

print(new_directory("PythonPrograms", "script.py"))
import datetime

#3. Check last time modiefied time

def file_date(filename):
    # Create the file in the current directory
    file = open("newfile.txt", "w")
    file.write("Hello Brother")
    file.close()

    timestamp = os.path.getmtime("newfile.txt")
    # Convert the timestamp into a readable format, then into a string
    conv = datetime.datetime.fromtimestamp(timestamp).isoformat()
    # Return just the date portion
    # Hint: how many characters are in “yyyy-mm-dd”?
    return ("{}".format(conv[:10]))


print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd