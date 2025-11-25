
#, f-string

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
