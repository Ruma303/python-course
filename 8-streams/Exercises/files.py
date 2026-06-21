
#% Files

import os

file_e_contenuti = {
  "dir1/file1.txt" : "Contenuto file 1",
  "dir1/file2.txt" : "Contenuto file 2",
  "dir2/file1.txt" : "Contenuto file 1 della dir 2",
}

for percorso, contenuto in file_e_contenuti.items():
  cartella = os.path.dirname(percorso)
  if not os.path.exists(cartella):
    os.makedirs(cartella)
  with open(percorso, "a") as file:
    file.write(contenuto)
  print(f"File {percorso} creato correttamente")