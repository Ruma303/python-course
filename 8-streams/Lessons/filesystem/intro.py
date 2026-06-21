
#% Introduzione filesystem


#, Lettura da file
file_obj = open("sample.txt", "r")
print(file_obj.read())
file_obj.close()

## Chiusura
f = open("sample.txt", "r")
# operazioni di lettura/scrittura
f.close()

#, Percorsi
from pathlib import Path

cwd = Path.cwd()
print(cwd) # Current working directory

import os
print(os.path.abspath("script.py"))  # Restituisce il percorso assoluto


#, Error handling
try:
    f = open("non_esiste.txt", "r")
except FileNotFoundError as e:
    print("Errore:", e)


#, Uso del context manager
with open("sample.txt", "r") as f:
    contenuto = f.read()
    print(contenuto)
# il file viene chiuso automaticamente