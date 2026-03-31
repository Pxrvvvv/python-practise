# try:
#     x = int(input("Whats your number? "))

# except ValueError:
#     print("x is not a number")

# else:
#     print(f"Your number is : {x}")


def main():
    x  = get_number()
    print(f"You number is : {x}")

def get_number():
    while True:
        try:
            x = int(input("Whats your number? "))
            return x
        except ValueError:
            pass
        
main()