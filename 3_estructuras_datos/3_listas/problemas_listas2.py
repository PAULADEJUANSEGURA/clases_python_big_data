# PASO POR REFERENCIA
animales = ["perro", "gato", "periquito", "tortuga", "conejo"]

# paso por referencia de la lista 
animales2 = animales

# Para NO hacer un paso por referencia tenemos que generar una copia de la lista original

# metodo 1: copy()

animales3 = animales.copy()

animales[2] = "nilo"

print(animales)  
print(animales2)
print(animales3)

print("-- PASO POR REFERENCIA y por otro lado COPIAS --")

frutas = ["manzana", "platano", "pera", "sandia"]

# Para no hacer un paso por referencia tenemos que generar un copia de la lista original
frutas2 = frutas

print(" frutas3 = copia ")

# Romper la referencia
# frutas3 = frutas[1:3]
frutas3 = frutas[:]
print(frutas3)


frutas[2] = "naranjas"
print(frutas) # Aqui cambia por naranjas (original modificada)
print(frutas2) # Aqui cambia por naranjas (paso por referencia de la original modificada)
print(frutas3) # Copia que rompe el paso por referencia


