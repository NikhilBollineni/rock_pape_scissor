import random

# Defining a list of choices
choices = ["Rock", "Scissor", "Paper"]


# Defining function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissor") or \
            (user == "Scissor" and computer == "Paper") or \
            (user == "Paper" and computer == "Rock"):
        return "User wins!"
    else:
        return "Computer wins!"


# Keep track of scores
user_score = 0
computer_score = 0

while True:
    print("\nRock, Paper, Scissors Game: User Score -", user_score, "Computer Score -", computer_score)
    user_opinion = input("Enter 'Rock' or 'Paper' or 'Scissor' or 'Quit' to exit: ").title()

    # check if user wants to quit
    if user_opinion == "Quit":
        break

    # check if user input is valid
    if user_opinion not in choices:
        print("Invalid input! Please enter 'Rock', 'Paper', or 'Scissor'.")
        continue

    computer_opinion = random.choice(choices)
    print("User chose:", user_opinion)
    print("Computer chose:", computer_opinion)

    result = determine_winner(user_opinion, computer_opinion)
    print(result)

    if result == "User wins!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
