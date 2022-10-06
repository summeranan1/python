#Write a program to take a string and rearrange it in jumbled form
word = input("Enter any word (Include 8 charachters): ")
print("Jumbled Form: ")
letters = len(word)
print(word[1] + word[2] + word[4] + word[3] + word[0])