class MyClass:
    def __init__(self, valore):
        self.valore = valore

    def __str__(self):
        return f"Valore: {self.valore}"

    def __repr__(self):
        return f"Valore: {self.valore}"


obj = MyClass(125)
print(obj)
print(str(obj))
print(repr(obj))