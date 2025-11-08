
#% Scopes delle variabili
x = 10  # Variabile globale

def funzione():
    x = 5  # Variabile locale
    print(f"Locale: {x}")

funzione()
print(f"Globale: {x}")


## Enclosed scope
def outer(x):
    y = 20
    def inner():
        print(x + y)
    inner()

print(outer(10))


## Visualizzare nomi namespace built-in
import builtins
print(dir(builtins))


## Shadowing
x = 100

def myFunc():
    x = 20
    print(x)

myFunc()     # stampa 20 (x locale)
print(x)     # stampa 100 (x globale)


## Ispezionare namespace
def test():
    a = 1
    b = 2
    print(locals()) # dizionario namespace locale
    print(globals()) # dizionario namespace globale
    print(vars(test)) # restituisce il __dict__ di un oggetto, se esiste

test() # Output: {'a': 1, 'b': 2}


#% Modifica di variabili global e enclosed

## Modifica delle variabili globali
x = 10

def modifica_globale():
    global x
    x = 20
    print(x) # 20

modifica_globale()
print(x)  # 20


## Modifica di variabili enclosed
def modifica_enclosed():
    y = 20
    def inner():
        nonlocal y
        y = 50
        print(y) # 50
    inner()
    print(y)  # 50

modifica_enclosed()


#* Esempio mixato
x = 10

def outer():
    y = 20
    def inner():
        global x
        nonlocal y
        x = 100
        y = 200
    inner()
    print(f"x (global): {x}")
    print(f"y (enclosed): {y}")

outer()


## Accessibilità locale -> globale
if True:
    y = 10

print(y)

