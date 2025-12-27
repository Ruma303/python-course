from .modulo2 import getInput, showOutput

# print(f"Nome del modulo __name__: {__name__}")

def verifyName():
    name = getInput().strip()
    if isinstance(name, str) and name != "":
        showOutput(name)

if __name__ == "__main__":
    verifyName()

def myFunc(x):
    print(x)
