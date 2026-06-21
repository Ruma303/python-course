from abc import ABC, abstractmethod


class Personaggio(ABC):
    def __init__(self, nome, forza, vita):
        self.nome = nome
        self.forza = forza
        self.vita = vita

    @abstractmethod
    def attacca(self):
        pass

    # Implementazione di default
    @abstractmethod
    def descrizione(self):
        print("Personaggio di base")


class Guerriero(Personaggio):
    def attacca(self):
        return f"{self.nome} attacca con la spada con una forza di {self.forza}"

    def descrizione(self):
        print(f"{self.nome} ha vita iniziale: {self.vita}")


class Mago(Personaggio):
    def attacca(self):
        return f"{self.nome} lancia incantesimo con una forza di {self.forza}"

    def descrizione(self):
        print(f"{self.nome} ha vita iniziale: {self.vita}")


class Ladro(Personaggio):
    def attacca(self):
        return f"{self.nome} attacca con la spada con una forza di {self.forza}"

    def descrizione(self):
        print(f"{self.nome} ha vita iniziale: {self.vita}")


if __name__ == "__main__":

    aragon = Guerriero("Guerriero", 20, 100)
    gandalf = Mago("Mago", 15, 100)
    legolas = Ladro("Ladro", 10, 100)

    print(aragon.descrizione())
    print(gandalf.descrizione())
    print(legolas.descrizione())

    print(aragon.attacca())
    print(gandalf.attacca())
    print(legolas.attacca())


#% Protocolli
from typing import Protocol

class Scrivibile(Protocol):
    def write(self, testo: str) -> None: ...

class FileScrivibile:
    def write(self, testo: str) -> None:
        print(f"Scrivo: {testo}")

def scrivi_qualcosa(s: Scrivibile):
    s.write("Ciao")

f = FileScrivibile()
scrivi_qualcosa(f)  # Accettato dal type checker