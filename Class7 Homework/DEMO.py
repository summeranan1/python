number = int(input("Enter a number: "))
root = number ** (1/2)
integer_root = int(root)
print(f"The square root of your number is {number ** (1/2)}")
if root == integer_root:
  print("The number is a perfect square")
else:
  print("Your number is not a perfect square")