
#% Il costruttore

class MyClass:
    def __init__(self, message):
        self.message = message

    def printMessage(self):
        print(self.message)

# m1 = MyClass() Caso errato, manca l'argomento message

m1 = MyClass("primo")
m2 = MyClass("secondo")

m1.printMessage()  # Stampa: primo
m2.printMessage()  # Stampa: secondo



#, Parametri opzionali e valori di default nel costruttore
class MyClass:
    def __init__(self, message="Nessun messaggio"):
        self.message = message

    def printMessage(self):
        print(self.message)

a = MyClass()
b = MyClass("Benvenuto")

a.printMessage()  # Stampa: Nessun messaggio
b.printMessage()  # Stampa: Benvenuto


#, Verifica del tipo o del contenuto del parametro
class MyClass:
    def __init__(self, message):
        if not isinstance(message, str):
            raise TypeError("message deve essere una stringa")
        self.message = message

# m = MyClass(123)  # TypeError: message deve essere una stringa


#% Il ciclo di creazione degli oggetti in Python:

#, Istanza personalizzata
class MyClass:
    def __new__(cls):
        istanza = super().__new__(cls)
        print("istanza creata")
        return istanza

    def __init__(self):
        print("istanza inizializzata")

mc = MyClass()


#, Esempio errato, new non restituisce nulla
class MyClass:
    def __new__(cls):
        print("istanza creata")
        # manca il return

    def __init__(self):
        print("istanza inizializzata")

mc = MyClass()


#, Esempio con argomenti
class MyClass:
    def __new__(cls, message):
        istanza = super().__new__(cls)
        print("istanza creata riceve il parametro: ", message)
        return istanza

    def __init__(self, message):
        self.message = message
        print("istanza inizializzata con messaggio:", self.message)

mc = MyClass("Python")


#, Esempi concreti di utilizzo di new

## Implementazione di un Singleton
class Singleton:
    _istanza = None

    def __new__(cls):
        if cls._istanza is None:
            cls._istanza = super().__new__(cls)
        return cls._istanza

    def __init__(self, valore=0):
        self.valore = valore
        print("inizializzazione")

    def set_val(self, valore):
        self.valore = valore

a = Singleton()
# b = Singleton(10) # Errore
b = Singleton()

print(a is b)  # True
print(a.valore)  # 0
a.set_val(10)
print(a.valore)  # 10


## Subclassing di tipi immutabili
class MiaStringa(str):
    def __new__(cls, valore):
        valore = valore.upper()
        return super().__new__(cls, valore)

s = MiaStringa("ciao mondo")
print(s)  # CIAO MONDO


## Validazione o controllo della creazione
class NonNegativo:
    def __new__(cls, valore):
        if valore < 0:
            raise ValueError("Il valore deve essere non negativo")
        return super().__new__(cls)

    def __init__(self, valore):
        self.valore = valore

try:
    x = NonNegativo(-5)
except ValueError as e:
    print(e)


## Factory Pattern
class A:
    def __new__(cls, tipo):
        if tipo == "B":
            return B()
        return super().__new__(cls)

class B:
    pass

a = A("B")
print(type(a))  # <class '__main__.B'>