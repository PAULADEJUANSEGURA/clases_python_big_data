# =============================================================================
# EJERCICIO 4: NOTAS DE CLASE — INSERTAR, ORDENAR Y ESTADÍSTICAS
# Tienes una lista de notas de un examen.
# Añade tres notas más con append() y una en la posición 2 con insert().
# Muestra la lista ordenada de mayor a menor.
# Calcula y muestra la media, la nota más alta y la más baja.
# Cuenta cuántos alumnos han aprobado (nota >= 5).
# notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]
# =============================================================================

# Menu
# Pintar el menu con Las opciones, lista notas, añadir una nota al final, añadir una nota por posicion, mostrar la lista ordenada, calcular media, calcular maximo, calcular minimo, cuantos alumnos han aprobado.
notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]

def agregar_nota():
    nota_nueva = float(input("Introduce en valor de la nota que quieres añadir a la lista: "))
    # agregar un unico elemento por el final
    notas.append(nota_nueva)

def insertar_nota_en_posicion(posicion, cambio_nota):
    notas.insert(posicion, cambio_nota)

def mostrar_notas(notas):
    for nota in notas:
        color = "1" if nota < 5 else "2"
        print(f'\033[3{color}m {nota} \033[0m')
    #print( f'\033[31m {nota} \033[0m' ) # rojo
    #print( f'\033[32m {nota} \033[0m' ) # verde

# def mostrar_cuantos_han_aprobado():
   
def main():
    menu = """ 
            ==================== NOTAS DE UN EXAMEN ==================================")
            Elige entre las siguientes opciones: 
            [1] Mostrar lista de notas
            [2] Añadir nota al final de la lista
            [3] Añadir una nota por posición
            [4] Mostrar lista ordenada de mayor a menor
            [5] Calcular media de las notas de la lista
            [6] Calcular maxima nota
            [7] Calcular minima nota
            [8] Mostrar cuantos alumnos han aprobado
            [x] Salir 
        """
    print(menu)

    opcion = input("Introduce la opción elegida: ")

    if opcion == "1":
        print(f"Imprimiendo notas: ")
        print(f"Tenemos esta lista de notas de un examen: ")
        mostrar_notas(notas)
        
    elif opcion == "2":
        print(f"Añadir nota al final: ")
        nota_nueva1 = agregar_nota()
        nota_nueva2 = agregar_nota()
        nota_nueva3 = agregar_nota()
        print(notas)
        

    elif opcion == "3":
        print(f"Insertar nota en posición elegida: ")
        # agregar un metodo en cualquier posicion
        posicion = int(input("Dime el indice de la posicion que quieres cambiar: "))
        cambio_nota = float(input("Dime el valor de la nota nueva que deseas introducir: "))
        insertar_nota_en_posicion(posicion, cambio_nota)

    elif opcion == "4":
        print(f"Ordenar de mayor a menor la lista de notas: ")
        nueva_lista_notas = sorted(notas, reverse=True)
        print(nueva_lista_notas)

    elif opcion == "5":
        print(f"Calcular media de las notas de la lista")

    elif opcion == "6":
        print(f"Calcular maxima nota")

    elif opcion == "7":
        print(f"Calcular minima nota")

    elif opcion == "8":
        print(f"Calcular aprobados: ")

    elif opcion == "x":
        print("Hasta pronto")
        return
    else:
        print("Opción no valida")
    
    print("-" * 40)
    print(" ")
    main()

main()


