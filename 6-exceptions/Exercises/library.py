"""
Creare un programma per gestire una piccola libreria.

1. Creare un dizionario per memorizzare i libri, utilizzando il titolo del libro come chiave e il numero di copie disponibili come valore.
2. Implementare le seguenti operazioni:
  1. aggiungere nuovo libro con titolo e numero di copie disponibili.
  2. visualizzare elenco dei libri disponibili
  3. cercare un libro per titolo, questo deve restituire il numero di copie disponibili
  4. rimuovere un libro cercandolo per titolo
3. Gestire adeguatamente tutte le eccezioni
4. Consentire al programma di chiedere più volte l'operazione da fare o il titolo da cercare, prima di uscire
5. Opzionalmente, implementare altre funzionalità di cortesia come aggiornare o sostituire il numero di copie
"""

def choice():
    while True:
        try:
            scelta = int(input(
                "\nScegli quale operazione effettuare:"
                "\n\t1. Aggiungi un nuovo libro"
                "\n\t2. Visualizza elenco dei libri disponibili"
                "\n\t3. Cerca un libro"
                "\n\t4. Rimuovi un libro"
                "\n\t5. Esci dal programma"
                "\nLa tua scelta: "
            ).strip())
            if 1 <= scelta <= 5:
                return scelta
            else:
                print("Inserisci un numero tra 1 e 5.")
        except ValueError:
            print("Inserisci un valore numerico valido.")

def add(library):
    titolo = input("Digita il titolo del libro: ").strip()
    if not titolo:
        print("Il titolo non può essere vuoto.")
        return
    try:
        copie = int(input("Digita il numero di copie da inserire: ").strip())
        if copie < 1:
            print("Il numero di copie deve essere almeno 1.")
            return
    except ValueError:
        print("Inserisci un numero di copie valido.")
        return
    titolo_normalizzato = titolo.lower()
    if titolo_normalizzato in library:
        print(f"Il libro '{titolo}' esiste già con {library[titolo_normalizzato]} copie.")
        aggiornamento = input("Vuoi aggiungere le nuove copie (a) o sovrascrivere il numero (s)? [a/s]: ").strip().lower()
        if aggiornamento == "a":
            library[titolo_normalizzato] += copie
            print(f"Numero di copie aggiornato a {library[titolo_normalizzato]} per il libro '{titolo}'.")
        elif aggiornamento == "s":
            library[titolo_normalizzato] = copie
            print(f"Numero di copie sovrascritto a {copie} per il libro '{titolo}'.")
        else:
            print("Operazione annullata.")
    else:
        library[titolo_normalizzato] = copie
        print(f"Hai inserito correttamente il libro '{titolo}' con {copie} copie.")

def show(library):
    if not library:
        print("La libreria è vuota.")
        return
    print("\nElenco dei libri disponibili:")
    for idx, (titolo, copie) in enumerate(library.items(), 1):
        print(f"{idx}. {titolo.title()} - {copie} copie disponibili")

def lookup(library):
    titolo = input("Digita il titolo del libro da cercare: ").strip()
    if not titolo:
        print("Il titolo non può essere vuoto.")
        return
    titolo_normalizzato = titolo.lower()
    if titolo_normalizzato in library:
        print(f"Libro '{titolo}' trovato con {library[titolo_normalizzato]} copie disponibili.")
    else:
        print(f"Libro '{titolo}' non trovato nella libreria.")

def delete(library):
    titolo = input("Digita il titolo del libro da rimuovere: ").strip()
    if not titolo:
        print("Il titolo non può essere vuoto.")
        return
    titolo_normalizzato = titolo.lower()
    if titolo_normalizzato in library:
        del library[titolo_normalizzato]
        print(f"Libro '{titolo}' rimosso dalla libreria.")
    else:
        print(f"Libro '{titolo}' non trovato nella libreria.")

def main():
    print("Benvenuto nella libreria!")
    library = {}
    while True:
        scelta = choice()
        if scelta == 1:
            add(library)
        elif scelta == 2:
            show(library)
        elif scelta == 3:
            lookup(library)
        elif scelta == 4:
            delete(library)
        elif scelta == 5:
            print("Grazie per aver visitato la nostra libreria!")
            break

if __name__ == "__main__":
    main()