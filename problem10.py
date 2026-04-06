def checker():
    
    while True:
        n = input("What's your email? ")

        if "@" in n and "." in n[n.index("@"):]:
            print("Your email is valid")
            break
    
        else:
            print("Your email is invalid")

    

checker()
