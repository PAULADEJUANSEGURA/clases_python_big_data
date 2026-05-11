# -------- MENU con 3 opciones
# [1]. Añadir un producto (nombre, cantidad)
# [2]. Mostrar Lista de la compra
# [3]. Borrar lista 
# [x]. Salir

# TRABAJAMOS CON MODULOS SEPARADOS , MODULO PRINCIPAL y MODULO SECUNDARIO

import data.funciones_ej7 as fn

def main():
    # try
    lista_de_la_compra = []
    menu = """
    ------- MENU con 3 opciones y la x para Salir : Programa LISTA DE COMPRA
            [1]. Añadir un producto (nombre, cantidad)
            [2]. Mostrar Lista de la compra
            [3]. Borrar lista 
            [x]. Salir
    """
    print(menu)
    fn.crear_fichero('lista_de_la_compra', './data/', '.txt')
    opcion = input("Dime la opción: ")
    if opcion == '1':
        print("Añadiendo producto")
        fn.actualizar_datos('lista_de_la_compra', './data/', '.txt', lista_de_la_compra)
    elif opcion == '2':
        print("Mostrar Lista de la compra")
        fn.leer_fichero(lista_de_la_compra)
    elif opcion == '3':
        print("Borramos lista")
        pass
    elif opcion == 'x':
        print("Hasta pronto y SALIR del PROGRAMA.")
        return 
    else:
        print("Opcion no valida")
    # except:
    # finally:    
    main()

main()