
#% Modulo pathlib

from pathlib import Path

## Costruzione e rappresentazione
p = Path("data") / "file.txt"  # Concatenazione dentro o fuori Path()
print(p)  # data/file.txt (Unix) o data\file.txt (Windows)
print(p.resolve())  # percorso assoluto

cwd = p.cwd()  # Current working directory
print(cwd)

p = Path("/home/user/file.txt")

## Oggetti
print(p.name)  # 'file.txt'
print(p.stem)  # 'file'
print(p.suffix)  # '.txt'
print(p.parent)  # '/home/user' Path
print(p.parents) # A sequence of this path's logical parents. <PosixPath.parents>
print(p.parts)  # ('/', 'home', 'user', 'file.txt')

file_path = Path(cwd, "scripts", "sample.txt")
print(file_path)

## Home directory dell’utente
home = Path.home()
print(home)

## Navigazione
p = cwd / "data" / "file.csv"
print(p)

## Confronto tra percorsi
p1 = Path("/home/user/file.txt")
p2 = Path("/home/user/./file.txt")
p3 = Path("/home/user/file.txt").resolve()

print("confronto p1 e p2", p1 == p2) # True

## Verifica oggetti
print(file_path.exists())  # True se esiste
print(file_path.is_file())  # True se è file
print(file_path.is_dir())  # True se è directory

## Creazione directory (ricorsiva)
p = Path("logs/2024/giugno")
p.mkdir(parents=True, exist_ok=True)

## Operazioni sui file con Path
file_path = Path(p, "output.txt")

# Scrittura
file_path.write_text("Contenuto", encoding="utf-8")

# Lettura
contenuto = file_path.read_text(encoding="utf-8")

# Apertura come file object
with file_path.open("r", encoding="utf-8") as f:
    dati = f.read()

## Iterazione su directory
for file in file_path.parent.iterdir():
    print(file.name)

for file in file_path.glob("*.txt"):
    print(file.name)

for file in file_path.rglob("*.py"):  # ricerca ricorsiva
    print(file)

## Conversione tra str e Path
stringa = str(file_path)
print(type(stringa))

# da stringa a Path
p2 = Path(stringa)
print(type(p2))

## Accesso avanzato ai metadati
file_path.stat().st_size       # dimensione in byte
file_path.stat().st_mtime      # ultima modifica (timestamp UNIX)
file_path.stat().st_ctime      # creazione (Windows) o metadata change (Unix)

for f in file_path.parents:
    print(f.name, f.stat().st_size, "bytes")


## Rimozione e operazioni distruttive
file_path.unlink()  # elimina file

d = Path(file_path.parent)
d.rmdir()   # elimina directory vuota