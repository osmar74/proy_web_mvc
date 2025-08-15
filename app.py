"""
app.py - Controlador principal del proyecto web MVC

Este archivo inicializa la aplicación Flask, configura las rutas básicas
y sirve como punto de entrada del servidor web.

Uso:
    python app.py

Resultado esperado:
    Servidor corriendo en http://localhost:5000
"""
from flask import Flask

# Inicializar la aplicación Flask
app = Flask(__name__)

# Ruta de prueba
@app.route('/')
def index():
    return '<h1 style="color: #39FF14; text-align: center; margin-top: 50px;">¡Hola Mundo! - proy_web_mvc</h1>'

# Punto de entrada
if __name__ == '__main__':
    app.run(debug=True)