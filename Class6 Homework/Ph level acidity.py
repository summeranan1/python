#Finding the PH level of a solution and the nature of the acid/base
#9/10/2022
#Made by Summer Anan

print("**********************")
print("||||||||||||||||||||||")
print("PH SOLUTION calculator")
print("||||||||||||||||||||||")
print("**********************")
print("a logarithmic scale, from 1 to 14, used to describe the acidity or alkalinity of a solution. Blood in the human body should be close to 7.4 on the pH scale. A pH level of less than 7 indicates an acidic solution while a pH greater than 7 indicates an alkaline solution. 7 is the pH level of distilled water.")
print("")
acid = int(input("Enter the PH level of your solution: "))
#find way to handle invalid number such and string value 

if acid >= 1 and acid <= 3:
  print("The nature of your acid is strong.")
elif acid >= 4 and acid <= 6:
  print("The nature of your acid is weak.")
elif acid == 7:
  print("The nature of your solution is neutral")
elif acid >= 8 and acid <= 11:
  print("The nature of your base is weak")
elif acid >= 12 and acid <= 14:
  print("The nature of your base is strong")
else:
  print("Invalid PH level")