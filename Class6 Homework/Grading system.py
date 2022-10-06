#Finding the grade of a paper with a score
#9/10/2022
#Made by Summer Anan


print("**********************")
print("||||||||||||||||||||||")
print("GRADING     calculator")
print("||||||||||||||||||||||")
print("**********************")

grade = int(input("Enter the grade of your student: "))
# need to work on : if we enter string it throws error. 
if grade < 25 and grade >= 0:
  print("The grade of your student is F")
elif grade >= 25 and grade <= 45:
  print("You recieved a E")
elif grade >= 45 and grade <= 50:
  print("You recieved a D")
elif grade >= 50 and grade <= 60:
  print("You recieved a C")
elif grade >= 60 and grade <= 80:
  print("You recieved a B")
elif grade > 80 and grade <= 100:
  print("You recieved an A")
else:
  print("Invalid GRADE score")