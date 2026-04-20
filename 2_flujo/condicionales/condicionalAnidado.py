# Programa 1

nota = float(input('dime tu nota: '))
if nota >= 5 and nota <= 10:
    print("Estas aprobado")
elif nota >= 0 and nota < 5:
    print("Estás Suspenso")
else:
    print("Nota no valida")

# Programa 2 

if 0 <= nota and nota < 5:
    print("Estás Suspenso")
elif nota >= 5  and nota < 6:
    print("Suficiente")
elif nota >= 6 and nota < 7:
    print("Bien")
elif nota >= 7 and nota < 9:
    print("Notable")
elif 9 <= nota <= 10:
    print("Sobresaliente")
else:
    print("Nota no válida")