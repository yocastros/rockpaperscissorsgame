import random

# creo las variables para llevar la cuenta de las victorias del jugador y de la computadora

player_wins = 0
computer_wins = 0

print("Let's play rock, paper, or scissors")

while player_wins < 2 and computer_wins < 2: # el juego termina cuando uno de los dos gana 2 veces

  player_choice = input("Please select rock, paper or scissors: ").lower() #

  choices = ["rock", "paper", "scissors"]

  if player_choice not in choices:
    print("Please select a correct choice")

  else:

    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    winner = ""

    if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
      winner = "Player"
      print(winner)
      player_wins += 1

    elif player_choice == computer_choice:
      winner = "Tie"
      print(winner)

    else:
      winner = "Computer"
      print(winner)
      computer_wins += 1

    if winner == "Player":
      print("You won")

    elif winner == "Computer":
      print("Computer won")

    else:
      print("It´s a tie")

    print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")

if player_wins > computer_wins:
  print("Congratulations! You won.")
else:
  print("Computer won!")