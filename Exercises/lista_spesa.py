"""
Creare un programma che chieda costantemente di aggiungere elementi alla lista della spesa.
Quando viene scritta la parola "fine", non aggiungere più niente e mostrare la lista.
"""

shopping_list = []

while True:
  item = input("Inserisci un elemento nella lista della spesa: ").strip()
  if item.lower() == "fine":
    print("Tutta la lista della spesa:\n", shopping_list)
    break
  shopping_list.append(item)
