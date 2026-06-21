
#%

#, Uso di try/ except

# Gestire eccezioni except all (generiche)
"""
try:
  suite
except:
  suite
"""


#, Cattura generica
# try:
#     x = 10 / 0
# except:
#     print("Errore generico")

# print("Codice dopo la cattura")


#, Gestione specifica su catture multiple
# try:
#     x = [1, 2, 3]
#     y = x[5]
# except IndexError:
#     print("Indice non valido")
# except ZeroDivisionError:
#     print("Divisione per zero")


#, Gestione unificata
# try:
#     print(10 // 0)
# except (ZeroDivisionError, ArithmeticError):
#     print("Errore aritmetico")


## Esempi di gestione eccezioni
# def f1():
#     try:
#         f2()
#     except (IndexError, ArithmeticError, ZeroDivisionError):
#         print("Eccezione gestita in f1: Divisione per zero")


# def f2():
#     try:
#         f3()
#     except ZeroDivisionError:
#         print("Eccezione gestita in f2: Divisione per zero")
#     f3()


# def f3():
#     f4()


# def f4():
#     return 1 // 0


# f1()
