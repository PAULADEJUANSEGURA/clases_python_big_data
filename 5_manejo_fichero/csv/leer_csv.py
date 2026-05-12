import csv

def pintar_datos(ruta, nombre_fichero):
    fichero = open(f"./{ruta}/{nombre_fichero}", 'r', encoding='UTF-8')
    # crear un elemento lector que me va a permitir leer el csv
    lector = csv.reader(fichero)
    # si el archivo tiene cabeceras me las salto
    next(lector)
    for fila in lector:
        print("-" * 20)
        print(f"{fila[0]}: {fila[1]} {fila[2]} - Departamento: {fila[4]}")
    else:
        print("-" * 20)
    fichero.close()



pintar_datos('data', 'empleados.csv')



lista_de_empleados = []


def crear_diccionario(ruta, nombre_fichero):
    fichero = open(f"./{ruta}/{nombre_fichero}", 'r', encoding='UTF-8')
    
    # crear un elemento lector que me va a permitir leer el csv
    lector = csv.DictReader(fichero)
    for empleado in lector:
        lista_de_empleados.append(empleado)
    return lista_de_empleados

resultado = crear_diccionario('data', 'empleados.csv')
print(resultado)



def crear_diccionario_2(ruta, nombre_fichero):
    fichero = open(f"./{ruta}/{nombre_fichero}", 'r', encoding='UTF-8')
    lector = csv.reader(fichero)
    next(lector, None)
    for fila in lector:
        empleado = {
                    "id": fila[0],
                    "nombre": fila[1],
                    "apellido": fila[2],
                    "email": fila[3],
                    "departamento": fila[4]
                }
    lista_de_empleados.append(empleado)
    fichero.close()
    return lista_de_empleados

resultado_2 = crear_diccionario_2('data', 'empleados.csv')
print(resultado_2)



def cargar_datos3(carpeta, fichero):
    fichero = open(f"{carpeta}/{fichero}", "r", encoding='UTF-8')
    lector = csv.DictReader(fichero) 
    # Lo convertimos a lista con LIST (lector)
    lista_empleados = list(lector)
    print(lista_empleados)
    

cargar_datos3('data', 'empleados.csv')  