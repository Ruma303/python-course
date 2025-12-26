"""Documentazione del modulo docstrings"""

#% Docstrings - Documentare il codice

def saluta(nome):
    """
    Questa funzione stampa un saluto personalizzato.

    Parametri:
    nome (str): Il nome della persona da salutare.

    Ritorno:
    str: Una stringa che contiene il saluto personalizzato.
    """
    return f"Ciao, {nome}!"

print(saluta("Mario"))

# Leggere la documentazione
print(saluta.__doc__)
# print(help(saluta))


#, Contesti
"""Modulo di esempio per la documentazione."""

class Libro:
    """Rappresenta un libro con titolo e autore."""
    def __init__(self, titolo, autore):
        """Inizializza il libro con titolo e autore."""
        self.titolo = titolo
        self.autore = autore

    def descrivi(self):
        """Restituisce una descrizione testuale del libro."""
        return f"{self.titolo} di {self.autore}"


# Formattazione e convenzioni
def funzione(par1, par2):
	"""
	Descrizione breve.

	Args:
		par1 (int): Descrizione di par1.
		par2 (str): Descrizione di par2.

	Returns:
		bool: Descrizione del valore di ritorno.
	"""
