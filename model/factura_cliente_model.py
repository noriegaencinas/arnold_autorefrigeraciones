import sqlite3
from flask import jsonify

def validar_factura_bd(folio, importe, fecha):
    try:
        with sqlite3.connect("instance/arnold_autorefrigeraciones.db") as conn:
            c = conn.cursor()
            query = "SELECT * FROM transacciones WHERE id_transaccion = ? AND monto = ? AND fecha_transaccion = ?"
            c.execute(query, (folio, importe, fecha))
            result = c.fetchone()
            if result:
                return jsonify({"status": "success"})
            else:
                return jsonify({"status": "error"})
    except sqlite3.Error as e:
        return [("error", str(e))]  # En caso de error, devolvemos una lista con una opción de error