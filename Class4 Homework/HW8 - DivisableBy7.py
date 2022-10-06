#create a program to display if the number entered by the user is divisible by 7 or not
#take input from the user and display the integer result of when you divide it by 7
number = int(input("Enter any Number "))
integer_or_not = input("Would you like your number divided by 7 as an whole number (Yes) or not? (No) ")
if integer_or_not == "Yes" or "yes":
  if number % 7 == 0:
    print("Your number is divisible by 7")
    print(int(number / 7))
  elif number % 7 != 0:
    print("Your number is not divisible by 7")
    print(float(number / 7))