import sqlite3
from sqlite3 import Error
from math import ceil

def select_automovil_db(page):
    limit=10
    start = limit * (page - 1)
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM automoviles WHERE activo = ? LIMIT ?, ?", (activo, start, limit))
        myresult = c.fetchall()

        # Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in c.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))    

        # Get total number of records
        count = contar_automoviles_activos_db()  
        total_pages = ceil(int(count) / int(limit)) 

        conn.close()
        return [insertObject, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None

def contar_automoviles_activos_db():
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        # Get total number of records
        c.execute("SELECT count(id_automovil) FROM automoviles WHERE activo = ?", (activo, ))
        count = c.fetchall()[0][0]        
        return int(count)
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()

def eliminar_automovil_db(id_automovil):
    inactivo = 0
    try:        
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE id_automovil SET activo = ? WHERE id_automovil = ?", (inactivo, id_automovil))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def agregar_automovil_db(motivo_ingreso, fecha_ingreso, notas, estado, modelo, placa, marca, nombre_propietario, telefono_propietario, correo_propietario):
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("INSERT INTO automoviles (motivo_ingreso, fecha_ingreso, notas, estado, modelo, placa, marca, nombre_propietario, telefono_propietario, correo_propietario) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (motivo_ingreso, fecha_ingreso, notas, estado, modelo, placa, marca, nombre_propietario, telefono_propietario, correo_propietario))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def actualizar_automovil_db(motivo_ingreso, fecha_ingreso, notas, estado, modelo, placa, marca, nombre_propietario, telefono_propietario, correo_propietario, id_automovil):
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE automoviles SET motivo_ingreso = ?, fecha_ingreso = ?, notas = ?, estado = ?, modelo = ?, placa = ?, marca = ?, nombre_propietario = ?, telefono_propietario = ?, correo_propietario = ? WHERE id_automovil = ?", (motivo_ingreso, fecha_ingreso, notas, estado, modelo, placa, marca, nombre_propietario, telefono_propietario, correo_propietario, id_automovil))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def select_automovil_by_filter_db(filtro):
    limit=10    
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        conn.row_factory = sqlite3.Row  # This allows you to access rows as dictionaries        
        c = conn.cursor()
        c.execute("SELECT * FROM automoviles WHERE nombre_completo LIKE '%' || ? || '%' AND activo = ?", (filtro, activo))
        rows = [dict(row) for row in c.fetchall()]  # Convert rows to dictionaries        
        # Get total number of records
        c.execute("SELECT count(id_automovil) FROM automoviles WHERE nombre_completo LIKE '%' || ? || '%'", (filtro,))        
        count = c.fetchall()[0][0]
        total_pages = ceil(count / limit)
        conn.close()
        return [rows, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None
   
test = False
if test:
    select_automovil_by_filter_db('javier')