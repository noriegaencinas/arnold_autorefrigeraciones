# Imports for database
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('database/arnold_autorefrigeraciones.db')
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
    conn = sqlite3.connect('database/arnold_autorefrigeraciones.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Inventario")
    rows = cur.fetchall()
    conn.close()
    return rows

def SelectAutomoviles():
    try:
        conn = sqlite3.connect('database/arnold_autorefrigeraciones.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Automoviles")
        rows = c.fetchall() 
        conn.close()
        return rows
    except Exception as e:
        return str(e) 
