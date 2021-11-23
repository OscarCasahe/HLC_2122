""" Mostrar series de Fibonacci hasta 10 términos. La secuencia de Fibonacci es una serie de números. 
El siguiente número se encuentra sumando los dos números anteriores. Los dos primeros números son 0 y 1. 
Por ejemplo, 0, 1, 1, 2, 3, 5, 8, 13, 21. El siguiente número en esta serie anterior es 13 + 21 = 34.

Resultado:

Secuencia Fibonacci: 0 1 1 2 3 5 8 13 21 34 """

num1 = 0
num2 = 1

print("Series de Fibonacci:")
for i in range(10):
    print(num1, end="  ")
    reslt = num1 + num2
    num1 = num2
    num2 = reslt