
#% Metodo enumerate

#, Utilizzi
frutti = ['mela', 'banana', 'ciliegia']
for idx, valore in enumerate(frutti):
    print(idx, valore)
# 0 mela
# 1 banana
# 2 ciliegia


for idx, valore in enumerate(frutti, start=1):
    print(idx, valore)
# 1 mela
# 2 banana
# 3 ciliegia

s = "abc"
print(list(enumerate(s)))
# [(0, 'a'), (1, 'b'), (2, 'c')]


def gen():
    for i in range(3, 6):
        yield i
print(list(enumerate(gen())))
# [(0, 3), (1, 4), (2, 5)]


d = {'a': 10, 'b': 20, 'c': 30}
print(list(enumerate(d)))
# [(0, 'a'), (1, 'b'), (2, 'c')]

print(list(enumerate(d.values())))
# [(0, 10), (1, 20), (2, 30)]


#, Conversione in strutture dati
conv1 = list(enumerate(['a', 'b', 'c']))
print(conv1)
# [(0, 'a'), (1, 'b'), (2, 'c')]
conv2 = tuple(enumerate('ab'))
print(conv2)
# ((0, 'a'), (1, 'b'))
conv3 = set(enumerate((1, 2, 3)))
print(conv3)
# {(0, 1), (1, 2), (2, 3)}


#, Operazione inversa: recuperare la sequenza originale
enum_list = [(0, 'a'), (1, 'b'), (2, 'c')]
# Usando comprensione di lista
valori = [v for i, v in enum_list]
print(valori)
# ['a', 'b', 'c']

# Usando zip e unpacking
_, valori = zip(*enum_list)
valori = list(valori)
print(valori)
# ['a', 'b', 'c']


enum_list = [(3, 'x'), (1, 'y'), (2, 'z')]
output = [None] * (max(i for i, v in enum_list) + 1)
for i, v in enum_list:
    output[i] = v
# output: [None, 'y', 'z', 'x']
print(output)