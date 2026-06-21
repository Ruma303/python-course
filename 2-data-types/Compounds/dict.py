
#% Dizionari

#, Creazione

dizionario_vuoto = {}
print(dizionario_vuoto)  # Output: {}

persona = {
    "nome": "Alice",
    "età": 25,
    "città": "Roma"
}
print(persona)
# Output: {'nome': 'Alice', 'età': 25, 'città': 'Roma'}

persona = dict(nome="Alice", età=25, città="Roma")
print(persona)
# Output: {'nome': 'Alice', 'età': 25, 'città': 'Roma'}


#, Accesso ai valori

persona = {"nome": "Alice", "età": 25}
print(persona["nome"])  # Output: Alice
print(persona["età"])   # Output: 25

# print(persona["città"])  # KeyError: 'città'

print(persona.get("nome"))  # Output: Alice
print(persona.get("città"))  # Output: None
print(persona.get("città", "Non disponibile"))  # Output: Non disponibile, non genera errore


#, Aggiungere e modificare entries

## Aggiunta nuovi elementi in un dizionari
contatti = {"nome": "Alice", "età": 25}
contatti["città"] = "Roma"
print(contatti)
# Output: {'nome': 'Alice', 'età': 25, 'città': 'Roma'}

## Modifica
contatti["nome"] = "Antonia"
print(contatti)
# Output: {'nome': 'Antonia', 'età': 25, 'città': 'Roma'}

## Update: Creazione
contatti.update({"città": "Milano"}) # Modifica
print(contatti)
# Output: {'nome': 'Antonia', 'età': 25, 'città': 'Milano'}

## Oppure con keyword args
contatti.update(nome="Ernesto", età=40)
print(contatti)
# Output: {'nome': 'Ernesto', 'età': 40, 'città': 'Milano'}


#, Rimuovere elementi

del contatti["città"]
print(contatti)
# Output: {'nome': 'Antonia', 'età': 25}

nome_da_rimuovere = contatti.pop('nome')
print(nome_da_rimuovere)
print(contatti)
# Output: {'età': 25}

persona = {"nome": "Alice", "età": 25, "città": "Roma"}
ultima_coppia = persona.popitem()
print(ultima_coppia)  # Output: ('città', 'Roma')
print(persona)  # Output: {'nome': 'Alice', 'età': 25}

persona.clear()
print(persona) # {}


#, Metodi utili dei dizionari

persona = {"nome": "Alice", "età": 25, "città": "Roma"}

keys = persona.keys()
print(keys)  # Output: dict_keys(['nome', 'età', 'città'])

keys = ["title", "author", "year"]
default_value = "undefined"
my_book = dict.fromkeys(keys, default_value)
print(my_book) # {'title': 'undefined', 'author': 'undefined', 'year': 'undefined'}

valori = persona.values()
print(valori) # Output: dict_values(['Alice', 25, 'Roma'])

coppie = persona.items()
print(coppie)
# Output: dict_items([('nome', 'Alice'), ('età', 25), ('città', 'Roma')])


#, Iterare su un dizionario

## Iterare sulle chiavi
persona = {"nome": "Alice", "età": 25, "città": "Roma"}
for chiave in persona:
    print(chiave)
# Output:
# nome
# età
# città
print()

## Iterare sui valori
for valore in persona.values():
    print(valore)
# Output:
# Alice
# 25
# Roma
print()

## Iterare sulle coppie chiave-valore
for chiave, valore in persona.items():
    print(f"{chiave}: {valore}")
# Output:
# nome: Alice
# età: 25
# città: Roma
print()

## Enumerazione
library = {
    "Il Signore degli Anelli": 3,
    "1984": 5,
    "Il Grande Gatsby": 2
}
for idx, (titolo, copie) in enumerate(library.items(), 1):
    print(f"{idx}. {titolo.title()} - {copie} copie disponibili")
print()


#, Dict Comprehension

string = "python"
a = {k : ord(k) for k in string}
print(a)

b = {k : ord(k) for k in string if ord(k) <= 110}
print(b)
print()

list_tuples = [("name", "John"), ("lastname", "Doe")]
person = {key: val for key, val in list_tuples}
print(person)
# {'name': 'John', 'lastname': 'Doe'}
print()


#, Esempi di utilizzo pratico

## Conteggio delle occorrenze
lista = ["a", "b", "a", "c", "b", "a"]
conteggio = {}
for lettera in lista:
    conteggio[lettera] = conteggio.get(lettera, 0) + 1
print(conteggio)
# Output: {'a': 3, 'b': 2, 'c': 1}
print()

## Raggruppare dati
studenti = {
    "Alice": {"età": 25, "corsi": ["matematica", "fisica"]},
    "Bob": {"età": 22, "corsi": ["chimica", "biologia"]}
}
print(studenti["Alice"]["corsi"])
# Output: ['matematica', 'fisica']

## Aggiornare un dizionario annidato (in-place)
studenti['Bob'].update({'età': 20})
print(studenti)

studenti.update({
    'Alice': {
        'età': studenti['Alice']['età'],
        'corsi': studenti['Alice']['corsi'] + ['seo', 'web design']
    },
    'Bob': {
        'età': studenti['Bob']['età'],
        'corsi': studenti['Bob']['corsi'] + ['marketing']
    },
    # Non è possibile aggiungere nuove chiavi, es: 'Charlie'
})
print(studenti)

## Copiare i dizionari
studenti = {
    "Alice": {"età": 25, "corsi": ["matematica", "fisica"]},
    "Bob": {"età": 22, "corsi": ["chimica", "biologia"]}
}

# Usando .copy() (shallow), l'append modificherà anche studenti
studenti_copia = studenti.copy()
studenti_copia['Bob']['corsi'].append('cybersecurity')
studenti_copia['Bob'].update({'età': 40})

print(studenti)
print(studenti_copia)
print(id(studenti), id(studenti_copia))

# Usando .deepcopy(), le modifiche non influiranno sul dizionario originale

from copy import deepcopy

studenti_copia_profonda = deepcopy(studenti)
studenti_copia_profonda['Alice']['corsi'].append('ingegneria')
studenti_copia_profonda['Alice'].update({'età': 20})
studenti_copia_profonda['Bob'].pop('età')

print(studenti_copia_profonda)
print(studenti)
print(id(studenti), id(studenti_copia_profonda))
print()


#, Ordinamento 3.7
myDict = {
    "primo": 10,
    "secondo": 20,
    "terzo": 30
}
myDict["quarto"] = 40

print(myDict.keys())
# Output: dict_keys(['primo', 'secondo', 'terzo', 'quarto'])

print(list(myDict))
# Output: ['primo', 'secondo', 'terzo', 'quarto']

for chiave, valore in myDict.items():
    print(f"{chiave}: {valore}")
# Output:
# primo: 10
# secondo: 20
# terzo: 30
# quarto: 40

d = {}
d["uno"] = 1
d["due"] = 2
d.update({"tre": 3})
del d["due"]
d["due"] = 22
print(list(d.keys()))  # ['uno', 'tre', 'due']


#, Union operators per i dizionari in Python 3.9

## Pre 3.9
my_dict1 = {"a": "primo", "b": "secondo", "c": "terzo"}
my_dict2 = {"d": "quarto", "e": "quinto"}

my_dict12 = my_dict1.copy()
for chiave, valore in my_dict2.items():
    my_dict12[chiave] = valore

print(my_dict12)
# Output: {'a': 'primo', 'b': 'secondo', 'c': 'terzo', 'd': 'quarto', 'e': 'quinto'}


## Union operator |
my_dict3 = {"a": "primo", "b": "secondo", "c": "terzo"}
my_dict4 = {"d": "quarto", "a": "quinto"}

my_dict34 = my_dict3 | my_dict4
print(my_dict34)
# Output: {'a': 'quinto', 'b': 'secondo', 'c': 'terzo', 'd': 'quarto'}
print("3: ", my_dict3)
print(my_dict4)

## Union assignment operator |=
my_dict3 |= my_dict4
print(my_dict34)
# Output: {'a': 'quinto', 'b': 'secondo', 'c': 'terzo', 'd': 'quarto'}
print("3: ", my_dict3)