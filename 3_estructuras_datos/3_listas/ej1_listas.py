# pedir numeros por pantalla,
# insertarlos en una lista de numeros, 
# el programa para cuando introduzcamos un letra 
# y dicha letra no estará en la lista.
lista = []

def pedir_numero():
    while True:
        numero = input("Dime un numero: ")
        # if numero.isalpha():
        numero_sin_signo = numero.replace("-", "")                  
        if not numero_sin_signo.isdigit():
                break
        lista.append(int(numero))
        # print(lista)
    print(lista)    

pedir_numero()
   

