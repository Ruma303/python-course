

#, Operatori di confronto

## Operatori unari
a = 35
print(+a)    # 35
print(-a)    # -35
print(not a) # False

## Valutazione intervalli
print(1 < 2 < 3)
print(10 >= 3 != 5)

## Valutazione logica
print(True and False)
print(True or False)
print(not True)

## Operatori logici
print(1 < 2 and 2 > 3)
print(1 < 2 or 2 > 3)
print(not 1 < 2 and 2 > 3)
print(not (3 < 2 or 2 > 3))


# Valori Falsy
print(bool(False))  # Output: False
print(bool(None))   # Output: False

print(bool(0))    # Output: False
print(bool(0.0))  # Output: False
print(bool(0j))   # Output: False

print(bool(""))        # Output: False
print(bool([]))        # Output: False
print(bool(()))        # Output: False
print(bool(set()))     # Output: False
print(bool({}))        # Output: False

class MyClass:
   def __bool__(self):
	   return False

obj = MyClass()
print(bool(obj))  # Output: False


# Valori Truthy
print(bool(True))  # Output: True

print(bool(1))      # Output: True
print(bool(-42))    # Output: True
print(bool(3.14))   # Output: True

print(bool("hello"))          # Output: True
print(bool(" "))              # Output: True
print(bool([1, 2, 3]))        # Output: True
print(bool((1,)))             # Output: True
print(bool({1, 2}))           # Output: True
print(bool({"key": "value"})) # Output: True

class MyClass:
   def __bool__(self):
	   return True

obj = MyClass()
print(bool(obj))  # Output: True


# Test booleani

x = 0
if x:
    print("x è vero")
else:
    print("x è falso")  # Output: x è falso

y = "ciao"
if y:
    print("y è vero")  # Output: y è vero
else:
    print("y è falso")

counter = 3
while counter:
    print(counter)  # Output: 3, 2, 1
    counter -= 1

class MyClass:
    def __bool__(self):
        return True

obj = MyClass()
print(bool(obj))  # Output: True


class MyClass:
    def __len__(self):
        return 0

obj = MyClass()
print(bool(obj))  # Output: False