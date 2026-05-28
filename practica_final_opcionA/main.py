# ===== CARGA =====
from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml, mostrar_resumen

# ===== AUDITORÍA =====
from lib.auditoria import (
    auditar_fichero,
    imprimir_auditoria,
    contar_vacios,
    detectar_duplicados,
    detectar_variaciones,
    detectar_espacios_extra,
    detectar_fuera_rango,
    validar_referencias
)

# ===== LIMPIEZA =====
from lib.limpieza import (
    limpiar_texto,
    normalizar_texto,
    limpiar_valor_numerico,
    limpiar_cache_eur,
    limpiar_artistas,
    normalizar_categoria,
    normalizar_fecha,
    eliminar_duplicados
)

# ===== EXPORTACIÓN =====
from lib.exportacion import exportar_csv, exportar_excel, generar_informe


def main():

    # -------------------------------------------------------
    # FASE 1: Carga
    # -------------------------------------------------------
    artistas       = cargar_csv("datos", "artistas.csv")
    ventas         = cargar_json("datos", "ventas_entradas.json")
    patrocinadores = cargar_xml("datos", "patrocinadores.xml")
    escenarios     = cargar_excel("datos", "escenarios_horarios.xlsx")

    mostrar_resumen("artistas.csv",            artistas)
    mostrar_resumen("ventas_entradas.json",     ventas)
    mostrar_resumen("patrocinadores.xml",       patrocinadores)
    mostrar_resumen("escenarios_horarios.xlsx", escenarios)

    # Guardamos registros originales para el informe final
    originales_artistas       = len(artistas)
    originales_ventas         = len(ventas)
    originales_patrocinadores = len(patrocinadores)
    originales_escenarios     = len(escenarios)

    # Inicializamos contadores para el informe final
    contadores = {
        "artistas.csv": {
            "vacios_tratados": 0, "categorias_normalizadas": 0,
            "fechas_convertidas": 0, "fuera_rango": 0
        },
        "ventas_entradas.json": {
            "vacios_tratados": 0, "categorias_normalizadas": 0,
            "fechas_convertidas": 0, "fuera_rango": 0
        },
        "patrocinadores.xml": {
            "vacios_tratados": 0, "categorias_normalizadas": 0,
            "fechas_convertidas": 0, "fuera_rango": 0
        },
        "escenarios_horarios.xlsx": {
            "vacios_tratados": 0, "categorias_normalizadas": 0,
            "fechas_convertidas": 0, "fuera_rango": 0
        },
    }

    # -------------------------------------------------------
    # FASE 2: Auditoría
    # -------------------------------------------------------
    imprimir_auditoria(auditar_fichero("artistas.csv",
        artistas,       campo_clave="nombre",        campo_rango="cache_eur",          rango_min=500,  rango_max=500000))
    imprimir_auditoria(auditar_fichero("ventas_entradas.json",
        ventas,         campo_clave="id_venta",       campo_rango="precio",             rango_min=20,   rango_max=500))
    imprimir_auditoria(auditar_fichero("patrocinadores.xml",
        patrocinadores, campo_clave="nombre_empresa", campo_rango="importe_patrocinio", rango_min=1000, rango_max=1000000))
    imprimir_auditoria(auditar_fichero("escenarios_horarios.xlsx",
        escenarios,     campo_clave="artista"))

    # -------------------------------------------------------
    # FASE 3: Limpieza de texto
    # -------------------------------------------------------
    artistas = limpiar_artistas(artistas)

    for escenario in escenarios:
        escenario['artista']   = normalizar_texto(escenario['artista'])
        escenario['escenario'] = normalizar_texto(escenario['escenario'])

    for venta in ventas:
        venta['nombre_comprador'] = normalizar_texto(venta['nombre_comprador'])

    for pat in patrocinadores:
        pat['nombre_empresa'] = normalizar_texto(pat['nombre_empresa'])
        pat['contacto']       = normalizar_texto(pat['contacto'])

    # -------------------------------------------------------
    # FASE 4: Limpieza numérica
    # -------------------------------------------------------
    for artista in artistas:
        if not artista['cache_eur']:
            contadores["artistas.csv"]["vacios_tratados"] += 1
        artista['cache_eur'] = limpiar_valor_numerico(artista['cache_eur'])

    for pat in patrocinadores:
        if not pat['importe_patrocinio']:
            contadores["patrocinadores.xml"]["vacios_tratados"] += 1
        pat['importe_patrocinio'] = limpiar_valor_numerico(pat['importe_patrocinio'])

    for venta in ventas:
        if not venta['precio']:
            contadores["ventas_entradas.json"]["vacios_tratados"] += 1
        venta['precio'] = limpiar_valor_numerico(venta['precio'])

    # -------------------------------------------------------
    # FASE 5: Normalización de categorías
    # -------------------------------------------------------
    mapeo_generos = {
        "rock": "Rock",        "rokc": "Rock",
        "pop": "Pop",
        "jazz": "Jazz",
        "techno": "Techno",
        "hip-hop": "Hip-Hop",  "hiphop": "Hip-Hop",
        "ska": "Ska",
        "metall": "Metal",     "metal": "Metal",
        "electrónic": "Electrónica", "electronica": "Electrónica",
        "electrónica": "Electrónica",
        "reggae": "Reggae",
        "flamenco": "Flamenco",
        "indie": "Indie",
    }

    mapeo_paises = {
        "españa": "España",    "espana": "España",
        "ee.uu.": "EE.UU.",    "usa": "EE.UU.",     "estados unidos": "EE.UU.",
        "venezuela": "Venezuela",
        "chile": "Chile",
        "portugal": "Portugal",
        "argetina": "Argentina", "argentina": "Argentina",
        "kolombia": "Colombia",  "colombia": "Colombia",
        "mexico": "México",    "méxico": "México",
        "brasil": "Brasil",
        "reino unido": "Reino Unido", "uk": "Reino Unido",
    }

    mapeo_categorias_pat = {
        "gold": "Gold",   "oro": "Gold",
        "silver": "Silver", "plata": "Silver",
        "bronce": "Bronce", "bronze": "Bronce",
    }

    mapeo_tipos_entrada = {
        "general": "General", "gral": "General",
        "premium": "Premium",
        "vip": "VIP",
    }

    mapeo_metodos_pago = {
        "paypal": "PayPal",
        "transfer.": "Transferencia", "transferencia": "Transferencia",
        "tarjeta": "Tarjeta",         "card": "Tarjeta",
        "efectivo": "Efectivo",       "cash": "Efectivo",
    }

    for artista in artistas:
        antes_genero = artista['genero_musical']
        antes_pais   = artista['pais']
        artista['genero_musical'] = normalizar_categoria(artista['genero_musical'], mapeo_generos)
        artista['pais']           = normalizar_categoria(artista['pais'],           mapeo_paises)
        if artista['genero_musical'] != antes_genero:
            contadores["artistas.csv"]["categorias_normalizadas"] += 1
        if artista['pais'] != antes_pais:
            contadores["artistas.csv"]["categorias_normalizadas"] += 1

    for venta in ventas:
        antes_tipo  = venta['tipo_entrada']
        antes_pago  = venta['metodo_pago']
        venta['tipo_entrada'] = normalizar_categoria(venta['tipo_entrada'], mapeo_tipos_entrada)
        venta['metodo_pago']  = normalizar_categoria(venta['metodo_pago'],  mapeo_metodos_pago)
        if venta['tipo_entrada'] != antes_tipo:
            contadores["ventas_entradas.json"]["categorias_normalizadas"] += 1
        if venta['metodo_pago'] != antes_pago:
            contadores["ventas_entradas.json"]["categorias_normalizadas"] += 1

    for pat in patrocinadores:
        antes = pat['categoria']
        pat['categoria'] = normalizar_categoria(pat['categoria'], mapeo_categorias_pat)
        if pat['categoria'] != antes:
            contadores["patrocinadores.xml"]["categorias_normalizadas"] += 1

    # -------------------------------------------------------
    # FASE 6: Normalización de fechas
    # -------------------------------------------------------
    for pat in patrocinadores:
        for campo_fecha in ['fecha_inicio', 'fecha_fin']:
            antes = pat[campo_fecha]
            pat[campo_fecha] = normalizar_fecha(pat[campo_fecha])
            if pat[campo_fecha] != antes and pat[campo_fecha] != "FECHA INVÁLIDA":
                contadores["patrocinadores.xml"]["fechas_convertidas"] += 1

    for venta in ventas:
        antes = venta['fecha_compra']
        venta['fecha_compra'] = normalizar_fecha(venta['fecha_compra'])
        if venta['fecha_compra'] != antes and venta['fecha_compra'] != "FECHA INVÁLIDA":
            contadores["ventas_entradas.json"]["fechas_convertidas"] += 1

    for escenario in escenarios:
        antes = escenario['fecha']
        escenario['fecha'] = normalizar_fecha(escenario['fecha'])
        if escenario['fecha'] != antes and escenario['fecha'] != "FECHA INVÁLIDA":
            contadores["escenarios_horarios.xlsx"]["fechas_convertidas"] += 1

    # -------------------------------------------------------
    # FASE 7: Eliminación de duplicados
    # -------------------------------------------------------
    artistas       = eliminar_duplicados(artistas,       ["nombre"])
    ventas         = eliminar_duplicados(ventas,         ["id_venta"])
    patrocinadores = eliminar_duplicados(patrocinadores, ["nombre_empresa"])
    escenarios     = eliminar_duplicados(escenarios,     ["escenario", "fecha", "hora_inicio"])

    # -------------------------------------------------------
    # FASE 8: Valores fuera de rango
    # -------------------------------------------------------
    for artista in artistas:
        cache = artista['cache_eur']
        if cache is not None:
            if cache < 0:
                artista['cache_eur'] = abs(cache)
                contadores["artistas.csv"]["fuera_rango"] += 1
                print(f"  CORREGIDO: {artista['nombre']} caché negativo → {artista['cache_eur']}")
            elif cache < 500 or cache > 500000:
                artista['cache_eur'] = "REVISAR MANUALMENTE"
                contadores["artistas.csv"]["fuera_rango"] += 1
                print(f"  FUERA DE RANGO: {artista['nombre']} caché = {cache}")

    for pat in patrocinadores:
        importe = pat['importe_patrocinio']
        if importe is not None:
            if importe < 0:
                pat['importe_patrocinio'] = abs(importe)
                contadores["patrocinadores.xml"]["fuera_rango"] += 1
            elif importe < 1000 or importe > 1000000:
                pat['importe_patrocinio'] = "REVISAR MANUALMENTE"
                contadores["patrocinadores.xml"]["fuera_rango"] += 1
                print(f"  FUERA DE RANGO: {pat['nombre_empresa']} importe = {importe}")

    for venta in ventas:
        precio = venta['precio']
        if precio is not None:
            if precio < 0:
                venta['precio'] = abs(precio)
                contadores["ventas_entradas.json"]["fuera_rango"] += 1
            elif precio < 20 or precio > 500:
                venta['precio'] = "REVISAR MANUALMENTE"
                contadores["ventas_entradas.json"]["fuera_rango"] += 1
                print(f"  FUERA DE RANGO: {venta['id_venta']} precio = {precio}")

    # -------------------------------------------------------
    # FASE 9: Validación cruzada
    # -------------------------------------------------------
    escenarios = validar_referencias(escenarios, "artista", artistas, "nombre")

    # -------------------------------------------------------
    # FASE 10: Exportación
    # -------------------------------------------------------
    exportar_csv(artistas,       "datos_limpios/artistas_limpio.csv")
    exportar_csv(ventas,         "datos_limpios/ventas_limpio.csv")
    exportar_csv(patrocinadores, "datos_limpios/patrocinadores_limpio.csv")
    exportar_csv(escenarios,     "datos_limpios/escenarios_limpio.csv")

    exportar_excel({
        "artistas":       artistas,
        "ventas":         ventas,
        "patrocinadores": patrocinadores,
        "escenarios":     escenarios
    }, "datos_limpios/datos_completos.xlsx")

    estadisticas = {
        "artistas.csv": {
            "originales":              originales_artistas,
            "finales":                 len(artistas),
            "duplicados":              originales_artistas       - len(artistas),
            "vacios_tratados":         contadores["artistas.csv"]["vacios_tratados"],
            "categorias_normalizadas": contadores["artistas.csv"]["categorias_normalizadas"],
            "fechas_convertidas":      contadores["artistas.csv"]["fechas_convertidas"],
            "fuera_rango":             contadores["artistas.csv"]["fuera_rango"],
        },
        "ventas_entradas.json": {
            "originales":              originales_ventas,
            "finales":                 len(ventas),
            "duplicados":              originales_ventas         - len(ventas),
            "vacios_tratados":         contadores["ventas_entradas.json"]["vacios_tratados"],
            "categorias_normalizadas": contadores["ventas_entradas.json"]["categorias_normalizadas"],
            "fechas_convertidas":      contadores["ventas_entradas.json"]["fechas_convertidas"],
            "fuera_rango":             contadores["ventas_entradas.json"]["fuera_rango"],
        },
        "patrocinadores.xml": {
            "originales":              originales_patrocinadores,
            "finales":                 len(patrocinadores),
            "duplicados":              originales_patrocinadores - len(patrocinadores),
            "vacios_tratados":         contadores["patrocinadores.xml"]["vacios_tratados"],
            "categorias_normalizadas": contadores["patrocinadores.xml"]["categorias_normalizadas"],
            "fechas_convertidas":      contadores["patrocinadores.xml"]["fechas_convertidas"],
            "fuera_rango":             contadores["patrocinadores.xml"]["fuera_rango"],
        },
        "escenarios_horarios.xlsx": {
            "originales":              originales_escenarios,
            "finales":                 len(escenarios),
            "duplicados":              originales_escenarios     - len(escenarios),
            "vacios_tratados":         contadores["escenarios_horarios.xlsx"]["vacios_tratados"],
            "categorias_normalizadas": contadores["escenarios_horarios.xlsx"]["categorias_normalizadas"],
            "fechas_convertidas":      contadores["escenarios_horarios.xlsx"]["fechas_convertidas"],
            "fuera_rango":             contadores["escenarios_horarios.xlsx"]["fuera_rango"],
        },
    }

    generar_informe(estadisticas, "datos_limpios/informe_limpieza.txt")


main()