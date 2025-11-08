"""
RPS sta per Rock, Paper, Scissors: Sasso carta forbice

Prendere una scelta dell'utente, il computer farà la sua scelta
Usare le regole del gioco per stabilire chi è il vincitore
"""

import random

rock, paper, scissors = 1, 2, 3

while True:
  user_choice = input("Inserisci un valore tra 'rock', 'paper', 'scissors', 'q' per uscire: ").lower().lstrip()
  print(f"Hai digitato {user_choice}")

  match user_choice:
    case 'rock':
      user_choice = 1
    case 'paper':
      user_choice = 2
    case 'scissors':
      user_choice = 3
    case 'q':
      exit("Grazie per aver giocato con noi!")
      break
    case _:
      print("Valore non valido, riprova.\n")

  computer_choice = random.randint(rock, scissors)
  print(f"Il computer ha scelto {computer_choice}")

  result = "Hai perso :(" if computer_choice > user_choice else "Hai vinto"
  print(result, "\n")
