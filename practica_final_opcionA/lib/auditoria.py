# Función para detectar Valores vacíos. 
# La función recibe como parámetro "datos" que va a ser una Lista de Diccionarios
def contar_vacios(datos):
    # Aqui creo mi propia lista con los valores considerados "vacios"
    valores_vacios = ["", None, "N/A", "-", "no disponible"]
    """ Creo un diccionario llamado resultado 
    para después guardar en él 
    los valores que encuentre 
    que estén dentro de 
    mi LISTA de valores considerados "vacíos"
    """
    resultado = {}
    # Después creo un BUCLE FOR que recorre y saca los datos de todos los campos o columnas
    """
    .keys(): Utilizado en diccionarios para obtener un listado 
    de todos los nombres de los campos o columnas
    """
    for campo in datos[0].keys():
        # Por cada columna pone el contador a cero
        contador = 0
        # Después creamos otro BUCLE FOR ANIDADO va fila por fila buscando los errores
        for registro in datos:
            """ Si el campo coincide o está dentro de mi LISTADO de Valores considerados vacíos
            pone el contador en +1 """
            if registro[campo] in valores_vacios:
                contador += 1
        # Al terminar el bucle anidado guardamos el numero final del recuento
        resultado[campo] = contador
        # Con este contador sabemos cuantos campos se encontraban entre el listado de Valores vacios
    return resultado
    
# Detectar duplicados
def detectar_duplicados(datos, campo):
    # Creamos un set para detectar los doplicados
    vistos = set()
    # Creamos un contador de duplicados inicializado en cero
    duplicados = 0
    # Usamos un bucle for que recorre registro por registro los datos
    for registro in datos:
        # Asignamos el campo a una variable llamada valor para usarla despues
        valor = registro[campo]
        # Usamos la variable valor_normalizado y le asignamos la anterior variable creada con el campo 
        """ Usamos los métodos de transformación de texto: 
        lower para minusculas todo
        y strip para quitar espacios por todos los lados"""
        valor_normalizado = valor.lower().strip()
        # Si el campo está ya normalizado y está dentro del set entonces se podria considerar que es un duplicado
        if valor_normalizado in vistos:
            # Por eso el contador de duplicados suma +1
            duplicados += 1
        else:
            # Si el valor_normalizado no se encuentra dentro del set entonces es que no está duplicado y lo añadimos al set
            vistos.add(valor_normalizado)
        # Por último devolvemos el contador de duplicados que nos dirá el numero de duplicados que ha encontrado la función
    return duplicados


def detectar_variaciones(datos, campo):
    variaciones = set()
    for registro in datos:
        valor = str(registro[campo]).lower().strip()
        variaciones.add(valor)
    return variaciones


def detectar_fuera_rango(datos, precio, minimo, maximo):
    contador = 0
    for registro in datos:
        try:
            valor = float(registro[precio])
            if valor < minimo or valor > maximo:
                contador += 1
        except:
            pass
    return contador


def detectar_espacios_extra(datos):
    resultado = {}
    for campo in datos[0].keys():
        contador = 0
        for registro in datos:
            valor = str(registro[campo])
            if valor != valor.strip() or "  " in valor:
                contador += 1
        resultado[campo] = contador
    return resultado


def auditar_fichero(nombre_fichero, datos):
    auditoria = {
        nombre_fichero: {
            "total_registros": len(datos),
            "valores_vacios": contar_vacios(datos),
            "duplicados": detectar_duplicados(datos, "nombre"),
            "formatos_inconsistentes": {
                "nombre": list(detectar_variaciones(datos, "nombre"))
            },
            "fuera_de_rango": {
                "cache_eur": detectar_fuera_rango(datos, "cache_eur", 500, 500000)
            },
            "espacios_extra": detectar_espacios_extra(datos)
        }
    }
    return auditoria