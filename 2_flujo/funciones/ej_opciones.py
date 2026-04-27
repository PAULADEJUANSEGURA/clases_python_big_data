# Hacer un programa en Python que permita elegir entre 5 opciones
    # 1 - pasar un texto a minúsculas
    # 2 - contar la cantidad de letras de un texto
    # 3 - invertir el texto -> Tony Stark -> Stark Tony
    # 4 - quitar espacios en blanco del texto y acentos
    # 5 - salir
# cualquier opcion no descrita vuelve a iniciar el programa

def obtener_texto():
    texto = input("Dime un texto: ")
    return texto


def pasar_a_minusculas(texto):
    texto = texto.lower()
    return texto

def quitar_espacios_acentos(texto):
    texto = texto.replace(" ", "")
    texto = texto.replace("á", 'a')
    texto = texto.replace("é", 'e')
    texto = texto.replace("í", 'i')
    texto = texto.replace("ó", 'o')
    texto = texto.replace("ú", 'u')
    texto = texto.replace("ü", 'u')
    return texto

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
    return resultado

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
    if option == "1":
        texto = obtener_texto()
        resultado = pasar_a_minusculas(texto)
    elif option == "2":
        texto = obtener_texto()
        resultado = contar_letras(texto)
    elif option == "3":
        texto = obtener_texto()
        resultado = invertir_palabras(texto)
    elif option == "4":
        texto = obtener_texto()
        texto = pasar_a_minusculas(texto)
        resultado = quitar_espacios_acentos(texto)
    elif option == "x":
        print("Hasta pronto, vuelve a usar este programa cuando quieras!")
        return False
    else:
        print("Valor introducido no válido. Introduce otro valor a continuación.")
        main()
    print("-------------------# Resultado #--------------------------------")    
    print(resultado)
    print("-------------------# Funcionalidad terminada #------------------")
    main()

main()