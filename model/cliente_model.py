import sqlite3
from sqlite3 import Error
from math import ceil

def select_clientes_db():
    try:
        with sqlite3.connect("instance/arnold_autorefrigeraciones.db") as conn:
            c = conn.cursor()
            c.execute("SELECT id_cliente, nombre FROM clientes")  # Solo seleccionamos el ID y el nombre del cliente
            myresult = c.fetchall()

            # Convertir los datos a una lista de tuplas (id, nombre)
            options = [(str(row[0]), row[1]) for row in myresult]
        
            return options
    except sqlite3.Error as e:
        return [("error", str(e))]  # En caso de error, devolvemos una lista con una opción de error

def agregar_cliente_db(nombre, telefono, correo):
    try:
        with sqlite3.connect("instance/arnold_autorefrigeraciones.db") as conn:
            c = conn.cursor()
            c.execute("INSERT INTO clientes (nombre_cliente, telefono, correo) VALUES (?, ?, ?)", (nombre, telefono, correo))
            conn.commit()
    except sqlite3.Error as e:
        return [("error", str(e))]  # En caso de error, devolvemos una lista con una opción de error