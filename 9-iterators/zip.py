
#% Metodo zip

nomi = ['Anna', 'Luca', 'Giulia']
eta = (22, 33, 44)
risultato = list(zip(nomi, eta))
print(risultato)
# [('Anna', 22), ('Luca', 33), ('Giulia', 44)]

s1 = "ABC"
s2 = "123"
risultato2 = list(zip(s1, s2))
print(risultato2)
# [('A', '1'), ('B', '2'), ('C', '3')]

## Lunghezza diversa
a = [1, 2, 3, 4]
b = ['x', 'y']
risultato3 = list(zip(a, b))
print(risultato3)
# [(1, 'x'), (2, 'y')]


set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
risultato4 = list(zip(set1, set2))
print(risultato4)
# Esempio possibile: [('a', 1), ('b', 2), ('c', 3)]


def g1():
    yield from range(3)
def g2():
    yield from 'xyz'
risultato5 = list(zip(g1(), g2()))
print(risultato5)
# [(0, 'x'), (1, 'y'), (2, 'z')]


a = [1, 2, 3]
b = [4, 5, 6]
c = ['a', 'b', 'c']
risultato6 = list(zip(a, b, c))
print(risultato6)
# [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]


z = zip([1, 2], [3, 4])
print(z)  # <zip object at ...>
print(list(z))  # [(1, 3), (2, 4)]


#. Stringhe non utilizzabili
stringa1 = "ABCDEFG"
stringa2 = "1234567"
# zip() restituisce un ITERATORE (oggetto lazy)
z = zip(stringa1, stringa2)

# str() NON itera l'oggetto - lo converte solo in rappresentazione testuale
str(z)  # → "<zip object at 0x...>"

# Invece list(), tuple(), set() sono COSTRUTTORI che materializzano l'iteratore
list(z)    # → [('A', '1'), ('B', '2'), ...]  ✓ Funziona!
tuple(z)   # → (('A', '1'), ('B', '2'), ...)  ✓ Funziona!
set(z)     # → {('A', '1'), ('B', '2'), ...}  ✓ Funziona!
str(z)     # → "<zip object at 0x...>"       ✗ Non funziona!

stringona = str(list(zip(stringa1, stringa2)))
# "[('A', '1'), ('B', '2'), ('C', '3'), ...]"

# Formattazione migliore
stringona = ', '.join([f"({a}, {b})" for a, b in zip(stringa1, stringa2)])
# "A, 1), (B, 2), (C, 3), ..."


## Trasposizione
tuples = [('a', 1, True), ('b', 2, False), ('c', 3, True)]
col1, col2, col3 = zip(*tuples)
print(col1, col2, col3)
# col1: ('a', 'b', 'c')
# col2: (1, 2, 3)
# col3: (True, False, True)

print([list(col) for col in zip(*tuples)])
# [['a', 'b', 'c'], [1, 2, 3], [True, False, True]]


#, Valori di default

from itertools import zip_longest
a = [1, 2, 3, 4]
b = ['x', 'y']
defaults = list(zip_longest(a, b, fillvalue='_'))
print(defaults)
# [(1, 'x'), (2, 'y'), (3, '_')]