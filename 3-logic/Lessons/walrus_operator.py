
# % Assignment Expression

"""
## Pre Python 3.8
val = input("Inserisci un valore: ")
while val != "q":
    print(val)
    val = input("Inserisci un valore: ")

## Da Python 3.8
while (val := input("Inserisci un valore: ")) != "q":
    print(val)
"""

## Esempio di utilizzo
def somma(a, b):
    return a + b

if (x := somma(5, 3)) > 6:
    print("x maggiore di 6:", x)


## Utilizzo nei cicli
mylist = [1, 2, 3, 4, 5]
while (x := len(mylist)) != 0:
    print(f"Numero elementi: {x}, estratto: {mylist.pop()}")


## Uso con valore di default
def saluta(nome = (n := "Susanna")):
    print("Ciao", nome)
    print("Saluto di default: ", n.upper())

saluta() # Ciao Susanna + default
saluta("Alice") # Ciao Alice + default


## Esempio filtraggio list comprehension
valori = ["1", "due", "3", "quattro"]
numeri = [int(x) for s in valori if (x := s).isdigit()]
print(numeri)  # [1, 3]