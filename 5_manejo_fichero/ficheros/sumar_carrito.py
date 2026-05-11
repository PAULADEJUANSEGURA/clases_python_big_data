# Funcion que reciba el nombre del fichero, lo abrirá, lo leerá y que devuelva la suma total de todos los productos del carrito

mi_carrito = open('./carrito.txt', 'r', encoding='UTF-8')

carrito = []

for linea in mi_carrito.readlines():
    linea = linea.replace('\n', "")
    linea = linea.split(" ")
    print(linea)
    carrito.append(int(linea[1]))
else:   
    print(carrito)
    suma = sum(carrito)
    print(suma)


# MUY IMPORTANTE: Cerrar el fichero
mi_carrito.close()

