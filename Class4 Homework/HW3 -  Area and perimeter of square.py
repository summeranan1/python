while True:
  area_peri = input("Would you like the area or perimeter of a square? area/perimeter > ")
  if area_peri == "perimeter" or area_peri == "Perimeter":
    side = int(input("Enter the length of one side: (Don't use ft, in, ect) > "))
    peri = side * 4
    print(side, "*", "4", "=", peri)
    print(f"Your answer is : {peri}!")
  if area_peri == "area" or area_peri == "Area":
    side2 = int(input("Enter one side of the square: (Don't use ft, in, ect) > "))
    area = side2 ** 2
    print(side2, "^", "2", area)
    print(f"Your answer is: {area}!")
  yn = input("Would you like to calculate again? yes/no > ")
  if yn == "yes" or yn == "Yes":
    continue
  elif yn == "no" or yn == "No":
    break
  else:
    print("Invalid Input")
    break