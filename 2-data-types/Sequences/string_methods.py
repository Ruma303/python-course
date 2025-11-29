
#% Metodi delle stringhe

#, Capitalizzazione e modifica del caso

s = "python è fantastico"
print(s.capitalize())  # Output: 'Python è fantastico'

s = "python è fantastico"
print(s.title())  # Output: 'Python È Fantastico'

s = "Python"
print(s.upper())  # Output: 'PYTHON'
print(s.lower())  # Output: 'python'

s = "Python"
print(s.swapcase())  # Output: 'pYTHON'


#, Ricerca e sostituzione

s = "python è fantastico"
print(s.find("è"))    # Output: 7
print(s.rfind("a"))   # Output: 15
print(s.find("z"))    # Output: -1 - non trovato

s = "python è fantastico"
print(s.index("è"))   # Output: 7

s = "ciao ciao"
print(s.replace("ciao", "salve"))  # Output: 'salve salve'

string = "Hello world"
print(min(string))
print(max(string))


#, Controlli su contenuto e formato

s = "documento.pdf"
print(s.startswith("doc"))   # Output: True
print(s.endswith(".pdf"))    # Output: True

print("123".isdigit())     # Output: True
print("abc".isalpha())     # Output: True
print("abc123".isalnum())  # Output: True
print("   ".isspace())     # Output: True

print("123".isnumeric())  # Output: True
print("abc".isascii())    # Output: True

s = "Python"
print(s.islower())   # Output: False
print(s.isupper())   # Output: False
print("Python Is Cool".istitle())  # Output: True


#, Allineamento e padding

s = "test"
print(s.center(10, '-'))  # Output: '---test---'
print(s.ljust(10, '.'))   # Output: 'test......'
print(s.rjust(10, '*'))   # Output: '******test'

s = "42"
print(s.zfill(5))  # Output: '00042'


#, Divisione e unione di stringhe

s = "uno,due,tre"
print(s.split(','))  # Output: ['uno', 'due', 'tre']

s = "prima riga\nseconda riga"
print(s.splitlines())  # Output: ['prima riga', 'seconda riga']

lista = ['a', 'b', 'c']
print('-'.join(lista))  # Output: 'a-b-c'


#, Rimozione e gestione spazi

s = "  testo  "
print(s.strip())   # Output: 'testo'
print(s.lstrip())   # Output: 'testo  '
print(s.rstrip())   # Output: '  testo'


#, Traduzione e codifica

tabella = str.maketrans("aeiou", "12345")
s = "ciao"
print(s.translate(tabella))  # Output: 'c143'

s = "test"
b = s.encode('utf-8')        # Output: b'test'
print(b.decode('utf-8'))     # Output: 'test'


#, Metodi di tabulazione e spaziatura

s = "uno\tdue"
print(s.expandtabs(4))  # Output: 'uno due'


#, Utility per controllo e conteggio

s = "banana"
print(s.count("a"))   # Output: 3

s = "abc:def:ghi"
print(s.partition(':'))  # Output: ('abc', ':', 'def:ghi')


#% Nuovi metodi per rimuovere prefissi e suffissi dalle stringhe

a = "resettare e ritentare"

print(a.lstrip('re'))   # Risultato: 'settare e ritentare'
print(a.rstrip('re'))   # Risultato: 'resettare e ritenta'
print(a.strip('er'))    # Risultato: 'settare e ritenta'

print(a.removeprefix('re')) # 'settare e ritentare'
print(a.removeprefix('er')) # 'resettare e ritentare' (nessun match all'inizio)
print(a.removesuffix('re')) # 'resettare e ritenta'
print(a.removesuffix('er')) # 'resettare e ritentare' (nessun match alla fine)