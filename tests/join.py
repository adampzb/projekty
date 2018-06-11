locations = {"Q: You are sitting in front of a computer learning Python",
             "N: You are standing at the end of a road before a small brick building",
             "W: You are at the top of a hill",
             "E: You are inside a building, a well house for a small stream",
             "S: You are in a valley beside a stream",
             "N: You are in the forest"}


loc = 1
while True:
    avExits = list()
    print(list(locations.keys()))

    if loc == 0:
        print("u run away")
        break
    direc = input("availible exits are: " + avExits + ", where u want to go? ").upper()
    print()
    if direc in locations:
        loc = locations
    else:
        print("u can not go here")
