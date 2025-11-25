# Definizione variabili

x = 10 # x è una variabile che contiene l'intero 10
nome = "Alice" # nome è una variabile che contiene la stringa "Alice"

# Pseudo-costanti
PI = 3.14159
VELOCITA_LUCE = 299_792_458  # velocità della luce in m/s

# Acquisizione da input
nome = input("Qual è il tuo nome?")
print(f"Piacere di conoscerti, {nome}")


# Assegnamento diretto per valore
print("Copia per riferimento")
a = [1, 2, 3]
b = a

print(id(a), id(b))  # stessi id -> stesso oggetto

# Creare una copia dell'oggetto
print("\nCopia per valore")
x = [1, 2, 3]
y = x.copy()

print(id(x), id(y))

# Assegnamento tipi immutabili
print("\nAssegnamento tipi immutabili")
d = 5
e = d
e += 1

print(d)  # 5
print(e)  # 6
print(id(d), id(e))  # id diversi

# Assegnamento tipi mutabili
print("\nAssegnamento tipi mutabili")
i = [1, 2, 3]
j = i
j.append(4)

print(i)  # [1, 2, 3, 4]
print(j)  # [1, 2, 3, 4]
print(id(i), id(j))

# Copia superficiale
print("\nCopie superficiale")
import copy

a = [1, [2, 3], 4]

# copia con slicing
b = a[:]

# copia con costruttore
c = list(a)

# copia con copy()
d = copy.copy(a)

print("Oggetti contenitori esterni: ", id(a), id(b), id(c), id(d))  # id diversi
print("Array interno condiviso: ",id(a[1]), id(b[1]))          # stessi id per la lista interna


# Copia profonda
print("\nCopie profonda")

a = [1, [2, 3], 4]
b = copy.deepcopy(a)

print(id(a), id(b))         # contenitori diversi
print(id(a[1]), id(b[1]))   # anche gli oggetti interni sono diversi

b[1][0] = 99
print(a)  # [1, [2, 3], 4]
print(b)  # [1, [99, 3], 4]