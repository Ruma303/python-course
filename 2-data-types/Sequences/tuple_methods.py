
#, Metodi comuni sulle tuple

t = (1, 2, 3, 2, 2, 4)
occorrenze = t.count(2)  # 3
print(occorrenze)


## conteggio di una sottotupla
t = (1, 2, 2, 3, 4, 2, 5)
sottotupla = t[1:5]  # (2, 2, 3, 4)
occorrenze = sottotupla.count(2)  # 2
print(occorrenze)

t = (10, 20, 30, 20, 40)
indice = t.index(20, 3, 4)  # 1
print(indice)


t = (3, 1, 4, 2)
lista_ordinata = sorted(t)  # [1, 2, 3, 4]
print(lista_ordinata)

t = ("pippo", "pluto", "qui", "paperino")
ordinati = sorted(t, key=len)  # ['qui', 'pippo', 'pluto', 'paperino']
print(ordinati)


t = (1, 2, 3)
reverse_iter = reversed(t)
lista_reverse = list(reverse_iter)  # [3, 2, 1]
print(lista_reverse)


t = ("a", "b", "c")
for idx, val in enumerate(t):
    print(idx, val)
# 0 a
# 1 b
# 2 c


t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
for a, b in zip(t1, t2):
    print(a, b)
# 1 a
# 2 b
# 3 c

t1 = (1, 2, 3, 4)
t2 = ('a', 'b')
result = list(zip(t1, t2))  # [(1, 'a'), (2, 'b')]
print(result)


t = (0, 1, 2)
print(any(t))  # True
print(all(t)) # False

t = (True, True, False)
print(all(t))  # False

t2 = (x > 0 for x in (1, 2, 3))
print(all(t2))  # True


t = (1, 2, 3, 4)
print(min(t))  # 1
print(max(t))  # 4
print(sum(t))  # 10

t = (1, 2, 3, 4, 5)
somma_pari = sum(x for x in t if x % 2 == 0)  # 6
print(somma_pari)


def f(a, b, c):
    return a + b + c

t = (1, 2, 3)
risultato = f(*t)  # 6


t = (1, 2, 3, 4)
quad = tuple(map(lambda x: x**2, t))  # (1, 4, 9, 16)
print(quad)

filtrati = tuple(filter(lambda x: x % 2 == 0, t))  # (2, 4)
print(filtrati)


print(dir("Test"))
print(dir(filtrati))