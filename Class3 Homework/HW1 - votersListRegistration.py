#Program to take information from user for voter’s list registration (name, age, address,contact) and display itProgram to take integer and float as input and convert them to float and integer.
while True:
    print("_______________________________")
    print("*******************************")
    print("Welcome to voting registration!")
    print("*******************************")
    print("_______________________________")
    print("")
    print("I will be asking you a few questions for this.")
    name = input("So, what is your name? > ")
    print(f"Ok great {name}, got it!")
    year = int(input("Now I need the year you were born in. > "))
    age = 2022 - int(year)
    yearlefttovote = 18-age
    if age < 18:
        print(f"You can't vote, you need to wate another {yearlefttovote} more years!")
    if age >= 18:
        print("Congratulations! You are eligible to vote!")
        print(f"If you were born in {year}, then your age should be {age}.")
        print("")
        print("Who would you like to vote? \n\nDonald Trump (1) \n\nJoe Biden (2)?")
    voted = input("> ")
    print("")
    yes_no = input("Would you like to vote again? y/n > ")
    if yes_no == "n":
        break