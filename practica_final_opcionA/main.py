# Importo la librería de funciones
import lib.carga as cargar
import lib.limpieza as limpiar

# Definimos funcion principal main
def main():
    # Leer artistas cargar artistas.csv
    lista_artistas = cargar.cargar_csv('datos', 'artistas.csv')
    # lista_empleados = cargar.cargar_csv('datos', 'empleados.csv' )
    print(lista_artistas)
    print("-" * 60)
    resultado_limpiar_artistas = limpiar.limpiar_texto(lista_artistas, mayusculas=False)
    # resultado_limpiar_empleados = limpiar.limpiar_texto(lista_empleados, mayusculas=False)
    # print(resultado_limpiar_empleados)
""" # cargar patrocinadores.xml
    resultado_patrocinadores = cargar.cargar_patrocinadores('datos', 'patrocinadores.xml')
    print(resultado_patrocinadores)
    # Leer venta_entradas.json
    ventas_entradas = cargar.leer_json('datos', "ventas_entradas.json")
    print(ventas_entradas)
    resultado_escenarios_horarios = cargar.leer_excel_escenarios('datos', "escenarios_horarios.xlsx")
    print(resultado_escenarios_horarios)"""



main()