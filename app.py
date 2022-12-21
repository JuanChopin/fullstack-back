"""Pizza full stack Backend"""
from flask import Flask, request, redirect, Response

app = Flask(__name__)

@app.route("/pizza", methods = ['POST'])
def prueba ():
    """Funcion que se ejecuta al invocarse /pizza"""
    nombre = request.form.get("nombreCliente")
    apellido = request.form.get("apellidoCliente")
    print(nombre, apellido)
    with open("pedidos.txt", "a", encoding = "utf-8") as file:
        file.write(nombre + " " + apellido + "\n")
        file.close()
    return redirect("http://localhost/solicita_pedido.html", code=302)

@app.route("/checksize", methods = ['POST'])
def checksize():
    """Funcion que encuentra la disponibilidad de la pizza"""
    size = request.form.get("size")
    if size == "S":
        mensaje = "No disponible"
    else:
        mensaje = "Disponible"
    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
