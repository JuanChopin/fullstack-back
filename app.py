"""Pizza full stack Backend"""
from flask import Flask, request, redirect

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
