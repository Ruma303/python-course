import pathlib

## Creare cartelle
dirs = [
  "dir1",
  "dir2",
  "dir3"
]

for singledir in dirs:
  path = pathlib.Path(singledir)
  try:
    path.mkdir(exist_ok=True)
    pathlib.Path(singledir).mkdir()
  except PermissionError:
    print("Operazione non concessa")
  except FileExistsError:
    print("Cartella già esistente")
  except Exception as e:
    print(f"Errore: {e}")