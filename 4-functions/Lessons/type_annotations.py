
#, Function annotations
def myFunc(x: str) -> "ritorno":
    return "rit"

print(myFunc.__annotations__)
# Output: {'x': 'parametro x', 'return': 'ritorno'}


#, Type hints
def foo(a: str, b: int) -> None:
  print(f"Primo parametro {a}, secondo parametro {b}")

foo("Hello", 42)
# Primo parametro Hello, secondo parametro 42

#, Syntax fo Variable annotations
a: int = 10
b: str

print(__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'str'>}

#, Per classi e attributi
class MyClass:
    nome: str
    cognome: str

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

mc = MyClass("Mario", "Rossi")
print(mc.nome)        # Mario
print(mc.cognome)     # Rossi