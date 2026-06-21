from connector import get_connection

with get_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, nome, cognome, data_nascita FROM persone")
        for row in cursor.fetchall():
            print(row)