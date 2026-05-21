# Filtrado de una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 74, 45, 89, 27]


numeros_pares = []
numeros_impares = []

def obtener_lista(lista):
    lista_resultante_pares = []
    lista_resultante_impares = []
    for numero in lista:
        if numero % 2 == 0:
            lista_resultante_pares.append(numero)
        else:
            lista_resultante_impares.append(numero)
    return lista_resultante_pares, lista_resultante_impares
           
numeros_pares = obtener_lista(numeros)[0]
print(numeros_pares)
numeros_impares = obtener_lista(numeros)[1]
print(numeros_impares)
