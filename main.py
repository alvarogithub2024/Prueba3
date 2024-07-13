from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar_ejercicio1', methods=['POST'])
def procesar_ejercicio1():
    try:
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
        return f'Promedio: {promedio:.1f}, Asistencia: {asistencia}%, Estado: {estado}'
    except ValueError:
        return "Por favor, asegúrate de ingresar valores válidos en todos los campos."

@app.route('/procesar_ejercicio2', methods=['POST'])
def procesar_ejercicio2():
    nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]
    mayor_nombre = max(nombres, key=len)
    longitud = len(mayor_nombre)
    return render_template('ejercicio2.html', resultado=f'El nombre con mayor cantidad de caracteres es: {mayor_nombre} - El nombre tiene: {longitud} caracteres')

if __name__ == '__main__':
    app.run(debug=True)
