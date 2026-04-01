def savings(saving_amount):
    above_5000 = 0

    for s in saving_amount:
        if s > 5000:
            above_5000 += 1

    total = sum(saving_amount)
    best_month = max(saving_amount)
    worst_month = min(saving_amount)

    print("total saving amount is : ", total)
    print("Best month : ", best_month)
    print("Worst month : ", worst_month)
    print("number of months you saved more than 5000 are : ", above_5000)
    


saving_amount = []

for i in range(12):
    s = int(input("Enter your saving for the month : "))
    saving_amount.append(s)

savings(saving_amount)
