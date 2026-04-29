# Una TUPLA es un conjunto de datos pero la principal carcteristica es que es INMUTABLE.
# No se puede cambiar , ni valor ni de longituds.
# El objetivo de la Tupla proteger los datos que hay dentro.
# La diferencia visual es que al inicializarla usamos los paréntesis
mi_primera_tupla = ("Paula", 38, True)

tupla_de_frutas = ("naranja", "pera", "platano", "manzana")

# No se pueden modificar ni añadir
print(f"Mi primera tupla contiene: {mi_primera_tupla}")
print(f"Mi segunda tupla contiene: {tupla_de_frutas}")

# ¿Como saber la longitud de una tupla?
print("Mi segunda tupla contiene nombres de frutas: ")
print(f"La longitud de la tupla es: {len(tupla_de_frutas)}")

# ¿Como obtener un índice de una tupla? Se numero de 0 a n-1 siendo n la Longitud
print(f"El primer elemento de mi_primera_tupla es: {mi_primera_tupla[0]}")
print(" #---- Tupla de frutas -----# ")
# Leyendo de izquierda a derecha
print(f"El primer elemento de tupla_de_frutas es (indice 0): {tupla_de_frutas[0]}")
print(f"El segundo elemento de tupla_de_frutas es (indice 1): {tupla_de_frutas[1]}")
print(f"El tercer elemento de tupla_de_frutas es (indice 2): {tupla_de_frutas[2]}")
print(f"El cuarto elemento de tupla_de_frutas es (indice 3): {tupla_de_frutas[3]}")
# Leyendo de derecha a izquierda
print(f"El último elemento de tupla_de_frutas es (indice -1): {tupla_de_frutas[-1]}")
print(f"El penúltimo elemento de tupla_de_frutas es (indice -2): {tupla_de_frutas[-2]}")
print(f"El antepenúltimo elemento de tupla_de_frutas es (indice -3): {tupla_de_frutas[-3]}")
print(f"El cuarto elemento desde el final de tupla_de_frutas es (indice -4): {tupla_de_frutas[-4]}")


# Para una base de datos 
config_db = ("127.0.0.1", "root", "123456")
direccionIP = config_db[0]
print(f"La dirección IP es: {direccionIP}")
usuario = config_db[1]
print(f"El usuario es: {usuario}")
password = config_db[2]
print(f"La contraseña es: {password}")


print(tupla_de_frutas[0:3:2]) # naranja, plátano
otras_frutas = tupla_de_frutas[1:3] # pera
print(otras_frutas)

def devolver_datos_usuario():
    nombre = input("Dime tu nombre: ")
    edad = int(input("Dime tu edad: "))
    email = input("Dime tu email: ")
    return nombre, edad, email



print(f"La tupla que se crea es: {devolver_datos_usuario()}")
# print(f"El nombre es: {devolver_datos_usuario()[0]}") # nombre
# print(f"La edad es: {devolver_datos_usuario()[1]}") # edad
# print(f"El email es: {devolver_datos_usuario()[2]}") # email
# print(f"Los valores de la tupla son de indice 0 a indice 1: {devolver_datos_usuario()[0:2]}") # nombre y edad
# print(f"Los valores de la tupla son de indice 0 a indice 2: {devolver_datos_usuario()[0:3]}") # nombre, edad y email


print("-------------------Bucle FOR --------------")
for i in range(0, len(tupla_de_frutas)):
    print(tupla_de_frutas[i])


print("----------------BUCLE FOR IN-----------------")
for fruta in tupla_de_frutas:
    print(fruta)

# ERROR en una TUPLA (No puede modificar ni reasignar elementos con otros valores ni añadir elementos a la tupla una vez ya creada)
# tupla_de_frutas[0] = "Mandarina"

# ERROR EN LA TUPLA SI SOLO LE DAS UN UNICO ELEMENTO
# tupla_de_unico_elemento = ("Paula")
tupla_de_unico_elemento = ("Paula", )
print(tupla_de_unico_elemento)

# Borrar una tupla con "del" = delete
del tupla_de_frutas 
# print(tupla_de_frutas) 