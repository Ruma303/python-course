
#% Functions

## Parametri posizionali
def somma(a, b):
    return a + b

risultato = somma(3, 4)
print(risultato)


## Parametri opzionali
def saluta(age=20, cognome="Rossi", nome="Mario"):
    print(f"Nome: {nome}, cognome: {cognome}, età: {age}")

saluta()         # Usa i valori di default
saluta(30, cognome="Maria", nome="Anna")   # Sovrascrive il valore di default


## Sintassi dei parametri positional-only con lo slash /
def somma(a, /, b, c):
    return a + b + c

y = somma(10, c=4, b=2)   # a viene passato per posizione, b e c come keyword
print(y)                  # Output: 16


## Parametri variabili

#* Argomenti posizionali variabili
def somma(n1, *numeri):
  print(*numeri) # stampiamo la tupla degli argomenti dinamici
  return n1 + sum(numeri)

print(somma(1, 2, 3))  # 6: Somma di tre numeri
print(somma(4, 5))     # 9: Somma di due numeri


#* Argomenti nominali variabili
def stampa_dettagli(**info):
    for chiave, valore in info.items():
        print(f"{chiave}: {valore}")

stampa_dettagli(nome="Marco", età=25, città="Roma")


## Parametri passati per riferimento

#* Passare oggetti immutabili
def myFunc(x):
    x = 10  # x viene reindirizzato a un nuovo oggetto intero
    print(x)  # Stampa 10

y = 20  # y è un intero, quindi immutabile
myFunc(y)  # All'interno di myFunc, x diventa 10
print(y)   # Stampa 20, poiché y non è stato modificato


#* Passare oggetti mutabili
def myFunc(x):
    x['b'] = 10  # Modifica il dizionario, aggiungendo una nuova coppia chiave-valore
    print(x)     # Stampa il dizionario modificato

d = {'a': 5}  # Dizionario, oggetto mutabile
myFunc(d)     # La funzione modifica direttamente l'oggetto referenziato da d
print(d)      # Stampa {'a': 5, 'b': 10}, evidenziando la modifica apportata


## L'istruzione return
def somma(a, b):
    return a + b  # La funzione restituisce la somma dei due parametri

risultato = somma(4, 7)
print(risultato)  # Output: 11

def operazioni(a, b):
    somma = a + b
    differenza = a - b
    return somma, differenza  # Restituisce una tupla con due valori

s, d = operazioni(10, 3)
print(f"Somma: {s}, Differenza: {d}")  # Output: Somma: 13, Differenza: 7


def funzione_senza_return():
    pass  # Corpo della funzione vuoto

risultato = funzione_senza_return()
print(risultato)  # Output: None


import math

def area_cerchio(raggio):
	if raggio >= 0:
		area = math.pi * (raggio**2)
		return area
	return

print(area_cerchio(-2))
print(area_cerchio(3))


## Combinazione tra tipi di parametri
def mix_parametri(a, b, /, c, d=4, *, e, f=5):
    print(a, b, c, d, e, f)

mix_parametri(1, 2, 3, e=7) # Output: 1 2 3 4 7 5
mix_parametri(3, 5, c=7, e=9) # Output: 3 5 7 4 9 5


#% Funzioni come oggetti

## Funzioni come oggetti di prima classe
def somma(x, y):
    return x + y

print(type(somma))  # <class 'function'>

f = somma
print(f(3, 4))      # 7


## Funzioni nidificate (nested functions)
def outer(x, y):
    def inner(a, b):
        return a + b
    return inner(x, y)

print(outer(2, 5))  # 7


## Closure
def power(exp):
    def inner(base):
        return base ** exp
    return inner

quadrato = power(2)
cubo = power(3)

print(quadrato(4))  # 16
print(cubo(2))      # 8


## Restituire funzioni da altre funzioni
def crea_sommatore(n):
    def somma(x):
        return x + n
    return somma

somma10 = crea_sommatore(10)
print(somma10(5))   # 15


## Funzioni come argomenti: callback e funzioni di ordine superiore
def saluta():
    return "Ciao!"

def esegui(funzione):
    print(funzione())

esegui(saluta)  # Ciao!


def raddoppia(x):
    return x * 2

numeri = [1, 2, 3]
risultato = map(raddoppia, numeri)
print(list(risultato))  # [2, 4, 6]


## Attributi delle funzioni
def f():
    """
    Questa é una funzione di esempio
    """
    pass

f.info = "Attributo di f"
print(f.info)
print(f.__doc__)
print(f.__name__)


## Funzioni ricorsive in Python
def fattoriale(n):
    if n == 0 or n == 1:         # Caso base
        return 1
    else:
        return n * fattoriale(n - 1)   # Chiamata ricorsiva

print(fattoriale(5))   # Output: 120


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def somma_lista(lista):
    if not lista:         # lista vuota
        return 0
    else:
        return lista[0] + somma_lista(lista[1:])

numeri = [1, 2, 3, 4]
print(somma_lista(numeri))   # Output: 10