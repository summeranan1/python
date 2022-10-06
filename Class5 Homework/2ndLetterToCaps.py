word = input("Enter any word: ")
print("Loading...")
print("Second letter uppercase is:")
print(word[0:1] + word[1:2].upper() + word[2:len(word)])