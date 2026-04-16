nombre_alumno = "Paula de Juan"
print(nombre_alumno)

print(type(nombre_alumno))

edad_alumno = 21
print(edad_alumno)
print(type(edad_alumno))

# Tipos basicos en Python

# Numéricos
edad = 36
precio = 1299.35 
grados = -27

# Booleanos
estado_verdadero = True
estado_falso = False

# Cadenas de caracteres de texto STRINGS
mensaje_usuario = "Hola Mundo"
nombre = "Irene"
apellidos = "Martínez"
mensaje = 'Hola mundo "¿Qué tal?"'
print(mensaje)


# Concatenación de Strings
# Objetivo: Irene Martinez: 36
nombre_completo = nombre + " " + apellidos + ": " + str(edad)
print(nombre_completo)


nombre_completo2 = f'{nombre} {apellidos}: {edad}'
print(nombre_completo2)

# String multilinea
texto_largo = """ 
Selecciona una opción
[1] Sopa
[2] Puré de calabaza
[3] Gazpacho

"""
print(texto_largo)

opcion = input(texto_largo)
print(f'La opcion es {opcion}')