#A program that tells if it is a leap year or not with inout from the user 
#Date: 9/12
#Developed by: Summer Anan

year = int(input("What is your current year? : "))
if year % 4 == 0:
  print("There are 29 days in Febuary")
if year % 4 != 0:
  print("There are 28 days in febuary")