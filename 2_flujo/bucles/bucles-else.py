# Todos los bucles tienes una secuencia de escape que se lanza siempre que se completa.

for i in range (1, 20):
    if i % 5 == 0:
        continue
    print(i)
# Si el bucle no termina no pinta el else
else:
    print("El bucle ha terminado")