
#% Conversioni tra tipi composti

## Lista ↔ Tupla
tupla = (1, 2, 3)
lista = list(tupla)       # [1, 2, 3]
lista.append(4) # Modifichiamo la tupla
tupla2 = tuple(lista)     # (1, 2, 3, 4)


## Lista/tupla ↔ Set
lista = [1, 2, 2, 3]
insieme = set(lista)      # {1, 2, 3}

insieme = {4, 5, 6}
lista = list(insieme)     # [4, 5, 6]
tupla = tuple(insieme)    # (4, 5, 6)


## Lista di tuple ↔ Dizionario
lista = [("a", 1), ("b", 2)]
dizionario = dict(lista)    # {'a': 1, 'b': 2}

dizionario = {"a": 1, "b": 2}
lista = list(dizionario.items())   # [('a', 1), ('b', 2)]


## Dizionario ↔ Liste di chiavi/valori
dizionario = {"a": 1, "b": 2}
chiavi = list(dizionario)          # ['a', 'b']
valori = list(dizionario.values()) # [1, 2]


## Stringa ↔ Lista/tupla di caratteri
s = "ciao"
lista = list(s)     # ['c', 'i', 'a', 'o']
tupla = tuple(s)    # ('c', 'i', 'a', 'o')

lista = ['c', 'i', 'a', 'o']
stringa = ''.join(lista)   # 'ciao'


## Lista di liste ↔ Lista di tuple
lista_liste = [[1, 2], [3, 4]]
lista_tuple = [tuple(x) for x in lista_liste]   # [(1, 2), (3, 4)]


## Range ↔ Lista/Tupla/Set
r = range(5)
lista = list(r)   # [0, 1, 2, 3, 4]
tupla = tuple(r)  # (0, 1, 2, 3, 4)
insieme = set(r)  # {0, 1, 2, 3, 4}


## Enumerate/Zip ↔ Lista/tupla
voci = ["a", "b"]
e = enumerate(voci)
lista_enum = list(e)     # [(0, 'a'), (1, 'b')]

x = [1, 2]
y = ['a', 'b']
zippati = list(zip(x, y))    # [(1, 'a'), (2, 'b')]


## Dizionario da liste
voci = ["a", "b"]
e = enumerate(voci)
lista_enum = dict(e)     # [(0, 'a'), (1, 'b')]
print(lista_enum)


## Diario da zip
chiavi = ['x', 'y']
valori = [10, 20]
dizionario = dict(zip(chiavi, valori))   # {'x': 10, 'y': 20}


## Unpacking da per ricostruire strutture
lista_di_tuple = [("a", 1), ("b", 2)]
chiavi, valori = zip(*lista_di_tuple)
# chiavi = ('a', 'b'), valori = (1, 2)