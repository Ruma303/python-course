
#% class 
class NomeClasse:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def metodo(self):
        print(f"Metodo invocato. Valori degli argomenti: {1}, {2}", self.arg1, self.arg2)


# Definizione membri di classe
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
    
    def saluta(self):
        print(f"Ciao, mi chiamo  {self.nome} e ho {self.eta} anni")

# Istanziamento della classe Persona
persona1 = Persona("Luca", 30)
persona1.saluta()


# Attributi di istanza e di classe
class Auto:
    ruote = 4

    def __init__(self, marca):
        self.marca = marca

auto1 = Auto("Fiat")
auto2 = Auto("BMW")

print(auto1.ruote)
print(auto2.ruote)
print(auto1.marca)
print(auto2.marca)


# Scope e visibilità
x = 5

class Prova:

    def stampa_x(self):
        print(x) # accede a x definita nel modulo

prova = Prova()
prova.stampa_x()


# Esecuzione immediata
class Test:
    print("Classe in fase di definizione")
    valore = 42 

print(Test.valore)


#% Attributi di classe
class MyClass:
    myAttr = 99

m1 = MyClass(); m2 = MyClass()
print(MyClass.myAttr) # 99
print(m1.myAttr) # 99
print(m2.myAttr) # 99

# Modifica locale
m1.myAttr = 100
print(MyClass.myAttr) # 99
print(m1.myAttr) # 100
print(m2.myAttr) # 99

# Accesso dinamico agli Attributi

print(getattr(MyClass, 'myAttr'))

setattr(MyClass, 'myAttr', 20)
print(MyClass.myAttr)

print(hasattr(MyClass, 'myAttr'))
print(hasattr(MyClass, 'valore'))

delattr(MyClass, 'myAttr')
print(hasattr(MyClass, 'myAttr'))


#% Metodi di istanza
class InstanceMethod:
    def myMethod(self):
        print("Chiamato da", id(self))

m3 = InstanceMethod()
m4 = InstanceMethod()
m3.myMethod()
m4.myMethod()

# Ispezione
print(type(m3.myMethod)) # <class 'method'>
print(type(InstanceMethod.myMethod)) # <class 'function'>

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


#% Metodi di classe
class MethodClass:

    @classmethod
    def class_method(cls, arg1):
        print(f"Metodo della classe {cls} e parametro: {arg1}")

MethodClass.class_method('Argomento 1')

# Esempio
class Counter:
    counter = 0

    def __init__(self):
        Counter.counter += 1

    @classmethod
    def instances(cls):
        print(f"Numero di instanze prodotte {cls.counter}")

c1 = Counter(); c2 = Counter(); c3 = Counter()
Counter.instances()


# Metodi statici
class StaticMethod:
    @staticmethod
    def static_method(val):
        return val

print(StaticMethod.static_method("Hello World"))


class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    @classmethod
    def da_stringa(cls, stringa):
        nome, eta = stringa.split(",")
        return cls(nome, int(eta))

p = Persona.da_stringa("Mario,40")
print(p.nome)  # Mario
print(p.eta)   # 40
