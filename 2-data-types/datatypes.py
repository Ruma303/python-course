# Verifica tipi

myInt = 10
myString = "Hello"

# tipi
print(type(myInt)) # Restituisce <class 'int'>
print(type(myInt)) # Restituisce <class 'str'>

# id
print(id(myInt))
print(id(myString))

# valori
print(myInt)
print(myString)


# Riassegnamento variabili

a = 20
print(a)

a = 10
print(a)


# Copia per riferimento e reference count
a = 10 # ref count = 1
print(a)

b = a # ref count = 2
print(b)

b = 50
print(a) # 50
print(b) # 50

print(id(a)) # es. id: 4347765024
print(id(b)) # es. id: 4347765024

c = []
c.append(b) # ref count = 3
print(id(c[0])) # es. id: 4347765024

del a # eliminando un riferimento al valore
# print(a) # Questo riferimento è stato rimosso dal GC
print(b) # ma gli altri riferimenti esisteranno ancora
print(c[0]) # gli altri riferimenti esisteranno ancora


# Assegnamento per valore
x = [1, 2, 3]
y = x.copy()

print(id(x), id(y))
x.pop() # Esempio di modifica: rimuove l'ultimo elemento

print(x) # [1, 2]
print(y) # [1, 2, 3]

## dir()
print(dir())
