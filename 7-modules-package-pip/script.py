import sys
import dir_a.main as main
import dir_a.dir_b.modulo1 as modulo1, dir_a.dir_b.modulo2 as modulo2, dir_a.dir_b.dir_c.math_module as math
from dir_a.main import saluta
from dir_a.main import *
from dir_a.main import grazie as ringrazia
from dir_a.dir_b.dir_c.calcoli import *

print(sys.path)             # stampa il percorso di ricerca dei moduli
modulo1.myFunc(10)          # chiama la funzione definita in modulo1
obj = modulo2.MyClass()     # crea un oggetto della classe in modulo2
print(type(math.math))      # <class 'module'>
main.saluta()               # chiama la funzione saluta definita in main
saluta()                    # chiama la funzione saluta definita in main
grazie()               # AttributeError: module 'main' has no attribute 'grazie'
ringrazia()
somma(3, 4)