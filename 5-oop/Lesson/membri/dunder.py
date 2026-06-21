
#% Membri dunder

#, str e repr

## Esempio repr
class MyClass:
    pass

obj = MyClass()
print(obj)  # <__main__.MyClass object at 0x...>


## Differenza str e repr
class MyClass:
    def __init__(self, valore):
        self.valore = valore

    def __str__(self):
        return f"Valore: {self.valore}"

    def __repr__(self):
        return f"{self.__class__} con valore: {self.valore}"

obj = MyClass(125)
print(obj)        # Valore: 125
print(str(obj))   # Valore: 125
print(repr(obj))  # <class '__main__.MyClass'> con valore: 125


## repr come fallback in assenza di str
class MyClass:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"MyClass({self.x})"

obj = MyClass(10)
print(obj)           # MyClass(10)


## Implementazione robusta consigliata
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def __str__(self):
        return f"Coordinate: ({self.x}, {self.y})"

p1 = Punto(3, 4)
print(p1)           # Coordinate: (3, 4)
print(repr(p1))     # Punto(3, 4)

p2 = eval(repr(p1)) # Ricostruzione dell'oggetto se Punto è definito
print(p2)           # Coordinate: (3, 4)
print(p2 == p1)     # False (a meno di definire __eq__)


#, dict
class Automobile:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

mia_auto = Automobile("Toyota", "Yaris")
print(mia_auto.__dict__)

## Modifica dict
mia_auto.__dict__["anno"] = 2010
print(mia_auto.anno)  # 2010

mia_auto.colore = "rosso"
print(mia_auto.__dict__)  # {'marca': 'Toyota', 'modello': 'Yaris', 'anno': 2010, 'colore': 'rosso'}

## Clonazione oggetti
# nuova_auto = Automobile(**mia_auto.__dict__)

for k, v in {"anno": 2010, "colore": "rosso"}.items():
    setattr(mia_auto, k, v)

## Accesso programmatico
for chiave, valore in mia_auto.__dict__.items():
    print(f"{chiave}: {valore}")


#, slots
class Automobile:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

mia_auto = Automobile("Toyota", "Yaris")
mia_auto.anno = 2010  # aggiunto dinamicamente
print(mia_auto.anno)  # 2010

print(mia_auto.__dict__)
# {'marca': 'Toyota', 'modello': 'Yaris', 'anno': 2010}

# sua_auto = Automobile("Honda", "Civic")
# print(sua_auto.anno)  # AttributeError: 'Automobile' object has no attribute 'anno'

## Uso di slots
class Automobile:
    __slots__ = ["marca", "modello"]

    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

mia_auto = Automobile("Toyota", "Yaris")
# mia_auto.anno = 2010 # AttributeError: 'Automobile' object has no attribute 'anno'

print(mia_auto.__slots__)   # ['marca', 'modello']
# oppure sulla classe
print(Automobile.__slots__) # ['marca', 'modello']

# print(mia_auto.__dict__)  # Non possibile
print(dir(mia_auto))        # Mostra tutti i nomi nello scope
