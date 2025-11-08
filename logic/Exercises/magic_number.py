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

