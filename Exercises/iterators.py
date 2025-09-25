myList = ["primo", "secondo", "terzo"]
myIterator = iter(myList)

print(type(myList))  # <class 'list'>
print(type(myIterator))  # <class 'list_iterator'>

print(next(myIterator))  # primo
print(next(myIterator))  # secondo
print(next(myIterator))  # terzo

# print(next(myIterator))

"""Traceback (most recent call last):
  File "/Users/ruma/Library/Mobile Documents/com~apple~CloudDocs/Sites/Coding/Python/Lessons/python-logic/iterables.py", line 11, in <module>
    print(next(myIterator)) # StopIteration
StopIteration"""

myList = [1, 2, 3, 4, 5]
myIterator = iter(myList)

for item in myIterator:
    print(item)

# Esercizio: creare un iteratore che restituisca un numero che raddoppia fino a 300

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
myiter = iter(myClass)
for i in myiter:
    print(i)