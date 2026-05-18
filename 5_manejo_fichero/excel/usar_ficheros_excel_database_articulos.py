# Importamos la libreria import os para trabajar con archivos y directorios
import os

# Importamos la librería para trabajar con archivos Excel para LEERLOS con load_workbook!!
from openpyxl import load_workbook, Workbook

"""" # Ejemplo de uso de la librería openpyxl para leer un archivo Excel
# Importamos la librería para trabajar con archivos Excel
# import openpyxl

# 1. Cargar el libro de trabajo
libro = openpyxl.load_workbook('ventas.xlsx')

# 2. Seleccionar la hoja activa (la primera)
hoja = libro.active

# 3. Leer el valor de una celda específica
print(hoja['A1'].value)

# 4. Iterar sobre las filas de la hoja
# Recorremos la hoja fila por fila
for fila in hoja.iter_rows(values_only=True):
    # 'fila' es una tupla con los valores de cada celda en esa línea
    print(fila)
"""

def cargar_excel(carpeta, fichero):
    #cargar el fichero de excel en nuestro archivo
    libro_excel = load_workbook(f'./{carpeta}/{fichero}')
    # seleccionar la hoja que quiero. Hoja activa la primera hoja del libro de excel.
    hoja = libro_excel['Dim_Articulos']

    # en caso de necesitar seleccionar una hoja concreta lo haremos de esta forma
    # hoja = libro_excel['Dim_Clientes'] siendo dim_clientes el nombre de la hoja
    # hoja = libro_excel['Dim_Clientes'] # Siendo dim_clientes el nombre de la hoja

    # Creamos una lista vacía para almacenar los datos de los artículos
    lista_articulos = []


    # 3. Leer el valor de una celda específica
    print(hoja['A1'].value)
    
    #cargamos las cabeceras
    filas = hoja.iter_rows(values_only = True)
    cabeceras = next(filas)

    # 4. Iterar sobre las filas de la hoja
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        articulo_dict = dict(zip(cabeceras, fila))
        lista_articulos.append(articulo_dict)
   
   
    return lista_articulos
       
lista_pruebas = cargar_excel('data', 'database_pruebas.xlsx')
print(lista_pruebas)