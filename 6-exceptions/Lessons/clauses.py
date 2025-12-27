# % Altre clausole

# , Clausola as
# try:
#     x = 1 // 0
# except ZeroDivisionError as e:
#     print(f"Errore: {e}") # integer division or modulo by zero
#     print(type(e))        # <class 'ZeroDivisionError'>


# , Clausola finally
# try:
#     x = 1 // 0
# except ZeroDivisionError:
#     print("Divisione per zero")
# finally:
#     print("Finito")


# , Clausola else
# try:
#     x = 1 + 1
# except ZeroDivisionError:
#     print("Divisione per zero")
# else:
#     print("Nessun errore")


# , Clausola else + finally
# try:
#     5 / 5
# except:
#     print("Eccezione gestita in f4: Divisione per zero")
# else:
#     print("Nessun errore")
# finally:
#     print("Finito")


# , Clausola raise: lanciare eccezioni

## Es1: Lancio eccezioni con nome classi
# for i in range(50):
#     print(i)
#     if i == 3:
#         raise IndexError

## Es2: Eccezione con argomenti
# try:
#     for i in range(50):
#       print(i)
#       if i == 5:
#           raise Exception("Eccezione generica lanciata all'iterazione", i)
# except Exception as e:
#     print(f"{e.args[0]}.\nEsecuzione terminata all'iterazione {i}")


## Es3: Rilancio eccezione
# def f(x, y):
#     return x // y


# try:
#     try:
#         f(10, 0)
#     except ZeroDivisionError as e:
#         print(f"Eccezione catturata: {e}")
#         raise
# except ZeroDivisionError:
#     print("Eccezione rilanciata intercettata al livello superiore")


## Esempio 4: catch-and-raise selettivo
# try:
#     numbers = ["a", "b", "c"]
#     try:
#         d = numbers[3]  # Qui si genera IndexError
#         if d:
#             raise IndexError("Indice fuori range")
#     except IndexError as e:
#         print("Log:", e)
#         raise  # Rilancia l'eccezione catturata
# except IndexError as E:
#     print(f"Cattura livello superiore: {E}")


# , Exception Chaining

## 1. Sollevamento di una nuova eccezione senza chaining esplicito
# try:
#     lst = [1, 2, 3]
#     try:
#         print(lst[5])
#     except IndexError as exc:
#         print(f"Eccezione interna: {exc.__class__}") # IndexError
#         raise RuntimeError("Errore personalizzato")
# except RuntimeError as err:
#     print(f"Gestito esternamente: {err.__context__}")  # list index out of range
#     print(f"Gestito esternamente: {err.__context__.__class__}")  # IndexError
#     raise


## 2. Sollevamento di una nuova eccezione con chaining esplicito con from
# try:
#     lst = [1, 2, 3]
#     try:
#         print(lst[5])
#     except IndexError as exc:
#         print(f"Eccezione interna: {exc.__class__}")
#         raise RuntimeError("Errore personalizzato") from exc
# except RuntimeError as err:
#     print(f"Gestito esternamente: {err.__cause__}")  # list index out of range
#     print(f"Gestito esternamente: {err.__cause__.__class__}")  # IndexError
#     raise


## 3. Disabilitazione del chaining from None
# try:
#     lst = [1, 2, 3]
#     try:
#         print(lst[5])
#     except IndexError:
#         raise RuntimeError("Errore personalizzato") from None
# except RuntimeError as err:
#     print(f"__context__: {err.__context__}")  # None
#     print(f"__cause__: {err.__cause__}")      # None


#, Clausola assert

## Esempio 1: condizione violata
# def f(x):
#     assert x > 0, "x deve essere maggiore di zero"
#     return x

# f(0)
# AssertionError: x deve essere maggiore di zero

## Esempio 2: uso con gestione try / except
# try:
#     f(-1)
# except AssertionError as e:
#     print(f"AssertionError: {e}")

## Esempio 3: asserzione senza messaggio
# x = 5
# assert x == 5  # Nessun errore
# assert x == 0  # Solleva AssertionError
