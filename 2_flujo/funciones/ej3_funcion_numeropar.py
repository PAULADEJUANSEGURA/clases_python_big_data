# Funcion que evalúa si un numero introducido por parametro es par o impar
print("-------------Evaluar numero para ver si es par o impar.-------------")
numero = int(input("Dime un numero para evaluarlo: "))
def evaluar(numero):
    if numero == 0:
        print(f"El numero {numero} es cero.")
    elif numero % 2 == 0:
        print(f"El numero {numero} es par.")
    elif numero % 2 != 0:
        print(f"El numero {numero} es impar.")
    else:
        print(f"El valor {numero} no es válido.")

print(f"Vamos a evaluar tu número = {numero}")
evaluar(numero)
print("..................FIN..............................................")
# evaluar(15)
# evaluar(14)
# evaluar(0)
# evaluar(1)
# evaluar(3)