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
    vistos = set()
    duplicados = 0
    for registro in datos:
        valor = str(registro[campo])          # ← añadir str() aquí
        valor_normalizado = valor.lower().strip()
        if valor_normalizado in vistos:
            duplicados += 1
        else:
            vistos.add(valor_normalizado)
    return duplicados

# Detectar variaciones
def detectar_variaciones(datos, campo):
    variaciones = set()
    for registro in datos:
        valor = str(registro[campo]).lower().strip()
        variaciones.add(valor)    # el set automáticamente ignora los repetidos
    return variaciones            # devuelve: {"rock", "rokc", "electrónica", "electro"...}


# Detectar fuera de rango
def detectar_fuera_rango(datos, precio, minimo, maximo):
    contador = 0
    for registro in datos:
        try:
            valor = float(registro[precio])     # intenta convertir a número
            if valor < minimo or valor > maximo:
                contador += 1                   # fuera de rango
        except:
            pass    # si no se puede convertir, lo ignora
    return contador


# Detectar espacios extra
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



# Auditar fichero
def auditar_fichero(nombre_fichero, datos, campo_clave="nombre", campo_rango=None, rango_min=0, rango_max=999999):
    auditoria = {
        nombre_fichero: {
            "total_registros":         len(datos),
            "valores_vacios":          contar_vacios(datos),
            "duplicados":              detectar_duplicados(datos, campo_clave),
            "formatos_inconsistentes": {
                campo_clave: list(detectar_variaciones(datos, campo_clave))
            },
            "fuera_de_rango":          {
                campo_rango: detectar_fuera_rango(datos, campo_rango, rango_min, rango_max)
            } if campo_rango else {},
            "espacios_extra":          detectar_espacios_extra(datos)
        }
    }
    return auditoria

def validar_referencias(datos, campo_validar, referencia, campo_referencia):
    validos = set(str(r[campo_referencia]).lower().strip() for r in referencia)
    for registro in datos:
        valor = str(registro[campo_validar]).lower().strip()
        if valor in validos:
            registro['estado_referencia'] = 'OK'
        else:
            registro['estado_referencia'] = 'REVISAR'
            print(f"  REVISAR: '{registro[campo_validar]}' no encontrado en fichero maestro")
    return datos




def imprimir_auditoria(auditoria):
    for nombre_fichero, datos in auditoria.items():
        print(f"\n=== AUDITORÍA: {nombre_fichero} ===")
        print("Total registros:", datos['total_registros'])

        print("\nValores vacíos:")
        for campo, cantidad in datos['valores_vacios'].items():
            if cantidad > 0:
                print(f"  - {campo}: {cantidad} vacíos")

        print("\nDuplicados:", datos['duplicados'])

        print("\nEspacios extra:")
        for campo, cantidad in datos['espacios_extra'].items():
            if cantidad > 0:
                print(f"  - {campo}: {cantidad} campos con espacios")

        print("\nFuera de rango:")
        for campo, cantidad in datos['fuera_de_rango'].items():
            print(f"  - {campo}: {cantidad} valores fuera de rango")