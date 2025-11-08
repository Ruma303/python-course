
#% Ereditarietà
print("\nEreditarietà")


#% Ereditarietà multipla
print("\nEreditarietà multipla")
class DClass:
  def xFunc(self):
    print("Sono in DClass")

class BClass:
    """ b = 10
    def bFunc(self):
        print("Sono in bFunc")
    def xFunc(self):
        print("Sono in BClass")
    """
    pass

class BClass(object):
    pass

class CClass(BClass):
    """ c = 20
    def cFunc(self):
        print("Sono in cFunc")
    def xFunc(self):
        print("Sono in CClass") """
    pass

class AClass(BClass, CClass):
    pass

a = AClass()
# print(a.b)
# print(a.c)

# a.bFunc()
# a.cFunc()

a.xFunc()
