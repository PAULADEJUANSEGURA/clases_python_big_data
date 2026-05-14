# Crear un archivo JSON
import json
import os

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]

def crear_json(carpeta, nombre_fichero, datos):
    # Crear la carpeta si no existe
    os.makedirs(carpeta, exist_ok=True)
    
    # Escribir los datos en el archivo JSON
    fichero = open(f"./{carpeta}/{nombre_fichero}", "w", encoding='UTF-8')
    # Volcar los datos de la lista en un Objeto.json
    json.dump(datos, fichero, indent=4, ensure_ascii=False)
    # si no le das los parametros indent y ensure_ascii, el resultado se mostrará en una sola línea y los caracteres acentuados se mostrarán con códigos Unicode y se verán mal las letras con tildes y la letra ñ. Con indent=4, el resultado se mostrará con una sangría de 4 espacios, lo que hace que sea más legible. Con ensure_ascii=False, los caracteres acentuados se mostrarán correctamente en lugar de ser convertidos a códigos Unicode.
    fichero.close()



crear_json("data", "trabajadores.json", lista_empleados)


