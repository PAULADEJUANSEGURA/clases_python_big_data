'''
### **Abrir un archivo**

Usa la función `open()` para abrir un archivo. Esta función devuelve un objeto de archivo que puedes usar para leer o escribir datos.


pythonCopy code
f = open('mi_archivo.txt', 'r')

El segundo argumento ('r' en este caso) es el modo en que se abre el archivo:

- 'r': Lectura (por defecto).
- 'w': Escritura (sobrescribe si el archivo ya existe o crea uno nuevo si no existe).
- 'a': Añadir (añade contenido al final si el archivo ya existe o crea uno nuevo si no existe).
- 'b': Modo binario (por ejemplo, para archivos de imagen, audio, etc.).
- 'x': Exclusivo (crea un archivo pero falla si el archivo ya existe).
- 't': Modo texto (por defecto).

"""
tres acciones para realizar con un fichero
open.
    r(read) -> leer fichero, extraer pero no puedo modificarlo
    w(write) -> sobreescribirlo, es decir lo que tenga se borrará y quedará sobreescrito
    a(append) -> añadir es decir a lo que tengo en el fichero añado puedo escribir en él
    
el ciclo de vida de un fichero consta de tres partes:
abrir fichero - realizar las acciones correspondientes W-R-A - cerrar fichero
    
"""
'''

# paso 1 : donde esta el fichero La RUTA
# paso 2 : crear variable

mi_fichero = open('./texto.txt', 'r', encoding='UTF-8')

# paso 3 : Leer el fichero y alojar las frases en nuestro "array" o lista 

frases = []

# paso 4 : Hacer el print del fichero con la función read()

# print(mi_fichero.read())

# readlines() me sirve para crear una lista por cada parrafo del txt
# frases = print(mi_fichero.readlines())
# print(frases)

# Vamos a quitar los \n retornos de carro Limpiamos el texto linea a linea y lo introducimos en la lista de frases []
for linea in mi_fichero.readlines():
    linea = linea.replace('\n', "")
    print(linea)
    frases.append(linea)
else:
    print(frases)


# MUY IMPORTANTE: Cerrar el fichero
mi_fichero.close()
