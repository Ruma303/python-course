from pathlib import Path

root = Path.home()
print("Root path", root)

absolute_path = Path.cwd()
print("Absolute path current directory", absolute_path)

file_path = Path(absolute_path, "scripts", "sample.txt")

file_obj = open(file_path, "r")
print(file_obj.read())
file_path.write_text("Hello World")
file_obj.close()

