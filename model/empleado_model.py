import sqlite3
from sqlite3 import Error
from math import ceil

def select_empleados_db(page):
    limit=10
    start = limit * (page - 1)
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM empleados WHERE activo = ? LIMIT ?, ?", (activo, start, limit))
        myresult = c.fetchall()

        # Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in c.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))    

        # Get total number of records
        count = contar_automoviles_activos_db()  
        total_pages = ceil(count / limit) 

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
        c.execute("SELECT count(id_empleado) FROM empleados WHERE activo = ?", (activo, ))
        count = c.fetchall()[0][0]        
        return count
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()

def eliminar_empleado_db(id_empleado):
    inactivo = 0
    try:        
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE empleados SET activo = ? WHERE id_empleado = ?", (inactivo, id_empleado))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def agregar_empleado_db(nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario):
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("INSERT INTO empleados (nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def actualizar_empleado_db(id_empleado, nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario):
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE empleados SET nombre_completo = ?, cargo = ?, fecha_contratacion = ?, activo = ?, horario_trabajo = ?, numero_contacto = ?, correo_electronico = ?, salario = ? WHERE id_empleado = ?", (nombre_completo, cargo, fecha_contratacion, activo, horario_trabajo, numero_contacto, correo_electronico, salario, id_empleado))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def select_empleado_by_filter_db(filtro):
    limit=10    
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        conn.row_factory = sqlite3.Row  # This allows you to access rows as dictionaries        
        c = conn.cursor()
        c.execute("SELECT * FROM empleados WHERE nombre_completo LIKE '%' || ? || '%' AND activo = ?", (filtro, activo))
        rows = [dict(row) for row in c.fetchall()]  # Convert rows to dictionaries        
        # Get total number of records
        c.execute("SELECT count(id_empleado) FROM empleados WHERE nombre_completo LIKE '%' || ? || '%'", (filtro,))        
        count = c.fetchall()[0][0]
        total_pages = ceil(count / limit)
        conn.close()
        return [rows, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None
   