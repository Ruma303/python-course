# % Ereditarietà


# , Ereditarietà e istanze
class Parent:
    pass


class Child(Parent):
    pass


m1 = Child()

print(isinstance(m1, Child))  # True
print(isinstance(m1, Parent))  # True


# , Ereditarietà di metodi


## Uso diretto
class MessageParent:
    def setMessage(self, message):
        self.message = message

    def printMessage(self):
        print(self.message)


class MessageChild(MessageParent):
    pass


m1 = MessageChild()
m1.setMessage("python")
m1.printMessage()  # Output: python


## Override
class Human:
    def saluta(self):
        print("Ciao da Human")


class Person(Human):
    def saluta(self):  # override
        print("Ciao da Person")


p1 = Person()
p1.saluta()  # "Ciao da Person"


## Estensione con super()
class Animal:

    def __init__(self, limbs=None):
        self.limbs = None
        print("Inizializzatore di Animal class")


class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.limbs = 4
        print("Inizializzatore di Dog class")

animal = Animal()
print(animal.limbs) # None

dog = Dog()
print(dog.limbs) # 4
print(issubclass(Dog, Animal)) # True


#, Ereditarietà multipla

class BClass:
    b = 10
    def bFunc(self):
        print("Sono in bFunc")
    def xFunc(self):
        print("Sono in BClass")

class CClass:
    c = 20
    def cFunc(self):
        print("Sono in cFunc")
    def xFunc(self):
        print("Sono in CClass")

class AClass(BClass, CClass):
    pass

a = AClass()
print(a.b)         # 10
print(a.c)         # 20
a.bFunc()          # Sono in bFunc
a.cFunc()          # Sono in cFunc
a.xFunc()          # Sono in BClass


## MRO
print(AClass.__mro__)
# oppure
# help(AClass)

## Utilizzo con super()
class A:
    def x(self):
        print("A")

class B(A):
    def x(self):
        print("B")
        super().x()

class C(A):
    def x(self):
        print("C")
        super().x()

class D(B, C):
    def x(self):
        print("D")
        super().x()

d = D()
d.x()