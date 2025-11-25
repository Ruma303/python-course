"""
class Automobile:

  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

mia_auto = Automobile("Toyota", "Yaris")
mia_auto.anno = 2010
print(mia_auto.marca)
print(mia_auto.modelo)
print(mia_auto.anno)

sua_auto = Automobile("Honda", "Civic", 2020)
print(sua_auto.anno)
"""

"""
class Automobile:
  __slots__ = ["marca", "modelo"]

  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo


mia_auto = Automobile("Toyota", "Yaris", 2010)
print(mia_auto.marca)
print(mia_auto.modelo)
print(mia_auto.anno)
"""

"""
mia_auto = Automobile("Honda", "Civic")
mia_auto.anno = 2010
print(sua_auto.anno)
"""
