
#% Attributi di classe
class MyClass:
    myAttr = 99

m1 = MyClass(); m2 = MyClass()

print(MyClass.myAttr) # 99
print(m1.myAttr) # 99
print(m2.myAttr) # 99

## Verifica degli scopes
print(m1.__dict__) # {} vuoto
print(m1.__class__.__dict__) # contiene 'myAttr': 99


#, Modifica livello di classe
MyClass.myAttr = 100
print(MyClass.myAttr) # 100
print(m1.myAttr) # 100
print(m2.myAttr) # 100


#, Modifica locale per istanza
m1.myAttr = 101
print(m1.myAttr) # 101
print(m2.myAttr) # 100
print(MyClass.myAttr) # 100

print(m1.__dict__) # {'myAttr': 101}
print(m2.__dict__) # {} vuoto


#, Accesso dinamico agli Attributi
class Prova:
    x = 5

print(getattr(Prova, 'x'))       # 5

setattr(Prova, 'x', 20) # Aggiorna valore attributo
setattr(Prova, 'y', "hello") # Crea nuovo attributo
print(Prova.__dict__) # { 'x': 20, 'y': 'hello', altri... }

print(hasattr(Prova, 'x'))       # True

delattr(Prova, 'x')
print(hasattr(Prova, 'x'))       # False


#% Metodi di classe
class MethodClass:

    @classmethod
    def class_method(cls, arg1):
        print(f"Metodo della classe {cls.__name__} e parametro: {arg1}")

MethodClass.class_method('Argomento 1')


#, Esempi
class Counter:
    counter = 0

    def __new__(cls):
        cls.counter += 1

    def __init__(self):
        pass
        # Counter.counter += 1
        # __class__.counter += 1

    @classmethod
    def instances(cls):
        print(f"Numero di istanze prodotte {cls.counter}")

c1 = Counter(); c2 = Counter(); c3 = Counter()
Counter.instances()


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


#, Metodi statici
class MyClass:

    @staticmethod
    def somma(a, b):
        return a + b

print(MyClass.somma(10, 20)) # 30

class StaticMethod:

    @staticmethod
    def static_method(val):
        return val

print(StaticMethod.static_method("Hello World"))
