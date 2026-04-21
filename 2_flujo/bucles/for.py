# Bucle FOR
cantidad = int(input("Introduce el numero de veces que quieres que diga Hola: "))
# print(type(cantidad))
for i in range(cantidad):
    print(f"Hola {i}") 

# Pasos del Algoritmo
# Paso 1: Almacenar la cantidad de unidades 
# Paso 2: Pedir esa cantidad por pantalla
# Paso 3: Convertir la unidad en numero
# Paso 4: Meterla en el for
# Paso 5: Ejecutar el script
print("------------")
# version 2: Poder elegir punto de inicio y punto de fin en el bucle
for i in range(2, 8):
    print(f"versión2: Valor {i}")
print("------------")

#version 3: Contar de tres en tres pudiendo elegir el inicio y el final y los saltos
for i in range (2, 15, 3):
    print(f"Valor de tres en tres: {i}")
print("------------")