import sqlite3
from sqlite3 import Error

def SelectRegistroReparaciones():
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM automoviles WHERE alta = 1")
        rows = c.fetchall()         
        conn.close()
        return rows
    except Exception as e:
        return str(e)    
    