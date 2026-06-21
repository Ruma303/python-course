import mysql.connector
from mysql.connector import Error

def get_connection():
    """
    Restituisce una nuova connessione a MySQL.
    Lancia un'eccezione in caso di errore.
    """
    database = "python_db"
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database=database,
        port=3306
    )

"""
conn = None

try:
    database = "python_db"

    conn = mysql.connector.connect(
        host="127.0.0.1", user="root", password="root", database=database, port=3306
    )

    if conn.is_connected():
        print(f"Connesso al database: {database}")

except mysql.connector.Error as err:
    print(f"Errore durante la connessione a MySQL: {err}")

finally:
    if conn is not None and conn.is_connected():
        conn.close()
        print("Connessione a MySQL chiusa con successo")
 """