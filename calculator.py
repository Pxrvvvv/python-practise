def calculator():
    while True:
        
        op = input("Enter the operator : ")

        if op == "quit":
            break

        n = int(input("Enter the first number : "))
        a = int(input("Enter the second number : "))
        

        total = int(n + a)
        difference = int(n - a)
        product = int(n * a)
        quotient = int(n / a)

        if op == "+":
            print("The sum is : ", total)
        elif op == "-":
            print("The difference is : ", difference)
        elif op == "*":
            print("The product is : ", product)
        elif op == "/":
            print("The quotient is : ", quotient)


calculator()