# importamos libreria con import os
import os

"""def leer_linea(carpeta, nombre_fichero):
	fichero = open(f"{carpeta}/{nombre_fichero}", 'r', encoding='UTF-8')
    # Leer la primera línea del fichero
	linea = fichero.readline()
    # Imprimir la línea leída
	print(linea)
    # Cerrar el fichero
	fichero.close()


leer_linea('./datos', 'notas_python.txt')"""

folder = './datos'
filename = 'notas_python.txt'
file = open(f"./{folder}/{filename}", 'r', encoding='UTF-8')
line_1 = file.readline()
line_2 = file.readline()
print(line_1)
print(line_2)
file.close()
