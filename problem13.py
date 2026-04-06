balance = 10000
pin = 1234

def amount():
    while True:
        print("\nWelcome to the ATM")
        deposit = balance + deposit
        withdraw = balance - withdraw

        if withdraw > balance:
            print("You can't withdraw more than your balance")
            continue
        
        for i in range(3):
            p = int(input("Enter your pin : "))
            if p == pin:
                print("Pin is correct")
                break
            else:
                print("Pin is incorrect")

        d = int(input("Enter the amount you want to deposit : "))
        

        menu = input("Read your menu below : ")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        if menu == "1":
            print("Your balance is : ", balance)
        elif menu == "2":
            print("Your balance after deposit is : ", deposit)
        elif menu == "3":
            print("Your balance after withdraw is : ", withdraw)
        else:
            print("Thank you for using the ATM")
            break

amount()