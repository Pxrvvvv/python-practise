def classify(numbers):
    positive = 0
    negative = 0
    zeroes = 0

    for n in numbers:
        if n > 0:
            positive +=1
        
        elif n < 0:
            negative +=1

        else:
            zeroes +=1

    print("positive numbers are : ", positive)
    print("Negative numbers are : ", negative)
    print("zeroes are : ", zeroes)

numbers = []

for i in range(10):
    n = int(input("Enter a number : "))
    numbers.append(n)

classify(numbers)