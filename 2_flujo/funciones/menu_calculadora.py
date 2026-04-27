# Menu 
# Vamos a crear un menú que me permita decidir que operación va a hacer mi calculadora


# Pedir los números para las futuras operaciones de la calculadora
def pedir_numeros():
    numero1 = float(input("Dime un primer número: "))
    numero2 = float(input("Dime un segundo número: "))
    return numero1, numero2


def main():
    menu = """
            ### BIENVENIDO A NUESTRA CALCULADORA ###
            ----------------------------------------
            ¿Qué operación quieres realizar?
            [1] Sumar
            [2] Restar
            [3] Multiplicar
            [4] Dividir
            [x] Salir
    """
    print(menu)
    option = input("¿Qué operación quieres realizar?: ")
    resultado = 0
    if option == "1":
        numeros = pedir_numeros()
        resultado = numeros[0] + numeros[1]
    elif option == "2":
        numeros = pedir_numeros()
        resultado = numeros[0] - numeros[1]
    elif option == "3":
        numeros = pedir_numeros()
        resultado = numeros[0] * numeros[1]
    elif option == "4":
        numeros = pedir_numeros()
        resultado = numeros[0] / numeros[1]
    elif option == "x":
        print("Hasta pronto, vuelve a usar esta calculadora cuando quieras!")
        return False
    else:
        print("Valor introducido no válido. Introduce otro valor a continuación.")
    print(resultado)
    main()

main()