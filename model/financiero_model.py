import sqlite3
from sqlite3 import Error
from math import ceil
from datetime import datetime

def select_transacciones_db(page):
    limit = 50
    start = limit * (page - 1)
    activo = 1
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("SELECT * FROM transacciones LIMIT ?, ?", (start, limit))
        myresult = c.fetchall()

        # Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in c.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))      

        # Get total number of records
        count = contar_transacciones_activos_db()  
        total_pages = ceil(count / limit) 

        another = select_grafica_db()
    
        conn.close()
        return [insertObject, total_pages, another]
    except sqlite3.Error as e:
        print("Error:", e)
        return None

def contar_transacciones_activos_db():
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        # Get total number of records
        c.execute("SELECT count(id_transaccion) FROM transacciones")
        count = c.fetchall()[0][0]        
        return count
    except Exception as e:
        return str(e)
    finally:
        if conn:
            conn.close()

def create_transaccion_db(tipo_transaccion, descripcion, monto, concepto, metodo_pago):
    fecha_transaccion = datetime.today().strftime('%Y-%m-%d')
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("INSERT INTO transacciones (fecha_transaccion, tipo_transaccion, descripcion, monto, concepto, metodo_pago) VALUES (?, ?, ?, ?, ?, ?)", (fecha_transaccion, tipo_transaccion, descripcion, monto, concepto, metodo_pago))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error:", e)

def select_grafica_db():
    try:
        conn = sqlite3.connect("instance/arnold_autorefrigeraciones.db")
        c = conn.cursor()
        c.execute("""
            SELECT fecha_transaccion, SUM(monto) AS total_transacciones
            FROM transacciones
            GROUP BY fecha_transaccion
        """)
        myresult = c.fetchall()

        # Convertir los datos a diccionario
        transacciones = []
        for record in myresult:
            transacciones.append({
                'fecha_transaccion': record[0],
                'total_transacciones': record[1]
            })

        conn.close()
        return transacciones
    except sqlite3.Error as e:
        print("Error:", e)
        return []