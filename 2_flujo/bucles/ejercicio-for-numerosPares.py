# Pintar por pantalla 1000 numeros  pero solo los pares. 
# Empezando de 1 hasta 1000. 
# No se puede cambiar los valores iniciales.

for i in range (1, 1000):
    if i % 2 == 0:
        print(f"Valores pares: {i}")
    # elif i % 2 == 1:
        # print(f"Valores impares: {i}")

# Version 2

for i in range (1, 1000):
    if i % 2 == 0:
        print(f"Valores pares {i} ")
    # elif i % 2 != 0:
        # print(f"Valores impares {i} ")