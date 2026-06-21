
#, Importazione moduli

# import sys
# import dir_a.main as main
import dir_a.dir_b.modulo1 as modulo1, dir_a.dir_b.modulo2 as modulo2, dir_a.dir_b.dir_c.math_module as math

## Importazioni specifiche
# from dir_a.main import saluta
# from dir_a.main import *
# from dir_a.main import grazie as ringrazia
# from dir_a.dir_b.dir_c.calcoli import *

#, Import __all__
from utils import *

print(math_utils.somma(3, 4))
# print(string_utils.upper("hello"))


## Percorsi di ricerca e importazione dei moduli
# print(sys.path)             # stampa il percorso di ricerca dei moduli

#, Utilizzo dei moduli
# modulo1.myFunc(10)          # chiama la funzione definita in modulo1

# print(type(math.math))      # <class 'module'>
# main.saluta()               # chiama la funzione saluta definita in main
# saluta()                    # chiama la funzione saluta definita in main
# grazie()               # AttributeError: module 'main' has no attribute 'grazie'

# ringrazia()
# somma(3, 4)




#, Ispezionare bytecode
# import dis

# def somma(a, b):
#     return a + b

# dis.dis(somma)