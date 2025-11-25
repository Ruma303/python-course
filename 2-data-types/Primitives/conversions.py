# Conversioni

#% Conversioni implicite

## Da integer a float
x = 10  # Intero
y = 3.5  # Float

result = x + y
print(result)  # Output: 13.5
print(type(result))  # Output: <class 'float'>

## Da integer a complex
x = 5  # Intero
y = 3 + 4j  # Complesso

result = x + y
print(result)  # Output: (8+4j)
print(type(result))  # Output: <class 'complex'>

## Da boolean a integer
x = True  # Booleano
y = 5  # Intero

result = x + y
print(result)  # Output: 6
print(type(result))  # Output: <class 'int'>


#% Conversioni esplicite
# Uso di funzioni di cast


## Conversione in integer
print(int(3.9))  # Output: 3
print(int("10"))  # Output: 10 solo se la stringa contiene solo numeri
print(int(True))  # Output: 1
# print(int("abc"))  # ValueError

x = input("Inserisci un numero: ")
print(int(x) + 10)


## Conversioni in float
print(float(5))  # Output: 5.0
print(float("3.14"))  # Output: 3.14 solo se la stringa contiene solo numeri
print(float(False))  # Output: 0.0
print(float(True))  # Output: 1.0
# print(float("abc"))  # ValueError


## Conversioni in booleani
print(bool(1))  # Output: True
print(bool(0))  # Output: False
print(bool(3.14))  # Output: True
print(bool(""))  # Output: False
print(bool("abc"))  # Output: True


## Conversioni in complex
print(complex(5))  # Output: (5+0j)
print(complex(3.14))  # Output: (3.14+0j)
print(complex(True))  # Output: (1+0j)
print(complex(False))  # Output: (0+0j)
print(complex("2+3j"))  # Output: (2+3j)
# print(complex("abc"))  # ValueError


## Conversioni in stringa
print(str(123))  # Output: "123"
print(str(3.14))  # Output: "3.14"
print(str(True))  # Output: "True"
print(str(False))  # Output: "False"


## Conversioni in collezioni
print(list("abc"))  # Output: ['a', 'b', 'c']
print(tuple("abc"))  # Output: ('a', 'b', 'c')
print(set("abc"))  # Output: {'a', 'b', 'c'}
print(dict(a=1, b=2, c=3))  # Output: {'a': 1, 'b': 2, 'c': 3}

# Da stringa a lista
print(list("abc"))  # Output: ['a', 'b', 'c']

# Da lista a set
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# Da lista di coppie a dizionario
print(dict([("a", 1), ("b", 2)]))  # Output: {'a': 1, 'b': 2}