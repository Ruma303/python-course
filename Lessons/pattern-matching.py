
#% Pattern Matching

## Esempio base
subject_value = [1, 2, 3]
match subject_value:
    case [p, s, t]:
        print(f"Trovato {p}, {s} e {t}")   # Output: Trovato 1, 2 e 3


## Esempio con wildcard
subject_value = [1, 2, 3, 4, 5, 6]
match subject_value:
    case [p, _, t]:
        print(f"Trovato {p} e {t}")   # Output: Trovato 1 e 3
    case _:
        print("Altri valori trovati")


## Esempio con resto "splat"
subject_value = [1, 2, 3, 4, 5, 6]
match subject_value:
    case [p, *splat, t]:
        print(f"Trovato {p} e {t}. Il resto è: {splat}")   # Output: Trovato 1 e 6. Il resto è: [2, 3, 4, 5]