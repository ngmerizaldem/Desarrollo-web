from flask import Flask, jsonify
from Conexión.conexion import conectar_db

app = Flask(__name__)

@app.route('/test_db')
def test_conexion():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        cursor.close()
        conexion.close()
        return f"Conexión exitosa. Versión MySQL: {version[0]}"
    except Exception as e:
        return f"Error de conexión: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
