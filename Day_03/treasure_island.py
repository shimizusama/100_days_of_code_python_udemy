print("Welcome to Treasure Island\nYour Mission is to find the treasure")

decision = input("You're at a cross road. Where do you want to go?\nType 'left or 'right\n'")

# print(type(decision))

if decision == "left":
    decision = input("Swin or wait?\n")
    if decision == "wait":
        decision = input("Which door?")
        if decision == "yellow":
            print("You Win!")
        elif decision == "red":
            print("Burned by fire\nGame Over")
        elif decision == "blue":
            print("eaten by beasts\nGame Over")
    else:
        print("Attacked by a trout.\nGame Over")
else:
    print("Fall into a hole\nGame Over")
