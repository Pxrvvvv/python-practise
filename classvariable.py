class Student:

    year = 2027
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Parv", 20)
student2 = Student("Pushti", 19)
student3 = Student("Het", 21)
student4 = Student("Pratham", 22)
student5 = Student("Nidhis", 18)

print(f"My class has {Student.num_students} students and their names are stated below :- \n")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print(student5.name)
print("\n")