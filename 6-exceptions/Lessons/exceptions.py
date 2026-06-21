
#% Exceptions

#, Esecuzione e propagazione delle eccezioni
# def myFunc(a,b):
#     res = a // b
#     print(res)
#     return res

# myFunc(10,0)


#, Meccanismo di propagazione lungo lo stack
# def f1():
#     f2()

# def f2():
#     f3()

# def f3():
#     f4()

# def f4():
#     return 1 // 0  # Qui si verifica l'errore

# f1()


## Esempio pratico con gerarchia di chiamate
# def div(a, b):
#     return a // b

# def compute():
#     return div(10, 0)

# def start():
#     return compute()

# start()