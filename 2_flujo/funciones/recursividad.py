# Funcion recursiva es una función que se llama a sí misma

'''
Función recursiva 
def saludar():
    print("hola")
    saludar()

saludar()
'''
# Funcion que pida un DNI y pida solo los números y validar que es una cadena numérica
# proceso de validacion

def validar_dni():
    dni = input('Dime el numero de tu DNI: ')
    if dni.isdigit():
        print('Es un dni valido')
        return dni
    else:
        print('Esto no es un numero')
        validar_dni()
        
mi_dni = validar_dni()


