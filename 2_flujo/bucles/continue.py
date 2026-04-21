# Continue

for i in range(1, 15):
    # Cuando llega a 8 divide y de resto de 0
    if i % 8 == 0:
        continue
    print(i)
    # Pinta los valores de 1 a 7
    # El break lo hace al llegar al valor 8