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
print("Java" not in stringa)  # True


## Confronto tra stringhe
print(ord('A'))  # 65
print(ord('a'))  # 97

stringa1 = "Ciao "
stringa2 = "Mondo"

print(stringa1 == stringa2)  # False
print(stringa1 > stringa2)   # False
print(stringa1 <= stringa2 and stringa1 != stringa2)  # True


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

#% Metodi
