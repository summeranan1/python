#Write a program to take string as input and reverse it
## initializing the string
string = input("Enter a sentence: ")
## splitting the string on space
words = string.split()
## reversing the words using reversed() function
words = list(reversed(words))
## joining the words and printing
print(" ".join(words))