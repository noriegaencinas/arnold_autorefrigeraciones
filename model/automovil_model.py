import sqlite3
from sqlite3 import Error
from math import ceil

def select_automoviles_db(page):
    limit=10
    start = limit * (page - 1)
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM empleados WHERE activo = ? LIMIT ?, ?", (activo, start, limit))
        myresult = c.fetchall()

        #Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in c.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))                

        # Get total number of records        
        empleadosCount = contar_automoviles_activos()
        total_pages = ceil(empleadosCount / limit)        
        
        return [insertObject, total_pages]
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()

def contar_automoviles_activos():
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        # Get total number of records
        c.execute("SELECT count(id_empleado) FROM empleados WHERE activo = ?", (activo, ))
        empleadosCount = c.fetchall()[0][0]        
        return empleadosCount
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()

    