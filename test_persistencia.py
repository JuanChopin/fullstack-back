import persistencia

with open("pedidos.txt", "w", encoding="utf-8") as file:
 file.write("")
 file.close()

pedidos = [{"nombre" : "Pedro", "apellido" : "Gil de Diego"},
            {"nombre" : "Michael", "apellido" : "Jordan"},
            {"nombre" : "Bill", "apellido" : "Gates"},
            {"nombre" : "Juan", "apellido" : "Alzate"}]

for elem in pedidos:
    persistencia.guardar_pedido(elem["nombre"], elem["apellido"])



