# Como hacer comentarios de una linea rapidamente?
# Ctrl + ç
# Con Ctrl + ç te comenta
# print("Hello World")
# ---------------------

# Operadores Lógicos: and (&&), or(||), not
# input() devuelve un string
# Lo convertimos en float

# Con AND

# True & True = True
# True & False = False
# False & True = False
# False & False = False

precio = float(input("Dime un precio: "))
marca = input("Dime una marca: ")
print("La marca que has elegido es: ", marca)
print("El precio es: ", precio)
resultado = precio > 100 and marca == "Apple"
print(resultado)

# Con OR

# True & True = True
# True & False = True
# False & True = True
# False & False = False

numero1 = float(input("Dime un numero:  "))
resultado1 = numero1 % 2 == 0 
print("El numero que me has dicho es:", numero1)
if (resultado1 == True):
    print("Tu numero es par")
else:
    print("Tu numero es impar")
resultado2 = numero1 % 5 == 0
if (resultado2 == True):
    print("Tu numero es divisible entre 5")
else:
    print("Tu numero no es divisible por 5 en división entera")

resultado3 = resultado1 or resultado2
if (resultado1 or resultado2):
    print("El resultado de ambas condiciones es: ", resultado3)
else:
    print("El valor es Falso: ", resultado3)


# Forma simplificada
print("Forma Simplificada de Mario Profesor")
numero = float(input("Introduce un número: "))
es_par = numero % 2 == 0
multiplo_5 = numero % 5 == 0

resultado = numero % 2 == 0 or numero % 5 == 0
print("El resultado es: ", resultado)


# Negación 
print("Operador 'not' (distinto, negación): ")
esta_activo = True
print(not esta_activo)