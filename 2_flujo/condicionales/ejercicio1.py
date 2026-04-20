"""
    Pide por input el importe de una compra
    Si el importe es mayor que 100 muestra el mensaje:
        "Aplicamos un 10% de descuento"
    Y además, mostramos el precio con el descuento aplicado
"""

# Programa Ejercicio 1

compra = float(input("Introduce el importe de precio de tu compra: "))
if (compra > 100):
    print("Aplicamos '10% por ciento' de descuento")
    # El descuento lo calculamos multiplicando el precio de la compra por 0.10 y luego lo restamos al precio original de la compra
    descuento = compra * 0.10
    compra_con_descuento = compra - descuento
    print(f"Tu compra con el precio original es: {compra} Tu compra tiene el precio con descuento de: {compra_con_descuento} € ")



# Solución Ejercicio

precio = float(input("Dime el importe: "))
if precio > 100:
    print("Aplicamos el '10%' de descuento")
    # El precio con descuento es el precio original multiplicado por 0.90 porque el descuento es del 10% y el precio con descuento es el precio original menos el descuento.
    precio_con_descuento2 = precio * 0.90
    print(f"Precio original: {precio} en €uros. Precio con descuento: {precio_con_descuento2} en €uros.")