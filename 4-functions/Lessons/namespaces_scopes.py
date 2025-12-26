
#% Scopes delle variabili
def funzione():
    x = 5  # Variabile locale
    print(f"Locale: {x}")

funzione()
# print(f"Globale: {x}") # Errore: x non sopravvive fuori dalla funzione

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
    print(locals()) # dizionario namespace locale {'a': 1, 'b': 2}
    print(globals()) # dizionario namespace globale
    print(vars(test)) # restituisce il __dict__ di un oggetto, se esiste

test()