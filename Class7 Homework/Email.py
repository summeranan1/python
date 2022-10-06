
#Checks if the email the user entered is a valid email
#Date: 9/11
#Developed by: Summer Anan


email = input("Enter your email here: ")
if "@" in email and ".com" in email and len(email) >= 8:
  print("Valid Email!")
else:
  print("invalid email")