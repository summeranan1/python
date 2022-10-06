#Calculates a person's BMI
#Date: 9/12/2022
#Devolped: Summer Anan



weight = float(input("Enter your weight: "))
height = float(input("Enter your height (Meters): "))
bmi = weight / height
print(f"Your BMI is {weight/height}")
if bmi == 0.0:
  print("Invalid BMI")
elif bmi >= 25:
  print("You are too overweight")
elif bmi < 25 and bmi > 18.5:
  print("You are healthy!")
elif bmi < 18:
  print("Too Underweight")
