# Función con parámetros
# una función puede tener dos tiops de parámetros
numero_1 = 4
numero_2 = 23

print("-----------------SUMAR------------------")
def sumar(numero_a, numero_b):
    resultado = numero_a + numero_b
    print(resultado)

sumar(3, 23)
sumar(23, 8)
sumar(numero_1, numero_2)

print("-----------------POTENCIA----------------------")
def potencia(base, exponente):
    resultado = base ** exponente
    print(resultado)

potencia(3, 4)
potencia(10, 6)

print("-----------------POTENCIA con PARAMETRO optativo--------------------")
# Los parametros optativos van al final
def potencia_optativos(base, exponente=3):
    resultado = base ** exponente
    print(resultado)

potencia_optativos(3)
potencia_optativos(10)



# MEDIA de 3 numeros
print("----------PROMEDIO O MEDIA DE 3 NUMEROS------------------")
def media(numero_1, numero_2, numero_3):
    promedio = (numero_1 + numero_2 + numero_3) / 3
    print(promedio)


media(5, 7, 9)
media(4, 2, 9)
media(5, 5, 10)
media(2, 3, 5)