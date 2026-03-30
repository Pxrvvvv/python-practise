# students = ["Parv","Pushti","Het"]


# for i in range(len(students)):
#     print(i + 1, students[i])


# students = {
#     "Parv": 19,
#     "Pushti": 18,
#     "Het": 20
# }

# for student in students:
#     print(student, "is" ,students[student],"years old")


datas = [
    {"name":"Parv", "age": 19, "city": "Ahmedabad"},
    {"name":"Pushti", "age": 18, "city": "goa"},
    {"name":"Het", "age": 20, "city": "banglore"},
    {"name":"Pratham", "age": 19, "city": None}
]

for data in datas:
    print(data["name"],data["age"], data["city"], sep=", ")