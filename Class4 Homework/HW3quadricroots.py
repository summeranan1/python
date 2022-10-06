#Program To find cube and square root of numbers
#8/8/2022
#Made by Summer Anan

#Asking the user for the values we need
number = int(input("Enter any number: "))
squared_or_cubed = input("Would you like it square root, or cube rooted? square(s)/cube(c) : ")

#Solving for if the user chooses "square rooted"
if squared_or_cubed == "square" or squared_or_cubed == "Square" or squared_or_cubed == "s":
  print(f"The formula for Square root is : {number}^(1/2)")
  print(f"Square root of {number} is : {number ** (1/2)}!")

#Solving for if the user picks "cube rooted"
if squared_or_cubed == "Cube" or squared_or_cubed == "cube" or squared_or_cubed == "c":
  print(f"The formula for Cube root is :{number}^(1/3)")
  print(f"Cube root of {number} is : {number ** (1/3)}!")
