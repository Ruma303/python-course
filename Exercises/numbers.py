"""_exercise_numbers.py
prendere in input 3 numeri x, y, z
assegnare il primo numero * 100 + secondo * 10, il tutto diviso per il terzo
mandare a schermo:
1. se x è int
2. il tipo di y
3. l'assoluto di z + la potenza alla terza di z
"""

x = int(input("Inserisci il primo numero per x: "))
y = int(input("Inserisci il primo numero per y: "))
z = int(input("Inserisci il primo numero per z: "))

x *= 100
y *= 10

final = (x + y) / z
print(final)

print("Il tipo di x è: ", type(x))

# oppure print(x.is_integer())

if isinstance(x, int):
  print("x è un intero")
else:
  print("x non è un intero")

print("Il tipo di y è: ", type(y))

print(abs(z) + pow(z, 3))