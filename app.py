from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from Conexion.conexion import obtener_conexion

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto_seguro'  # Necesario para formularios con CSRF


@ @-39

, 6 + 40, 43 @ @


def resultado():
    @app.route('/about')
    def about():
        return render_template('about.html')


@app.route('/test_db')
def test_db():
    conexion = obtener_conexion()
    if conexion:
        return "Conexión exitosa a MySQL"
    else:
        return "Error en la conexión a MySQL"


# Ruta para obtener todos los usuarios de la base de datos
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)  # Para obtener los resultados en formato de diccionario
        cursor.execute("SELECT * FROM usurios")
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify(usuarios)  # Retornar los datos en formato JSON
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500


# Ruta para mostrar los usuarios en una tabla HTML
@app.route('/usuarios_formulario', methods=['GET'])
def usuarios_tabla():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)  # Para obtener los resultados en formato de diccionario
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return render_template('usuarios_formulario.html', usuarios=usuarios)
    else:
        return "Error en la conexión a la base de datos", 500


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)