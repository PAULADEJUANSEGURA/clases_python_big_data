"""
Tu objetivo es escribir un programa que haga lo siguiente:
Crea una lista con 5 recompensas (textos).
Pide al usuario que introduzca el número de la recompensa que quiere extraer (del 0 al 4).
Utiliza un bloque try-except-finally para controlar los posibles errores:
Maneja el ValueError: Si el usuario escribe letras en lugar de un número.
Maneja el IndexError: Si el usuario escribe un número que no está en la lista (por ejemplo, el 9 o el 25).
El programa debe imprimir siempre al final (haya fallado o no) un mensaje que diga: "Cerrando el catálogo de recompensas. ¡Gracias por jugar!". """

recompensas = ["Espada de madera", "Poción de salud", "Escudo", "Botas de velocidad", "Oro"]
def pedir_recompensa():
    try:
        numero_recompensa = int(input("Dime que recompensa quieres: "))
        print(recompensas[numero_recompensa])
    except IndexError:
        print("Escribe un numero de 0 a 4. Por ejemplo: 'Espada de madera' = 0. ")  
        pedir_recompensa()
    except ValueError:
        print("Escribe un numero en lugar de con letras")
        pedir_recompensa()
    finally:
        print("Cerrando el catálogo de recompensas. ¡Gracias por jugar!")

pedir_recompensa()