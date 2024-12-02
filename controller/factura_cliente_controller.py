from main import app

from model.factura_cliente_model import *

from flask import render_template
# Menu facturas

@app.route("/menu/facturas/")
def menu_facturas_clientes():    
    return render_template('menu_facturas_clientes.html')