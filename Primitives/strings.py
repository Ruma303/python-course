# Stringhe

# , Definizione
a = "Ciao"
b = "Mondo"
print(a + " " + b)
c = str("Hello World")


# , Sequenze di escape

## Uso di apici diversi
print('Ciao "Mondo"')
print("Ciao 'Mondo'")
print("Ciao 'Mondo'")
print('Ciao "Mondo"')

escaping_phrase = """
Stiamo scrivendo una stringa multilinea
dove gli apici singoli ' e doppi "
sono automaticamente sfuggiti all'interprete
come se li avessimo preceduti con il backslash \' e \"
"""

print(escaping_phrase)

## Sequenze di escape comuni
print("Ciao\nMondo")  # \n: Nuova linea
print("Ciao\rMondo")  # \r: Ritorno a capo
print("Ciao\tMondo")  # \t: Tabulazione orizzontale
print("Ciaoo\bMondo")  # \b: Backspace (cancella la 'o')
print("Ciao\fMondo")  # \f: Feed di pagina (effetto visivo dipende dal terminale)
print("Ciao\aMondo")  # \a: Campanello (potresti sentire un suono)
print("Ciao\\Mondo")  # \\: Backslash
print("Ciao'Mondo'")  # \': Apostrofo
print('Ciao"Mondo"')  # \": Virgolette


## Valore ottale, esadecimale e Unicode
print("\141")  # \ooo: Valore ottale (141 ottale = 'a')
print("\x61")  # \xhh: Valore esadecimale (61 esadecimale = 'a')
print("\u03a9")  # \uxxxx: Carattere Unicode (Ω)
print("\U0001f600")  # \Uxxxxxxxx: Carattere Unicode esteso (😀)


## Funzione raw
print(r"Ciao\nMondo")
print(r"C:\Desktop\Dir")  # Output: C:\Desktop\Dir


# , Proprietà delle stringhe

## Immutabilità
stringa = "Ciao"
# Questo solleva un errore
# stringa[0] = 'P' non è possibile sostituire un carattere di una stringa

# Creazione di una nuova stringa
nuova_stringa = "P" + stringa[1:]
print(nuova_stringa)  # 'Piao'


## Lunghezza
stringa = "Buongiorno a tutti"
lunghezza = len(stringa)
print(lunghezza)  # 18


## String interpolation
name = "John"
age = 30
print("Ciao, sono " + name + " e ho " + str(age) + " anni.")


## Concatenazione
stringa1 = "Ciao"
stringa2 = "Python"
risultato = stringa1 + " " + stringa2
print(risultato)  # 'Ciao Python'

# print('ciao ' + type('ciao')) TypeError


## Controllo di appartenenza
stringa = "Ciao Python"
print("Python" not in stringa)  # False
print("Java" not in stringa)  # True


## Ripetizione
stringa = "Ciao! "
print(stringa * 3)  # 'Ciao! Ciao! Ciao!'


## Verifica appartenenza
stringa = "Ciao Python"
print("Python" in stringa)  # True
print("Java" in stringa)  # False


#, String indexing
stringa = "Ciao Python"
print(stringa[0])  # 'C'
print(stringa[1])  # 'i'
print(stringa[2])  # 'a'
print(stringa[3])  # 'o'
print(stringa[4])  # ' '


## Negative indexing
stringa = "Ciao Python"
print(stringa[-1])  # ' '
print(stringa[-2])  # 'o'
print(stringa[-3])  # 'n'
print(stringa[-4])  # 'h'
print(stringa[-5])  # 't'


#, Slicing delle stringhe

stringa = "Python"

#? [start:stop:step]

# Non indicare numeri comporta la restituzione dell'intera stringa
print(stringa[:])  # 'Python'

# Sottostringa dal secondo al terzo carattere
print(stringa[1:3])  # 'yt'

# Dall'inizio stringa al quarto carattere
print(stringa[:4])  # 'Pyth'

# Sottostringa dal terzo carattere in poi
print(stringa[2:])  # 'thon'

# Tutti i caratteri con passo 2
print(stringa[::2])  # 'Pto'

# Stringa al contrario
print(stringa[::-1])  # 'nohtyP'

# La partenza è dal terzultimo carattere
print(stringa[-3::])  # 'hon'

# Utilizzo dello step, saltando un carattere alla volta
print(stringa[0::1])  # 'Pto'

# Slicing negativo sbagliato
print(stringa[-1:-4:])  # ''

# Slicing negativo corretto
print(stringa[-4:-1:])  # 'tho'


#, Formattazione stringhe

## Operatore %
nome = "Alice"
anni = 30
altezza = 1.72
numero = 255

# Inserimento di stringa e intero
print("Nome: %s, Età: %d" % (nome, anni))  # Nome: Alice, Età: 30

# Inserimento di float con default a 6 cifre decimali
print("Altezza: %f" % altezza)             # Altezza: 1.720000

# Inserimento di float con precisione specificata
print("Altezza: %.2f" % altezza)           # Altezza: 1.72

# Numeri in esadecimale e ottale
print("Numero in esadecimale: %x" % numero)  # Numero in esadecimale: ff
print("Numero in ottale: %o" % numero)       # Numero in ottale: 377

# Notazione scientifica
val = 0.00012345
print("Valore in notazione scientifica: %e" % val)  # Valore in notazione scientifica: 1.234500e-04

# Inserimento del simbolo %
progresso = 75
print("Completato al %d%%" % progresso)     # Completato al 75%

x = 42
print("|%5d|" % x)    # |   42|
print("|%05d|" % x)   # |00042|

pi = 3.1415926535
print("%.2f" % pi)    # 3.14
print("%10.3f" % pi)  #      3.142

parola = "ciao"
print("|%-10s|" % parola)  # |ciao      |


#, str.format()

## Esempio base
nome = "Marco"
età = 25
print("Ciao, mi chiamo {} e ho {} anni.".format(nome, età))
# Ciao, mi chiamo Marco e ho 25 anni.


## Utilizzando gli indici
marca = "Fiat"
modello = "Punto"
prezzo = 5000.00
print("La mia {2} {0} è costata {1} euro".format(modello, prezzo, marca))


## Key arguments
marca = "fiat"
modello = "funto"
prezzo = 5000.00
print("La mia {A} {B} è costata {C} euro".format(
  A=marca.capitalize(),
  B=modello.replace("f", "p").capitalize(),
  C=(prezzo  + 1000))
)
# La mia Fiat Punto è costata 6000.0 euro


#% f-string

## Tipi di interpolazioni
title = "Lo Hobbit"
author = "Tolkien"
print(f"{title} di {author}")
# Lo Hobbit di Tolkien

title = "Le cronache di Narnia"
print(F"Il film {title} contiene {title.lower().count('n')} lettere 'n'")
# Il film Le cronache di Narnia contiene 3 lettere 'n'

print(f"Domani farò {10 * 3 - 1} anni")
# Domani farò 29 anni

def area(r):
    return 3.14 * r * r

raggio = 5
print(f"L'area del cerchio è {area(raggio)}")
# Output: 'L'area del cerchio è 78.5'


## Specificatori di formato
val = 12.34567
print(f"Valore: {val:.2f}")      # Output: 'Valore: 12.35'
numero = 42
print(f"Numero: {numero:04d}")   # Output: 'Numero: 0042'

print(f"Larghezza caratteri: {numero:>5}")   # Output: 'Larghezza caratteri:    42'
print(f"Numeri di zero prima: {numero:07}")   # Output: 'Numeri di zero prima: 0000042'
print(f"Numeri di zero prima: {numero:,}")   # Output: ''

## Utilizzo avanzato multilinea
nome = "Anna"
età = 30
testo = f"""
  Nome: {nome}
  Età: {età}
"""
print(testo)
# Output:
# Nome: Anna
# Età: 30


#% Metodi