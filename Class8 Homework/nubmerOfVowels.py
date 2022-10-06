word = input("Enter a word: ")
x = word.count("a")
y = word.count("e")
z = word.count("i")
a = word.count("o")
b = word.count("u")
xu = word.count("A")
yu = word.count("E")
zu = word.count("I")
au = word.count("O")
bu = word.count("U")
length = len(word)
totalVowels = x + y + z + a + b + xu + yu + zu + au + bu
if totalVowels == 0:
  print("There are no vowels!")
else:
  print(f"{totalVowels} vowels.")