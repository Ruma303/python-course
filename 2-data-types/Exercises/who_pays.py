"""
Creare una lista di persone
A caso sorteggiare chi pagherà il conto
"""
import random

friends = ["Marco", "Luca", "Elia", "Maria", "Sara"]

indice = random.randint(0, (len(friends) - 1))

persona_scelta = friends[indice]

print(f"{persona_scelta} pagherà il conto per tutti!")


"""
Versione semplice
"""

print(f"{random.choice(friends)} pagherà il conto per tutti!")