
#% Modifica di variabili global e enclosed

## Modifica delle variabili globali
x = 10

def modifica_globale():
    global x
    x = 20
    print(x) # 20

modifica_globale()
print(x)  # 20


## Modifica di variabili enclosed
def modifica_enclosed():
    y = 20
    def inner():
        nonlocal y
        y = 50
        print(y) # 50
    inner()
    print(y)  # 50

modifica_enclosed()


#* Esempio mixato
x = 10

def outer():
    y = 20
    def inner():
        global x
        nonlocal y
        x = 100
        y = 200
    inner()
    print(f"x (global): {x}")
    print(f"y (enclosed): {y}")

outer()


## Accessibilità locale -> globale
if True:
    y = 10

print(y)

