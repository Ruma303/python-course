
## Creazione dizionario
class Automobile:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo


mia_auto = Automobile("Toyota", "Yaris")
print(mia_auto.__dict__)