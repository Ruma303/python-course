
#% Metodi per liste

## Metodi per aggiungere o modificare elementi
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Output: [1, 2, 3, 4]

lista = [1, 2, 3]
lista.extend([4, 5])
print(lista)  # Output: [1, 2, 3, 4, 5]

lista = [1, 2, 3]
lista.insert(1, 10)  # Inserisce 10 alla posizione 1
print(lista)  # Output: [1, 10, 2, 3]


## Metodi per rimuovere elementi
lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)  # Output: [1, 3, 2]

lista = [1, 2, 3]
ultimo = lista.pop()
print(ultimo)  # Output: 3
print(lista)   # Output: [1, 2]

lista = [1, 2, 3]
lista.clear()
print(lista)  # Output: []


## Trovare informazioni
lista = [1, 1, 0, 2]
posizione = lista.index(2)
print(posizione)  # Output: 3

lista = [1, 1, 0, 3, 5, 6, 2, 2]
slice_list = lista[:-1].index(2)
print(posizione)  # Output: 2

lista = [1, 2, 3, 2]
conteggio = lista.count(2)
print(conteggio)  # Output: 2


## Ordinare o invertire la lista
lista = [3, 1, 4, 2]
lista.sort()
print(lista)  # Output: [1, 2, 3, 4]

lista.sort(reverse=True)
print(lista)  # Output: [4, 3, 2, 1]

# Ordinare per lunghezza delle stringhe
lista_stringhe = ["abc", "a", "ab"]
lista_stringhe.sort(key=len)
print(lista_stringhe)  # Output: ['a', 'ab', 'abc']

lista = [1, 2, 3]
lista.reverse()
print(lista)  # Output: [3, 2, 1]
