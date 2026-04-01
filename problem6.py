def budget(expenses):
    overspent = 0

    for e in expenses:
        if e > 500:
            overspent +=1

    total = sum(expenses)
    average = total / 7

    print("total expenses are : ", total)
    print("average expenses are : ", average)
    print("number of days you overspent are : ", overspent)


expense = []

for i in range(7):
    e = int(input("Enter your expense : "))
    expense.append(e)

budget(expense)
