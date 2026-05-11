# Funcion que reciba el nombre del fichero, lo abrirá, lo leerá y que devuelva la suma total de todos los productos del carrito

def sumar_carrito(nombre_fichero):
    try:
        mi_carrito = open(f"{nombre_fichero}.txt", 'r', encoding='UTF-8')

        carrito = []

        for linea in mi_carrito.readlines():
            linea = linea.replace('\n', "")
            linea = linea.split(" ")
            print(linea)
            carrito.append(float(linea[1]))
        else:   
            print(carrito)
            suma = sum(carrito)
            print(suma)
        # MUY IMPORTANTE: Cerrar el fichero
        mi_carrito.close()
    except FileNotFoundError:
        print("El fichero no existe")

sumar_carrito('carrito')
sumar_carrito('productos')