
#% Metodi di istanza
class InstanceMethod:
    def myMethod(self):
        print("Chiamato da", id(self))

m1 = InstanceMethod()
m2 = InstanceMethod()

m1.myMethod()
m2.myMethod()


#, Introspezione
print(type(m1.myMethod))             # <class 'method'>
print(type(InstanceMethod.myMethod)) # <class 'function'>

print(m1.myMethod.__self__)    # <__main__.InstanceMethod object at 0x10...>
print(m1.myMethod.__func__)    # <function InstanceMethod.myMethod at 0x10...>


#, Ispezione
class Contatore:
    def __init__(self):
        self.valore = 0

    def incrementa(self):
        self.valore += 1

    def mostra(self):
        print(self.valore)

c = Contatore()
c.incrementa()
c.incrementa()
c.mostra()  # 2


#, Overload dei metodi
"""
class Person:
    def saluta(self):
        print("Saluto base")

    def saluta(self):
        print("Saluto base sovrascritto")

    def saluta(self, name):
        print(f"Saluto {name}")

    def saluta(self, id):
        print(f"Saluto random a utente con id: {id}")

p = Person()

p.saluta()
p.saluta("Andrea")
p.saluta(20)
"""

## Soluzione 1
class Person:
    def saluta(self, arg=None):
        if arg is None:
            print("Saluto base")
        elif isinstance(arg, str):
            print(f"Saluto {arg}")
        elif isinstance(arg, int):
            print(f"Saluto random a utente con id: {arg}")
        else:
            print("Saluto sconosciuto")

p = Person()
p.saluta()           # Saluto base
p.saluta("Andrea")   # Saluto Andrea
p.saluta(20)         # Saluto random a utente con id: 20


## Soluzione 2
class Person:
    def saluta(self, *args, **kwargs):
        if not args:
            print("Saluto base")
        elif len(args) == 1 and isinstance(args[0], str):
            print(f"Saluto {args[0]}")
        elif len(args) == 1 and isinstance(args[0], int):
            print(f"Saluto random a utente con id: {args[0]}")
        else:
            print("Saluto sconosciuto")

p = Person()
p.saluta()
p.saluta("Andrea")
p.saluta(20)


## Soluzione 3
"""
from functools import singledispatchmethod

class Person:
    @singledispatchmethod
    def saluta(self, arg):
        print("Saluto sconosciuto")

    @saluta.register
    def _(self, name: str):
        print(f"Saluto {name}")

    @saluta.register
    def _(self, id: int):
        print(f"Saluto random a utente con id: {id}")

    @saluta.register
    def _(self):
        print("Saluto base")

p = Person()
p.saluta()
p.saluta("Andrea")
p.saluta(20)
"""

## Soluzione 4
class Person:
    def saluta(self):
        print("Saluto base")

    def saluta_con_nome(self, name):
        print(f"Saluto {name}")

    def saluta_con_id(self, id):
        print(f"Saluto random a utente con id: {id}")

p = Person()
p.saluta()
p.saluta_con_nome("Andrea")
p.saluta_con_id(20)