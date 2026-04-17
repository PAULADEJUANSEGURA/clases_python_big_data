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
    con_descuento = compra * 0.9
    print(f"Tu compra con el precio original es: {compra} Tu compra tiene el precio con descuento de: {con_descuento} € ")



# Solución Ejercicio

precio = float(input("Dime el importe: "))
if precio > 100:
    print("Aplicamos el '10%' de descuento")
    precio_con_descuento2 = precio * 0.9
    print(f"Precio original: {precio} en €uros. Precio con descuento: {precio_con_descuento2} en €uros.")