#A custom login 
#Date: 9/11
#Developed by: Summer Anan



input("If you want to make an account, press ENTER: ")
print("Great lets get started:")
login = False
password = False
email = input("Enter your email: ")
signup_username = input("Enter your username: ")
sighnup_password = input("Enter your password: ")
confirm_password = input("Please confirm your password: ")
print("")
print("")
if sighnup_password == confirm_password:
  print("Great! Lets sign up to see if your password works.")
  login_username = input("Username Here: ")

  if login_username == signup_username:
    print("Great!")
    login = True
  elif login_username != signup_username:
    print("Wrong username!")
    login = False
  login_password = input("Password here: ")
  if login == True and login_password == sighnup_password:
    print("Logged In!!!")
    password == True
    
  elif sighnup_password != login_password:
    print("Wrong Password!")
elif sighnup_password != confirm_password:
  print("Wrong password")