from flask import Flask, render_template, request, jsonify
import json
import csv
from flask_sqlalchemy import SQLAlchemy

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

### 2.1 Persistencia con Archivos TXT

# Ruta para guardar datos en un archivo TXT
@app.route('/guardar_txt', methods=['POST'])
def guardar_txt():
    if request.method == 'POST':
        data = request.form['data']
        with open('datos/datos.txt', 'a') as file:
            file.write(data + '\n')
        return render_template('resultado.html', message="Datos guardados en archivo TXT.")

# Ruta para leer datos desde un archivo TXT
@app.route('/leer_txt')
def leer_txt():
    try:
        with open('datos/datos.txt', 'r') as file:
            data = file.readlines()
        return render_template('resultado.html', data=data)
    except FileNotFoundError:
        return render_template('resultado.html', message="El archivo no existe o está vacío.")

### 2.2 Persistencia con Archivos JSON

# Ruta para guardar datos en un archivo JSON
@app.route('/guardar_json', methods=['POST'])
def guardar_json():
    if request.method == 'POST':
        data = request.form['data']
        try:
            with open('datos/datos.json', 'r') as file:
                content = json.load(file)
        except FileNotFoundError:
            content = []

        content.append(data)

        with open('datos/datos.json', 'w') as file:
            json.dump(content, file, indent=4)

        return render_template('resultado.html', message="Datos guardados en archivo JSON.")

# Ruta para leer datos desde un archivo JSON
@app.route('/leer_json')
def leer_json():
    try:
        with open('datos/datos.json', 'r') as file:
            data = json.load(file)
        return render_template('resultado.html', data=data)
    except FileNotFoundError:
        return render_template('resultado.html', message="El archivo JSON no existe o está vacío.")

### 2.3 Persistencia con Archivos CSV

# Ruta para guardar datos en un archivo CSV
@app.route('/guardar_csv', methods=['POST'])
def guardar_csv():
    if request.method == 'POST':
        data = request.form['data']
        with open('datos/datos.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([data])
        return render_template('resultado.html', message="Datos guardados en archivo CSV.")

# Ruta para leer datos desde un archivo CSV
@app.route('/leer_csv')
def leer_csv():
    try:
        with open('datos/datos.csv', 'r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return render_template('resultado.html', data=data)
    except FileNotFoundError:
        return render_template('resultado.html', message="El archivo CSV no existe o está vacío.")

### 2.4 Persistencia con SQLite

# Ruta para guardar datos en la base de datos SQLite
@app.route('/guardar_sqlite', methods=['POST'])
def guardar_sqlite():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_usuario = Usuario(nombre=nombre)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return render_template('resultado.html', message="Usuario guardado en la base de datos.")

# Ruta para leer usuarios desde la base de datos SQLite
@app.route('/leer_sqlite')
def leer_sqlite():
    usuarios = Usuario.query.all()
    return render_template('resultado.html', usuarios=usuarios)

# Inicialización de la base de datos (si no existe)
@app.before_first_request
def crear_base_de_datos():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
