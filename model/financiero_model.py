import sqlite3
from sqlite3 import Error
from math import ceil

def select_transacciones_db(page):
    limit=10
    start = limit * (page - 1)
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM transacciones LIMIT ?, ?", (start, limit))
        myresult = c.fetchall()

        # Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in c.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))    

        # Get total number of records
        count = contar_transacciones_activos_db()  
        total_pages = ceil(count / limit) 

        conn.close()
        return [insertObject, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None

def contar_transacciones_activos_db():
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        # Get total number of records
        c.execute("SELECT count(id_transaccion) FROM transacciones")
        count = c.fetchall()[0][0]        
        return count
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()