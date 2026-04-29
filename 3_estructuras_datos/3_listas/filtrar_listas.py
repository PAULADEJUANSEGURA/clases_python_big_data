# Filtrado de una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 74, 45, 89, 27]


numeros_pares = []
numeros_impares = []

def obtener_lista_pares(lista):
    lista_resultante = []
    for numero in lista:
        if numero % 2 == 0:
            lista_resultante.append(numero)
    return lista_resultante

def obtener_lista_impares(lista):
    lista_resultante_impares = []
    for numero in lista:
        if numero % 2 != 0:
            lista_resultante_impares.append(numero)
    return lista_resultante_impares


numeros_pares = obtener_lista_pares(numeros)
print(numeros_pares)
numeros_impares = obtener_lista_impares(numeros)
print(numeros_impares)
