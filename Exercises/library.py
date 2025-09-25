"""
1. Creare una lista con dei libri
2. Da terminale chiedere un libro
3. Verificare se il libro esiste e mostrare posizione e dettagli interni
4. Opzionalmente, chiedere nuovamente se continuare a cercare altri libri
"""

libreria = {
    "Il Signore degli Anelli": {"autore": "J.R.R. Tolkien", "copie": 3},
    "1984": {"autore": "George Orwell", "copie": 5},
    "Il Grande Gatsby": {"autore": "F. Scott Fitzgerald", "copie": 2},
}

chiedi = True
while chiedi == True:
  titolo = input("Inserisci il titolo di un libro da cercare: ").strip().lower()

  trovato = None
  for libro in libreria:
      if libro.lower() == titolo:
          trovato = libro
          break

  if trovato:
      print(f"Trovate {libreria[trovato]['copie']} copie di {trovato} dell'autore {libreria[trovato]['autore']}")
  else:
      print("Libro non trovato")
  scelta = input("\nVuoi cercare un altro libro? Rispondi si o no: ").strip().lower()
  if scelta == "si":
      pass
  elif scelta == "no":
      chiedi = False
      print("Grazie per averci visitato. A presto!")
      break
