""" Escriba un programa para mostrar todos los números primos dentro de un rango
Nota: Un número primo es un número que no se puede formar multiplicando otros números enteros. Un número primo es un número natural mayor que 1 que no es producto de dos números naturales más pequeños.
Ejemplos:
6 no es un número primo porque puede ser hecho por 2 × 3 = 6 37 es un número primo porque ningún otro número entero se multiplica para formarlo.
Dado:
# rango
comienzo = 25
fin = 50
Resultado:
Los números primos entre 25 y 50 son:
29
31
37
41
43
47 """

x = 25
y = 50
print("Los numeros primos entre", x, "y", y, "son:")

for num in range(x, y + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)