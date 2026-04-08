# text = "I love Pizza and drinks!"

# output_data = "names.txt"

# with open(output_data, "a") as f:
#     f.write(text + "\n")
#     print(f"Text file '{output_data}' is created ")







# employees = ["Alice", "Bob", "Charlie", "David", "Eve"]

# output_data = "names.txt"

# try:
#     with open(output_data, "a") as f:
#         for employee in employees:
#             f.write(employee + "\n")
#         print(f"Text file '{output_data}' is created ")
# except FileExistsError:
#     print("That file already exists.")







# import json

# data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "job": "Software Engineer"
# }

# output_data = "names.json"

# try:
#     with open(output_data, "w") as f:
#         json.dump(data, f, indent=4)
#         print(f"JSON file '{output_data}' is created ")
# except FileExistsError:
#     print("That file already exists.")





import csv

names = [["Name", "Age", "City"],
        ["Parv", 25, "New York"],
        ["Pushti", 20, "Los Angeles"],
        ["kat", 22, "Chicago"]]

output_data = "names.csv"

with open(output_data, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(names)
    print(f"CSV File '{output_data}' is created ")
