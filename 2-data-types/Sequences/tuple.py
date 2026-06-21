# Tuple

#, Definizioni

## Tupla vuota
tupla_vuota = ()
print(tupla_vuota)  # Output: ()


## Tupla con un solo elemento
tupla_singola = (42,)
print(tupla_singola)  # Output: (42,)


## Esempio errato senza virgola
non_tupla = (42)
print(non_tupla)  # Output: 42 (non è una tupla, è un numero)


## Tupla con più elementi
tupla = (1, 2, 3, 4, 5)
print(tupla)  # Output: (1, 2, 3, 4, 5)


## Creazione senza parentesi (packing)
tupla = 1, 2, 3
print(tupla)  # Output: (1, 2, 3)


## Creazione con la funzione tuple()
my_tuple = tuple((10, 20, 30))
print(my_tuple)

# oppure

tuple1 = (10, 20, 30)
tuple2 = tuple(tuple1)
print(tuple2)


## Tuple comprehension
tuple_comprehension = tuple(x for x in range(10) if x // 3 == 0)
print(tuple_comprehension)


#, Proprietà delle tuple

## Indexing e slicing
tupla = (10, 20, 30, 40, 50)

print(tupla[0])   # Output: 10 (primo elemento)
print(tupla[-1])  # Output: 50 (ultimo elemento)
print(tupla[1:4]) # Output: (20, 30, 40) (sub-tupla con slicing)
print(tupla[::-1])  # Output: (50, 40, 30, 20, 10) (reversed tuple)
print(tupla[:3:2])  # Output: (10, 30) (dal primo al quarto elemento saltando di 2)


## Immutabilità
"""
tupla = (1, 2, 3)
tupla[0] = 10  # Errore: TypeError: 'tuple' object does not support item assignment
"""

#* 1. Conversione da tupla a lista e viceversa
tupla = (1, 2, 3)
lista = list(tupla)
lista[0] = 10
tupla = tuple(lista)
print(tupla)  # Output: (10, 2, 3)

#* 2. Creare una seconda tupla
tupla1 = (1, 2, 3)
tupla2 = tuple(ele * 2 for ele in tupla1)
print(tupla2)  # Output: (2, 4, 6)

#* 3. Concatenazione di tuple
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)  # Output: (1, 2, 3, 4, 5, 6)


## Tuple nidificate
tupla_nidificata = (1, (2, 3), (4, 5, 6))
print(tupla_nidificata[1])  # Output: (2, 3)
print(tupla_nidificata[1][0])  # Output: 2


## Packing
tupla = 1, 2, 3
print(tupla)  # Output: (1, 2, 3)

## Unpacking
tupla = (10, 20, 30)
a, b, c = tupla
print(a)  # Output: 10
print(b)  # Output: 20
print(c)  # Output: 30

## Utilizzando l'operatore rest *
tupla = (1, 2, 3, 4, 5)
a, *b, c = tupla
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

## Unpacking avanzato
tupla = (1, 2, 3, 4, 5, 6)
a, b, *c, d = tupla
print(a, b, c, d)
# a = 1, b = 2, c = [3, 4, 5], d = 6

t = (1, (2, 3))
x, (y, z) = t
print(x, y, z)
# x = 1, y = 2, z = 3


#,Operazioni comuni

## Concatenazione
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
nuova_tupla = tupla1 + tupla2
print(nuova_tupla)  # Output: (1, 2, 3, 4, 5, 6)

## Ripetizione
tupla = (1, 2, 3)
ripetuta = tupla * 3
print(ripetuta)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

## Verifica di appartenenza
tupla = (10, 20, 30, 40)
print(20 in tupla)   # Output: True
print(50 in tupla)   # Output: False

## Lunghezza
tupla = (1, 2, 3, 4, 5)
print(len(tupla))  # Output: 5


## Iterazione
tupla = (10, 20, 30)
for elemento in tupla:
    print(elemento)


#, Proprietà avanzate

## Hashabilità e tuple come chiavi
t1 = (1, 2, 3)  # hashable
d = {t1: "valore"}
print(d)
# d[(1, 2, 3)] restituisce 'valore'

t2 = ([1, 2], 3)  # NON hashable, contiene una lista
# d = {t2: "errore"}  # TypeError: unhashable type: 'list'

## Tuple come oggetti ricorsivi e contenimento
t = (1, 2)
t_nid = (t, (3, 4), ("a", "b", (5, 6)))
print(t_nid)
# t_nid[2][2][1] restituisce 6

## Ordinamento e conversione
t = (5, 3, 1, 4)
ordinata = tuple(sorted(t))
# ordinata = (1, 3, 4, 5)

## Confronti tra tuple
print((1, 2, 3) < (1, 2, 4))   # True
print((1, 2) < (1, 2, -1))      # True
print((2, 0) > (1, 10, 100))    # True

## Utilizzo nei cicli e in assegnazioni multiple
def coord():
    return (10, 20)

x, y = coord()
# x = 10, y = 20

dati = [("a", 1), ("b", 2), ("c", 3)]
for lettera, numero in dati:
    print(lettera, numero)

## Utilizzo di tuple come chiavi di dizionario
diz = {}
chiave = (3, 5)
diz[chiave] = "valore"
print(diz)

## Conversione tra tuple e altri tipi
tuple("abc")         # ('a', 'b', 'c')
tuple([1, 2, 3])     # (1, 2, 3)
tuple({1, 2, 3})     # (1, 2, 3) - ordine arbitrario coi set

## Rappresentazione letterale e annidamento
t = (1, 2, (3, 4))
print(repr(t))  # restituisce '(1, 2, (3, 4))'
