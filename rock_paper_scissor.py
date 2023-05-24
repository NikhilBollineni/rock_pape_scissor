import random

while True:
    user_opinion = input("Lets start!\nEnter 'Rock' or 'Paper' or 'Scissor': ").title()
    computer_list = ["Rock", "Scissor", "Paper"]
    computer_opinion = random.choice(computer_list)

    if user_opinion not in computer_opinion:
        print("Invalid input! Please select 'Rock', 'Paper', or 'Scissor'. Good luck!")


    if user_opinion == "Rock" and computer_opinion == "Scissor":
        print(user_opinion, "1st block, USER has WON")
        break
    elif computer_opinion == "Rock" and user_opinion == "Scissor":
        print(computer_opinion, "1st block computer has won")
        break
    else:
        pass

    if user_opinion == "Scissor" and computer_opinion == "Paper":
        print(user_opinion, "2nd block USER has WON")
        break
    elif computer_opinion == "Scissor" and user_opinion == "Paper":
        print(computer_opinion, "2nd block computer has won")
        break
    else:
        pass

    if user_opinion == "Paper" and computer_opinion == "Rock":
        print(user_opinion, "3rd block USER has WON")
        break
    elif computer_opinion == "Paper" and user_opinion == "Rock":
        print(computer_opinion, "3rd block computer has won")
        break
    else:
        pass

    if user_opinion == computer_opinion:
        print("Opinions are tie! play again")
