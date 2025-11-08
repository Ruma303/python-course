from abc import ABC, abstractmethod


class Personaggio(ABC):
    def __init__(self, nome, forza, vita):
        self.nome = nome
        self.forza = forza
        self.vita = vita

    @abstractmethod
    def attacca(self):
        pass


class Guerriero(Personaggio):
    def attacca(self):
        return f"{self.nome} attacca con la spada con una forza di {self.forza}"


class Mago(Personaggio):
    def attacca(self):
        return f"{self.nome} lancia incantesimo con una forza di {self.forza}"


class Ladro(Personaggio):
    """ def attacca(self):
        return f"{self.nome} attacca con la spada con una forza di {self.forza}" """


if __name__ == "__main__":
    aragon = Guerriero("Guerriero", 20, 100)
    gandalf = Mago("Mago", 15, 100)
    legolas = Ladro("Ladro", 10, 100)
    print(aragon.attacca())
    print(gandalf.attacca())
    print(legolas.attacca())
