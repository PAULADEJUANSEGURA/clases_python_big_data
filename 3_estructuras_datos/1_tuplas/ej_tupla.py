# Tenemos un producto

producto = ("Laptop Pro", 899.94, 15, "electronica" )

producto2 = ("Ratón gaming", 34.90, 100, "electronica")
# precio total del stock del producto

'''def precio_total_stock():
    for i in range(0, len(producto)):
        precio_producto = producto[1]
        cantidad_stock = producto[2]
        total_stock = precio_producto * cantidad_stock
        print(f"El total del stock del {producto[0]} es: {total_stock}")
    
precio_total_stock()'''


def calcular_precio_stock(producto):
    return producto[1] * producto[2]

precio_p1 = calcular_precio_stock(producto)
precio_p2 = calcular_precio_stock(producto2)

print(precio_p1, precio_p2)
