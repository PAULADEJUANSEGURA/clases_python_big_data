# Realizar una funcion que me introduzca un texto y me cuente sus vocales.
texto_elegido = input("Dime un texto: ").lower()

def contar_vocales(texto_elegido):
    numero_vocales = 0
    for i in range (len(texto_elegido)):
        if texto_elegido[i] == "a" or texto_elegido[i] == "á":
            numero_vocales += 1
        elif texto_elegido[i] == "e" or texto_elegido[i] == "é":
            numero_vocales += 1
        elif texto_elegido[i] == "i" or texto_elegido[i] == "í":
            numero_vocales += 1
        elif texto_elegido[i] == "o" or texto_elegido[i] == "ó":
            numero_vocales += 1
        elif texto_elegido[i] == "u" or texto_elegido[i] == "ú":
            numero_vocales += 1
        
    print(f"Numero de vocales: {numero_vocales} ")

contar_vocales(texto_elegido)
print(" ----- Contar vocales in aeiouáéíóú ------- ")
def contar_vocales_in(texto_elegido):
    numero_de_vocales = 0
    texto_elegido = texto_elegido.lower()
    for i in range (len(texto_elegido)):
        if texto_elegido[i] in "aeiouáéíóú":
            numero_de_vocales += 1
    print(f"Numero de vocales = {numero_de_vocales}")

contar_vocales_in(texto_elegido)
