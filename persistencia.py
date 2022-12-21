"""Guardar pedido"""
def guardar_pedido(nombre, apellido):
    """Esta funcion guarda un pedido en un archivo txt."""
    with open("pedidos.txt","a", encoding = "utf-8") as file:
        file.write(nombre + " " + apellido + "\n")
        file.close()
