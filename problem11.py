def Celsius_Fahrenheit(c):
    return (c * 9/5) + 32

def Fahrenheit_Celsius(f):
    return (f - 32) * 5/9

def Celsius_Kelvin(c):
    return c + 273.15


while True:
    print("1. celsius to fahrenheit")
    print("2. fahrenheit to celsius")
    print("3. celsius to kelvin")
    choice = input("Enter your choice : ")

    if choice == "quit":
        break

    temp = float(input("Enter the temperature : "))

    if choice == "1":
        print("your temperature in fahrenheit is : ", Celsius_Fahrenheit(temp))
    elif choice == "2":
        print("your temperature in celsius is : ", Fahrenheit_Celsius(temp))
    elif choice == "3":
        print("your temperature in kelvin is : ", Celsius_Kelvin(temp))
    else:
        print("Invalid choice")


    