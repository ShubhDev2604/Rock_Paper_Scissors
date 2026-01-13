import random
def check_win(player, computer):
    print(f"You chose: {player}, cp chose: {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "You win!"
        else: return "Computer wins!"
    elif player == "paper":
        if computer == "rock":
            return "You win!"
        else: return "Computer wins!"
    else:
        if computer == "paper":
            return "You win!"
        else: return "Computer wins!"

def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    return {"computer_choice": computer_choice, "player_choice": player_choice}

choices = get_choices()
result = check_win(choices["player_choice"], choices["computer_choice"])

print(result)



