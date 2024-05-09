from controller.DBController import *
from server import app
from model.models import *

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, LoginManager, login_required
from werkzeug.security import check_password_hash

# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

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
    rows = SelectAutomoviles()
    return render_template('menu_automoviles.html', automoviles=rows)

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