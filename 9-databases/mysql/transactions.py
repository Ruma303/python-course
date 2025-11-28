from connector import get_connection
from mysql.connector import Error

try:
    with get_connection() as conn:
      try:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE persone SET nome = %s WHERE id = %s", ("Giovanni", 1))
            cursor.execute("INSERT INTO tizio (nome, cognome, data_nascita) VALUES (%s, %s, %s)",
                           ("Laura", "Verdi", "2001-03-08"))
        conn.commit()  # Conferma tutte le modifiche della transazione
        print("Transazione eseguita correttamente")
      except:
        conn.rollback()
        raise
except Error as err:
    print("Errore:", err)
    conn.rollback()  # Annulla tutte le modifiche se si verifica un errore