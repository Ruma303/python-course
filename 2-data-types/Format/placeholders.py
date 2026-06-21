
#, Operatore %
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
