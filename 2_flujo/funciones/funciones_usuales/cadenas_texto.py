# Funciones para las cadenas de texto:

# Paradigma FUNCIONAL
# nombre_funcion(texto)
# len(nombre)

# Paradigma Orientado a Objetos
# texto.nombre_funcion()
# nombre.upper()


texto = "hOlA"
print(texto.lower()) # hola
print(texto.upper()) # HOLA
# lower() y upper() no cambian el valor del texto original
print(texto)

titulo = "Hola COMO estas?"
# Primera letra de toda la frase en Mayuscula
print(titulo.capitalize()) # Hola como estas
# Convertir la primera Letra de cada palabra en Mayuscula
print(titulo.title()) # Hola Como Estas

print(texto.swapcase()) # hOlA -> HoLa


# funciones de comprobación
dni = "2157819M"
print(dni.zfill(9))


frase = "En un lugar de la ManchA..."
print(frase.lower().count('a'))
ciudad = "Alcarria"
frase_modificada = frase.replace("ManchA", ciudad)
print(frase)
print(frase_modificada)

# En esta frase: ¿Como están los máquinas?
frase_con_espacios = "¿Como están los máquinas?"
frase_sin_espacios = frase_con_espacios.replace(" ", "")
frase_sin_2_espacios = frase_con_espacios.replace(" ", "", 2)
print(frase_sin_espacios)
print(frase_sin_2_espacios)