"""
El cálculo de la letra del Documento Nacional de Identidad (DNI) es un proceso matemático sencillo que se basa en obtener el resto de la división entera del número de DNI y el número 23. 
A partir del resto de la división, se obtiene la letra seleccionándola dentro de un lista de letras.

El array de letras es:
letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B','N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E','T'];

Por tanto si el resto de la división es 0, la letra del DNI es la T y si el resto es 3 la letra es la A. 
Con estos datos, elaborar un pequeño script que:

1. Almacene en una variable el número de DNI indicado por el usuario y en otra variable la letra del
DNI que se ha indicado.

2. Si el numero no introducido no esta formado por numeros solo deberá para la ejecución y lanzar 
un error de numero no valido.

3. Si el número es válido, se calcula la letra que le corresponde según el método explicado
anteriormente.

4. Una vez calculada la letra, se debe comparar con la letra indicada por el usuario. Si no coinciden, 
se muestra un mensaje al usuario diciéndole que la letra que ha indicado no es correcta. En otro caso, se muestra un mensaje indicando que el número y la letra de DNI son correctos.     
"""
letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B','N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

def main():
    dni_completo = input("Introduce tu DNI: ")
    if len(dni_completo) <= 9:
        numeros = dni_completo[:-1] 
        letra = dni_completo[-1]  
        print(f"Los numeros son {numeros} y la letra es {letra}." )  
        calculo = int(numeros) % 23
        print(f"El indice de tu letra es {calculo}.")
        for i in range (0,len(letras)):
            if calculo == i:
                print(letras[i])
        print(letras)
main ()
# El numero del DNI dividido entre 23 da un numero 

# Contar si tiene 9 o menos en len()

# Separar el numero = 12345678 y la letra Z en otra variable

# El numero convertirlo a numero / 23 = resto (es decir modulo = indice del array)