#Finding The amount of days in each month
#9/10/2022
#Made by Summer Anan

month = input("Enter the current month(e.g 'January'): ")
if month == "January" or month == "january":
  print("There are 31 days in January")
elif month == "Febuary" or month == "febuary":
  year = int(input("What is your current year? : "))
  if year % 4 == 0:
    print("There are 29 days in Febuary")
  if year % 4 != 0:
    print("There are 28 days in febuary")
elif month == "march" or month == "March":
  print("There are 31 days in march")
elif month == "April" or month == "april":
  print("There are 30 days in april")
elif month == "may" or month == "May":
  print("There are 31 days in May")
elif month == "June" or month == "june":
  print("There are 30 days in june")
elif month == "july" or month == "July":
  print("There are 31 days in july")
elif month == "August" or month == "august":
  print("There are 32 days in august")
elif month == "september" or month == "september":
  print("There are 30 days in september")
elif month == "October" or month == "october":
  print("There are 31 days in October")
elif month == "November" or month == "november":
  print("There are 30 days in November")
elif month == "december" or month == "December":
  print("There are 31 days in December")
else:
  print("Invalid Month, Enter current month in correct format and try again")