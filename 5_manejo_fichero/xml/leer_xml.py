# importamos la librería para manejar XML
import xml.etree.ElementTree as et

def leer_xml(carpeta, fichero):
    # ¿Como leer un fichero XML?
    # Para leer un fichero XML, lo primero que tenemos que hacer es cargar el fichero en memoria. Para ello, utilizamos la función parse() de la librería xml.etree.ElementTree. Esta función recibe como parámetro el nombre del fichero XML que queremos cargar.
    fichero = et.parse(f'{carpeta}/{fichero}')
    # Una vez que hemos cargado el fichero XML en memoria, podemos acceder a su contenido. Para ello, utilizamos la función getroot() de la clase ElementTree. Esta función nos devuelve el elemento raíz del árbol XML.
    nodo_raiz = fichero.getroot()
    # Ahora que tenemos el nodo raíz, podemos acceder a sus hijos. Para ello, utilizamos la función findall() del nodo raíz. Esta función recibe como parámetro el nombre del elemento que queremos buscar. En nuestro caso, queremos buscar todos los elementos "empleado".
    lista_empleados = []


    for empleado in nodo_raiz.findall('empleado'):
        empleado_dict = {
            'id': empleado.get('id'),
            'nombre': empleado.find('nombre').text,
            'apellidos': empleado.find('apellidos').text,
            'correo': empleado.find('correo').text,
            'departamento': empleado.find('departamento').text
        }
        lista_empleados.append(empleado_dict)

    return lista_empleados



fichero_xml = leer_xml('data', 'empleados.xml')
print(fichero_xml)