
#% Set

esempio = set([1, 2, 2, 3, 4, 4])
print(esempio)
# esempio sarà {1, 2, 3, 4}

# esempio[0] errore

#, Creazione Set

s1 = {10, 20, 30}
s2 = set() # Vuoto
s3 = set([1, 2, 3]) # Set da lista
s4 = set((1, 2, 3)) # Set da tupla
s5 = set("Banana") # Set da stringa

print(s1, s2, s3, s4, s5, sep="\n")

#, Immutabilità
# Esempio valido:
s = {(1, 2), "pippo", 42}
# Esempio non valido:
# s = { [1, 2], {3, 4} }  # genera TypeError

#, Operazioni

## Unione


## Intersezione


## Differenza


## Differenza simmetrica


#% Frozenset