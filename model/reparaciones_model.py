import sqlite3
from sqlite3 import Error
from math import ceil

def select_automovil_db(page):
    limit=10
    start = limit * (page - 1)
    alta = 1
    inactivo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM automoviles WHERE alta = ? AND activo = ? LIMIT ?, ?", (alta, inactivo, start, limit))
        myresult = c.fetchall()

        # Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in c.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))    

        # Get total number of records
        count = contar_automoviles_inactivos_db()  
        total_pages = ceil(int(count) / int(limit)) 

        print(insertObject)
        print("Total records: ", count)
        print("Total pages: ", total_pages)
        conn.close()
        return [insertObject, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None

def contar_automoviles_inactivos_db():
    alta = 1
    inactivo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        # Get total number of records
        c.execute("SELECT count(id_automovil) FROM automoviles WHERE alta = ? AND activo = ?", (alta, inactivo))
        count = c.fetchall()[0][0]        
        return int(count)
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()

def select_automovil_by_filter_db(filtro):
    limit=10    
    alta = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        conn.row_factory = sqlite3.Row  # This allows you to access rows as dictionaries        
        c = conn.cursor()
        c.execute("SELECT * FROM automoviles WHERE marca LIKE '%' || ? || '%' OR modelo LIKE '%' || ? || '%' OR placa LIKE '%' || ? || '%' OR motivo_ingreso LIKE '%' || ? || '%' OR fecha_ingreso LIKE '%' || ? || '%' OR notas LIKE '%' || ? || '%' OR nombre_propietario LIKE '%' || ? || '%' OR telefono_propietario LIKE '%' || ? || '%' OR correo_propietario LIKE '%' || ? || '%' AND alta = ?", (filtro, filtro, filtro, filtro, filtro, filtro, filtro, filtro, filtro, alta))
        rows = [dict(row) for row in c.fetchall()]  # Convert rows to dictionaries        
        # Get total number of records
        c.execute("SELECT count(id_automovil) FROM automoviles WHERE marca LIKE '%' || ? || '%' OR modelo LIKE '%' || ? || '%' OR placa LIKE '%' || ? || '%' OR motivo_ingreso LIKE '%' || ? || '%' OR fecha_ingreso LIKE '%' || ? || '%' OR notas LIKE '%' || ? || '%' OR nombre_propietario LIKE '%' || ? || '%' OR telefono_propietario LIKE '%' || ? || '%' OR correo_propietario LIKE '%' || ? || '%' AND alta = ?", (filtro, filtro, filtro, filtro, filtro, filtro, filtro, filtro, filtro, alta))
        count = c.fetchall()[0][0]
        total_pages = ceil(count / limit)
        conn.close()
        return [rows, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None
   
def activar_automovil_db(id_automovil):
    activar = 0 
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE automoviles SET alta = ? WHERE id_automovil = ?", (activar, id_automovil))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)
        return None
    finally:
        if conn:
            conn.close()

test = True
if test:
    select_automovil_db(1)