import sys

if len(sys.argv) != 3:
    print("Usage: python problem14.py <number1> <number2>")
else:
    unit = sys.argv[1]
    value = float(sys.argv[2])

if unit == "km":
    print(f"{value} km is equal to {value * 0.621371} miles")
elif unit == "kg":
    print(f"{value} kg is equal to {value * 2.20462} pounds")
elif unit == "cm":
    print(f"{value} cm is equal to {value * 0.393701} inches")
else:
    print("Invalid unit. Please use 'km', 'kg', or 'cm'.")