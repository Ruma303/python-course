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