def calcular_total(subtotal, impuesto):
    total = subtotal + (subtotal * impuesto)
    return total

def generar_factura(nombre_cliente, items, subtotal, impuesto, total):
    print("Factura de Venta")
    print("Cliente: {}".format(nombre_cliente))
    print("-----------------------------")
    for item in items:
        print("{} - ${}".format(item[0], item[1]))
    print("-----------------------------")
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Impuesto: ${:.2f}".format(subtotal * impuesto))
    print("Total: ${:.2f}".format(total))
    print("-----------------------------")
    print("¡Gracias por su compra!")

nombre_cliente = "Alberto"
items = [("Bisteck", 10.99), ("Azúcar", 5.99), ("Pollo", 7.50), ("Harina", 3.6), ("Chuleta", 9), ("Verduras", 5.3), ("Queso", 2.6)]
subtotal = sum(item[1] for item in items)
impuesto = 0.16  # Impuesto del 16%
total = calcular_total(subtotal, impuesto)
generar_factura(nombre_cliente, items, subtotal, impuesto, total)
