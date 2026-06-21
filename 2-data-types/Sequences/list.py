
#% Creazioni liste
# Lista vuota
lista_vuota = []

# Lista di numeri
numeri = [1, 2, 3, 4]

# Lista di stringhe
parole = ["Python", "è", "fantastico"]

# Lista mista (numeri, stringhe, booleani)
mista = [42, "ciao", True, 3.14]

# Lista annidata (liste dentro una lista)
annidata = [[1, 2], [3, 4], [5, 6]]

# Uso della funzione list()
nuova_lista = list((1, 3, 19, "Hello", True, 12.0))
print(nuova_lista)



## Modifica elementi
numeri = [10, 20, 30]
numeri[1] = 25  # Modifica del secondo elemento
print(numeri)  # [10, 25, 30]


## Slicing
numeri = [10, 20, 30, 40, 50]

# Sottoinsieme dal primo al terzo elemento
print(numeri[0:3])  # [10, 20, 30]

# Elementi dal terzo in poi
print(numeri[2:])  # [30, 40, 50]

# Tutti gli elementi con passo 2
print(numeri[::2])  # [10, 30, 50]

# Lista al contrario
print(numeri[::-1])  # [50, 40, 30, 20, 10]


#% Operazioni comuni

## Concatenare liste
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
unione = lista1 + lista2
print(unione)  # [1, 2, 3, 4, 5, 6]


## Ripetizione
ripetuta = [1, 2] * 3
print(ripetuta)  # [1, 2, 1, 2, 1, 2]


## Controllo appartenenza
numeri = [1, 2, 3]
print(2 in numeri)  # True
print(5 in numeri)  # False


## Lunghezza
numeri = [1, 2, 3]
print(len(numeri))  # 3


## Eliminazione
numeri = [10, 20, 30]
del numeri[2]
print(numeri)


#, Iterare sulle liste

## Sugli elementi
numeri = [10, 20, 30]
for numero in numeri:
    print(numero)


## Sulle posizioni
numeri = [10, 20, 30]
for numero in range(len(numeri)):
    print(numero)

numeri = [10, 20, 30]
for indice, numero in enumerate(numeri):
    print(indice, ":", numero)


## IndexError
numeri = [10, 20, 30]
# print(numeri[3])
# IndexError: list index out of range

print(numeri[2]) # Ok
print(f"Numero elementi {len(numeri) = }")

# print(f"Accesso errato all'ultimo elemento {numeri[len(numeri)]}")
# IndexError: list index out of range

print(f"Accesso corretto all'ultimo elemento {numeri[len(numeri) - 1] = }")
# Accesso corretto all'ultimo elemento numeri[len(numeri) - 1] = 30

print(f"L'indice vale {len(numeri) - 1 = }")
# L'indice vale len(numeri) - 1 = 2


## List Comprehensions
#  Lista di quadrati
quadrati = [x**2 for x in range(5)]
print(quadrati)  # [0, 1, 4, 9, 16]

# Lista di numeri pari
pari = [x for x in range(10) if x % 2 == 0]
print(pari)  # [0, 2, 4, 6, 8]


#, Copie

## Per riferimento - da lista a lista
originale = [1, 2, 3]
copia_riferimento = originale
originale[1] = "Hello"

print(originale) # [1, 'Hello', 3]
print(copia_riferimento) #  [1, 'Hello', 3]


## Shallow copy - copia riferimenti elementi interni
lista_originale = [[1, 2], [3, 4]] # Gli elementi interni sono mutabili (altre liste)
copia_superficiale = lista_originale.copy()

# Modifica di un elemento nella lista annidata della lista originale
lista_originale[0][0] = 99

print("Lista originale:", lista_originale)  # Output: [[99, 2], [3, 4]]
print("Copia superficiale:", copia_superficiale)  # Output: [[99, 2], [3, 4]]

## Deep copy - copia valori elementi interni
import copy

lista_originale = [[1, 2], [3, 4]]
copia_profonda = copy.deepcopy(lista_originale)

# Modifica di un elemento nella lista annidata della lista originale
lista_originale[0][0] = 99

print("Lista originale:", lista_originale)  # Output: [[99, 2], [3, 4]]
print("Copia profonda:", copia_profonda)    # Output: [[1, 2], [3, 4]]
