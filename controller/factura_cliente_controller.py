from main import app

from model.factura_cliente_model import *

from flask import render_template, request
# Menu facturas

@app.route("/menu/facturas/")
def menu_facturas_clientes():    
    return render_template('menu_facturas_clientes.html')

@app.route("/menu/facturas/datos")
def menu_facturas_clientes_datos():    
    return render_template('menu_facturas_clientes_datos.html')

@app.route("/menu/facturas/validar", methods=['POST'])
def validar_factura():    
    if request.method == 'POST':
        data = request.json  # Usar JSON ya que el script envía datos en formato JSON
        folio = data.get('folio')
        importe = data.get('importe')
        fecha = data.get('fecha')

        # Llama al modelo y devuelve su resultado
        return validar_factura_bd(folio, importe, fecha)


    
    