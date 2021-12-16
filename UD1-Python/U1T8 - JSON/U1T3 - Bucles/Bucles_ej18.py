""" Imprima el siguiente patrón. Escriba un programa para imprimir el siguiente patrón de inicio usando el bucle for

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* """

fila = 5
for i in range(0, fila):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(fila, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")