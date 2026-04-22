# Arbolito
asteriscos = int(input("Dime  el número máximo de asteriscos: "))
espacios = 10
for i in range(1, asteriscos + 1):
    print(f"*" * i)
        
for j in range(asteriscos + 1 , 0, -1):
    print(f"*" * j)