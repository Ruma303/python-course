# % Modalità di apertura

# , Modalità di lettura file testuali
from pathlib import Path

file = Path.cwd() / "scripts" / "sample.txt"
lorem = Path("scripts", "lorem.txt").resolve()
image = Path("assets", "diamond.png").resolve()

print("ABS text path:\t", str(file))
print("ABS image path:\t", str(file))


# , Metodo read
# with open(file, "rt", encoding="utf-8") as f:
#     contenuto = f.read()
#     print(contenuto, "\n")

## Lettura quantizzata
# with open(file, "rt", encoding="utf-8") as f:
#     read_first_5_characters = f.read(5)
#     print(read_first_5_characters)

#     read_more_characters = f.read(10)
#     print(read_more_characters)


## Lettura riga per riga
# with open(file, "rt", encoding="utf-8") as f:
#   for line in f:
#     print(line.strip())


## Lettura controllata di un file esteso
# try:
#   with open(lorem, "r") as i:
#     while True:
#       chunk = i.read(1024)
#       if not chunk: break
#       print(chunk)
# except FileNotFoundError as err:
#   print("File non trovato")


# , Metodo readline

## Singola riga
# with open(file, "rt", encoding="utf-8") as f:
#     riga = f.readline()
#     print(riga)


## Lettura di più righe in sequenza
with open(file, "rt", encoding="utf-8") as f:
    print(f.readline().rstrip())  # riga 1
    print(f.readline().rstrip())  # riga 2
    print(f.readline())  # riga 3


## Iterazione righe
with open(file, "rt", encoding="utf-8") as f:
    while True:
        riga = f.readline()
        if not riga:
            break
        print(riga.strip())


# , Metodo readlines()
## Restituzione lista di linee
with open(file, "rt", encoding="utf-8") as f:
    righe = f.readlines()
    print(righe)

## Iterazione su linee
with open(file, "rt", encoding="utf-8") as f:
    for riga in f.readlines():
        print(riga.strip())


#, Altri utilizzi generici

## Iterazione riga per riga con conteggio
with open(file, "rt", encoding="utf-8") as f:
    counter = 0
    for line in f:
        print(line.strip())
        counter += 1
    print("Righe:", counter)

with open(file, "rt", encoding="utf-8") as f:
    content = f.readlines()
    print(len(content))
