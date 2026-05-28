# exportacion.py completo
import csv
import os
from openpyxl import Workbook
from datetime import date


def exportar_csv(datos, ruta_salida):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    with open(ruta_salida, 'w', newline='', encoding='UTF-8') as f:
        escritor = csv.DictWriter(f, fieldnames=datos[0].keys())
        escritor.writeheader()
        escritor.writerows(datos)
    print(f"  CSV exportado: {ruta_salida}")


def exportar_excel(diccionario_hojas, ruta_salida):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    wb = Workbook()
    wb.remove(wb.active)  # quitamos la hoja vacía por defecto

    for nombre_hoja, datos in diccionario_hojas.items():
        ws = wb.create_sheet(title=nombre_hoja)
        ws.append(list(datos[0].keys()))      # cabeceras
        for registro in datos:
            ws.append(list(registro.values()))

    wb.save(ruta_salida)
    print(f"  Excel exportado: {ruta_salida}")


def generar_informe(estadisticas, ruta_salida):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    lineas = [
        "=== INFORME DE LIMPIEZA ===",
        f"Fecha del proceso: {date.today().strftime('%d/%m/%Y')}",
        f"Ficheros procesados: {len(estadisticas)}",
        "",
        "--- RESUMEN POR FICHERO ---"
    ]

    for fichero, stats in estadisticas.items():
        lineas.append(f"\n{fichero}:")
        lineas.append(f"  Registros originales : {stats['originales']}")
        lineas.append(f"  Registros finales    : {stats['finales']}")
        lineas.append(f"  Duplicados eliminados: {stats['duplicados']}")
        lineas.append(f"  Vacíos tratados      : {stats['vacios_tratados']}")
        lineas.append(f"  Categorías norm.     : {stats['categorias_normalizadas']}")
        lineas.append(f"  Fechas convertidas   : {stats['fechas_convertidas']}")
        lineas.append(f"  Fuera de rango       : {stats['fuera_rango']}")

    texto = "\n".join(lineas)
    print(texto)
    with open(ruta_salida, 'w', encoding='UTF-8') as f:
        f.write(texto)
    print(f"\n  Informe guardado: {ruta_salida}")