
#% Pattern Matching

## Esempio base
print("\nEsempi base")
subject_value = [1, 2, 3]
match subject_value:
    case [p, s, t]:
        print(f"Trovato {p}, {s} e {t}")   # Output: Trovato 1, 2 e 3


## Esempio con wildcard
print("\nEsempi con wildcard")
subject_value = [1, 2, 3, 4, 5, 6]
match subject_value:
    case [p, _, t]:
        print(f"Trovato {p} e {t}")   # Output: Trovato 1 e 3
    case _:
        print("Altri valori trovati")


## Capture pattern
print("\nCapture pattern")
subject_value = [1, 2, 3]
match subject_value:
    case [p, s]:
        print(f"Trovati {p} e {s}")
    case [p, s, t]:
        print(f"Trovati {p}, {s} e {t}")
    case _:
        print("Nessun valore trovato")


## Esempio con resto "splat"
print("\nResto splat")
subject_value = [1, 2, 3, 4, 5, 6]
match subject_value:
    case [i, *splat, f]:
        print(f"Primo elemento: {i}, ultimo: {f}. Altri elementi del pattern: {splat}")
        # Primo elemento: 1, ultimo: 6. Altri elementi del pattern: [2, 3, 4, 5]


## Literal patterns
print("\nLiteral pattern")
subject_value = [1, 2, 3]
match subject_value:
    case [1, 2, 3]:
        print("Trovata lista 1,2,3")
    case [1, *rest]:
        print(f"Il resto è {rest}")


## Or patterns
print("\nOr pattern")
subject_value = ["autunno", "stagione autunnale"]
match subject_value:
    case ["autunno", msg] | ["inverno", msg]:
        print(f"Nella {msg} fa più freddo")
    case ["primavera", msg] | ["estate", msg]:
        print(f"Nella {msg} fa più caldo")


## As patterns
print("\nAs pattern")
subject_value = "estate"
match subject_value:
    case "primavera" | "estate" as stagione:
        print(f"in {stagione} fa più caldo")
    case "autunno" | "inverno" as stagione:
        print(f"in {stagione} fa più freddo")


## Conditional Patterns (Guards)
print("\nConditional pattern")
subject_value = ["pari", "50"]
match subject_value:
    case ["pari", valore] if int(valore) % 2 == 0:
        print(f"{valore} è un numero pari")
    case ["dispari", valore] if int(valore) % 2 != 0:
        print(f"{valore} è un numero dispari")
    case _:
        print("C'è un errore nei dati")


## Esempio su dizionari
print("\nEsempio di utilizzo su dizionari")
subject_value = {"tipo": "errore", "messaggio": "file mancante"}
match subject_value:
    case {"tipo": "errore", "messaggio": msg}:
        print(f"Errore: {msg}")