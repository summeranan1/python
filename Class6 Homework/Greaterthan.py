#Finding the greatest of three numbers
#9/10/2022
#Made by Summer Anan

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your last number: "))
#find way to handle invalid number such and string value 
if a > b and a > c:
  print(f"The greatest among the three numbers is your first number, {a}")
if b > a and b > c:
  print(f"Your largest number among the three numbers is your second number, {b}")
if c > b and c > a:
  print(f"The largest number among the three numbers is your third number, {c}")