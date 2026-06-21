import os
import shutil

original_path = input("Inserire un percorso del file da copiare: ").strip()

if not os.path.exists(original_path):
  print("File non trovato. Controllare che il percorso sia corretto")
else:
  file_name = os.path.basename(original_path)
  target_directory = input("Inserire un percorso di destinazione: ").strip()

  if not os.path.exists(target_directory):
    print("La cartella esiste e verrà creata")
    os.makedirs(target_directory)

  final_file_path = os.path.join(target_directory, file_name)
  shutil.copy(original_path, final_file_path)

  print(f"File copiato in: {final_file_path}")

  with open(final_file_path, "a") as file:
    file.write(f"\nCopiato da {original_path} a {final_file_path}")