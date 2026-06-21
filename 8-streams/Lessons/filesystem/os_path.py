# % Gestione percorsi del file system

#% Modulo os
import os


# Unione di componenti di percorso
path = os.path.join("data", "file.txt")
print(path)

# Percorso assoluto
abs_path = os.path.abspath("file.txt")
print(abs_path)

# Directory corrente
cwd = os.getcwd()
print(cwd)

# Estrazione del nome del file
filename = os.path.basename("/home/user/file.txt")  # "file.txt"
print(filename)

# Estrazione della directory
dirname = os.path.dirname("/home/user/file.txt")    # "/home/user"
print(dirname)

# Separazione estensione
name, ext = os.path.splitext("report.pdf")          # ("report", ".pdf")
print(name, ext)

# Verifica esistenza file
print(os.path.exists("paths.py"))

# Verifica se è file o directory
print(os.path.isfile("paths.py"))
print(os.path.isdir("paths.py"))