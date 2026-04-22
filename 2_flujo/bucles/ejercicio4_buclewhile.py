# Necesito que pidais varios numeros por pantalla y que los sumeis. El programa termina cuando metemos el numero 0;
# while.
# paso 1: pedir numero constantemente
# paso 2: crear una variables suma = 0
# paso 3: añadir a suma el valor introducido previmente convertido.
# paso 4: pulsando 0 acabamos el ejercicio.
print("-" * 30)
print("EJERCICIO 4 - SUMA ACUMULADA")
print("Termina al introducir el valor 0 ")
print("-" * 30)
suma = 0
numero = 0
while True:
    numero = int(input("Dime otro numero "))
    suma = suma + numero
    print(f"La suma es {suma}")
    if numero == 0:
        break