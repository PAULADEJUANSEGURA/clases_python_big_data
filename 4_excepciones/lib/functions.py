# Función 

def pedir_datos(option):
    if option == '1' or option == '2' or option == '3' or option == '4' or option == '5' or option == '6':
        try:
            n1 = float(input('Dime un numero: '))
            n2 = float(input('Dime otro numero: '))
            return n1, n2
        except ValueError:
            print("El valor introducido no es un numero")
            return False
            


# restar de los datos de una tupla
def restar(datos):
    return datos[0] - datos[1]


def multiplicar(datos):
    return datos[0] * datos[1]
    
def dividir(datos, option='4'):
    try: 
        return datos[0] // datos[1] if option == '5' else datos[0] / datos[1]
    except ZeroDivisionError:
        return "Error. No se puede dividir entre cero."
        
'''def dividir(datos, option = '4'):
    try:
        if option == '5':
            resultado = datos[0] // datos[1]
        else:
            resultado = datos[0] / datos[1]
        return resultado
    except ZeroDivisionError:
        return 'No se puede dividir por cero'
        '''


def modulo(datos):
    try:
        return datos[0] % datos[1]
    except ZeroDivisionError:
        return "El modulo no puede usar cero en el divisor"
