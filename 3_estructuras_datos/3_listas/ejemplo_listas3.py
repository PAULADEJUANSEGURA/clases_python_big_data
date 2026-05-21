# Ejercicio con una LISTA coN TUPLAS dentro
lista_productos = [("Laptop", 1200), ("Ratón", 39), ("Memoria RAM", 200), ("Teclado", 10)]

#Pintar una tupla entera de la lista
print(lista_productos[1]) # Tupla ("Ratón", 39)

print(lista_productos[1][1]) # 39

print(lista_productos[3][0]) # Teclado


# Ordena por orden alfabetico
lista_ordenada = sorted(lista_productos) 
print(lista_ordenada)


# Ordenar con sorted y lambda por precio de menor a mayor
print("---- Ordenar con sorted y lambda por precio de menor a mayor-----")
lista_ordenada2 = sorted(lista_productos, key=lambda producto: producto[1])
print(lista_ordenada2)

# Ordenar con sorted y lambda por precio de mayor a menor
print("---- Ordenar con sorted y lambda por precio de mayor a menor-----")
lista_ordenada3 = sorted(lista_productos, key=lambda producto: producto[1], reverse=True)
print(lista_ordenada3)

# Ordena a los alumnos por altura
alumnos = [('Carlos', 34, 180), ('Lucia', 24, 165), ('Raul', 18, 190), ('Berta', 24, 172)]
print("--------- Ordenar con sorted y lambda por altura de mayor a menor ----------------")
alumnos_altura = sorted(alumnos, key=lambda alumno: alumno[2], reverse=True)
print(alumnos_altura)