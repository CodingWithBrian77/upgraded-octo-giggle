import random

options = ("rock", "paper", "scissors")
is_running = True

while is_running: # useful to use a boolean variable if large coding needs to be done
    
    options = ("rock", "paper", "scissors")
    computer = random.choice(options)
    player = None
    
    while player not in options: #if the player chooses something not in the options, will loop again and again
        player = input("Enter a choice (rock, paper, or scissors): ").lower()
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    
    if not input("Play again? (y/n): ").lower() == "y":
        is_running = False

print("Thanks for playing!")

