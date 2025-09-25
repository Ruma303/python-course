numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newGen = (n * n for n in numbers if n % 2 == 1)
type(newGen) # <class 'generator'>
print(newGen)

for e in newGen:
  print(e) # 1, 9, 25, 49, 81

for e in newGen:
  print(e) # Vuota