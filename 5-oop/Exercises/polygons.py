"""
Tramite OOP (implementando le opportune classi) implementa un codice per poter definire e gestire un poligono.

Il codice deve poter:

creare un poligono specificandone il numero di lati
calcolare il perimetro del poligono
stabilire se due poligoni sono congruenti (confrontandone i lati)
permettere la stampa di un oggetto poligono nel formato "Poligono con <N> lati di valore: <valore dei lati>"
Testa la/e classe/i creata/e con un opportuno codice.
"""

# Creazione classe base

class Polygon:
  def __init__(self, number_of_sides, *side_lengths):
    self.sides = number_of_sides

    # Verificare se il numero di lati corrisponde a quelli effettivamente passati
    if len(side_lengths) != number_of_sides:
      raise ValueError(
          f"Attesi {number_of_sides} lati, ma ricevuti {len(side_lengths)} valori."
        )
    self.side_lengths = side_lengths

  def perimeter(self):
    return sum(self.side_lengths)

  def number_of_sides(self):
    return self.sides

  def __str__(self):
    # Crea una stringa dei valori dei lati separati da spazio
    side_values = " ".join(str(x) for x in self.side_lengths)
    return format(f"Poligono con {self.sides} lati di valore: {side_values}")

  def __eq__(self, other):
    # Verifica che l'altro oggetto sia un Polygon
    if isinstance(other, Polygon):
        return self.sides == other.sides
    # Se non è un Polygon, restituisce NotImplemented (comportamento standard)
    return NotImplemented


#, Variante 1: Implementazioni poligoni

triangle = Polygon(3, 1, 2, 3)
print("Triangolo creato")
print(f"Perimetro è: {triangle.perimeter()}")
print(triangle)

square = Polygon(4, 4, 3, 2, 4)
print("Quadrato creato")
print(f"Perimetro è: {square.perimeter()}")
print(square)

print("I due poligoni sono uguali?")
if triangle == square:
  print(f"Le due figure sono uguali")
else:
  print(f"Le due figure non sono uguali")


#, Variante 2: input e sottoclassi

# Implementare gli input
# polygon1 = int(print("""
#   Inserire come primo argomento quanti lati del poligono creare,
#   tutti gli altri sono i valori di ogni lato
# """).strip())
