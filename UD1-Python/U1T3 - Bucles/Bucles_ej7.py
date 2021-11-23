""" Ejercicio 7
Escriba un programa para usar el bucle for para imprimir el siguiente patrón numérico inverso:

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1 """

num = 5
num2 = 5
for i in range(0,num+1):
    for j in range(num2-i,0,-1):
        print(j,end=' ')
    print()