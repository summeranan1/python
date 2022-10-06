import random
wins = 0
lose = 0
games = 0
max = 3
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",  "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter_random = random.choice(letters)
print(f"Enter a word that starts with {letter_random}")
word = input("> ")
if word[0] == letter_random:
  print("You won!")
  games = 1
  wins = 1
elif word != letter_random:
  print("You lose!")
  games = 1
  lose = 1
letter_random1 = random.choice(letters)
print(f"Enter a word that starts with {letter_random1}")
word2 = input("> ")
if word2[0] == letter_random1:
  print("You won!")
  games = 2
  wins = 2
elif word2 != letter_random1:
  print("You lose!")
  games = 2
  lose = 2
letter_random2 = random.choice(letters)
print(f"Enter a word that starts with {letter_random2}")
word3 = input("> ")
if word3[0] == letter_random2:
  print("You won!")
  games = 3
  wins = 3
else:
  print("You lose!")
  games = 3
  lose = 3
print(f"You won {wins}/3 times!")