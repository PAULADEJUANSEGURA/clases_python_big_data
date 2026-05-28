"""
8.	Crea una función limpiar_texto(texto) que:
•	Elimine espacios al principio y al final (.strip()).
•	Elimine espacios dobles o múltiples en medio del texto.
•	Devuelva el texto limpio sin cambiar mayúsculas/minúsculas

"""

def limpiar_texto(texto, mayusculas=False):
    if not texto:
        return 'Sin datos'
    texto = str(texto).strip()              # Quita espacios al principio y al final
    while "  " in texto:                    # Elimina espacios dobles en medio
        texto = texto.replace("  ", " ")
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
    texto = limpiar_texto(texto)      # Paso 1: limpia espacios y convierte
    texto = texto.lower()             # Paso 2: todo a minúsculas
    palabras = texto.split()          # Paso 3: divide en lista de palabras
    
    palabras_corregidas = []
    for palabra in palabras:          # Paso 4: revisa cada palabra en el diccionario
        if palabra in correcciones_tildes:
            palabras_corregidas.append(correcciones_tildes[palabra])  # corrige
        else:
            palabras_corregidas.append(palabra)                       # deja igual
    
    texto = " ".join(palabras_corregidas)   # Paso 5: vuelve a unir todo
    texto = texto.title()                   # Primera letra de cada palabra en mayúscula
    return texto


def limpiar_cache_eur(lista_artistas):
    lista_limpia = []
    for artista in lista_artistas:
        artista['cache_eur'] = artista['cache_eur'].replace(".", "")   # quita punto de miles
        artista['cache_eur'] = artista['cache_eur'].replace(",", ".")  # coma decimal → punto
        artista['cache_eur'] = artista['cache_eur'].replace("€", "")  # quita símbolo €
        artista['cache_eur'] = artista['cache_eur'].replace("$", "")  # quita símbolo $
        artista['cache_eur'] = float(artista['cache_eur'])             # convierte a número
        
        if artista['cache_eur'] > 250000:
            artista['cache_eur'] = 'None'   # fuera de rango
        else:
            lista_limpia.append(artista['cache_eur'])
    
    return lista_limpia


def limpiar_artistas(lista_artistas):
    lista_normalizada = []
    for artista in lista_artistas:
        artista['id_artista']     = normalizar_texto(artista['id_artista'])
        artista['nombre']         = normalizar_texto(artista['nombre'])
        artista['genero_musical'] = normalizar_texto(artista['genero_musical'])
        artista['pais']           = normalizar_texto(artista['pais'])
        artista['email_manager']  = normalizar_texto(artista['email_manager'])
        artista['telefono']       = normalizar_texto(artista['telefono'])
        lista_normalizada.append(artista)
    return lista_normalizada


# FASE 4 — limpieza numérica genérica
def limpiar_valor_numerico(valor):
    if not valor:
        return None
    try:
        valor = str(valor).strip()
        valor = valor.replace("€", "").replace("$", "").replace(" ", "")

        # Si tiene coma, asumimos formato europeo: 1.000,50 → quitar punto, coma→punto
        if "," in valor:
            valor = valor.replace(".", "").replace(",", ".")
        # Si solo tiene un punto, es decimal normal: 220.687 → dejarlo
        # Si tiene varios puntos, son separadores de miles: 1.000.000 → quitarlos
        elif valor.count(".") > 1:
            valor = valor.replace(".", "")

        return float(valor)
    except:
        return None


# FASE 5 — normalizar categorías
def normalizar_categoria(valor, diccionario_mapeo):
    if not valor:
        return "SIN DATOS"
    clave = str(valor).lower().strip()
    if clave in diccionario_mapeo:
        return diccionario_mapeo[clave]
    else:
        print(f"  AVISO: valor no reconocido → '{valor}'")
        return valor


# FASE 6 — normalizar fechas
meses = {
    "enero":1, "febrero":2, "marzo":3, "abril":4,
    "mayo":5, "junio":6, "julio":7, "agosto":8,
    "septiembre":9, "octubre":10, "noviembre":11, "diciembre":12,
    "jan":1, "feb":2, "mar":3, "apr":4, "may":5, "jun":6,
    "jul":7, "aug":8, "sep":9, "oct":10, "nov":11, "dec":12
}

def normalizar_fecha(fecha_texto):
    if not fecha_texto:
        return "FECHA INVÁLIDA"
    fecha = str(fecha_texto).strip()
    try:
        # AAAA-MM-DD  →  el primer trozo tiene 4 dígitos
        if "-" in fecha and len(fecha.split("-")[0]) == 4:
            partes = fecha.split("-")
            return f"{int(partes[2]):02d}/{int(partes[1]):02d}/{partes[0]}"

        # DD/MM/AAAA o DD/M/AA
        elif "/" in fecha:
            partes = fecha.split("/")
            anio = int(partes[2])
            if anio < 100:
                anio += 2000
            return f"{int(partes[0]):02d}/{int(partes[1]):02d}/{anio}"

        # DD de mes de AAAA
        elif " de " in fecha:
            partes = fecha.split(" de ")
            dia = int(partes[0])
            mes = meses[partes[1].lower()]
            anio = int(partes[2])
            return f"{dia:02d}/{mes:02d}/{anio}"

        # DD-MM-AAAA  o  DD-mes-AAAA
        elif "-" in fecha:
            partes = fecha.split("-")
            dia = int(partes[0])
            mes = meses[partes[1].lower()] if not partes[1].isdigit() else int(partes[1])
            anio = int(partes[2])
            return f"{dia:02d}/{mes:02d}/{anio}"

        # mes DD, AAAA
        elif "," in fecha:
            partes = fecha.replace(",", "").split()
            mes = meses[partes[0].lower()]
            dia = int(partes[1])
            anio = int(partes[2])
            return f"{dia:02d}/{mes:02d}/{anio}"

    except:
        pass

    print(f"  AVISO: fecha no reconocida → '{fecha_texto}'")
    return "FECHA INVÁLIDA"


# FASE 7 — eliminar duplicados
def eliminar_duplicados(datos, campos_clave):
    vistos = {}
    valores_vacios = ["", None, "N/A", "-", "no disponible", "SIN DATOS"]

    for registro in datos:
        clave = tuple(str(registro[c]).lower().strip() for c in campos_clave)

        if clave not in vistos:
            vistos[clave] = registro
        else:
            # conservamos el más completo (el que tiene menos vacíos)
            vacios_nuevo    = sum(1 for v in registro.values() if v in valores_vacios)
            vacios_guardado = sum(1 for v in vistos[clave].values() if v in valores_vacios)
            if vacios_nuevo < vacios_guardado:
                vistos[clave] = registro

    resultado  = list(vistos.values())
    eliminados = len(datos) - len(resultado)
    print(f"  Duplicados eliminados: {eliminados} ({len(datos)} → {len(resultado)} registros)")
    return resultado