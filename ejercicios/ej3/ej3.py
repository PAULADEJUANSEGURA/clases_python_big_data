## Construir un programa que de por pantalla tres opciones
#      - 1 añadir un contacto a lista
#      - 2 leer todos los contactos de la lista
#      - 3 salir

# Si no pulso salir no me debe sacar de la aplicacion dandome opcion a elegir nuevamente cada vez que se termine mi eleccion anterior.

# lista_contactos sera un lista de diccionarios donde cada elemento tendrá los siguentes datos. Nombre, telefono, email

# Añadir un contacto deberá pedir esos datos y comprobar que nombre no es vacio, que telefono esta formado por digitos,y que el email estan bien escrito, al menos tiene que tener @. Si esto ocurre añadimos el contacto si no lanzamos un error y volvemos al menu principal 

# Leer contacto mostrara todos los contactos por pantalla

# importamos una libreria con un archivo
import lib.functions 

# importamos una funcion de una libreria
# from lib.functions import insertar_contacto

agenda = []

def insertar_contacto(nombre, email, tel, lista):
    pass
    

def main():
    menu = """### Directorio de Contactos ####
[1]. Añadir contacto a lista
[2]. Leer todos los contactos
[3]. Salir
################################
"""
    print(menu)
    option = input('Dime que opción quieres: ')
    if option == '1':
       nombre = input('Introduce tu nombre: ')
       email = input('Introduce tu email: ')
       telefono = input('Introduce tu teléfono: ')
       es_valido = validar_contacto(lista_contactos, nombre, telefono, email)
       insertar_contacto(nombre, email, telefono, agenda)
    elif option == '2':
        print('leer')
    elif option == '3':
        print('hasta pronto')
        return
    else:
        print('opcion no valida')
    main()

main()