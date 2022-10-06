#take input from the user and display if its positive, negative or zero
number = int(input("Enter a positive or negative number "))
if number == 0:
  print("This number is niether positive nor negative")
elif number < 0:
  print("It is a negative number")
elif number > 0:
  print("It is a positive number")