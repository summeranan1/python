word = input("Enter a four letter word: ")
if len(word) > 4:
  print("Too much letters!")
elif len(word) < 5:
  if word == word[3] + word[2] + word[1] + word[0]:
    print("The words are the same.")
  else:
    print("The words are not the same.")
