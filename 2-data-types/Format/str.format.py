
#, str.format()

## Esempio base
nome = "Marco"
età = 25
print("Ciao, mi chiamo {} e ho {} anni.".format(nome, età))
# Ciao, mi chiamo Marco e ho 25 anni.


## Utilizzando gli indici
marca = "Fiat"
modello = "Punto"
prezzo = 5000.00
print("La mia {2} {0} è costata {1} euro".format(modello, prezzo, marca))


## Key arguments
marca = "fiat"
modello = "funto"
prezzo = 5000.00
print("La mia {A} {B} è costata {C} euro".format(
  A=marca.capitalize(),
  B=modello.replace("f", "p").capitalize(),
  C=(prezzo  + 1000))
)
# La mia Fiat Punto è costata 6000.0 euro
