# # Realizar una funcion que me introduzca un texto y me cuente sus vocales.
nombre_y_apellidos = input("Dime tu nombre y apellidos: ")

def solo_iniciales(nombre_y_apellidos):
    cantidad = len(nombre_y_apellidos)
    for i in range (cantidad):
        if i == 0:
            print(f"{nombre_y_apellidos[i].upper()}.")
        if nombre_y_apellidos[i] == " ":
            print(f"{nombre_y_apellidos[i + 1].upper()}.")
          
solo_iniciales(nombre_y_apellidos)