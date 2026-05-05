## Construir un programa que de por pantalla tres opciones
#      - 1 añadir un contacto a lista
#      - 2 leer todos los contactos de la lista
#      - 3 salir

# Si no pulso salir no me debe sacar de la aplicacion dandome opcion a elegir nuevamente cada vez que se termine mi eleccion anterior.

# lista_contactos sera un lista de diccionarios donde cada elemento tendrá los siguentes datos. Nombre, telefono, email

# Añadir un contacto deberá pedir esos datos y comprobar que nombre no es vacio, que telefono esta formado por digitos,y que el email estan bien escrito, al menos tiene que tener @. Si esto ocurre añadimos el contacto si no lanzamos un error y volvemos al menu principal 

# Leer contacto mostrara todos los contactos por pantalla
lista_contactos = {
    
}

def agregar_usuario(lista_contactos, nombre, telefono, email):
    usuario_id = len(lista_contactos) + 1
    lista_contactos[usuario_id] = {
        "nombre": limpiadora_datos(nombre),
        "telefono": validar_telefono(telefono),
        "email": validar_email(email),
    }



def pintamos_agenda(lista_contactos):
    for i in range(0, len(lista_contactos)):
        print("------# Contacto #------")
        print("Nombre: ", lista_contactos[i]["nombre"])
        print("Telefono: ", lista_contactos[i]["telefono"])
        print("Email: ", lista_contactos[i]["email"])


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
        usuario_id = len(lista_contactos) + 1
        agregar_usuario(lista_contactos, usuario_id, nombre, telefono, email)

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