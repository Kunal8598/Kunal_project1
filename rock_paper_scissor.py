import random

options = ["rock", "paper", "scissor"]

computer_choice = random.choice(options)
user_choice = input("Guess between rock,paper,scissor = ").lower()

if user_choice == "rock" and computer_choice == "scissor":
    print("you won")
elif user_choice == "paper" and computer_choice == "rock":
    print("you won")
elif user_choice == "scisssor" and computer_choice == "paper":
    print("you won")
elif user_choice == computer_choice:
    print("you have tied")
else:
    print(f"you lost.computer choose {computer_choice}")
