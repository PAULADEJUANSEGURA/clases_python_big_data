# Leer un archivo JSON
import json

def leer_json(carpeta, nombre_archivo):
    try:
        fichero = open(f"./{carpeta}/{nombre_archivo}", "r", encoding='UTF-8')
        # Cargar los datos del archivo JSON en una variable
        datos = json.load(fichero)
        return datos
    except FileNotFoundError:
        print("El archivo o carpeta no existe.")
    

lista_empleados = leer_json("data", "empleados.json")
print(lista_empleados)




