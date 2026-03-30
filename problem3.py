marks = []

for i in range(5):
    n = int(input("Enter marks - "))
    marks.append(n)

total = sum(marks)
print("total marks is : ", total)
percentage = total / 500 * 100
print(f"percentage is : {percentage:.2f}%")

if percentage >= 75:
    print("Grade A")
elif percentage >=60:
    print("Grade B")
elif percentage >= 45:
    print("Grade C")
else:
    print("Fail")