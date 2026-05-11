# Para crear un fichero tenemos "w"
# Si no existe lo crea, 
# Si existe, lo sobreescribe

# mi_fichero = open('./texto_creado.txt', 'w', encoding='UTF-8')

notas_modulo_python = [
    {'nombre': 'Paula', 'nota': 8},
    {'nombre': 'Pablo', 'nota': 3.5},
    {'nombre': 'Lara', 'nota': 4},
    {'nombre': 'Miguel Angel', 'nota': 6},
    {'nombre': 'Miriam', 'nota': 9},
    {'nombre': 'Reniel', 'nota': 6.5},
    {'nombre': 'David', 'nota': 3},
    {'nombre': 'Luis', 'nota': 6},
]

notas_modulo_python2 = [
    {'nombre': 'Mario', 'nota': 10},
    {'nombre': 'Juanan', 'nota': 10},

]

def crear_fichero(nombre_fichero, ruta, extension, datos):
    path = f"{ruta}{nombre_fichero}{extension}"
    print(path)
    mi_fichero = open(path, 'w', encoding='UTF-8')
    # Guardar los valores en mi fichero:
    for alumno in datos:
        mi_fichero.write(f"{alumno["nombre"]}: {alumno["nota"]}\n")

    
    mi_fichero.close()



# MUY IMPORTANTE: Cerrar el fichero
crear_fichero('notas_python', './datos/', '.txt', notas_modulo_python)
# crear_fichero('notas_python', './datos/', '.txt', notas_modulo_python2)
