# Actualizar fichero

def actualizar_datos(ruta, nombre_fichero):
    mi_fichero = open(f"{ruta}{nombre_fichero}", 'a', encoding='UTF-8')
    nombre = input("Dime el nombre del alumno: ")
    nota = input("Dime la nota del alumno: ")
    mi_fichero.write(f"{nombre}: {nota}\n")
    mi_fichero.close()


actualizar_datos('./datos/', 'notas_python.txt')