word = input("Type a variable name: ")
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_charachters = ["@", "!", "#", "$", "%", "^", "&", "*", "(", ")", ":", ";", ",", ".", "<", ">", "?", "/", "~", "`"]
if word[1] not in number and word[1] not in special_charachters and " " not in word:
  print("Valid Variable")
else:
  print("Invalid Variable")