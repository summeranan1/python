sub1p1 = int(input("Enter the score of your first subject of the first person: "))
sub2p1 = int(input("Enter the score of the second subject of the first person: "))
sub3p1 = int(input("Enter the score of the third subject of the first person: "))
sub4p1 = int(input("Enter the score of the fourth subject of the first person: "))
sub5p1 = int(input("Enter the score of the fifth subject of the first person: "))
print("")
print("")
sub1p2 = int(input("Enter the score of your first subject of the second person: "))
sub2p2 = int(input("Enter the score of the second subject of the second person: "))
sub3p2 = int(input("Enter the score of the third subject of the second person: "))
sub4p2 = int(input("Enter the score of the fourth subject of the second person: "))
sub5p2 = int(input("Enter the score of the fifth subject of the second person: "))

avrp1 = (sub1p1 + sub2p1 + sub3p1 + sub4p1 + sub5p1) / 5
avrp2 = (sub1p2 + sub2p2 + sub3p2 + sub4p2 + sub5p2) / 5
if avrp1 > avrp2:
  print("The first person is more topper")
elif avrp2 > avrp1:
  print("The second person is more topper")
elif avrp1 == avrp2:
  print("Average scores are the same")
else:
  print("Invalid Input")