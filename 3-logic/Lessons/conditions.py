# % Conditionals

# , Costrutti condizionali

## Struttura if
# x = 5
# if x > 5:
#     print("x è maggiore di 5")


## Struttura if-elif-else
# x = 20
# if x < 10:
#     print("x è minore di 10")
# elif x == 10:
#     print("x è uguale a 10")
# elif x < 20:
#     print("x è maggiore di 10 ma minore di 20")
# else:
#     print("x è maggiore o uguale a 20")


# , Condizioni multiple con operatori logici
# x = 8

# if x > 5 and x < 10 or x != 0:
#     print("x è compreso tra 5 e 10")

# x = 3
# if x < 5 or x > 10:
#     print("x è minore di 5 o maggiore di 10")

# x = 5
# if not x > 10:
#     print("x non è maggiore di 10")


# #, Condizioni nidificate (nested)
# x = 5
# y = 0

# if x > 0:
#     if y < 0:
#         print("x e y sono entrambi positivi")
#     elif y == 0:
#         print("x è positivo ma y è 0")
#     else:
#         print("x è positivo, ma y è negativo")


# autenticato = True
# autorizzato = True
# is_cookie_ok = True

# # Codice funzionante ma poco leggibile
# if autenticato:
#     print("Sei autenticato")
#     if autorizzato:
#         print("Sei autorizzato")

#         if is_cookie_ok:
#             print("biscotto ok")
#             print("Tie, ecco la risorsa")
#         else:
#             print("Token scaduto")
#     else:
#         print("Non sei autorizzato, 403")
# else:
#     print("Non sei autenticato, vai al login 401")


# # Refactoring
# def verifica_credenziali():
#     if not autenticato:
#         print("Non sei autenticato, vai al login 401")
#         return
#     if not autorizzato:
#         print("Non sei autorizzato, 403")
#         return
#     if not is_cookie_ok:
#         print("Token scaduto")
#         return

#     print("Tie, ecco la risorsa")


# verifica_credenziali()

# #, L'operatore ternario
# x = 10
# messaggio = "Maggiore di 5" if x > 5 else "Minore o uguale a 5"
# print(messaggio)
