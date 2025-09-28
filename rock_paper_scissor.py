import random

def rock_paper_scissor():
    choices = ["rock", "paper", "scissor"]
    #Taking user input(choice):
    user_choice = input("Enter your choice(rock/paper/scissor): ").lower()

    computer_choice = random.choice(choices)

    print("User choice: ", user_choice)
    print("Computer choice: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "scissor" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("User Won!")
    else:
        print("Computer Won!")

rock_paper_scissor()