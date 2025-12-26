
# % Lambdas

## Esempi
quadrato = lambda x: x**2
print(quadrato(5))  # 25

somma = lambda x, y: x + y
print(somma(3, 6))  # 9

pari = lambda x: x % 2 == 0
print(pari(7))  # False

sottostringa = lambda stringa, inizio, fine: stringa[inizio:fine]
print(sottostringa("Python", 2, 4)) # th
print(sottostringa("Java", 0, 3)) # Jav
print(sottostringa("Elixir", 0, -2)) # Elix

saluti = ["buongiorno", "arrivederci", "salve", "ciao"]
saluti_ordinati = sorted(saluti, key=lambda parola: len(parola))
print(saluti_ordinati)

dati = [{'nome': 'Anna', 'età': 30}, {'nome': 'Luca', 'età': 25}]
ordinati = sorted(dati, key=lambda x: x['età'])
print(ordinati)

numeri = [1, 2, 3, 4]
quadrati = list(map(lambda x: x**2, numeri))
print(quadrati)  # [1, 4, 9, 16]

pari = list(filter(lambda x: x > 4, quadrati))
print(pari)

funzioni = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]

for f in funzioni:
    print(f(3))
# Output: 4, 6, 9