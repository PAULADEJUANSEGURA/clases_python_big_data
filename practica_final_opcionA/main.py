# Importo la librería de funciones
import lib.carga as cargar

# Definimos funcion principal main
def main():
    # cargar artistas.csv
    # cargar.cargar_csv('datos', 'artistas.csv')
    # cargar patrocinadores.xml
    # resultado_patrocinadores = cargar.cargar_patrocinadores('datos', 'patrocinadores.xml')
    # print(resultado_patrocinadores)
    # Leer venta_entradas.json
    ventas_entradas = cargar.leer_json('datos', "ventas_entradas.json")
    print(ventas_entradas)


main()