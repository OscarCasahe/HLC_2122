""" Escribe un programa para imprimir la tabla de multiplicar de un número dado. Por ejemplo, num = 2 la salida debe ser

2
4
6
8
10
12
14
16
18
20 """

x = int(input("Dime un numero "))

for i in range(11):
    print(i*x)
print()