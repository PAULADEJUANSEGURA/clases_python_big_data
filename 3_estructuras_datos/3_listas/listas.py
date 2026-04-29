# Una lista es un conjunto de elementos ordenador por posición

lista_nombres = ["Miguel Angel", "Paula", "Pablo", "Juan Antonio"]

# longitud 
print(len(lista_nombres))

# imprimir un valor de la lista
print(lista_nombres[1])  # Paula


# añadir elementos a lista pòr el final
nombre_nuevo = "Reniel" 
lista_nombres.append(nombre_nuevo)
print(lista_nombres)

# Recorrer listas - varios metodos :
print("--------for i in range( )------------------------")
for i in range (len(lista_nombres)):
    print(lista_nombres[i])

print("---------for nombre in lista_nombres---------------")
for nombre in lista_nombres:
    print(nombre)
    # if nombre == "Pablo":
        # break
else:
    print("La lista ha terminado")


# Las listas si permiten cambiar elementos Son mutables
lista_nombres[1] = "Miriam"
print(lista_nombres)


