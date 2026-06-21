
# % Properties

# , Attributi privati
class Libro:
    def __init__(self, titolo, autore, rating):
        self.titolo = titolo  # membro pubblico
        self._autore = autore  # membro "protetto"
        self.__rating = rating  # membro "privato"

libro = Libro("1984", "Orwell", 9)
print(libro.titolo)          # Accesso libero
print(libro._autore)         # Accessibile, ma sconsigliato fuori dalla classe
print(libro._Libro__rating)  # Accessibile, ma sconsigliato fuori dalla classe

class Libricino(Libro):
    def __init__(self):
        print(libro._autore)        # Accesso a membro privato
        print(libro._Libro__rating) # Accesso tramite name mangling

print(Libricino())


#, property()
class MyClass:
    def __init__(self, my_attr):
        self._priv_attr = my_attr

    def get_attr(self):
        return self._priv_attr

    def set_attr(self, value):
        self._priv_attr = value

    attr = property(get_attr, set_attr)

obj = MyClass("python")
print(obj.attr)        # python  (usa get_attr)

## Accesso con property()
obj.attr = "prova"     # (usa set_attr)
print(obj.attr)        # prova

## Accesso diretto
obj.set_attr("manuale")     # accesso diretto al setter
print(obj.get_attr())       # accesso diretto al getter
obj._priv_attr = "forzato"  # accesso diretto all'attributo (sconsigliato)
print(obj._priv_attr)


#, @property
class Prodotto:
    def __init__(self, prezzo):
        self.__prezzo = prezzo

    @property
    def prezzo(self):
        print("Accesso al prezzo")
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, valore):
        if valore < 0:
            raise ValueError("Il prezzo non può essere negativo")
        print("Modifica del prezzo")
        self.__prezzo = valore

    @prezzo.deleter
    def prezzo(self):
        print("Eliminazione del prezzo")
        del self.__prezzo


p = Prodotto(100)
print(p.prezzo)  # Accesso al prezzo → 100
p.prezzo = 150   # Modifica del prezzo
print(p.prezzo)
# p.prezzo = -10   # ValueError

del p.prezzo
print(p.__dict__) # {} nessun attributo