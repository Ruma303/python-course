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


def get_doppio_gen():
    e = 2
    while True:
        yield e
        e *= 2
        if e >= 300:
            return


gen = get_doppio_gen()
for i in range(10):
    print(next(gen))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newGen = (n * n for n in numbers if n % 2 == 1)
type(newGen) # <class 'generator'>
print(newGen)

for e in newGen:
  print(e) # 1, 9, 25, 49, 81

for e in newGen:
  print(e) # Vuota