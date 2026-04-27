# Hacer un programa en Python que permita elegir entre 5 opciones
    # 1 - pasar un texto a minúsculas
    # 2 - contar la cantidad de letras de un texto
    # 3 - invertir el texto -> Tony Stark -> Stark Tony
    # 4 - quitar espacios en blanco del texto y acentos
    # 5 - salir
# cualquier opcion no descrita vuelve a iniciar el programa

def pasar_a_minusculas(texto):
    resultado = texto.lower()
    return resultado


def contar_cantidad_letras(texto):
    texto_sin_espacios = texto.replace(" ", "")
    print(f"Tu texto sin espacios es: {texto_sin_espacios}")
    print(f"El numero de caracteres es:{len(texto_sin_espacios)}")

def quitar_espacios_acentos(texto):
    return texto.replace(" ", "")

def contar_letras(texto):
    # quitar el caracter espacio para que no me lo cuente
    resultado = quitar_espacios_acentos(texto)
    contador = 0
    for caracter in resultado:
        if caracter.isalpha():
            contador += 1
    return contador

def invertir_palabras(texto):
    lista_palabras = texto.split(" ")
    resultado = ""
    for i in range (len(lista_palabras)):
        resultado = lista_palabras[i] + " " + resultado
    print(resultado)

def quitar_espacios_en_blanco_acentos(texto):
    texto_sin_espacios = texto.replace(" ", "")
    for i in range (len(texto_sin_espacios)):
        otro_texto = texto_sin_espacios.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
    resultado = texto_sin_espacios[i] + otro_texto





def main():
    menu = """
            ### BIENVENIDO A NUESTRO MENÚ ###
            ----------------------------------------
            ¿Qué operación quieres realizar?
            [1] Pasar un texto a minúsculas
            [2] Contar la cantidad de letras de un texto
            [3] Invertir el texto -> Tony Stark -> Stark Tony
            [4] Quitar espacios en blanco del texto y acentos
            [x] Salir
    """
    print(menu)
    option = input("¿Qué operación quieres realizar?: ")
    resultado = ""
    texto = input("Dime un texto: ")
    if option == "1":
        pasar_a_minusculas(texto)
    elif option == "2":
        contar_cantidad_letras(texto)
        contar_letras(texto)
    elif option == "3":
        invertir_palabras(texto)
    elif option == "4":
        quitar_espacios_en_blanco_acentos
        pass
    elif option == "x":
        print("Hasta pronto, vuelve a usar este programa cuando quieras!")
        return False
    else:
        print("Valor introducido no válido. Introduce otro valor a continuación.")
    print(resultado)
    main()


main()