# Variable de texto
texto = input("Dime una cadena de caracteres: ")
# Un String es una cadena de caracteres, es un conjunto
print(f"Tu nombre tiene este numero de caracteres: {len(texto)}") # Cantidad de caracteres
# print(texto[0]) # P
# print(texto[5]) # es el primer espacio
print(f"Tu nombre es: {texto}")
for i in range(len(texto)):
    # Pintar las MAYÚSCULAS
    if texto[i] == texto[i].upper():
        print(texto[i])
    # Pintar solo las minúsculas
    # elif texto[i] == texto[i].lower():
        # print(texto[i])
