# Ejercicio FOR
# Me gustaria que pidiendo un numero por pantalla int(input()) (ejemplo: 7)
# 7 x 1 = 7

numero_tabla = int(input("Dime el numero del que quieras la tabla: "))
for i in range(11):
    resultado = numero_tabla * i
    print(f"{numero_tabla} x {i} = {resultado}")
    

print("----- version 2 --------- ")    
# version 2 del Ejercicio FOR
numero = int(input("Dime un numero: "))
for i in range(1, 10):
    print(f"{numero} x {i} = {numero * i}")