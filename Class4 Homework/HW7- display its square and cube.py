#take input from the user and display its square and cube
#take input from the user and display its square and cube
number = int(input("Enter any number: "))
squared_or_cubed = input("Would you like it squared or cubed? S/C: ")
squared = number ** 2
cubed = number ** 3
if squared_or_cubed == "S" or squared_or_cubed == "s":
  print(number,  " squared is : " , squared)
if squared_or_cubed == "C"or squared_or_cubed == "c":
  print(number ,  " cubed is : " , cubed)
  