dollar500 = 0
dollar100 = 0
dollar50 = 0
dollar20 = 0
dollar10 = 0
dollar5 = 0
dollar2 = 0
dollar1 = 0
while True:
    print("Enter how much 500 dollar bills you have")
    bill500 = int(input("> "))
    print("Enter how much 100 dollar bills you have")
    bill100 = int(input("> "))
    print("Enter how much 50 dollar bill you have")
    bill50 = int(input("> "))
    print("Enter how much 20 dollar bills")
    bill20 = int(input("> "))
    print("Enter how much 10 dollar bills you have")
    bill10 = int(input("> "))
    print("Enter how much 5 dollar bills you have")
    bill5 = int(input("> "))
    print("Enter how much 2 dollar bills you have")
    bill2 = int(input("> "))
    print("Enter how much 1 dollar bill you have")
    bill1 = int(input("> "))
    money500 = bill500
    if bill500 > 0:
        dollar500 += int(bill500)
        money500 = money500 * 500
    if bill100 > 0:
        dollar100 += int(bill100)
        money100 = dollar100 * 100
    if bill50 > 0:
        dollar50 += bill50
        money50 = dollar50 * 50
    if bill20 > 0:
        dollar20 += bill20
        money20 = dollar20 * 20
    if bill10 > 0:
        dollar10 += bill10
        money10 = dollar10 * 10
    if bill5 > 0:
        dollar5 += bill5
        money5 = dollar5 * 5
    if bill2 > 0:
        dollar2 += bill2
        money2 = dollar2 * 2
    if bill1 > 0:
        dollar1 += bill1
        money1 = dollar1 * 1
    total = money1 + money2 + money5 + money10 + money20 + money50 + money100 + money500
    print(f"Total is ${total}!")
    break