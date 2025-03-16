from flask import Flask
import mysql.connector

app = Flask(__name__)

# Configuración básica
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'tu_contraseña'  # Cambia a tu contraseña
app.config['MYSQL_DB'] = 'desarrollo_web'

# Método de conexión directa
def conectar_db():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
