
#% Generators

## Differenze funzioni e generatori
def normale():
    return [1, 2, 3]

def generatore():
    for i in range(1, 4):
        yield i

print(normale())            # [1, 2, 3]
gen = generatore()
print(next(gen))            # 1
print(next(gen))            # 2


## Stato interno
print(gen.gi_frame)      # <frame object ...>
print(gen.gi_running)    # False
print(gen.gi_code)       # <code object g ...>



def get_doppio_gen():
    e = 2
    while e < 300:
        yield e
        e *= 2


gen = get_doppio_gen()

print(gen)
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())


def g():
    yield 1
    return 42

gen = g()
print(next(gen))          # 1
try:
    next(gen)
except StopIteration as e:
    print(e.value)        # 42


## Metodo send
def echo():
    valore = yield "start"
    while True:
        valore = yield f"ricevuto {valore}"

gen = echo()
print(next(gen))        # "start"
print(gen.send(100))    # "ricevuto 100"
print(gen.send(200))    # "ricevuto 200"

# def get_doppio_gen():
#     e = 2
#     while True:
#         yield e
#         e *= 2
#         if e >= 300:
#             return


# gen = get_doppio_gen()
# for i in range(10):
#     print(next(gen))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newGen = (n * n for n in numbers if n % 2 == 1)
# type(newGen) # <class 'generator'>
# print(newGen)

# for e in newGen:
#   print(e) # 1, 9, 25, 49, 81

# for e in newGen:
#   print(e) # Vuota