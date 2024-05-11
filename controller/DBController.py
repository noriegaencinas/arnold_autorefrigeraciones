# Imports for database
import sqlite3
from sqlite3 import Error

def SelectInventario():
    conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventario")
    rows = cur.fetchall()
    conn.close()
    return rows

def SelectRegistroReparaciones():
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM automoviles WHERE Activo = 0")
        rows = c.fetchall()         
        conn.close()
        return rows
    except Exception as e:
        return str(e)    
    