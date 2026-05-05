## Construir un programa que de por pantalla tres opciones
#      - 1 añadir un contacto a lista
#      - 2 leer todos los contactos de la lista
#      - 3 salir

# Si no pulso salir no me debe sacar de la aplicacion dandome opcion a elegir nuevamente cada vez que se termine mi eleccion anterior.

# lista_contactos sera un lista de diccionarios donde cada elemento tendrá los siguentes datos. Nombre, telefono, email

# Añadir un contacto deberá pedir esos datos y comprobar que nombre no es vacio, que telefono esta formado por digitos,y que el email estan bien escrito, al menos tiene que tener @. Si esto ocurre añadimos el contacto si no lanzamos un error y volvemos al menu principal 

# Leer contacto mostrara todos los contactos por pantalla
lista_contactos = {}

def insertar_contacto(nombre, telefono, email, lista_contactos):
    # paso 1: crear el diccionario
    usuario = {
        'nombre': limpiadora_datos(nombre),
        'telefono': validar_telefono(telefono),
        'email': validar_email(email)
    }
    # paso 2: añadir el diccionario a la lista
    lista_contactos[usuario['nombre']] = usuario['nombre']
    lista_contactos[usuario['telefono']] = usuario['telefono']
    lista_contactos[usuario['email']] = usuario['email']
    print("------# Contacto añadido correctamente #------")

def pintamos_agenda(lista_contactos):
    for usuario in lista_contactos:
        print('   ')
        print(lista_contactos[usuario['nombre']])
        print('   ')
        print(lista_contactos[usuario['telefono']])
        print('   ')
        print(lista_contactos[usuario['email']])
        print('   ')
        print('###'*10)          


def validar_telefono(telefono):
    telefono_limpio = telefono.replace("+", "").replace(" ", "").replace("-", "")
    if telefono_limpio.isdigit():
        return True
    else:
        return False


def validar_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False


def limpiadora_datos(texto):
    # paso 1: pasar a minusculas
    texto = texto.lower()
    # paso 2: quitar acentos
    lista_vocales_acentos = ['á', 'é', 'í', 'ó', 'ú', 'ü']
    lista_vocales = ['a', 'e', 'i', 'o', 'u', 'ü']
    for i in range (len(lista_vocales_acentos)):
        texto = texto.replace(lista_vocales_acentos[i], lista_vocales[i])
    return texto


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
        nombre = input('Nombre del contacto: ')
        telefono = input('Teléfono: ')
        email = input('Email: ')
        insertar_contacto(nombre, telefono, email, lista_contactos)

    elif opcion == "2":       
        print("Has elegido la opción 2")
        pintamos_agenda(lista_contactos)
        
    elif opcion == "x": 
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    main()

main()