# -------- MENU con 3 opciones
# [1]. Añadir un producto (nombre, cantidad)
# [2]. Mostrar Lista de la compra
# [3]. Borrar lista 
# [x]. Salir

# TRABAJAMOS CON MODULOS SEPARADOS , MODULO PRINCIPAL y MODULO SECUNDARIO

import data.funciones_ej7 as fn

def main():
    # try
    menu = """
    ------- MENU con 3 opciones y la x para Salir : Programa LISTA DE COMPRA
            [1]. Añadir un producto (nombre, cantidad)
            [2]. Mostrar Lista de la compra
            [3]. Borrar lista 
            [x]. Salir
    """
    print(menu)
    opcion = input("Dime la opción: ")
    if opcion == '1':
        print("Has elegido la opción 1, añadir un producto a la lista de la compra")
        try:
            fn.crear_fichero('lista_de_la_compra', './data/', '.txt')
            print("Fichero creado AHORA mismo, ahora añadimos productos a la lista de la compra")
        except FileExistsError:
            print("El fichero ya fue creado correctamente, ahora añadimos productos a la lista de la compra")
        fn.actualizar_datos('lista_de_la_compra', './data/', '.txt')
        print("Producto añadido a la lista de la compra")
    elif opcion == '2':
        print(f"Has elegido la opción 2, mostrar la lista de la compra\n")
        fn.leer_fichero('lista_de_la_compra', './data/', '.txt')
        print("Lista de la compra mostrada correctamente")
    elif opcion == '3':
        print("Has elegido la opción 3, borrar la lista de la compra")
        fn.sobrescribir_fichero('lista_de_la_compra', './data/', '.txt')
        print("Lista de la compra borrada correctamente")
    elif opcion == 'x':
        print("Hasta pronto y SALIR del PROGRAMA.")
        return 
    else:
        print("Opcion no valida")
    # except:
    # finally:    
    main()

main()