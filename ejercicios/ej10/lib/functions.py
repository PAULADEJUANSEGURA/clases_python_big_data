def limpiar_id(id_producto):
    # Si el id no existe o es nulo, devolvemos None
    if not id:
        return None
    # Limpiamos el id eliminando espacios y convirtiendo a entero
    id = str(id).strip()
    return int(id)

def limpiar_texto(texto, mayusculas=False):
    if not texto:
        return None
    texto = str(texto).strip()
    return texto == texto.upper() if mayusculas else texto.lower()



def limpiar_precio():
    pass



def limpiar_stock():
  pass  