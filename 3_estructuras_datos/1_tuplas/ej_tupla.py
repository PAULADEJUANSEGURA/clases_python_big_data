# Tenemos un producto

producto = ("Laptop Pro", 899.94, 15, "electronica" )

producto2 = ("Ratón gaming", 34.90, 100, "electronica")
# precio total del stock del producto

def calcular_precio_stock(producto):
    return producto[1] * producto[2]

precio_p1 = calcular_precio_stock(producto)
precio_p2 = calcular_precio_stock(producto2)

print(f"El precio total del stock de {producto[0]} es: {precio_p1}  por un stock de {producto[2]}")
print(f"El precio total del stock de {producto2[0]} es: {precio_p2} por un stock de {producto2[2]}")
