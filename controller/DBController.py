# Imports for database
from math import ceil
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        print("Conexión exitosa a la base de datos con SQLite versión:", sqlite3.version)

        # Crear un objeto cursor
        cur = conn.cursor()

        # Ejecutar una consulta SELECT
        cur.execute("SELECT * FROM Inventario") 

        # Imprimir los resultados de la consulta
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def SelectInventario():
    conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Inventario")
    rows = cur.fetchall()
    conn.close()
    return rows

def SelectAutomoviles():
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Automoviles")
        rows = c.fetchall() 
        conn.close()
        return rows
    except Exception as e:
        return str(e) 
    
def select_empleados(page):
    limit=10
    start = limit * (page - 1)
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Empleados LIMIT ?, ?", (start, limit))
        rows = c.fetchall()

        # Get total number of records
        c.execute("SELECT count(id_empleado) FROM Empleados")
        empleadosCount = c.fetchall()[0][0]
        total_pages = ceil(empleadosCount // limit)

        conn.close()
        return [rows, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None

def SelectRegistroReparaciones():
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Automoviles WHERE Activo = 0")
        rows = c.fetchall()         
        conn.close()
        return rows
    except Exception as e:
        return str(e)    