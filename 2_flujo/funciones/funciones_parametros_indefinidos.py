# Función de parámetros indefinidos

def sumar (*numeros):
    resultado = 0
    for i in range(len(numeros)):
        resultado = resultado + numeros[i]
    print(resultado)    
    print("----------------")


# *numeros tiene posicion empezando en cero y acabando en n-1 siendo n la longitud de elementos
# *numeros representa un conjuto de datos, ese conjunto tiene posicion empezando en 0 y acaban n-1 siendo n la longitud o cantidad
# Tuplas: no se pueden ni quitar ni añadir valores a una Tupla
sumar(1,2)
sumar(1, 2, 3)
sumar(1,2,3,4,5,12)


# MEDIA de 3 numeros
print("----------PROMEDIO O MEDIA DE 3 NUMEROS------------------")
def media(*numeros):
    resultado = 0
    for i in range(len(numeros)):
        resultado = resultado + numeros[i]
    promedio = resultado / len(numeros)
    print(promedio)

media(1,2)
media(1, 2, 3)
media(1, 2, 3, 4, 5, 12)
media(1, 2, 3, 4, 5)
media(2, 3, 4)


def promedio(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    print(suma / len(numeros))


promedio(1, 2, 3, 4, 5)
promedio(2, 3, 12)