import random

print("Let's play Rock, Paper, Scissors!")
choice_dict = {0:"rock", 1:"paper", 2:"scissors"}

player_choice = input("What do you choose? Type 'Rock', 'Paper', or 'Scissors': ").lower()
#lowercase_playerchoice = player_choice.lower()
computer_number = random.randint(0,2)
computer_choice = choice_dict[computer_number]
print(f"Computer chose {computer_choice}")

if player_choice == computer_choice:
    print("Tie!")
elif player_choice == "rock":
    if computer_choice == "paper":
        print("Computer wins!")
    else:
        print("You win!")
elif player_choice == "paper":
    if computer_choice == "scissors":
        print("Computer wins!")
    else:
        print("You win!")
elif player_choice == "scissors":
    if computer_choice == "rock":
        print("Computer wins!")
    else:
        print("You win!")