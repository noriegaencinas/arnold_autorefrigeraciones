# Imports for Flask
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap4
# Imports for database
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
bootstrap = Bootstrap4(app)

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('database/arnold_autorefrigeraciones.db')
        print("Conexión exitosa a la base de datos con SQLite versión:", sqlite3.version)

        # Crear un objeto cursor
        cur = conn.cursor()

        # Ejecutar una consulta SELECT
        cur.execute("SELECT * FROM Inventario")  # Reemplaza 'my_table' con el nombre de tu tabla

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
    conn = sqlite3.connect('database/arnold_autorefrigeraciones.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Inventario")
    rows = cur.fetchall()
    return rows

# Flask routes
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('sign-in.html')
    if request.method == 'POST':
        return render_template('menu.html')

@app.route("/sign-in")
def signin():
    return render_template('sign-in.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/menu/inventario")
def menu_inventario():
    data = SelectInventario()
    return render_template('menu_inventario.html', data=data)

@app.route("/menu/automoviles")
def menu_automoviles():
    return render_template('menu_automoviles.html')

@app.route("/menu/empleados")
def menu_empleados():
    return render_template('menu_empleados.html')

@app.route("/menu/financiero")
def menu_financiero():
    return render_template('menu_financiero.html')

@app.route("/menu/facturas")
def menu_facturas():
    return render_template('menu_facturas.html')

if __name__ == '__main__':
    create_connection()
    app.run(debug=True, port=5007)
