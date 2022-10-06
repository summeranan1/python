#display age and find out eligablility to vote###################
#Developed by Summer Anan #######################################
#Date : July 24 2022 ############################################

import datetime

def get_currentYear():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    currentyear = date.strftime("%Y")
    return int(currentyear)


vote = input("Hello would you like to vote?- ")
if vote == "Yes" or vote == "yes":
    year = input("Great! Can I have your birth year? --> ")
    age = get_currentYear() - int(year)
    print(f"You are {age} years old")
    yearlefttovote = 18-age
    if age >= 18:
        print("Congratulations! You are eligible to vote!")
    else:
        print(f"Sorry, but you have to be 18 to vote, need to wait another {yearlefttovote} year(s) to vote")
if vote == "No" or vote == "no":
    print("Ok sorry!")
    

