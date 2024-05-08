# Imports for Flask
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_bootstrap import Bootstrap4
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user
# Imports for database
import sqlite3
from sqlite3 import Error
# Imports for security
from werkzeug.security import check_password_hash
# Imports for SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

# Inicializando aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'miguelito'

# CREATE DATABASE 
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB for sqlalchemy
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

# CREATE TABLE IN DB 
with app.app_context():
    db.create_all()

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('database/arnold_autorefrigeraciones.db')
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
    conn = sqlite3.connect('database/arnold_autorefrigeraciones.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Inventario")
    rows = cur.fetchall()
    return rows

# Flask routes
@app.route("/", methods=['GET', 'POST'])
@app.route('/sign-in', methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('signin'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('signin'))
        else:
            login_user(user)
            return redirect(url_for('menu'))
    # Passing True or False if the user is authenticated. 
    return render_template("sign-in.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('signin'))

@app.route("/menu")
@login_required
def menu():
    return render_template('menu.html')

@app.route("/menu/inventario")
@login_required
def menu_inventario():
    data = SelectInventario()
    return render_template('menu_inventario.html', data=data)

@app.route("/menu/automoviles")
@login_required
def menu_automoviles():
    return render_template('menu_automoviles.html')

@app.route("/menu/empleados")
@login_required
def menu_empleados():
    return render_template('menu_empleados.html')

@app.route("/menu/financiero")
@login_required
def menu_financiero():
    return render_template('menu_financiero.html')

@app.route("/menu/facturas")
@login_required
def menu_facturas():
    return render_template('menu_facturas.html')

@app.route("/menu/reparaciones")
@login_required
def registro_reparaciones():
    return render_template('menu_reparaciones.html')

if __name__ == '__main__':
    create_connection()
    app.run(debug=True, port=5001)
