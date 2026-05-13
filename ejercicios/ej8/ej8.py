import csv

def carga_fichero(carpeta, nombre):
    fichero = open(f"./{carpeta}/{nombre}", "r", encoding="UTF-8")
    lector = csv.DictReader(fichero)
    lista = list(lector)
    fichero.close()
    return lista
    
juegos = carga_fichero('data', 'game.csv')


def pintar_bbdd(juegos, stock):
    for game in juegos:
        if int(game['en_stock']) == stock:
            print('=' * 50)
            print(f"{game['titulo']} - {game['genero']} => precio: {game['precio']} - {game['lanzamiento']}")


def crear_fichero(carpeta, nombre, datos):
    fichero = open(f"./{carpeta}/{nombre}", 'w', encoding='UTF-8')
    cabeceras = []
    for key in datos.keys():
        cabeceras.append(key)
    mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras)
    # escribir primero las cabeceras
    mi_csv.writeheader()
    # pintas las filas
    mi_csv.writerows(datos)
    fichero.close()

juegos = carga_fichero('data', 'game.csv')
pintar_bbdd(juegos, 0)