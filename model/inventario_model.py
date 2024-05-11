import sqlite3
from sqlite3 import Error

def SelectInventario():
    conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventario")
    rows = cur.fetchall()
    conn.close()
    return rows