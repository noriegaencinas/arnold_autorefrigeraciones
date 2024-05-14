import sqlite3
from sqlite3 import Error
from math import ceil


def select_inventario_db(page):
    limit = 10
    start = limit * (page - 1)
    activo = 1
    try:
        with sqlite3.connect("instance/arnold_autorefrigeraciones.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM inventario WHERE activo = ? LIMIT ?, ?", (activo, start, limit))
            myresult = c.fetchall()

            # Convertir los datos a diccionario
            insertObject = []
            columnNames = [column[0] for column in c.description]
            for record in myresult:
                insertObject.append(dict(zip(columnNames, record)))                

            # Obtener el número total de registros        
            count = contar_activos_inventario_db()  
            total_pages = ceil(count / limit)        
        
            return [insertObject, total_pages]
    except sqlite3.Error as e:
        return str(e)

def contar_activos_inventario_db():
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        # Get total number of records
        c.execute("SELECT count(id_inventario) FROM inventario WHERE activo = ?", (activo, ))
        count = c.fetchall()[0][0]        
        return count
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()
            
def actualizar_producto_db(id_inventario, nombre, cantidad, precio_compra, tipo, descripcion, precio_venta):
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE inventario SET Nombre = ?, Cantidad = ?, PrecioCompra = ?, Tipo = ?, Descripcion = ?, PrecioVenta = ? WHERE id_inventario = ?", (nombre, cantidad, precio_compra, tipo, descripcion, precio_venta, id_inventario))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)
        
def eliminar_producto_db(id_inventario):
    inactivo = 0
    try:        
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("UPDATE inventario SET Activo = ? WHERE id_inventario = ?", (inactivo, id_inventario))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def crear_producto_db(nombre, cantidad, precio_compra, tipo, descripcion, precio_venta):
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("INSERT INTO inventario (Nombre, Cantidad, PrecioCompra, Tipo, Descripcion, PrecioVenta) VALUES (?, ?, ?, ?, ?, ?)", (nombre, cantidad, precio_compra, tipo, descripcion, precio_venta))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)
        
def select_producto_by_filter_db(filtro):
    limit=10    
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        conn.row_factory = sqlite3.Row  # This allows you to access rows as dictionaries
        c = conn.cursor()
        c.execute("SELECT * FROM inventario WHERE Nombre LIKE '%' || ? || '%'", (filtro,))
        rows = [dict(row) for row in c.fetchall()]  # Convert rows to dictionaries
        print(rows)
        # Get total number of records
        c.execute("SELECT count(id_inventario) FROM inventario WHERE Nombre LIKE '%' || ? || '%'", (filtro,))        
        count = c.fetchall()[0][0]
        total_pages = ceil(count / limit)
        conn.close()
        return [rows, total_pages]
    except sqlite3.Error as e:
        print("Error:", e)
        return None
   