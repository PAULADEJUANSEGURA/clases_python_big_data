# EJERCICIO 1: FUNCIÓN QUE CLASIFICA UNA LISTA DE NÚMEROS

numeros = [4, -2, 0, 7, -5, 0, 3, -1, 8, 0, -9, 6]
print(f"Dada la lista de numeros: {numeros}")
# - Crea una función clasificar_numeros(lista) que reciba una lista de números y devuelva tres listas: positivos, negativos y ceros.
# - Crea también una función estadisticas(lista) que devuelva la suma, el mayor numero, menor numero y la media

lista_resultante_positivos = []
lista_resultante_negativos = []
lista_resultante_ceros = []

def clasificar_numeros(numeros):
    for numero in numeros:
        if numero == 0:
            lista_resultante_ceros.append(numero)
        elif numero > 0:
            lista_resultante_positivos.append(numero)
        else:
            lista_resultante_negativos.append(numero)
    print(lista_resultante_ceros)
    print(lista_resultante_positivos)
    print(lista_resultante_negativos)

clasificar_numeros(numeros)



def estadisticas(lista):
    resultado = 0
    for numero in lista:
        resultado = resultado + numero
    print(resultado)
    print(f'El numero maximo es {max(numeros)}')
    print(f'El numero minimo es {min(numeros)}')
    for i in range(0, len(numeros)):
        promedio = resultado / len(numeros)
        i = i + 1
    print(promedio) 
     
estadisticas(numeros)
