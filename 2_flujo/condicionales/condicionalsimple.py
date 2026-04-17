# Condicional Simple

nota = float(input("Dime tu nota: "))
if (nota >= 0 and nota < 5):
    print("Suspenso")
    print("Tienes que ir a la Recuperación")

if (nota >= 5 and nota <= 10):
    print("Aprobado")
    print("Tu nota es", nota)

else:
    print("El numero dado no es válido")