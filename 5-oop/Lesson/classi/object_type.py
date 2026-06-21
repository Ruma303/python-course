
#% object e type


#,La classe object
class MyClass(object):
    pass

myObject = MyClass()

print(isinstance(myObject, object))  # True
print(isinstance(MyClass, object))  # True


#, Metaclasse Type
class MyClass:
    pass

print(type(MyClass))     # <class 'type'> (oggetto classe)
print(type(MyClass()))   # <class '__main__.MyClass'> (oggetto istanza)
print(isinstance(myObject, type))  # False

## Verifica di appartenenza
class MyClass:
    pass

myObject = MyClass()

print(isinstance(myObject, MyClass))  # True
print(isinstance(myObject, object))   # True
print(isinstance(MyClass, object))    # True
print(isinstance(MyClass, type))      # True
print(isinstance(myObject, type))     # False
print(isinstance(object, object))     # True
print(isinstance(type, type))         # True
print(isinstance(object, type))       # True
print(isinstance(type, object))       # True


#, Classe dinamica
MyClass2 = type('MyClass', (), {'x': 42})

istanza = MyClass2()
print(istanza.x)  # 42
