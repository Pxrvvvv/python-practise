correct_number = 42
attempts = 0

while True:
    n = int(input("Guess the number : "))
    attempts += 1

    if n == correct_number:
        print("You guess the correct number")
        print("The numbers of attempts are : ", attempts)
        break

    elif n > correct_number:
        print("Lower")
    
    else:
        print("Higher")