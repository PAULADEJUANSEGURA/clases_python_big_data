# importamos una libreria de python operating system
import os

# Funcion crear un archivo

def crear_archivo(carpeta, nombre, extension):
    os.makedirs(carpeta, exist_ok=True)
    fichero = open(f"./{carpeta}/{nombre}.{extension}", "w", encoding="UTF-8")
    fichero.write("Algo como ejemplo")
    fichero.close()

crear_archivo('data', 'prueba', 'txt')

