# Importo librería para csv
import csv

# Importamos la librería para manejar XML
import xml.etree.ElementTree as et

# Importamos un archivo JSON
import json

# Importamos la libreria import os para trabajar con archivos y directorios
import os

# Importamos la librería para trabajar con archivos Excel para LEERLOS con load_workbook!!
from openpyxl import load_workbook, Workbook



# Creo función para cargar csv (artistas)
def cargar_csv(carpeta, nombre_fichero):
    lista_artistas = []
    # Cargo archivo csv
    fichero_csv = open(f"./{carpeta}/{nombre_fichero}", 'r', encoding='UTF-8')
    # Creo elemento lector que me va a permitir leer el csv
    lector = csv.reader(fichero_csv)
    # si el archivo tiene cabeceras me las salto
    next(lector)
    for fila in lector:
        lista_artistas.append(fila)
    return lista_artistas


# Creo función para leer patrocinadores.xml
def cargar_patrocinadores(carpeta, nombre_fichero):
    # Para leer un fichero XML, lo primero que tenemos que hacer es cargar el fichero en memoria. Para ello, utilizamos la función parse() de la librería xml.etree.ElementTree. Esta función recibe como parámetro el nombre del fichero XML que queremos cargar.
    mi_fichero_xml = et.parse(f"./{carpeta}/{nombre_fichero}")
     # Una vez que hemos cargado el fichero XML en memoria, podemos acceder a su contenido. Para ello, utilizamos la función getroot() de la clase ElementTree. Esta función nos devuelve el elemento raíz del árbol XML.
    nodo_raiz = mi_fichero_xml.getroot()
    # Ahora que tenemos el nodo raíz, podemos acceder a sus hijos. Para ello, utilizamos la función findall() del nodo raíz. Esta función recibe como parámetro el nombre del elemento que queremos buscar. En nuestro caso, queremos buscar todos los elementos
    lista_patrocinadores = []
    for patrocinador in nodo_raiz.findall('patrocinador'):
        patrocinador_dict ={
        "nombre_empresa": patrocinador.find("nombre_empresa").text,
        "contacto": patrocinador.find("contacto").text,
        "email": patrocinador.find("email").text,
        "importe_patrocinio": patrocinador.find("importe_patrocinio").text,   
        "categoria": patrocinador.find("categoria").text,
        "fecha_inicio": patrocinador.find("fecha_inicio").text,
        "fecha_fin": patrocinador.find("fecha_fin").text,
        }
        lista_patrocinadores.append(patrocinador_dict)
    
    return lista_patrocinadores


# Definimos función de carga de archivos json (venta entradas)
def leer_json(carpeta, nombre_fichero):
    fichero = open(f"./{carpeta}/{nombre_fichero}", 'r', encoding='UTF-8')
    ventas_entradas_datos = json.load(fichero)
    return ventas_entradas_datos

# Definimos función para obtener los Excel (Escenarios_horarios.xlsx)
def leer_excel_escenarios(carpeta, nombre_fichero):
    #cargar el fichero de excel en nuestro archivo
    libro_excel = load_workbook(f'./{carpeta}/{nombre_fichero}')
    hoja = libro_excel.active
    # Creamos una lista vacía para almacenar los datos
    escenarios_horarios = []
    filas = hoja.iter_rows(values_only = True)
    cabeceras = next(filas)
    # Iterar sobre las filas de la hoja
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        escenarios_dict = dict(zip(cabeceras, fila))
        escenarios_horarios.append(escenarios_dict)
    
    return escenarios_horarios