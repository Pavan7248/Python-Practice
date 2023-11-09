#Make a two-player Rock-Paper-Scissors game. Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.

def get_player_choice():
 while True:
   player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
   if player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors':
     return player_choice
   else:
     print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(player1_choice, player2_choice):
  if player1_choice == player2_choice:
    return "It's a tie!"
  elif (
    (player1_choice == 'rock' and player2_choice == 'scissors') or
    (player1_choice == 'paper' and player2_choice == 'rock') or
    (player1_choice == 'scissors' and player2_choice == 'paper')
  ):
    return "Player 1 wins!"
  else:
    return "Player 2 wins!"
  
while True :
  player1_choice = get_player_choice()
  player2_choice = get_player_choice()
  print("Let's play Rock-Paper-Scissors!")
  print(f"Player 1 chose {player1_choice} and Player 2 chose {player2_choice}.")
  print(determine_winner(player1_choice, player2_choice))
  
  play_again = input("Do you want to play again? (yes/no): ").lower()
  if play_again != 'yes':
    break