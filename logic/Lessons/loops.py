# , While

## Evitare cicli infiniti
counter = 0
while counter < 10:
    print(f"Conto: {counter + 1}")
    counter += 1

"""
password = ""
while password != "python123":
    password = input("Inserisci la password: ")
print("Accesso consentito!")
"""


## Range
for i in range(5):  # Da 0 a 4
    print(i)

for i in range(2, 10, 2):  # Da 2 a 8 con step 2
    print(i)


## Iterazioni
parola = "Python"
for lettera in parola:
    print(lettera)
else:
    print("Else attivato")


## Iterazioni su dizionari
dizionario = {'a': 1, 'b': 2, 'c': 3}

# Iterare sulle chiavi
for chiave in dizionario:
    print(chiave)

# Iterare sui valori
for valore in dizionario.values():
    print(valore)

# Iterare su chiavi e valori
for chiave, valore in dizionario.items():
    print(f"{chiave}: {valore}")


## Enumerate
students = ("Luca", "Piero", "Giorgio")
for index, name in enumerate(students):
    print(f"{index + 1}. {name}")


## break
for i in range(10):
    if i == 5:
        break
    print(i)


## continue
for i in range(10):
    if i == 5:
        continue
    print(i)


## Nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")