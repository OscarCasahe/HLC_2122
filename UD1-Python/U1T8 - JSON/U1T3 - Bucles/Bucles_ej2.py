""" Escriba un programa para imprimir el siguiente patrón numérico usando un bucle.

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5 """

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print(j, end=" ")
    print("")
    