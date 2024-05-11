import sqlite3
from sqlite3 import Error
from math import ceil

def select_automoviles_db(page):
    limit = 10
    start = limit * (page - 1)
    activo = 1
    try:
        with sqlite3.connect("instance/arnold_autorefrigeraciones.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM automoviles WHERE activo = ? LIMIT ?, ?", (activo, start, limit))
            myresult = c.fetchall()

            # Convertir los datos a diccionario
            insertObject = []
            columnNames = [column[0] for column in c.description]
            for record in myresult:
                insertObject.append(dict(zip(columnNames, record)))                

            # Obtener el número total de registros        
            count = contar_automoviles_activos()  
            total_pages = ceil(count / limit)        
        
            return [insertObject, total_pages]
    except sqlite3.Error as e:
        return str(e)

def contar_automoviles_activos():
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        # Get total number of records
        c.execute("SELECT count(id_automovil) FROM automoviles WHERE activo = ?", (activo, ))
        count = c.fetchall()[0][0]        
        return count
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()