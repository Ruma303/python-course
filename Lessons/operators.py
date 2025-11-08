
#% Operatori di confronto

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


## Operatore ternario
x = 10
messaggio = "Maggiore di 5" if x > 5 else "Minore o uguale a 5"
print(messaggio)


## Operatore di appartenenza
voglia = "cioccolato"
if "ciocco" in voglia:
    print("Ho voglia di qualcosa di dolce!")


## Confronto di valori
x = 8
if 5 < x < 10:
    print("x è compreso tra 5 e 10")


## Espressioni complesse
a, b, c = 5 ,4, 2

print(f"{not (a < b) or (a > c) = }")
print(f"{not ((a < b) or (a > c)) = }")

print("Scomposizione espressioni complesse sostituendo i valori:")
print(f"{not a >= c or (a == b or (b == c or a > c)) = }")
print(f"{not a >= c or (a == b or (False or True)) = }")
print(f"{not a >= c or (False or True) = }")
print(f"{not a >= c or True = }")
print(f"{not True or True = }")
print(f"{True = }")
