item_names = []
item_prices = []

while True:
    n = input("What's the item name? ")
    if n == "end":
        break
    j = input("What's the item price? ")

    
    item_names.append(n)
    item_prices.append(float(j))

print("Your total bill is : ", sum(item_prices)*1.18)