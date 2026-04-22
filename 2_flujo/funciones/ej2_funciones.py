# Funcion devuelve parametros
print("----------PROMEDIO O MEDIA DE 3 NUMEROS------------------")
numero1 = int(input("Dime un primer numero: "))
numero2 = int(input("Dime un segundo numero: "))
numero3 = int(input("Dime un tercer numero: "))
print("#########################################################")
print("SUMA: --------")
def suma(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3
    print(f"La suma es {suma} ")
    return suma

print("DIVIDIR: --------")
def dividir(divisor, dividendo):
    print(f"La division es {divisor/dividendo}")
    return divisor / dividendo

print("----------PROMEDIO O MEDIA DE 3 NUMEROS------------------")
def promedio(numero1, numero2, numero3):
    resultado_suma = suma(numero1, numero2, numero3)
    media = dividir(resultado_suma, 3)
    print(f"La suma es {resultado_suma}")
    print(f"El promedio es {media}")
    
promedio(numero1, numero2, numero3)
