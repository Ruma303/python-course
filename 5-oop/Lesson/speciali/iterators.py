
#% Iterables and iterators
myList = ["primo", "secondo", "terzo"]
myIterator = iter(myList)

print(type(myList))      # <class 'list'>
print(type(myIterator))  # <class 'list_iterator'>

## Avanzamento manuale
print(next(myIterator))  # primo
print(next(myIterator))  # secondo
print(next(myIterator))  # terzo

#! Un altro print solleverebbe l'eccezione StopIteration
# print(next(myIterator))

"""
Traceback (most recent call last):
  File ".../iterables.py", line 15, in <module>
    print(next(myIterator)) # StopIteration
StopIteration
"""


#, Iterazione automatica con for in
myList = [1, 2, 3, 4, 5]

for item in myList: # crea automaticamente iter(iterable)
    print(item) # chiama automaticamente next(iterator)
    # Gestisce automaticamente StopIteration


#, Verificare se un oggetto è iterabile o iteratore
hasattr(myList, "__iter__") # True (iterabile)
hasattr(myList, "__next__") # False (non iteratore)

it = iter(myList)
hasattr(it, "__iter__") # False (non iterabile)
hasattr(it, "__next__") # True (iteratore)


#, Oggetti che sono sia iterabili che iteratori

## Iteratore che restituisca un numero che raddoppia fino a 300
class MyIterator:
    def __init__(self):
        self.myattr = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.myattr < 300:
            n = self.myattr
            self.myattr *= 2
            return n
        else:
            raise StopIteration

myClass = MyIterator()
myIter = iter(myClass)
for i in myIter:
    print(i)


## Iteratori infiniti (omettere StopIteration)
class Infinite:
    def __init__(self):
        self.n = 1

    def __iter__(self):
        return self

    def __next__(self):
        n = self.n
        self.n += 1
        return n

myInfinite = Infinite()
myInfiniteIter = iter(myInfinite)
for i in myInfiniteIter:
    print(i)
    if i > 100: # Condizione di stop
        break


## Iteratore con classe personalizzata

class Sequence:
  def __init__(self, start = 1, limit = 10):
      self.current = start
      self.limit = limit

  def __iter__(self):
      return self

  def __next__(self):
      if self.current <= self.limit:
          n = self.current
          self.current += 3
          return n
      else:
          raise StopIteration

for number in Sequence(3, 15):
    print(number)