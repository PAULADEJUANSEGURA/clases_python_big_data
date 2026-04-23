# # Realizar una funcion que me introduzca un texto y me cuente sus vocales.
print("------------- Obtener iniciales version propia--------------")
nombre_y_apellidos = input("Dime tu nombre y apellidos: ")

def solo_iniciales(nombre_y_apellidos):
    cantidad = len(nombre_y_apellidos)
    resultado = ""
    for i in range (cantidad):
        if i == 0:
            resultado = resultado + nombre_y_apellidos[i].upper()+  ". "
        if nombre_y_apellidos[i] == " ":
            resultado = resultado + nombre_y_apellidos[i + 1].upper()+ ". "
    print(f"Las iniciales son {resultado}")
    
solo_iniciales(nombre_y_apellidos)


print("------------------Obtener iniciales version 2 -------------")
nombre2 = input("Dime un nombre y apellidos: ")
def obtener_iniciales(nombre2):
    resultado = ""
    for i in range (len(nombre2)):
        if i == 0:
            resultado = resultado + nombre2[i].upper() + ". "
        if nombre2[i] == " ":
            resultado = resultado + nombre2[i+1].upper() + ". "
    print(resultado)

obtener_iniciales(nombre2)
# obtener_iniciales("Juan Antonio Perez")