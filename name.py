import sys

# if len(sys.argv) < 2:
#     print("Too less arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, My name is", sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("Too less arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, My name is", sys.argv[1])