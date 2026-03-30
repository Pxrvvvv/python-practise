recharges = []

while True:
    n = input("Whats your recharge amount? ")

    if n == "done":
        break

    recharges.append(float(n))

print("Total recharge is : ", sum(recharges))
print("Number of recharges is : ", len(recharges))
print("Average recharge is : ", sum(recharges) / len(recharges))
