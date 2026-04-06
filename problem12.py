def bill(name, night_stayed, room_service_done):
    room_charge = 2000 * night_stayed

    if room_service_done == "y":
        service_charge = 500
    else:
        service_charge = 0

    total = room_charge + service_charge

    print("Name : ", name)
    print("Night stayed : ", night_stayed)
    print("Room charge : ", room_charge)
    print("room_service_charge : ", service_charge)
    print("total bill is : ", total)


name = input("What's your name? ")
night_stayed = int(input("How many nights did you stay? "))
room_service_done = input("Did you do room service? (y/n) ")

bill(name, night_stayed, room_service_done)