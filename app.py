from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta'

# Definir la clase del formulario
class NombreForm(FlaskForm):
    nombre = StringField('Ingresa tu nombre', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Ruta para mostrar y procesar el formulario
@app.route('/usuario/', methods=['GET', 'POST'])
def usuario_form():
    form = NombreForm()  # Crear una instancia del formulario
    if form.validate_on_submit():  # Si el formulario es enviado y validado
        nombre = form.nombre.data  # Obtener el nombre ingresado
        return redirect(url_for('resultado', nombre=nombre))  # Redirigir a la página de resultado
    return render_template('formulario.html', form=form)  # Mostrar el formulario

# Ruta para mostrar el resultado
@app.route('/resultado/<nombre>')
def resultado(nombre):
    return render_template('resultado.html', nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
