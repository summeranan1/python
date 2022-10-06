print("Welcome to Rock,Paper & Scissors Game")
print("*************************************")
user = input("Enter your first name:")
print("Paper beats rock \n\nRock beats scissors \n\nScissors beats paper \n\nEnter Your choice( rock||paper||scissor): ")
print("")
choice = input(">")
options = ["Rock", "rock", "Paper", "paper", "Scissors", "scissors"]

computer = ["rock", "paper", "scissors"]
import random

result = random.choice(computer)

if choice not in options:
    print(f"Hello {user}, please enter your choice only as rock, paper, or scissors!")
else:
    if choice == "Rock" or choice == "rock":
        if result == "rock":
            print(f"Computer chose {result}")
            print("This is a tie!")
        if result == "paper":
            print(f"Computer chose: {result}")
            print("Computer has won!")
        if result == "scissors":
            print(f"Computer chose: {result}")
            print(f"{user} have won the match!")

    if choice == "Paper" or choice == "paper":
        if result == "paper":
            print(f"Computer chose: {result}")
            print("This is a tie!")
        if result == "rock":
            print(f"Computer chose: {result}")
            print(f"{user} have won the match!")
        if result == "scissors":
            print(f"Computer chose: {result}")
            print("Computer has won!")

    if choice == "scissors" or choice == "scissors":
        if result == "scissors":
            print(f"Computer chose: {result}")
            print("This is a tie!")
        if result == "rock":
            print(f"Computer chose: {result}")
            print("Computer has won!")
        if result == "paper":
            print(f"Computer chose {result}")
            print(f"{user} have won the match!")

print(f"Thank you for playing {user}")