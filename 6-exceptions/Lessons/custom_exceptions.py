
#% Eccezioni personalizzate

#, Creazione classe personalizzata
# class CustomError(Exception):
#     def __init__(self, message="Errore personalizzato"):
#         super().__init__(message)
#         self.message = message

#     def __str__(self):
#         return f"CustomError: {self.message}"

# x = 1

# try:
#     if x < 10:
#         raise CustomError("x non può essere minore di 10")
#     print("Ok, x è minore di 10")
# except CustomError as error:
#     print(f"Errore rilevato: {error.message}")


#, Eccezioni con dati aggiuntivi
# class RangeError(Exception):
#     def __init__(self, valore, minimo, massimo):
#         self.valore = valore
#         self.minimo = minimo
#         self.massimo = massimo
#         super().__init__(f"Valore {self.valore} errato.")

#     def __str__(self):
#         return f"Valore {self.valore} fuori dal range {self.minimo}-{self.massimo}"

# try:
#     x = 15
#     if not (0 <= x <= 10):
#         raise RangeError(x, 0, 10)
# except RangeError as e:
#     print(e)  # Valore 15 fuori dal range 0-10
#     print(e.valore, e.minimo, e.massimo)


## Esempio: uso avanzato in un’applicazione
# class NegativeCopiesError(Exception):
#     def __init__(self, copie):
#         self.copie = copie
#         super().__init__(f"Numero di copie non valido: {copie}")

# def aggiungi_libro(library, titolo, copie):
#     if copie < 0:
#         raise NegativeCopiesError(copie)
#     library[titolo] = copie

# try:
#     aggiungi_libro({}, "1984", -5)
# except NegativeCopiesError as e:
#     print(e)  # Numero di copie non valido: -5