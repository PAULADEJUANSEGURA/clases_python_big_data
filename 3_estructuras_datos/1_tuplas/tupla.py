# Una TUPLA es un conjunto de datos pero la principal carcteristica es que es INMUTABLE.
# No se puede cambiar , ni valor ni de longituds.
# El objetivo de la Tupla proteger los datos que hay dentro.
# La diferencia visual es que al inicializarla usamos los paréntesis
mi_primera_tupla = ("Paula", 38, True)

tupla_de_frutas = ("naranja", "pera", "platano", "manzana")

# No se pueden modificar ni añadir
print(mi_primera_tupla)
print(tupla_de_frutas)   

# ¿Como saber la longitud de una tupla?
print(len(tupla_de_frutas))

# ¿Como obtener un índice de una tupla? Se numero de 0 a n-1 siendo n la Longitud
print(mi_primera_tupla[0])
print(" #---- Tupla de frutas -----# ")
# Leyendo de izquierda a derecha
print(tupla_de_frutas[0])
print(tupla_de_frutas[1])
print(tupla_de_frutas[2])
print(tupla_de_frutas[3])
# Leyendo de derecha a izquierda
print(tupla_de_frutas[-1])
print(tupla_de_frutas[-2])
print(tupla_de_frutas[-3])
print(tupla_de_frutas[-4])


# Para una base de datos 
config_db = ("127.0.0.1", "root", "123456")
direccionIP = config_db[0]
print(direccionIP)
usuario = config_db[1]
print(usuario)
password = config_db[2]
print(password)


print(tupla_de_frutas[0:3:2]) # naranja, plátano
otras_frutas = tupla_de_frutas[1:3] # pera
print(otras_frutas)

def devolver_datos_usuario():
    nombre = input("Dime tu nombre: ")
    edad = int(input("Dime tu edad: "))
    email = input("Dime tu email: ")
    return nombre, edad, email

print(devolver_datos_usuario()[0])
print(devolver_datos_usuario()[0:2])