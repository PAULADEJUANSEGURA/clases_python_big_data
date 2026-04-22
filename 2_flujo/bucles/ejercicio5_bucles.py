# Arbolito
asteriscos = 1
espacios = 10
for i in range(1, 11):
    print(f"*" * asteriscos + espacios * " ")
    asteriscos += 1
    espacios -= 1
    if asteriscos == 10:
        for j in range(1, 11):
            print(f"*" * asteriscos + espacios * " ")  
            asteriscos -= 1
            espacios += 1  
    
