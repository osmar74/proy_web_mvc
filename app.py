"""
app.py - Controlador principal del proyecto web MVC

Este archivo inicializa la aplicación Flask, configura las rutas básicas
y sirve como punto de entrada del servidor web.

Uso:
    python app.py

Resultado esperado:
    Servidor corriendo en http://localhost:5000
"""
from flask import Flask, render_template

# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta de prueba
@app.route('/')
def index():
    return render_template('layouts/base.html')

# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)