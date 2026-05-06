## Construir un programa que de por pantalla tres opciones
#      - 1 añadir un contacto a lista
#      - 2 leer todos los contactos de la lista
#      - 3 salir

# Si no pulso salir no me debe sacar de la aplicacion dandome opcion a elegir nuevamente cada vez que se termine mi eleccion anterior.

# lista_contactos sera un lista de diccionarios donde cada elemento tendrá los siguentes datos. Nombre, telefono, email

# Añadir un contacto deberá pedir esos datos y comprobar que nombre no es vacio, que telefono esta formado por digitos,y que el email estan bien escrito, al menos tiene que tener @. Si esto ocurre añadimos el contacto si no lanzamos un error y volvemos al menu principal 

# Leer contacto mostrara todos los contactos por pantalla
from lib.functions import insertar_contacto, validar_contacto, pintamos_contactos
# Una lista con un diccionario de contactos dentro
agenda = []

   
def main():
    menu = """## Bienvenido a la agenda de contactos ##
    [1] Insertar un contacto en la lista
    [2] Leer todos los contactos de la lista
    [x] Salir del programa
    """
    print(menu)
    opcion = input("Elige una opción: ")
    if opcion == "1":
        print("Has elegido la opción 1")
        # Pedimos los datos al usuario
        nombre = input('Nombre del contacto: ')
        telefono = input('Teléfono: ')
        email = input('Email: ')
        # Validamos los datos
        es_valido = validar_contacto(nombre, telefono, email)
        # Si los datos son correctos insertamos el contacto
        if es_valido:
           insertar_contacto(nombre, telefono, email, agenda)
        else:
            print("""#####- Los datos introducidos no son correctos, prueba otra vez -#####""")

    elif opcion == "2":       
        print("Has elegido la opción 2")
        pintamos_contactos(agenda)

    elif opcion == "x": 
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    main()

main()