# Función simple
# Una función tiene dos partes sin la otra no pueden convivir.
# La definición y la llamada.

# La DECLARACIÓN o DEFINICIÓN

def saludar():
    for i in range(5):
        print("Hola desde una función")

def despedir():
    for i in range(2):
        print("Hasta luegorrrl")

for i in range(100):
    saludar()
despedir()
despedir()

def arbol(altura):
    for i in range(altura):
        espacios = " " * (altura - i - 1)
        estrellas = "*" * (2 * i + 1)
        print(espacios + estrellas)
    
    # Tronco
    print(" " * (altura - 1) + "|")
    print(" " * (altura - 1) + "|")

# Ejemplo
arbol(20)