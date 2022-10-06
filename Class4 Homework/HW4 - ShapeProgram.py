# create a triangle, rectangle, square, straight line and a slanting line using /,\,|,_
# HW6 - ShapeProgram

# Tested and Completed by Summer ANan
while True:
    print("Which shape would you like to pick?")
    print("")
    print("1. Square")
    print("")
    print("2. Triangle")
    print("")
    print("3. Line")
    print("")
    print("4. Rectangle")
    print("")
    print("Choose 1/2/3/4")
    print("")
    shape = int(input("> "))
    if shape == 1:
        print(" ___________________ \n|                   | \n|                   |\n|                   | \n|                   | \n|                   | \n|                   | \n|                   |\n|                   |\n|                   |\n|___________________|\n")
        print("")
        print("This is a SQUARE")
    if shape == 2:
        print("               /\              \n              /  \            \n             /    \           \n            /      \          \n           /        \        \n          /          \        \n         /            \      \n        /              \      \n       /                \     \n      /__________________\    ")
        print("")
        print("This is a TRIANGLE")
    if shape == 3:
        print("           |\n           |\n           |\n           |\n           |\n           |")
        print("")
        print("This is a LINE")
    if shape == 4:
        print(" ______________________________\n|                              |\n|                              |\n|                              |\n|                              |\n|                              |\n|                              |\n|                              |\n|                              |\n|______________________________|")
        print("This is a RECTANGLE")
    yn = input("Would you like to play again? y/n > ")
    if yn == "n":
        break

