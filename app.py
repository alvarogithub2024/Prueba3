from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formulario1', methods=['GET', 'POST'])
def formulario1():
    nombre = None
    total_sin_descuento = None
    descuento = None
    total_con_descuento = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro


        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        else:
            descuento = total_sin_descuento * 0.25

        total_con_descuento = total_sin_descuento - descuento

    return render_template('formulario1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, total_con_descuento=total_con_descuento)


@app.route('/formulario2', methods=['GET', 'POST'])
def formulario2():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']


        if nombre == "juan" and contrasena == "admin":
            mensaje = "Bienvenido administrador juan"
        elif nombre == "pepe" and contrasena == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Usuario o Contraseña incorrecta"

    return render_template('formulario2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
