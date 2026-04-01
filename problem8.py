def attendance(attend):
    present = 0
    absent = 0
    

    for a in attend:
        if a == "p":
             present += 1
        elif a == "a":
             absent += 1

    percentage = present / 7 * 100

    print("present days are : ", present)
    print("absent days are : ", absent)
    print(f"Attendance percentage is : {percentage:.2f}%")

    if percentage >= 75:
        print("You are eligible to sit for the exam")
    else:
        print("You are not eligible to sit for the exam")

attend = []

for i in range(7):
    a = (input("Enter your attendance (p/a) : "))
    attend.append(a)

attendance(attend)
