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
        if not str(numero).isdigit() and str(numero)[0] != '-':
            continue
        elif numero == 0:
            lista_resultante_ceros.append(numero)
        elif numero > 0:
            lista_resultante_positivos.append(numero)
        elif numero < 0:
            lista_resultante_negativos.append(numero)
        else:
            print("Numero no valido")
    print(lista_resultante_ceros)
    print(lista_resultante_positivos)
    print(lista_resultante_negativos)
    return lista_resultante_ceros , lista_resultante_positivos, lista_resultante_negativos

clasificar_numeros(numeros)


def estadisticas(lista):
    print(f'El numero maximo es {max(lista)}')
    print(f'El numero minimo es {min(lista)}')
    print(f"La suma es igual {sum(lista)}")
    promedio = sum(lista) / len(numeros)
    print(f"El promedio o la media es {round(promedio)}")
     
estadisticas(numeros)
