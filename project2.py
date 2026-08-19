# Rock paper scissor game

import random

game_choices = ["rock" , "paper" , "scissor"]

your_choice = input("Enter your choice in the rock paper or scissor game = ")
computer_choice = random.choice(game_choices)

print(f"your choice is {your_choice} and computer choice is {computer_choice}")

if your_choice == computer_choice:
    print("It's a tie")

elif your_choice == "rock" :
    if computer_choice == "paper":
        print("computer win")
    elif computer_choice == "scissor":
        print("you win")

elif your_choice == "paper" :
    if computer_choice == "rock":
        print("you win")
    elif computer_choice == "scissor":
        print("computer win")

elif your_choice == "scissor" :
    if computer_choice == "paper":
        print("you win")
    elif computer_choice == "rock":
        print("computer win")
