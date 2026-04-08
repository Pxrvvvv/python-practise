# import json

# try:
#     with open("names.json", "r") as f:
#         content = json.load(f)
#         print(content["name"])
# except json.decoder.JSONDecodeError:
#     print("Error: The file 'names.txt' does not contain valid JSON data.")


import csv


with open("names.csv", "r") as f:
    content = csv.reader(f)
    for line in content:
        print(line)
        
