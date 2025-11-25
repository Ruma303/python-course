"""
1. Creare una classe persona con nome, cognome e codice fiscale
2. Creare degli oggetti studente e insegnante con delle proprietà specifiche aggiunte all'oggetto iniziale
3. Ogni oggetto deve avere un metodo per stampare la sua specifica descrizione
"""

class Persona:
    def __init__(self, nome, cognome, codice_fiscale):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale

    def descrizione(self):
        print("Persona generica")

persona1 = Persona("Mario", "Rossi", "RMRS00")
persona1.descrizione()

class Studente(Persona):
    def __init__(self, nome, cognome, codice_fiscale, classe, voti):
        super().__init__(nome, cognome, codice_fiscale)
        self.classe = classe
        self.voti = voti

    def descrizione(self):
        print(f"Studente {self.nome}")

studente1 = Studente("Luca", "Bianchi", "LBCN2", "2A", [10, 9, 8])
studente1.descrizione()

class Insegnante(Persona):
    def __init__(self, nome, cognome, codice_fiscale, materia, orari):
        super().__init__(nome, cognome, codice_fiscale)
        self.materia = materia
        self.orari = orari

    def descrizione(self):
        print(f"Insegnante {self.nome}")

insegnante1 = Insegnante("Eugenio", "Grigi", "EGGR00", "Matematica", [8, 9, 10])
insegnante1.descrizione()