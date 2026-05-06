def insertar_contacto(nombre, telefono, email, lista):
    print("Conectando módulos")
    # nuevo contacto en diccionario
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
        }
    no_duplicado = comprobar_duplicados(telefono, email, lista)
    # insertarlo en la agenda, no puede ocurrir append si el email o el telefono ya existe en la agenda
    if no_duplicado:
        lista.append(contacto)
        print(lista)
    else:
        print("Usuario duplicado")

def comprobar_duplicados(telefono, email, lista):
    for contacto in lista:
        if contacto["email"] == email or contacto["telefono"] == telefono:
            return False
    return True

def validar_contacto(nombre, telefono, email):
    telefono_limpio = telefono.replace("+", "").replace(" ", "").replace("-", "")
    if not telefono_limpio.isdigit():
        return False
    elif nombre == "":
        return False 
    elif '@' not in email and '.' not in email:
        return False
    return True

def pintamos_contactos(lista):
    for contacto in lista:
        print("------# Contacto #------")
        print(f"Nombre: {contacto["nombre"]}")
        print(f"Telefono: {contacto["telefono"]}")
        print(f"Email: {contacto["email"]}")