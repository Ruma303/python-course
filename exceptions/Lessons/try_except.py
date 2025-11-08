# Uso di try/ except

# Gestire eccezioni except all (generiche)
"""try:
  suite
except:
  suite"""


# Gestire eccezioni diverse
""" try:
  suite
except exception1:
  suite
except exception2:
  suite   """

# Gestire eccezioni di tipo diverso
""" try:
  suite
except exception1:
  suite
except (exception2, exception3):
  suite """

""" def myFunc(a, b):
    res = a // b
    print(res)
    return res


try:
    myFunc(10, 0)
except ZeroDivisionError:
    print("Divisione per zero") """


# Esempi di gestione eccezioni
""" def f1():
    try:
        f2()
    except (IndexError, ArithmeticError, ZeroDivisionError):
        print("Eccezione gestitia in f1: Divisione per zero")


def f2():
    try:
        f3()
    except ZeroDivisionError:
        print("Eccezione gestita in f2: Divisione per zero")
    f3()


def f3():
    f4()


def f4():
    return 1 // 0


f1() """

# Clausola as
""" try:
    x = 1 // 0
except ZeroDivisionError as e:
    print(f"Errore: {e}") """

# Clausola finally
""" try:
    f4()
except ZeroDivisionError:
    print("Eccezione gestita in f4: Divisione per zero")
finally:
    print("Finito") """

# Clausola else
""" try:
    f4()
except ZeroDivisionError:
    print("Eccezione gestita in f4: Divisione per zero")
else:
    print("Nessun errore")
 """

# Clausola else + finally
""" try:
    5 / 5
except:
    print("Eccezione gestita in f4: Divisione per zero")
else:
    print("Nessun errore")
finally:
    print("Finito") """


# Clausola raise: lanciare eccezioni
""" for i in range(50):
    print(i)
    if i == 3:
        raise IndexError

for i in range(50):
    print(i)
    if i == 5:
        raise Exception("Eccezione generica lanciata all'iterazione", i)

try:
    raise Exception("Errore generico", 42)
except Exception as e:
    print(e.args)  # ('Errore generico', 42) """


""" def f(x, y):
    return x // y


try:
    f(10, 0)
except ZeroDivisionError:
    print("Errore intercettato, lo rilancio")
    raise

try:
    raise IndexError("Indice fuori range")
except IndexError as e:
    print("Log:", e)
    raise  # Rilancia IndexError dopo log """


# Clausola assert:
# assert expression, argument


"""
def f(x):
    assert x > 0, "x deve essere maggiore di zero"
    return x


try:
    f(-1)
except AssertionError as e:
    print(f"AssertionError: {e}")

# Asserzioni senza messaggio
x = 5
assert x == 5  # Nessun errore
assert x == 0  # Solleva AssertionError
"""