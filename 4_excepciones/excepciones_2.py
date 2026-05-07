# Pedimos 2 numeros
try:
    numero1 = int(input("Dime un numero: "))
    numero2 = int(input("Dime un numero: "))

    resultado = numero1 / numero2
    print(resultado)

# Excepciones propias de Python
except ValueError:
    print("Los valores introducidos no son correctos.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
# excepcion genérica
except:
    print("Futuro error no previsto.")


print("---- El programa continua tras el error ---")