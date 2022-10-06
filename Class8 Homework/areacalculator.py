
shape = input("Calculate are of which shape, square, rectangle, triangle, circle: ")
if shape == "square" or shape == "Square":
  side = int(input("Enter the length of one side: "))
  print(f"The area of your sqaure is {side * 4}")
if shape == "Triangle" or shape == "triangle":
  heightTriangle = int(input("Enter the height of the triangle: "))
  widthTriangle = int(input("Enter the width of the triangle: "))
  print(f"The area of your triangle is {(heightTriangle * widthTriangle) / 2}")
if shape == "circle" or shape == "Circle":
  radius = int(input("Enter the radius of the circle: "))
  print(f"The area of your circle is {(radius * radius) * 3.1415926535897}")
if shape == "square" or shape == "Square":
  length = int(input("Enter the length of the rectangle: "))
  width = input("Enter the width of the rectangle: ")
  print(f"The area of your rectangle is {length * width}")