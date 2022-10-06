#Small program to find area of a trapezoid
#Made by Summer Anan
#7/29/2022

print("((base 1 + base 2) / 2) * height is the formula for the area of trapiezum/trapezoid")

#Taking the values I need from the user
base1 = int(input("Value for base 1: "))
base2 = int(input("Value for base 2: "))
height = int(input("Value for height: "))

#Calculating...
parenthesis = base1 + base2
divide = parenthesis * 0.5
areaOfTrapezoid = divide * height

#showing the user the steps to solve
print(f"(({base1} + {base2}) / 2) * {height}")
print(f"> ({parenthesis} / 2) * {height}")
print(f"> {divide} * {height}")
print(f"> {areaOfTrapezoid}")

#Telling the user the end result
print(f"Area of Trapezoid is: {areaOfTrapezoid}!")
