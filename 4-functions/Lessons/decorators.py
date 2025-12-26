
#% Decoratori

## Esempio base
def decoratore(funzione):
    def wrapper():
        print("Prima della funzione")
        funzione()
        print("Dopo la funzione")
    return wrapper

@decoratore
def saluto():
    print("Ciao!")

saluto()


## Decorare manualmente
def myDecorator(f):
    def decorator():
        print('ho decorato')
        f()
    return decorator

def myFunc():
    print('la funzione myFunc')

myFunc = myDecorator(myFunc)
myFunc()


## Decoratori con argomenti
def decoratore(f):
    def wrapper(*args):
        print("Chiamata a funzione con decoratore")
        return f(*args)
    return wrapper

@decoratore
def somma(a, b):
    return a + b

print(somma(2, 3))


## Decoratori annidati (multipli)
def decoratore1(f):
    def wrapper(*args):
        print("decoratore1")
        return f(*args)
    return wrapper

def decoratore2(f):
    def wrapper(**kwargs):
        print("decoratore2")
        return f(**kwargs)
    return wrapper

@decoratore1
@decoratore2
def funzione():
    print("Funzione decorata")

funzione()


## Decoratori con parametri
def ripeti(n):
    def decoratore(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return wrapper
    return decoratore

@ripeti(3)
def saluta():
    print("Ciao!")

saluta()


## Decoratori e functools.wraps
import functools

def decoratore(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print("Decorato")
        return f(*args, **kwargs)
    return wrapper

@decoratore
def saluta():
    """Stampa un saluto."""
    print("Ciao!")

print(saluta.__name__)     # saluta
print(saluta.__doc__)      # Stampa un saluto.


## Decoratori come oggetti di classe (callable)
class Decoratore:
    def __init__(self, funzione):
        self.funzione = funzione

    def __call__(self, *args, **kwargs):
        print("Inizio")
        risultato = self.funzione(*args, **kwargs)
        print("Fine")
        return risultato

@Decoratore
def saluta():
    print("Ciao!")

saluta()