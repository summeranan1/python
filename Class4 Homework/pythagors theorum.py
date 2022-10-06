#This is a computer solving big equattions
#Made by Summer Anan
#7/29/2022

print("The theorum I will solve is: (-b+(b^2-4ac)^1/2)/2a")
#taking all the values I need from the user

a = int(input("What should the value of 'a' be? : "))
b = int(input("What value should 'b' be? : "))
c = int(input("Great now what value should 'c' be? : "))

#calculating
end_value = (-b+(b**2-4*a*c)**1/2)/2 * a

#Telling the user the end result
print(f"Your answer is {end_value}!")