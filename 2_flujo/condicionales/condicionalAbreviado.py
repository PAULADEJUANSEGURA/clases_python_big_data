# Definir el valor de una variable en función de una condición
valor = input("Dime si quieres encender o apagar la luz: [S/N]")

estado_luz = False

if valor == "S":
    estado_luz = True
elif valor == "N": 
    estado_luz = False

if estado_luz:
    mensaje = "La luz esta encendida"
else:
    mensaje = "La luz esta apagada"

# En una unica linea

print("Programa abreviado Condicional abreviado... ---- ")

mensaje = "Luz encendida" if estado_luz else "Luz apagada"

print(mensaje)