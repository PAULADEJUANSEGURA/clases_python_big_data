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
        if tarjeta_residente == "s":
            descuento_residente = 0.20
            multiplicador_vehiculo = 1
            if tipo_vehiculo == "moto":
                multiplicador_vehiculo = 0.7
                total = precio * multiplicador_vehiculo * descuento_residente
            elif tipo_vehiculo == "furgoneta":
                multiplicador_vehiculo = 1.5
                total = precio * multiplicador_vehiculo * descuento_residente
            elif tipo_vehiculo == "coche":
                total = precio * descuento_residente
            else:
                print("No tienes tarjeta de residente")
                if tarjeta_residente == "n":
                    multiplicador_vehiculo = 1    
                    if tipo_vehiculo == "moto":
                        multiplicador_vehiculo = 0.7
                        total = precio * multiplicador_vehiculo
                    elif tipo_vehiculo == "furgoneta":
                        multiplicador_vehiculo = 1.5
                        total = precio * multiplicador_vehiculo
                    elif tipo_vehiculo == "coche":
                        total = precio * multiplicador_vehiculo
                    else:
                        print("Tu tipo de vehiculo no puede aparcar en el parking")          
            dinero_ahorrado = total - descuento_residente       
    print(f"""     
    --- TICKET DE APARCAMIENTO ---
    "Horas:{horas_aparcamiento} | Vehículo: {tipo_vehiculo} | Residente: {tarjeta_residente}
    Precio base: {precio} €
    Descuento residente: {dinero_ahorrado} €
    TOTAL: {total}
    ------------------------------ """)