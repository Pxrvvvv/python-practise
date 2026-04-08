import os

file = "names.txt"

if os.path.exists(file):
    print("File exists!")

# if os.path.isfile(file):
#     print("Thats a file!")
# elif os.path.isdir(file):
#     print("Thats a directory!")

else:
    print("File doesn't exists!")