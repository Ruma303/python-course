
#% Dataclasses

from dataclasses import dataclass

@dataclass(init=True, repr=True, eq=True, order=True, frozen=False)
class Persona:
    nome: str
    cognome: str
    eta: int = 18 # Valori di default

p1 = Persona(nome="Giulio", cognome="Verne")
p2 = Persona(nome="Mario", cognome="Rossi")

print(p1)        # Persona(nome='Giulio', cognome='Verne')
print(p2)        # Persona(nome='Mario', cognome='Rossi')
print(p1 == p2)  # False


#, Classi immutabili
@dataclass(init=True, frozen=True)
class Record:
    id_number: int
    author: str

r1 = Record(1, "John")
# r1.id_number = 2 # Errore: Genera dataclasses.FrozenInstanceError