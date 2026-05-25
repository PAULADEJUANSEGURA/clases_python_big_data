"""
8.	Crea una función limpiar_texto(texto) que:
•	Elimine espacios al principio y al final (.strip()).
•	Elimine espacios dobles o múltiples en medio del texto.
•	Devuelva el texto limpio sin cambiar mayúsculas/minúsculas

"""
def limpiar_texto(texto, mayusculas = False):
    if not texto:
        return 'Sin datos'
    texto = str(texto)
    # while "  " in texto:
        # texto = texto.replace("  ","")
    return texto.upper() if mayusculas else texto.lower()


"""
9.	Crea una función normalizar_texto(texto) que:
•	Aplique limpiar_texto primero.
•	Convierta el texto a formato estándar (primera letra en mayúscula, resto en minúsculas).
•	Corrija tildes que faltan usando el diccionario de correcciones que se proporciona más abajo.


"""


correcciones_tildes = {
    "jose":       "José",  
    "maria":      "María",
    "garcia":     "García",
    "gonzalez":   "González",
    "martinez":   "Martínez",
    "lopez":      "López",
    "perez":      "Pérez", 
    "sanchez":    "Sánchez",
    "gomez":      "Gómez",  
    "fernandez":  "Fernández",
    "rodriguez":  "Rodríguez",
    "hernandez":  "Hernández",
    "ramirez":    "Ramírez", 
    "gutierrez":  "Gutiérrez",
}

def normalizar_texto(texto):
    """
    Normaliza un texto aplicando limpieza, corrección de tildes y formato.

    La función realiza varias transformaciones sobre el texto recibido:
    - Limpia espacios y normaliza el formato utilizando `limpiar_texto()`.
    - Convierte el texto a minúsculas.
    - Corrige palabras según un diccionario de tildes.
    - Reconstruye el texto con la primera letra en mayúscula.

    Parámetros:
        texto (str): Texto que se desea normalizar.

    Retorna:
        str: Texto normalizado y corregido.

    Funcionamiento:
        - Limpia el texto mediante la función `limpiar_texto()`.
        - Convierte todo el texto a minúsculas.
        - Divide el texto en palabras.
        - Comprueba cada palabra en el diccionario `correcciones_tildes`.
        - Sustituye las palabras encontradas por su versión corregida.
        - Une nuevamente las palabras en una sola cadena.
        - Convierte la primera letra del texto a mayúscula.

    Ejemplos:
        Suponiendo el siguiente diccionario:

        >>> correcciones_tildes = {
        ...     "camion": "camión",
        ...     "arbol": "árbol"
        ... }

        >>> normalizar_texto("  CAMION rojo ")
        'Camión rojo'

        >>> normalizar_texto("ARBOL grande")
        'Árbol grande'

    Requisitos:
        - Debe existir previamente:
              - La función `limpiar_texto()`
              - El diccionario `correcciones_tildes`
        - `correcciones_tildes` debe contener pares:
              palabra_sin_tilde -> palabra_corregida

    Notas:
        - Solo corrige palabras exactas presentes en el diccionario.
    """
    texto = limpiar_texto(texto)
    texto = texto.lower()
    palabras = texto.split()
    
    palabras_corregidas = []

    for palabra in palabras:
        if palabra in correcciones_tildes:
            palabras_corregidas.append(correcciones_tildes[palabra])
        else:
            palabras_corregidas.append(palabra)

    texto = " ".join(palabras_corregidas)
    texto = texto.title() 

    return texto


def limpiar_cache_eur(lista_artistas):
    lista_artistas_limpiado_cache = []
    for artista in lista_artistas:
       
        artista['cache_eur'] = artista['cache_eur'].replace(".","")
        artista['cache_eur'] = artista['cache_eur'].replace(",",".") 
        artista['cache_eur'] = artista['cache_eur'].replace("€","")
        artista['cache_eur'] = artista['cache_eur'].replace("$","")
        artista['cache_eur'] = float(artista['cache_eur']) 
        if artista['cache_eur'] > 250000:
            artista['cache_eur'] = 'None'
        else:
            lista_artistas_limpiado_cache.append(artista['cache_eur'])
            print(artista['cache_eur'])       
    
    return lista_artistas_limpiado_cache    



def limpiar_artistas(lista_artistas):
    lista_artistas_normalizado_texto = []
    for artista in lista_artistas:
        artista['id_artista'] = normalizar_texto(artista['id_artista'])
        artista['nombre'] = normalizar_texto(artista['nombre'])
        artista['genero_musical'] = normalizar_texto(artista['genero_musical'])
        artista['pais'] = normalizar_texto(artista['pais'])
        artista['email_manager'] = normalizar_texto(artista['email_manager'])
        artista['telefono'] = normalizar_texto(artista['telefono'])
        print(artista)
        lista_artistas_normalizado_texto.append(artista)
       
    return lista_artistas_normalizado_texto



