# quiero un menu cli, 2 opciones insertar contacto y salir
# crear un lista de contactos vacia.
# contactos = []
# en la opcion 1 inserta contacto pedir los datos de contacto, nombre y telefono. E insertarlo en la lista.
# podremos insertar los contactos que queramos antes de salir
contactos = []

def insertar_contacto(nombre, tlf, lista):
    # paso 1: crear el diccionario
    contacto_nuevo = {
        'nombre': nombre,
        'telefono': tlf
    }
    # paso 2: añadir el diccionario a la lista
    lista.append( contacto_nuevo )
    print(lista)

## opcion 2: pintar la lista contactos 
# Juan Antonio : 9876543
# ----------------------
# Miguel Angel: 567899
# ----------------------
def pintamos_agenda(lista):
    for contacto in lista:
        print(f"Nombre: {contacto['nombre']}")
        print(f"Telefono: {contacto['telefono']}")  
        print('###'*8)      

def main():
    menu = """## Bienvenido a la agenda de contactos ##
[1]. Insertar un contacto
[2]. Listar contactos
[3]. Borrar el ultimo contacto de la agenda
[4]. Borrar un contacto por nombre
[x]. Salir de la app
"""
    print(menu)
    option = input('Dime que opción eliges: ')
    if option == '1':
        nombre = input('Dime el nombre del contacto: ')
        telefono = input('Teléfono: ')
        insertar_contacto(nombre, telefono, contactos)
    elif option == '2':
        pintamos_agenda(contactos)
    elif option == '3':
        contactos.pop()
    elif option == '4':
        nombre = input('Dime el nombre del contacto a borrar: ')
        for contacto in contactos:
            if contacto['nombre'] == nombre:
                contactos.remove(contacto)
                break
    elif option == 'x':
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    main()

main()