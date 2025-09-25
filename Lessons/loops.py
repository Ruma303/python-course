
#, While
## Evitare cicli infiniti

counter = 0
while counter < 10:
	print(f"Conto: {counter + 1}")
	counter += 1

""" password = ""
while password != "python123":
    password = input("Inserisci la password: ")
print("Accesso consentito!") """


## Iterazioni
parola = "Python"
for lettera in parola:
    print(lettera)
else:
	print("Else attivato")


## Enumerate
students = ("Luca", "Piero", "Giorgio")

for index, name in enumerate(students):
  print(f"{index + 1}. {name}")