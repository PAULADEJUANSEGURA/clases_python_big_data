import os 
from openpyxl import Workbook

lista_de_productos = [

]

def crear_excel(carpeta, fichero, datos):
    # crear primero el libro de excel
    wb = Workbook()
    # seleccionamos al primera hoja
    hoja = wb.active
    hoja.title = 'Inventario'
    
    # extraer de un diccionario cualquier de mi lista las cabeceras.
    cabeceras = list(datos[0].keys())
    # quiero añadirlo a mi hoja
    hoja.append(cabeceras)
    
    # recorremos nuestra de lista de datos para imprimir en cada fila un dato concreto
    for producto in datos:
        # para que esto funcione el producto tiene que tener los datos en el mismo orden que la lista caberas. Y estar convertido en lista.
        lista_producto = list(producto.values())
        lista_producto = [producto[clave] for clave in cabeceras ]
        hoja.append(lista_producto)
    
    wb.save(f'./{carpeta}/{fichero}')


crear_excel('data', 'productos.xlsx', lista_de_productos)