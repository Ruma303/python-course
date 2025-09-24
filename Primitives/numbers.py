# Tipi numerici

# , Rappresentazioni int
x = 10
y = -1234567890123456789
z = 0
binario = 0b1010  # 10 in decimale
ottale = 0o7640  # 4000 in ottale
esadecimale = 0xFF  # 255 in decimale
print(x, y, z, binario, ottale, esadecimale)

## Operazioni comuni
a = 10 + 5
b = 10 * 3
c = 17 // 3  # Divisione intera: 5
d = 17 % 3  # Modulo: 2
e = 2**10  # Potenza: 1024

grande = 1_000_000_000  # Python 3.6+: underscore per separare le cifre


# , Rappresentazioni float
x = 3.14
y = -2.71
z = 1.0
w = 1e6  # 1.0 * 10^6 = 1000000.0
inf = float("inf")
minusInf = float("-inf")
nan = float("nan")

print(x, y, w, inf, minusInf, nan)
print(0.1 + 0.2)  # Output: 0.30000000000000004

## Operazioni comuni
a = 3.5 + 2.5
b = 3.5 / 2
c = 2.0**0.5  # Radice quadrata di 2


# , Numeri complessi (complex)
z1 = 2 + 3j
z2 = -1 - 4j
print(z1, z2)

## Operazioni comuni
add = z1 + z2
sub = z1 - z2
mul = z1 * z2
div = z1 / z2

"""
#, Decimal
from decimal import Decimal, getcontext

getcontext().prec = 10     # Imposta precisione globale
x = Decimal('0.1')
y = Decimal('0.2')
z = x + y                  # Output: Decimal('0.3')
print(z)

#, Fractions
from fractions import Fraction

f1 = Fraction(1, 3)
f2 = Fraction(2, 3)
print(f1 + f2)             # Output: 1
print(f1 * 2)              # Output: 2/3
print(float(f1))           # Output: 0.3333333333333333
"""


#% Conversioni tra tipi numerici

# Conversione tra tipi di base
a = float(7)  # 7.0
b = int(8.9)  # 8 (troncamento)
c = complex(5)  # (5+0j)
d = int("123")  # 123
e = float("2.71")  # 2.71

#, Conversione con tipi avanzati
"""from decimal import Decimal
from fractions import Fraction

f = Decimal("2.5")
g = Fraction("2.5")
print(f, g)"""

#, Conversione e promozione automatica dei tipi
a = 10
b = 2.5
print(a + b)        # 12.5, risultato è float
print(type(a))      # <class 'int'>
print(type(a + b))  # <class 'float'>


#% Metodi per tipi numerici