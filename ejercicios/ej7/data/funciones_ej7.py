# Funciones del Ejercicio 7 


def crear_fichero(nombre_fichero, ruta, extension):         
    path = f"{ruta}{nombre_fichero}{extension}"
    print(path)
    mi_fichero = open(path, 'w', encoding='UTF-8')
    # Cerramos fichero
    mi_fichero.close()



def actualizar_datos(nombre_fichero, ruta, extension, datos):
    path = f"{ruta}{nombre_fichero}{extension}"
    print(path)
    mi_fichero = open(path, 'a', encoding='UTF-8')
    nombre = input("Dime el nombre del producto: ")
    precio = input("Dime el precio del producto: ")
    return mi_fichero.write(f"{nombre}: {precio}\n")


"""def leer_fichero():
    mi_fichero = open('./lista_de_la_compra.txt', 'r', encoding='UTF-8')
    for linea in mi_fichero.readlines():
"""
