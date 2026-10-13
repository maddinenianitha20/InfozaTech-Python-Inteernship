import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
draws = 0
print("===== ROCK, PAPER, SCISSORS GAME =====")
while True:
    user = input(
        "\nChoose rock, paper, or scissors (or type exit): "
    ).lower().strip()

    if user == "exit":
        break

    if user not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer = random.choice(choices)

    print("Your choice:", user)
    print("Computer choice:", computer)

    if user == computer:
        print("It's a draw!")
        draws += 1

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("Congratulations! You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print("\n----- CURRENT SCORE -----")
    print("Your score:", user_score)
    print("Computer score:", computer_score)
    print("Draws:", draws)

print("\n===== FINAL SCORE =====")
print("Your total wins:", user_score)
print("Computer total wins:", computer_score)
print("Total draws:", draws)

if user_score > computer_score:
    print("Congratulations! You won the game!")

elif computer_score > user_score:
    print("Computer won the game. Better luck next time!")

else:
    print("The game ended in an overall draw!")

print("Thank you for playing!")