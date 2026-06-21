
#% class
class NomeClasse:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def metodo(self):
        print(f"Metodo invocato. Valori degli argomenti: {1}, {2}", self.arg1, self.arg2)


#, Definizione membri di classe
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo  {self.nome} e ho {self.eta} anni")


## Istanziamento della classe Persona
persona1 = Persona("Luca", 30)
persona1.saluta()


#, Membri di classe e di istanza
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


#, Class body
class Esempio:
    x = 10
    def stampa(self):
        print(self.x)


#, Scope e visibilità
x = 5

class Prova:

    def stampa_x(self):
        print(x) # accede a x definita nel modulo

prova = Prova()
prova.stampa_x()


#, Classi come first-class objects
def aggiungi_metodo(cls):
    def nuovo_metodo(self):
        return "Metodo Aggiunto"
    cls.metodo = nuovo_metodo
    return cls

@aggiungi_metodo
class Prova:
    pass

p = Prova()
print(p.metodo())  # Metodo Aggiunto


#, Esecuzione immediata
class Test:
    print("Classe in fase di definizione")
    valore = 42

print(Test.valore)
