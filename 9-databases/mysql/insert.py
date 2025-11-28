from connector import get_connection
from mysql.connector import Error

query_create_table = """
  CREATE TABLE IF NOT EXISTS persone (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cognome VARCHAR(255) NOT NULL,
    data_nascita DATE NULL
  )
"""

query_insert_people = """
  INSERT INTO persone (nome, cognome, data_nascita)
  VALUES (%s, %s, %s)
"""

people = [
    ("Luca", "Rossi", "1995-07-23"),
    ("Mario", "Bianchi", "1990-10-01"),
    ("Simona", "Gialli", "2005-12-15")
]

try:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query_create_table)
            cursor.executemany(query_insert_people, people)
        conn.commit()
        print("Tabella creata e dati inseriti con successo.")
except Error as err:
    print(f"Errore durante l'operazione su MySQL: {err}")