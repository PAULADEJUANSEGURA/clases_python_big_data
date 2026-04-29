# Listas con texto
nombres = ["Juan", "Mario", "Pablo", "Paula", "Miriam"]

# agregar un unico elemento por el final
nombres.append("Joaquin")
print("Con 'append' = ", nombres)

# agregar varios elementos a la vez en una lista por el final
nombres.extend(["Miguel Angel", "Reniel"])
print("Con 'extend' = ", nombres)

# agregar un metodo en cualquier posicion
nombres.insert(3, "Luis")
print("Con 'insert' = ", nombres)

# borrar un elemento de la list
# metodo pop
ultimo_elemento = nombres.pop()
print(nombres)
print(ultimo_elemento)

elemento_tres = nombres.pop(3)
print(elemento_tres)

# eliminar elementos de al lista por contenido
# nombres.remove("Quique") # Elemento que no esta da ERROR
nombres.remove("Mario")
print(nombres)



