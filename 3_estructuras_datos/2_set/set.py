# Set sirve mucho para borrar elementos duplicados de una lista.
# Un Set es un conjunto ordenado de elementos únicos!
# El uso más común es usarlo para eliminar elementos duplicados de un conjunto.

# Una lista es:
lista = [ 1, 1, 1, 2, 2, 2, 2, 3, 3, 3 ,3 ,3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 6, 7, 5, 9 ]
mi_set = set(lista)

# Una lista completa en consola se ve [entre corchetes]
print(f"Lista original: {lista}")  # Lista original: [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 3, 6, 7, 5, 9]

# Un set en consola se ve {entre llaves}
print(f"Set: {mi_set}") # Set: {1, 2, 3, 4, 5, 6, 7, 9}

# Convertir de nuevo en lista
print(f"lista_sin_duplicados", list(mi_set))


# conjunto de elementos o set el orden es aleatorio, esto complica un poco el manejo por posiciñon
frutas = {"Manzana", "Naranja", "Pera", "Plátano"}
lista_frutas = list(frutas)
print(lista_frutas)

# Añadimos un elemento nuevo al SET
frutas.add("Melón")
print(frutas)
# "Añadimos" un elemento existente al SET. No da error pero está duplicado y no lo añade.
frutas.add("Pera")
print(frutas)

# Borramos un elemento del SET
frutas.remove("Melón")

# Borrar elementos de un SET si estamos seguros de su existencia ( Si no estamos seguros NOS DA UN ERROR )
# frutas.remove("Sandia")


# Borrar elementos si no estas seguro de si existen en el SET y con discard no da problemas en la ejecucion del programa
frutas.discard("Sandia")


# Vaciarlo Dejarlo en Blanco
frutas.clear() # Se visualiza en consola como -> "set()"
print(frutas)
# Eliminar el SET
del(frutas)

# set()
# list()
# tuple()
# dictionary()
