
#% Context manager

from pathlib import Path

file_path = Path.cwd() / "scripts" / "sample.txt"

#, Utilizzi context manager
with open(file_path, "r", encoding="utf-8") as file_obj:
    print(file_obj.encoding)
    print(file_obj.read())

with open(file_path, "rt") as f:
    text = f.read(5)
    print(text) # Hello

with open(file_path, "rt") as f:
    line = f.readline()
    print(line)


## Iterare
with open(file_path, "rt") as f:
    counter = 0
    for line in f:
        line = line.strip()
        print(line)
        counter += 1
    print("Righe:", counter)

with open(file_path, "rt") as f:
    for line in f.readlines():
        line = line.strip()
        print(line)


#, Implementazione personalizzata
class MyContext:
    def __enter__(self):
        print("Entrato nel contesto")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Uscito dal contesto")

with MyContext():
    print("Dentro il blocco")


#, Gestione delle eccezioni in __exit__()
class SuppressException:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Eccezione gestita:", exc_val)
        return True  # sopprime l’eccezione

with SuppressException() as se:
    raise ValueError(f"Errore di tipo {se.__class__.__name__}")
print("Continuo")



#, @contextmanager

## Esempio basilare
from contextlib import contextmanager

@contextmanager
def apri_file(path):
    f = open(path, "r", encoding="utf-8")
    try:
        yield f
    finally:
        f.close()

with apri_file(file_path) as f:
    print(f.read())


## Esempio: Gestione delle eccezioni
from contextlib import contextmanager

@contextmanager
def gestisci_file(path):
    f = open(path, "r")
    try:
        yield f
    except UnicodeDecodeError:
        print("Errore di codifica nel file.")
    finally:
        f.close()

## Esempio: Context manager per il cambio temporaneo di directory
import os
from contextlib import contextmanager

@contextmanager
def cambia_directory(path):
    vecchia = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(vecchia)

with cambia_directory("/tmp"):
    # Qui siamo temporaneamente in /tmp
    print(os.getcwd())
# Qui si torna alla directory originale

## Esempio: Context manager per il lock di un threading.Lock
import threading
from contextlib import contextmanager

@contextmanager
def lock_acquisito(lock):
    lock.acquire()
    try:
        yield
    finally:
        lock.release()

lock = threading.Lock()
with lock_acquisito(lock):
    # Operazioni thread-safe
    pass