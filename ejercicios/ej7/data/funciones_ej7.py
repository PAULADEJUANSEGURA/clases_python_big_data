# Funciones del Ejercicio 7 
lista_de_la_compra = []

def crear_fichero(nombre_fichero, ruta, extension):         
    path = f"{ruta}{nombre_fichero}{extension}"
    # print(path)
    mi_fichero = open(path, 'x', encoding='UTF-8')
    # Cerramos fichero
    mi_fichero.close()



def actualizar_datos(nombre_fichero, ruta, extension):
    path = f"{ruta}{nombre_fichero}{extension}"
    # print(path)
    mi_fichero = open(path, 'a', encoding='UTF-8')
    nombre = input("Dime el nombre del producto: ")
    precio = input("Dime el precio del producto: ")
    mi_fichero.write(f"{nombre}: {precio}\n")
    # Cerramos fichero
    mi_fichero.close()


def leer_fichero(nombre_fichero, ruta, extension):
    path = f"{ruta}{nombre_fichero}{extension}"
    # print(path)
    mi_fichero = open(path, 'r', encoding='UTF-8')
    for producto in mi_fichero.readlines():
        print(f"Producto: \033[33m{producto}\033[0m")
        lista_de_la_compra.append(producto)
    # else:
        # print(lista_de_la_compra)      
    # Cerramos fichero  
    mi_fichero.close()


def sobrescribir_fichero(nombre_fichero, ruta, extension):
    path = f"{ruta}{nombre_fichero}{extension}"
    # print(path)
    mi_fichero = open(path, 'w', encoding='UTF-8')
    mi_fichero.write("")    
    # Cerramos fichero
    mi_fichero.close()