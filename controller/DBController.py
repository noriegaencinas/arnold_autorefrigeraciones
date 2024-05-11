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
    
# Menu empelados

def select_empleados_db(page):
    limit=10
    start = limit * (page - 1)
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM Empleados WHERE activo = ? LIMIT ?, ?", (activo, start, limit))
        rows = c.fetchall()

        # Get total number of records
        c.execute("SELECT count(id_empleado) FROM Empleados WHERE activo = ?", (activo, ))
        empleadosCount = c.fetchall()[0][0]
        total_pages = ceil(empleadosCount / limit)

        conn.close()
        return [rows, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None

def eliminar_empleado_id(id_empleado):
    inactivo = 0
    try:        
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE Empleados SET activo = ? WHERE id_empleado = ?", (inactivo, id_empleado))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def agregar_empleado_db(nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario):
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("INSERT INTO Empleados (nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def actualizar_empleado_db(id_empleado, nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario):
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE Empleados SET nombre_completo = ?, cargo = ?, fecha_contratacion = ?, activo = ?, horario_trabajo = ?, numero_contacto = ?, correo_electronico = ?, salario = ? WHERE id_empleado = ?", (nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario, id_empleado))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

# Menu reparaciones

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