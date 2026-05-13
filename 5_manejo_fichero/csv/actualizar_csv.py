import csv

def actualizar_datos(carpeta, nombre):
    empleado_nuevo = pedir_datos()
    fichero = open(f'./{carpeta}/{nombre}', 'a', encoding='UTF-8', newline="")
    mi_csv = csv.DictWriter(fichero)
    mi_csv.writerow(empleado_nuevo)

id = 6
def pedir_datos():
    global id 
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    correo = input("Correo: ")
    dpto = input("Departamento: ")
    id += 1
    return {
            "id": id,
            "nombre": nombre,
            "apellidos": apellidos,
            "correo": correo,
            "departamento": dpto
                }

