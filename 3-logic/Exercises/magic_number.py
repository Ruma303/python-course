"""
Dato un qualsiasi numero intero contenuto nella variabile number
decidere se quello è un magic number

- magic se compreso tra 12 e 124 ed è multiplo di 3 e di 5
- oppure se è compreso tra 12 e 50 ed è pari
- oppure se è negativo
- oppure se è pari e multiplo di 7
"""

# Step 1: acquisire il numero
number = int(input("Inserisci un numero intero: ").strip())

# Step 2: condizioni
if (12 <= number <= 124) and (number % 3 == 0 and number % 5 == 0):
    # Esempio di magic number: 15
    print(f"{number} è un magic number")

elif (12 <= number <= 50) and (number % 2 == 0):
    # Esempio di magic number: 12
    print(f"{number} è un magic number")

elif number < 0:
    # Esempio di magic number: -1
    print(f"{number} è un magic number")

elif (number % 2 == 0) and (number % 7 == 0):
    # Esempio di magic number: 14
    print(f"{number} è un magic number")

else:
    print(f"{number} non è un magic number")


# Unire le condizioni
number = 15

expr1 = 12 <= number <= 124 and number % 3 == 0 and number % 5 == 0
expr2 = 2 <= number <= 50 and number % 2 == 0
expr3 = number < 0
expr4 = number % 2 == 0 and number % 7 == 0

if expr1 or expr2 or expr3 or expr4:
    print(f"{number} è un magic number")

else:
    print(f"{number} non è un magic number")


# Esempio con lista
# Se fosse stato richiesto che tutte le condizioni siano vere, avremmo usato all().
conditions = list([expr1, expr2, expr3, expr4])

if any(conditions):
    print(f"{number} è un magic number")
else:
    print(f"{number} non è un magic number")