# Pediremos un numero por pantalla y lo convertiremos en un int o float
# Vamos a ver los fallos o errores

# numero = int(input("Dime un numero: "))
# print(numero)

## try - except
# TRY maneja la parte correcta o parte esperada
# EXCEPT maneja el posible error

def pedir_numero_a_usuario():
    try:
        entrada = input("Dime un numero: ")
        numero = int(entrada)
        print(numero)
    except ValueError: # Excepción particular
        print(f"Error. Valor inválido no númerico {entrada}.")
        pedir_numero_a_usuario()
    # except: # Excepción genérica
        # print("Error generico")

pedir_numero_a_usuario()

