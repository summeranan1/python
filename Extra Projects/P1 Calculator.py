# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# This function solves expontential numbers
def exponent(x, y):
    return x ** y


print("Select operation.")
print("")
print("1.Add, 2.Subtract, 3.Multiply, 4.Divide, 5.Exponent")


while True:
    # take input from the user
    print("Enter choice add(1) sub(2) mul(3) div(4) exp(5):")
    choice = input("> ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        if choice == '5':
            base = int(input("Enter base number. > "))
            expontent_num = int(input("Enter the exponent. > "))
            print(base, "**", expontent_num, "=", exponent(base, expontent_num))

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, "=", add(num1, num2))


        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")