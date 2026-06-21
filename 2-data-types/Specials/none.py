
# NoneType

print(type(None))  # Output: <class 'NoneType'>

x = None
print(x is None)  # Output: True
print(x == None)  # Output: True

# Utilizzi

x = None  # Variabile inizializzata ma senza valore associato
if x is None:
    print("x non ha un valore definito.")  # Output: x non ha un valore definito.

def no_return():
    pass  # Nessun valore restituito

result = no_return()
print(result)  # Output: None


def greet(name=None):
    if name is None:
        print("Ciao, ospite!")
    else:
        print(f"Ciao, {name}!")

greet()         # Output: Ciao, ospite!
greet("Alice")  # Output: Ciao, Alice!

data = {"name": "Alice", "age": None}  # Età non definita
if data["age"] is None:
    print("L'età non è specificata.")  # Output: L'età non è specificata.

# Differenza dai valori false

x = None
y = 0

print(bool(x))  # Output: False (perché None è "falso")
print(bool(y))  # Output: False (perché 0 è "falso")

print(x == y)   # Output: False (None e 0 non sono equivalenti)