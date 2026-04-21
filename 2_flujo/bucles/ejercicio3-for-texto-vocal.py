# Quiero pedir un texto por pantalla de cualquier longitud y quiero que pidais una vocal.
# Contar cuantas vocales tiene el texto.
numero_veces_repetido = 0
texto_elegido = input("Dime un texto: ").lower()
vocal_elegida = input("Dime una vocal: ").lower()
cantidad = len(texto_elegido)
for i in range (cantidad):
    if texto_elegido[i] == vocal_elegida:
        numero_veces_repetido += 1
print(f"Numero de veces repetidas: {numero_veces_repetido} ")