password = "python123"
trial = 3

while trial > 0:
    n = input("What's the password? ")

    if n == password:
        print("Correct Password")
        break
    else:
        trial -= 1
        if  trial == 0:
            print("Account Locked")
        else:
            print(f"Wrong password, you have {trial} trials left")