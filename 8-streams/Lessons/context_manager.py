from pathlib import Path

absolute_path = Path.cwd()
file_path = Path(absolute_path, "scripts", "sample.txt")

with open(file_path, "r") as file_obj:
    print(file_obj.encoding)

with open(file_path, "rt") as f:
    text = f.read(5)
    print(text) # Hello

with open(file_path, "rt") as f:
    line = f.readline()
    print(line)

# Iterare

with open(file_path, "rt") as f:
    counter = 0
    for line in f:
        line = line.strip()
        print(line)
        counter += 1
    print("Righe:", counter)

with open(file_path, "rt") as f:
    for line in f.readlines():
        line = line.strip()
        print(line)

""" with open(file_path, "w") as file_obj:
    file_obj.write("Hello World") """
