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


#% Operazioni comuni

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


## List Comprehensions
#  Lista di quadrati
quadrati = [x**2 for x in range(5)]
print(quadrati)  # [0, 1, 4, 9, 16]

# Lista di numeri pari
pari = [x for x in range(10) if x % 2 == 0]
print(pari)  # [0, 2, 4, 6, 8]


#% Metodi