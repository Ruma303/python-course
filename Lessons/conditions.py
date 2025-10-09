
#% Conditionals

## Costrutti condizionali
x = 15
if x < 10:
    print("x è minore di 10")
elif x == 10:
    print("x è uguale a 10")
elif x < 20:
    print("x è maggiore di 10 ma minore di 20")
else:
    print("x è maggiore o uguale a 20")


## Condizioni multiple con operatori logici
x = 8
if x > 5 and x < 10:
    print("x è compreso tra 5 e 10")

x = 3
if x < 5 or x > 10:
    print("x è minore di 5 o maggiore di 10")

x = 5
if not x > 10:
    print("x non è maggiore di 10")

