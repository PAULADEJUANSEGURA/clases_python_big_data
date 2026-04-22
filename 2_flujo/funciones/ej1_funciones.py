def sumar(numero_a, numero_b):
    return numero_a + numero_b

def restar(numero_a, numero_b):
    return numero_a - numero_b

def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


# funciones
def calcular(numero1, numero2, operacion):
    if operacion == "sumar":
        resultado = sumar(numero1, numero2)
        print(resultado)
    elif operacion == "restar":
        resultado = restar(numero1, numero2)
        print(resultado)
    elif operacion == "multiplicar":
        resultado = multiplicar(numero1, numero2)
        print(resultado)
    else:
        print("operacion no valida")
    print(resultado)


calcular (2, 5, "sumar")
calcular (5, 5, "multiplicar")   
calcular (10, 5, "restar")
calcular (12, 2, "restar")


