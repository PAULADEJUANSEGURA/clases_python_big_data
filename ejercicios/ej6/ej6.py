# Pide un numero de ticket de compra y hay que validar que la entrada no contenga letras 

# ["Un Café Gratis", "10% de Descuento", "Un Boligrafo"]

# Premio se obtiene con el resto del numero de ticket entre 5 (division entera)

# El dato obtenido es la posicion de la lista, es decir, el precio

# Si el numero se sale rango no hay premio

def main ():
    lista_premios = ["Un Café Gratis", "10 por ciento de Descuento", "Un Boligrafo"]
    try:
        numero_ticket = int(input("Dime el numero de ticket para ver si tienes premio: "))
        calculo = numero_ticket % 5
        print(calculo)
        if calculo < len(lista_premios):
            for i in range(0, len(lista_premios)):
                if i == calculo:
                    print(f"Tu premio es {lista_premios[calculo]}")
        else:
            print("No tienes premio")            
    except ValueError:
        print("El ticket solo puede contener numeros ")
    except IndexError:
        print("No tienes premio")

main ()