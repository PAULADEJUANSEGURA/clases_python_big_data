# Ejercicio Condicionales

horas_aparcamiento = float(input("Introduce el numero de horas que has estado aparcado: "))
tarjeta_residente = input("¿Tiene tarjeta de residente. Diga: [s/n] ").lower() 
tipo_vehiculo = input("¿Cual es su tipo de vehiculo? Diga si es:  [moto/coche/furgoneta] ").lower()

precio = 0

if horas_aparcamiento <= 0:
    print("Las horas deben ser un valor positivo")
elif tarjeta_residente != "s" and tarjeta_residente != "n":
    print("Responde s o n para la tarjeta de residente")
elif tipo_vehiculo not in ('moto', 'coche', 'furgoneta'):
    print("Tu tipo de vehiculo no puede aparcar en el parking")
else:
    if horas_aparcamiento <= 1:  
       precio = 2.00
    elif horas_aparcamiento <= 3:
        precio = 2.00 + (horas_aparcamiento - 1) * 1.5
    else:
        #Primera hora (2€) + Siguientes 2 horas (1.5€) + Resto de horas (1€)
        precio = 2.00 + (2.00 * 1.5) + (horas_aparcamiento - 3) * 1
         # Cálculo multiplicador x vehículo
        multiplicador = 1

        if tipo_vehiculo == 'moto':
            multiplicador = 0.7
        elif tipo_vehiculo == 'furgoneta':
            multiplicador = 1.5

        total = precio * multiplicador

        # Descuento residente
        descuento = total * 0.20 if tarjeta_residente == 's' else 0
        total -= descuento
        dinero_ahorrado = round(descuento, 2)

    print(f"""     
    --- TICKET DE APARCAMIENTO ---
    "Horas:{horas_aparcamiento} | Vehículo: {tipo_vehiculo} | Residente: {tarjeta_residente}
    Precio base: {precio} €
    Descuento residente: {dinero_ahorrado} €
    TOTAL: {total}
    ------------------------------ """)