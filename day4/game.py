# Import the random module to generate random choices
import random

# Define the options and the rules of the game
options = ["paper", "tiger", "scissors"]
rules = {"paper": "scissors", "tiger": "paper", "scissors": "tiger"}

# Initialize the scores of the user and the computer
user_score = 0
computer_score = 0

# Ask the user how many rounds they want to play
rounds = int(input("How many rounds do you want to play? "))

# Loop through the rounds
for i in range(rounds):
    # Print the current round number
    print(f"Round {i+1}")

    # Ask the user to choose an option
    user_choice = input("Choose paper, tiger, or scissors: ").lower()

    # Validate the user input
    while user_choice not in options:
        print("Invalid choice. Please try again.")
        user_choice = input("Choose paper, tiger, or scissors: ").lower()

    # Generate a random choice for the computer
    computer_choice = random.choice(options)

    # Print the choices of the user and the computer
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Compare the choices and determine the winner
    if user_choice == computer_choice:
        # It's a tie
        print("It's a tie!")
    elif rules[user_choice] == computer_choice:
        # The user wins
        print("You win!")
        user_score += 1
    else:
        # The computer wins
        print("Computer wins!")
        computer_score += 1

    # Print the current scores
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    print()

# Print the final result
if user_score > computer_score:
    # The user wins the game
    print("You win the game!")
elif user_score < computer_score:
    # The computer wins the game
    print("Computer wins the game!")
else:
    # It's a draw
    print("It's a draw!")
